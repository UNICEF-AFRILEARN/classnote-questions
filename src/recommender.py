from bson import ObjectId
import pandas as pd
import random
import logging


logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


N_QUESTIONS = 3

def handle_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)


def get_recommendations(lessonId):
    questions =  pd.read_parquet("questions.parquet")
    questions = questions[questions['lessonId']==lessonId]
    n_questions = min(N_QUESTIONS,len(questions))
    recommended_questions=random.choices(list(questions['_id'].unique()),k=n_questions)
    recommended_questions = questions[questions['_id'].isin(recommended_questions)]
    recommended_questions['_id'] = recommended_questions['_id'].astype(str)
    recommended_questions['options'] = recommended_questions['options'].apply(lambda x: [{'key': k, 'value': v} for k, v in eval(x).items()])
    return recommended_questions.to_dict(orient="records")