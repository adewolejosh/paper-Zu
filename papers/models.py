
from bson import ObjectId
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import Dict, List, Optional




class QuestionType(str, Enum):
    SHORT = "short"
    LONG = "long"
    MCQ = "mcq"

class Question(BaseModel):
    question:           str
    answer:             str
    type:               QuestionType
    question_slug:      str
    reference_id:       str
    hint:               Optional[str]
    params:             Dict = Field(default_factory=dict)


class Section(BaseModel):
    questions:          List[Question]
    section_type:       str = 'default'
    marks_per_question: int = Field(gt=0)


class PaperType(str, Enum):
    PREVIOUS_YEAR = "previous_year"
    PRACTICE = "practice"
    MOCK = "mock"

class PaperParams(BaseModel):
    board:              str
    grade:              int = Field(ge=1, le=14)
    subject:            str


class Paper(BaseModel):
    title:              str
    paper_type:         PaperType
    paper_time:         int = Field(gt=0)
    marks:              int = Field(gt=0)
    params:             PaperParams
    tags:               List[str]
    chapters:           List[str]
    sections:           List[Section]
    created_at:         Optional[datetime] = datetime.now()
    updated_at:         Optional[datetime] = datetime.now()


class TaskStatus(BaseModel):
    task_id:            str
    status:             str
    result:             Optional[Dict]
    error:              Optional[str]
    created_at:         datetime
    completed_at:       Optional[datetime] = None
    


class ExtractionResponse(BaseModel):
    task_id:            str
