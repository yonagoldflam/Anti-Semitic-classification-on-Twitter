import pandas as pd

class DataLoader:
    def __init__(self,data_url):
        self.data_url = data_url
        self.df = pd.read_csv(self.data_url)