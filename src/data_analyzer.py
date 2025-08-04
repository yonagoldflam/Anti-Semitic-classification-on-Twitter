import pandas as pd
from collections import Counter

class DataAnalyzer:
    def __init__(self,data_frame):
        self.df = data_frame
        self.result_dict = {"total_tweets":{},"average_length":{},'longest_3_tweets':{},'common_words':[],'uppercase_words':{}}

    # print the result analyses for tests
    def print_result_dict(self):
        print(self.result_dict)

    # count how much tweets per category and total
    def tweets_count_per_category(self):
        counts = self.df['Biased'].value_counts()
        self.result_dict['total_tweets']['antisemitic'] = int(counts.loc[0])
        self.result_dict['total_tweets']['non_antisemitic'] = int(counts.loc[1])
        self.result_dict['total_tweets']['total'] = len(self.df)
        self.result_dict['total_tweets']['unspecified'] = len(self.df) - int(counts.loc[0]) - int(counts.loc[1])

    # calculate the average length of tweets per category and total
    def average_word_tweets_per_category(self):
        antis_words = 0
        count_antis = 0
        non_antis_words = 0
        count_non_antis = 0
        total_words = 0
        count_total = 0

        for col in range(len(self.df)):
            row = self.df.iloc[col]
            tweet_words = len(str(row['Text']).split())
            total_words += tweet_words
            count_total += 1

            if row['Biased']:
                antis_words += tweet_words
                count_antis += 1
            else:
                non_antis_words += tweet_words
                count_non_antis += 1
        self.result_dict['average_length']['antisemitic'] = antis_words / count_antis
        self.result_dict['average_length']['non_antisemitic'] = non_antis_words / count_non_antis
        self.result_dict['average_length']['total'] = total_words / count_total

    # find the longest 3 tweets (chars) per category
    def longest_3_tweets_per_category(self):
        antis_tweets = []
        non_antis_tweets = []

        for col in range(len(self.df)):
            row = self.df.iloc[col]
            if row['Biased']:
                antis_tweets.append(row['Text'])
            else:
                non_antis_tweets.append(row['Text'])

        sorted_antis = sorted(antis_tweets,key=len, reverse=True)
        sorted_non_antis = sorted(non_antis_tweets,key=len, reverse=True)
        self.result_dict['longest_3_tweets']['antisemitic'] = sorted_antis[:3]
        self.result_dict['longest_3_tweets']['non_antisemitic'] = sorted_non_antis[:3]

    # find the most 10 common words from all tweets
    def common_words(self):
        all_words = ' '.join(self.df['Text']).split()
        most_10 = Counter(all_words).most_common(10)

        for i in most_10:
            self.result_dict['common_words'].append(i[0])

    # count how much upper words per category and total
    def uppercase_words_per_category(self):
        count_antis_upp = 0
        count_non_antis_upp = 0
        count_total_upp = 0

        for col in range(len(self.df)):
            row = self.df.iloc[col]
            tweet_words = str(row['Text']).split()

            for word in tweet_words:
                if word.isupper():
                    count_total_upp += 1
                    if row['Biased']:
                        count_antis_upp += 1
                    else:
                        count_non_antis_upp += 1

            self.result_dict['uppercase_words']['antisemitic'] = count_antis_upp
            self.result_dict['uppercase_words']['non_antisemitic'] = count_non_antis_upp
            self.result_dict['uppercase_words']['total'] = count_total_upp







