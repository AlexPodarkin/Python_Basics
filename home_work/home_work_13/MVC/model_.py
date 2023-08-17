import json
import pickle

import view_


class MadelCashMachine:
    """Клас банкомата"""
    __FREE_LIMIT = 5_000_000
    __COMMISSION_BANK = 0.9
    __DIVISION_CHECK = 50
    __MIN_COMMISSION = 30
    __COMMISSION = 1.5
    __MAX_COMMISSION = 600
    __BONUS_OPERATION = 3
    __BONUS_PERCENT = 1.03

    def __init__(self, cash=0, counter=0, history=None):
        """
        Метод инициализации банкомата
        :param cash: баланс
        :param counter: счетчик операций
        :param history: история операций
        """
        self.__cash = cash
        self.__counter = counter
        if history is None:
            self.__history = []
        else:
            self.__history = history

    def launch_cash_machine(self):
        """Старт банкомата"""
        self.__counter += 1
        if self.__cash > self.__FREE_LIMIT:
            self.__cash *= self.__COMMISSION_BANK
            view_.print_(f'комиссия банка 10% баланс: {round(self.__cash, 2)} у.е')
            self.__history.append(f'комиссия банка 10% баланс: {round(self.__cash, 2)} у.е')

        view_.print_menu(self.__cash)

    def __division_check_50(self, value):
        """Проверка деления на 50 (что-бы не нарушать принцип DRY)
        используется при внесении и снятии у.е"""
        if value % self.__DIVISION_CHECK == 0:
            return True
        else:
            view_.print_('! ошибка: неверная сумма')
            self.__history.append(f"ошибка: неверная сумма, баланс: {round(self.__cash, 2)} у.е")
            return False

    def put_money(self, add):
        """Метод для внесения денег"""
        if self.__division_check_50(add):
            self.__cash += add
            self.__history.append(f"пополнение счета на {str(add)} у.е, баланс: {round(self.__cash, 2)} у.е")

    def give_money(self, take):
        """Метод для снятия денег"""
        if self.__division_check_50(take):
            percent = take * 0.01 * self.__COMMISSION
            if percent < self.__MIN_COMMISSION:
                percent = self.__MIN_COMMISSION
            if percent > self.__MAX_COMMISSION:
                percent = self.__MAX_COMMISSION
            if self.__cash < (take + percent):
                view_.print_(f'! ошибка снятия денег: недостаточно средств баланс: {round(self.__cash, 2)} у.е')
                self.__history.append(f"ошибка снятия денег: недостаточно средств, баланс: {round(self.__cash, 2)} у.е")
            else:
                self.__cash -= (take + percent)
                self.__history.append(f"снятие {str(take)} у.е "
                                      f"(комиссия банка {percent} у.е), баланс: {round(self.__cash, 2)} у.е")

    def print_history(self):
        """Метод для печати истории операций"""
        view_.print_('->история операций:\n' + '\n'.join(self.__history))
        input("для продолжения нажмите ENTER...")

    def give_percent(self):
        """Метод начисления процентов за каждую третью операцию в банкомате"""
        if self.__counter % self.__BONUS_OPERATION == 0:
            self.__cash *= self.__BONUS_PERCENT
            view_.print_(f'-> {self.__counter} операция ! Банк начислил проценты по вкладу !')
            self.__history.append(f"-> {self.__counter} операция !"
                                  f" Банк начислил проценты по вкладу ! баланс: {round(self.__cash, 2)} у.е")

    def save_json(self):
        with open('save.json', 'w', encoding='utf-8') as file:
            dict_to_json = {'cash': self.__cash, 'counter': self.__counter, 'history': self.__history}
            json.dump(dict_to_json, file, indent=2, ensure_ascii=False)
            view_.print_('Файл save.json сохранен в данной директории!')

    def load_json(self):
        with open('save.json', 'r', encoding='utf-8') as file:
            load_dict = json.load(file)
            self.__cash = load_dict['cash']
            self.__counter = load_dict['counter']
            self.__history = load_dict['history']
            view_.print_('Файл save.json загружен из данной директории... \n'
                         'Статус: баланс, история операций и счетчик обновлены !')
