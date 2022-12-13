from fastapi import APIRouter, File, UploadFile
from ..schemas.schemas import ReviewInput
from ..utils.model_utils import ModelFuncs

model_router = APIRouter()



@model_router.post("/reviewAnalysis", tags=["Model Operations"])
async def call_model(ReviewInput):

    result = ModelFuncs.review_analysis(ReviewInput)

    response = {
        "review": ReviewInput,
        "result": result
    }
    return response


@model_router.post("/uploadFile", tags=["Model Operations"])
async def upload_file(file: UploadFile = File(...)):

    df = await ModelFuncs.process_file(file)
    data = df.head().fillna('None').to_dict()

    review_list = []
    for review in data['Review'].values():
        review_list.append(review)

    result = ModelFuncs.review_analysis(review_list)



    response = {
        "review": review_list,
        "result": result,
    }
    return response


