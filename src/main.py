from manager import Manager

class Main:
    def __init__(self):
        self.data_url = "../data/tweets_dataset.csv"
        cleaned_data_url = "../data/tweets_dataset_cleaned.csv"
        anlyzed_data_url = "../data/result.json"
        self.manager = Manager(self.data_url)
        self.manager.analyse_data()
        self.manager.da.print_result_dict()
        self.manager.cleaning_data()
        self.manager.write_to_json_file(anlyzed_data_url)
        self.manager.write_to_csv_file(cleaned_data_url)



if __name__ == "__main__":
    Main()