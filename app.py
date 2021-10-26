import pandas as pd

CSV = 'naive_bayes_classificador.csv'

class Bayes_Analysis:
    def __init__(self, gen, age, educ, prof, target):
        self.gen = gen
        self.age = age
        self.educ = educ
        self.prof = prof
        self.target = target
        self.count_age = 0
        self.count_gen = 0
        self.csv = pd.read_csv(CSV)

    def analysis(self):
        try:
            for index, row in self.csv.iterrows():
                if row['target']:
                    pass
        except Exception as e:
            print(e)

read = Bayes_Analysis('F', 'a - Ate 25 anos ', 'Fundamental', 'a', 0).analysis()
