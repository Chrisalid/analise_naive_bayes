from os import sep
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
        self.count_educ = 0
        self.count_prof = 0
        self.count_target = 0
        self.count_rows = 0
        self.csv = pd.read_csv(CSV, sep=';')

        print(
        self.gen,
        self.age,
        self.educ,
        self.prof,
        self.target
        )

    def analysis(self):
        print(
            self.gen, ';',
            self.age, ';',
            self.educ, ';',
            self.prof, ';',
            self.target)
        for index, row in self.csv.iterrows():
            if row['Target'] is self.target:
                # print('Tipo dos Selfies ',type(self.age), type(self.gen), type(self.educ), type(self.prof))
                # print('Tipo das colunas ',type(row['Idade']), type(row['Genero']), type(row['Escolaridade']), type(row['Profissao']))
                if row['Idade'] is self.age:
                    # print('0')
                    self.count_age += 1
                if row['Genero'] is self.gen:
                    # print('1')
                    self.count_gen += 1
                if row['Escolaridade'] is self.educ:
                    # print('2')
                    self.count_educ += 1
                if row['Profissao'] is self.prof:
                    # print('3')
                    self.count_prof += 1
                self.count_target += 1
            self.count_rows += 1
        return float(((
                self.count_age/self.count_target)*(
                    self.count_gen/self.count_target)*(
                        self.count_educ/self.count_target)*(
                            self.count_prof/self.count_target)*(
                                self.count_target/self.count_rows)))

genero = 'M'
idade = 'c - 36 a 45 anos'
escolaridade = 'Fundamental'
profissao = 'c'
target = 1


read = Bayes_Analysis(
    genero,
    idade,
    escolaridade,
    profissao,
    target
).analysis()

print(read)
