"""This file is responsible for creating content-based features through embedding methods"""

from sentence_transformers import SentenceTransformer
import pandas as pd

class Embedder():

    def __init__(self, model_type:str='paraphrase-MiniLM-L6-v2'):
        model = SentenceTransformer(model_type)


class ExtractFeatures:

    def __init__(self, dataframe:pd.DataFrame):
        pass