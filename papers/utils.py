
import json

from ast import literal_eval
from datetime import datetime
from fastapi import UploadFile

from main import ai_model, db

from .models import Paper

tasks_db = db.tasks


def manual_serialize(res):
    for k, v in res.items():
        res[k] = literal_eval(v)
    
    return res


def replace(res):
    if res.get('_id', None):
        res['_id'] = str(res['_id'])
    if res.get('created_at', None):
        res['created_at'] = str(res['created_at'])
    if res.get('updated_at', None):
        res['updated_at'] = str(res['updated_at'])

    return res


async def process_pdf(newfile: UploadFile, task_id: str, db):
    try:
        contents = await newfile.read()
        prompt = 'Accurately summarize the following document'
        response = ai_model.generate_content(
            f'{prompt}; DOCUMENT: {contents}; USING JSON SCHEMA: {Paper}'
        )

        # Paper(**json.dumps(response))

        db.tasks.update_one(
            {"_id": task_id},
            {
                "$set": {
                    "status": "COMPLETED",
                    "result": response,
                    "completed_at": datetime.now()
                }
            }
        )

    except Exception as e:
        db.tasks.update_one(
            {"_id": task_id},
            {
                "$set": {
                    "status": "FAILED",
                    "error": str(e),
                    "completed_at": datetime.now()
                }
            }
        )
