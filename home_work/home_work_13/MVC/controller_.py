from model_ import MadelCashMachine
import view_


def work(model):
    """функция work (controller cash_machine) !"""
    while True:
        model.launch_cash_machine()

        action = input("\nваш выбор -> ")
        match action:
            case "1":
                try:
                    add = float(input('внесите сумму кратную 50: '))
                    model.put_money(add)
                except ValueError as ex:
                    view_.print_('Неверный ввод !')
                    continue

            case "2":
                try:
                    take = float(input('внесите сумму кратную 50: '))
                    model.give_money(take)
                except ValueError as ex:
                    view_.print_('Неверный ввод !')
                    continue
            case "3":
                model.print_history()
            case "4":
                model.save_json()
            case "5":
                model.load_json()
            case "0":
                quit()
        model.give_percent()


def controller_cash_machine(cash=0, counter=0, history=None):
    """Функция создания объекта cash_machine !"""
    cash_machine = MadelCashMachine(cash, counter, history)
    work(cash_machine)
