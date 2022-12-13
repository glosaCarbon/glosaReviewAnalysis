from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
from fastapi import UploadFile, HTTPException, Security
from typing import Union, Tuple
from .data_functions import NamedFile
import pandas as pd


class ModelFuncs:

    @staticmethod
    def review_analysis(review):

        tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
        model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

        classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

        X_train = review
        res = classifier(X_train)

        for element in res:
            print(element)
            if element["label"] == "1 star":
                element["label"] = "negative"
            elif element["label"] == "2 stars":
                element["label"] = "neutral close to negative"
            elif element["label"] == "4 stars":
                element["label"] = "neutral close to positive"
            elif element["label"] == "5 stars":
                element["label"] = "positive"
            else:
                element["label"] = "neutral"
            

        return res


    @staticmethod
    async def process_file(file: UploadFile) -> Tuple[pd.DataFrame, int]:

        dot_index = file.filename.rfind('.') + 1
        extension = file.filename[dot_index:]
        length: int
        file = file.file._file

        if extension == 'xlsx' or extension == 'xls':
            dataset = pd.read_excel(file)
        elif extension == 'csv':
            dataset = pd.read_csv(file)
        else :
            raise HTTPException(status_code=406, detail='Extension of the file should be xlsx,xls or csv!')
        return dataset

