from data_analyzer import DataAnalyzer

class Manager:
    def __init__(self,data_analyzer):
        self.da = DataAnalyzer(data_analyzer)

    def analyse_data(self):
        self.da.tweets_count_per_category()
        self.da.average_word_tweets_per_category()
        self.da.longest_3_tweets_per_category()
        self.da.common_words()
        self.da.uppercase_words_per_category()





