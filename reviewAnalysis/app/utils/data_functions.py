import collections
import random
from enum import Enum

import pandas
import pandas as pd
from pydantic import BaseModel, Field
import datasets
from typing import Optional, List, Dict, Tuple, Iterable


class NamedFile:
    name: str
    extension: str
    file = None

    def __init__(self, name, file):
        self.name = name
        dot_index = self.name.rfind('.') + 1
        self.extension = self.name[dot_index:]
        self.file = file