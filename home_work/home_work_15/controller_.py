import model_
import view_


def start_project():
    __model = model_.ModelCashMachine()
    while True:
        view_.print_menu()
        view_.view_print(__model.launch_cash_machine())
        match view_.view_chose('ваш выбор -> '):
            case "1":
                try:
                    view_.view_print(__model.put_money(float(view_.view_chose('внесите сумму кратную 50: '))))
                except ValueError:
                    view_.view_chose('Ошибка ввода (воспользуйтесь цифровой клавиатурой) !')
            case "2":
                try:
                    view_.view_print(__model.give_money(float(view_.view_chose('внесите сумму кратную 50: '))))
                except ValueError:
                    view_.view_chose('Ошибка ввода (воспользуйтесь цифровой клавиатурой) !')
            case "3":
                view_.view_print(__model.print_history())
                view_.wait()
            case "4":
                view_.view_print(__model.save_json())
            case "5":
                view_.view_print(__model.load_json())
            case "0":
                quit()
        view_.view_print(__model.give_percent())
