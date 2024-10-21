
import json
import sys

from bson import ObjectId
from datetime import datetime
from fastapi import (
    APIRouter, BackgroundTasks, Depends, File, Form, HTTPException, UploadFile 
)
from fastapi_limiter.depends import RateLimiter

from main import ai_model, app, db, logger, redis

from .models import Paper, ExtractionResponse, TaskStatus
from .utils import replace, process_pdf


router = APIRouter()

dependencies = []
if "pytest" not in sys.modules:
    dependencies.append(
        Depends(
            RateLimiter(times=2, seconds=5)
        )
    )
api_router = APIRouter(prefix="/api", dependencies=dependencies)
app.include_router(api_router)


paper_db = db.sample_paper
tasks_db = db.tasks


@router.post('/papers')
async def create_papers(paper: Paper):
    logger.info(paper)
    result = paper_db.insert_one(paper.model_dump())
    return {"id": str(result.inserted_id)}


@router.get('/papers/{paper_id}')
async def get_paper(paper_id):
    logger.info('working')
    cached_paper = redis.get(f"paper - {str(paper_id)}")
    if cached_paper:
        return Paper.parse_raw(cached_paper)
    
    paper = paper_db.find_one({'_id': ObjectId(str(paper_id))})

    if not paper:
        raise HTTPException(status_code=401, detail='Paper not found')
    
    redis.set(f'paper - {str(paper_id)}', json.dumps(replace(paper)), ex=3600)
    return paper


@router.put('/papers/{paper_id}')
async def put_paper(paper_id: str, paper_update: Paper):
    result = paper_db.find_one_and_update(
        {'_id': ObjectId(str(paper_id))},
        {'$set': paper_update.model_dump(exclude_unset=True)}
    )
    
    # Invalidate Redis cache
    redis.delete(f"paper - {str(paper_id)}")
    return paper_update


@router.delete('/papers/{paper_id}')
def delete_paper(paper_id: str):
    result = paper_db.delete_one({'_id': ObjectId(paper_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail='Paper not found')
    
    redis.delete(f'paper - {str(paper_id)}')
    return {'message': 'Paper deleted successfully'}


@router.post('/extract/pdf')
async def extract_pdf(
    newfile: UploadFile = File(),
    bg_tasks: BackgroundTasks = BackgroundTasks()
):
    task_id = str(datetime.now().timestamp())

    tasks_db.insert_one({
        '_id': task_id,
        'task_id': task_id,
        'status': 'PROCESSING',
        'result': {},
        'error': '',
        'created_at': datetime.now(),

    })

    bg_tasks.add_task(process_pdf, newfile, task_id, tasks_db)
    return ExtractionResponse(task_id=task_id)


@router.post('/extract/text', dependencies=[Depends(RateLimiter(times=2, seconds=5))])
def extract_text(text: str = Form()):
    try:
        prompt = 'Accurately summarize the following text'
        response = ai_model.generate_content(
            f'{prompt}: {text};  and break it down into a JSON SCHEMA: {json.dumps(Paper.schema())}'
        )

        return {'message': response.text}
    except Exception as e:
        raise HTTPException(status_code=400, detail='An error occured while extracting')
    


@router.get('/tasks/{task_id}')
def task_status(task_id):
    task = tasks_db.find_one({'_id': task_id})
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')

    return TaskStatus(**task)
