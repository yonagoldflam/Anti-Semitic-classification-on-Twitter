from manager import Manager

class Main:
    def __init__(self):
        self.data_url = "../data/tweets_dataset.csv"
        self.manager = Manager(self.data_url)
        self.manager.analyse_data()


if __name__ == "__main__":
    Main()