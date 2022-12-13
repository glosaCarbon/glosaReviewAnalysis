from pydantic import BaseModel
from typing import Union


class ReviewInput(BaseModel):
    review: Union[str, None] = None
