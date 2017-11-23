import matplotlib.pyplot as plt


class Hist:
    # данные гистаграммы
    _age_dictionary = dict()

    def __init__(self, age_list):
        self._ages_list = sorted(age_list)
        for value in self._ages_list:
            self._age_dictionary.update(
                {value: self._age_dictionary.get(value, 0) + 1})

    def get_data(self):
        return self._ages_list

    def printGist(self):
        for age, count in self._age_dictionary.items():  # dict.items возвращает пары
            print(str(age).ljust(4) + ":" + "#" * count)

    def showBar(self, title1, title_x, title_y):
        plt.bar(list(self._age_dictionary.keys()),
                self._age_dictionary.values(), color='g', width=0.9, linewidth=20)
        plt.show()
