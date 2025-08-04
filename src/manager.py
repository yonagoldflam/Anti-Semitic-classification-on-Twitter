from data_analyzer import DataAnalyzer

class Manager:
    def __init__(self,data_analyzer):
        self.dataAnalyzer = DataAnalyzer(data_analyzer)
        self.dataAnalyzer.print_data()