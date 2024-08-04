"""This file is responsible for reading in the data, cleaning it, and returning a proper data frame"""

import pandas

class DataReader():
    """Abstract base class for reading in data
    """

    def __init__(self, df_path:str):
        pass

    
    def clean(self):
        pass



class MusicDataReader(DataReader):
    pass