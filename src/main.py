from manager import Manager

class Main:
    def __init__(self):

        self.data_url = "anti-semitic_on_twitter/data/tweets_dataset.csv"
        self.manager = Manager(self.data_url)

if __name__ == "__main__":
    Main()