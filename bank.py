class Bank:
    def __init__(self, name, last_name, money):
        self.name = name
        self._last_name = last_name
        self.__money = money

    def get_balance(self):
        return self.__balance

    def set_balance(self, bebrik):
        self.__balance = bebrik

vanya = Bank('Иван', 'Петров', 150000000)
vanya.__balance = 120393948491
vanya.name = 'Анастасия'
print(vanya.name, vanya._last_name ,vanya.money)