class Cleaner:
    def __init__(self,data_frame):
        self.df = data_frame

    # Choosing the relevant columns with us are the text and the classification as anti-Semitic
    def save_relevant_columns(self):
        self.df = self.df[['Text','Biased']]

    # removes all punctuation marks from the text
    def removing_punctuation_marks(self):
        punctuation_marks = ["'",",","/",".",":"]
        for col in range(len(self.df)):
            text = str(self.df.iloc[col]['Text'])
            for char in self.df.iloc[col]['Text']:
                if char in punctuation_marks:
                    text = text.replace(char, '')
            self.df.at[col, 'Text'] = text

    # convert to smol letters
    def convert_to_smol_letters(self):
        for col in range(len(self.df)):
            text = str(self.df.iloc[col]['Text']).lower()
            self.df.at[col, 'Text'] = text

    # sub all tweets without classification
    def remove_tweets_without_classify(self):
        index_to_drop = []
        for col in range(len(self.df)):
            if self.df.iloc[col]['Biased'] != 0 and self.df.iloc[col]['Biased'] != 1:
                index_to_drop.append(self.df.index[col])
        self.df.drop(index=index_to_drop, inplace=True)



