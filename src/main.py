from manager import Manager
from data_analyzer import DataAnalyzer

class Main:
    def __init__(self):

        self.data_url = "../data/tweets_dataset.csv"
        self.manager = Manager(self.data_url)
        # self.data_analyzer = DataAnalyzer(self.data_url)
        # self.data_analyzer.tweets_count_per_category()
        # print(self.data_analyzer.average_word_tweets())

if __name__ == "__main__":
    Main()