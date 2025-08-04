from data_analyzer import DataAnalyzer
from data_loader import DataLoader

class Manager:
    def __init__(self,data_url):
        self.data_loader = DataLoader(data_url)
        self.da = DataAnalyzer(self.data_loader.df)

    def analyse_data(self):
        self.da.tweets_count_per_category()
        self.da.average_word_tweets_per_category()
        self.da.longest_3_tweets_per_category()
        self.da.common_words()
        self.da.uppercase_words_per_category()





