class Nation:
    def __init__(self,country,continent,life_exp_w,life_exp_m):
        self.__fcountry=country
        self.__fcon=continent
        self.__fexpw=life_exp_w
        self.__fexpm=life_exp_m

    def get_country(self):
        return self.__fcountry

    def get_continent(self):
        return self.__fcon

    def get_life_men(self):
        return self.__fexpm

    def get_life_women(self):
        return self.__fexpw

    def calculate_average(self):
        return (float(self.__fexpm)+float(self.__fexpw))/2

    def __lt__(self, other):
        return self.get_country() < other.get_country()

    def __repr__(self):
        return 'Country: ' + self.__fcountry + '\n' + 'Continent: ' + self.__fcon + '\n' + 'Life expectancy for male: '+ str(self.__fexpm) +'\n'+'Life expectancy for Females: '+str(self.__fexpw)+'\n'

    def __str__(self):
        return 'Country: ' + self.__fcountry + '\n' + 'Continent: ' + self.__fcon + '\n' + 'Average Life expectancy: '+ str(self.calculate_average())

