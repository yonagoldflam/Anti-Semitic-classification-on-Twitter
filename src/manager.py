from data_analyzer import DataAnalyzer
from data_loader import DataLoader
from cleaner import Cleaner
from write_data_files import WriteDataFiles


class Manager:
    def __init__(self,data_url):
        self.data_loader = DataLoader(data_url)
        self.da = DataAnalyzer(self.data_loader.df)
        self.clean_data = Cleaner(self.data_loader.df)
        self.files = WriteDataFiles()

    def analyse_data(self):
        self.da.tweets_count_per_category()
        self.da.average_word_tweets_per_category()
        self.da.longest_3_tweets_per_category()
        self.da.common_words()
        self.da.uppercase_words_per_category()

    def cleaning_data(self):
        self.clean_data.save_relevant_columns()
        self.clean_data.removing_punctuation_marks()
        self.clean_data.convert_to_smol_letters()
        self.clean_data.remove_tweets_without_classify()

    def write_to_json_file(self, anlyzed_data_url):
        self.files.write_to_json_file(self.da.result_dict,anlyzed_data_url)

    def write_to_csv_file(self,cleaned_data_url):
        self.files.write_to_csv_file(self.da.result_dict,cleaned_data_url)






