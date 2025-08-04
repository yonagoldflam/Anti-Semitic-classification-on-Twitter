from data_analyzer import DataAnalyzer

class Manager:
    def __init__(self,data_analyzer):
        self.da = DataAnalyzer(data_analyzer)
        self.da.tweets_count_per_category()
        self.da.print_result_dict()
        self.da.average_word_tweets_per_category()
        self.da.print_result_dict()


        #self.dataAnalyzer.print_data()
