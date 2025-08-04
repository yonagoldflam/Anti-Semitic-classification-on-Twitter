import pandas as pd

class DataAnalyzer:
    def __init__(self,data_url):
        self.data_url = data_url
        self.df = pd.read_csv(self.data_url)
        self.result_dict = {"total_tweets":{},"average_length":{},}

    def print_data(self):
        print(self.df)

    def print_result_dict(self):
        print(self.result_dict)

    def tweets_count_per_category(self):
        a = self.df['Biased'].value_counts()
        print(a.head())
        print(a.sum())

        self.result_dict['total_tweets']['antisemitic'] = int(a.loc[0])
        self.result_dict['total_tweets']['non_antisemitic'] = int(a.loc[1])
        self.result_dict['total_tweets']['total'] = len(self.df)
        self.result_dict['total_tweets']['unspecified'] = len(self.df) - int(a.get(0,0)) - int(a.get(1,0))




    # def average_word_tweets_per_category(self):
    #     tweet_count_words_per_category = 0
    #     for col in self.df['Text']:



