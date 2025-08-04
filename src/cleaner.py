class Cleaner:
    def __init__(self,data_frame):
        self.df = data_frame

    def save_relevant_columns(self):
        self.df = self.df[['Text','Biased']]

