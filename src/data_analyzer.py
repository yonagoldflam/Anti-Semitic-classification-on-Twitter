import pandas as pd

class DataAnalyzer:
    def __init__(self,data_url):
        self.data_url = data_url
        self.df = pd.read_csv(self.data_url)

    def print_data(self):
        print(self.df)

    def tweets_count_per_category(self):
        return self.df['Biased'].value_counts()



