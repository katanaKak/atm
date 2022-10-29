from model.debit_card import card
from model.bank_model import bank
from controller.card_work import card_controll
from controller.payments import pay_mob, pay_tv, pay_fine
from controller.transactions import cash, cash2


class Interface:

    def __init__(self):
        pass

    def home(self):
        card.set_current_card(None)
        bank.set_amount(None)
        enter = input("""Вставьте карту и нажмите 1 чтобы начать: """)

        if enter == "1":
            self.enter_menu()
        else:
            print("Введены не корктные значения, попробуйте снова...")
            self.home()

    def more(self):
        ans = input("Хотите совершить ещё операции Введите 1 если да иначе 0 \nВведите : ")
        if ans == "1":
            self.menu()
        else:
            self.home()

    def if_int(self, val):
        try:
            val = int(val)
            return True
        except:
            print("Ошибка. Введено не коректное занчение str")
            self.more()

    def enter_menu(self):
        card_num = input("Введите номер карты : ")
        card_pin = input("Введите пароль карты : ")

        try:
            # ifin получает False если карта не существует Если существует получт 1
            ifin = card_controll.check_card(num=card_num, pin=card_pin)
        except:
            print("Ошибка проверки наличия карты, попробуйте снова...")
            ifin = False
            self.enter_menu()

        if ifin == False:
            print(f"Картa c номером {card_num} и паролем {card_pin} не сущуствует\nПоробуйте ввести данные снова...")
            self.enter_menu()
        elif ifin == True:
            print(f"Доступ к карте {card_num} получен")
            self.menu()
        elif ifin == None:
            print(f"Карта {card_num} заблокированна, пожалуйста обратитесь в банк")
            self.home()
        else:
            print(f"Error")
            self.home()

    def menu(self):
        operations_list = """\nВыберите операцю
        \n1. Проверть баланс\n2. Оплата телевидения\n3. Оплата телефона\n4. Оплата штрафов ГИБДД \n5. Снятие наличных \n6. Поплнение карты\n0. Выход
        \nВведите : """

        n = input(operations_list)
        if n in [str(x) for x in range(1, 7)]:
            self.operations(n)

        elif n == "0":
            print("Главное меню")
            self.home()
        else:
            print("Такой оперции не существует. Попробуйте снова...")
            self.menu()

    def operations(self, option):
        if option in ["1"]:
            balance = card_controll.get_balance()
            print(f"На вашем балансе: {balance} BYN")
            self.menu()
        elif option in ["2", "3", "4"]:
            self.payment_view(option)
        elif option in ["5", "6"]:
            self.transaction_view(option)
        else:
            print(f"Выбранна оперция {option}")

    def payment_view(self, case):
        if case == "2":
            place = input("Введите лицевой счёт : ")
            amount = input("Введите сумму оплаты : ")
            self.if_int(amount)
            card_now = card.get_current_card()
            try_pay = pay_tv.pay(card_num=card_now, place=place, amount=amount)
            self.payment_ans(try_pay=try_pay)

        elif case == "3":
            place = input("Введите номер : ").strip()
            amount = input("Введите сумму оплаты : ")
            card_now = card.get_current_card()
            try_pay = pay_mob.pay(card_num=card_now, place=place, amount=amount)
            self.payment_ans(try_pay=try_pay)
        elif case == "4":
            auto = input("Введите регистрационный номер автомобиля : ")
            place = input("Введите кодовый номер штрафа : ")
            amount = input("Введите сумму оплаты : ")
            card_now = card.get_current_card()
            try_pay = pay_fine.pay2(card_num=card_now, place=[auto, place], amount=amount)
            self.payment_ans(try_pay=try_pay)
        else:
            print("Пока не реализованно")
            self.more()

    def payment_ans(self, try_pay):
        if try_pay ==  False:
            print("Недостаточно средста на карте")
        elif try_pay == True:
            print("Операция оплаты прошла успешно")
        else:
            print("Ошибка оплаты :-(\nВозможно введённых данных не существует")

        self.more()

    def transaction_view(self, case):
        if case == "5":
            amount = input("Введите сумму которую хотите снять : ")
            self.if_int(amount)

            card_now = card.get_current_card()
            bank_now = bank.set_amount(amount)
            enough = cash.if_enough(card_now, amount)

            if enough:
                trans = cash.transfer(place=card_now, amount=amount)
                self.transaction_ans(trans)
            else:
                print("Недостаточно средста на карте :-(")
                self.more()
        elif case == "6":
            print("Внимение банкомат принимет купюты напимнлом 200, 100, 50, 20, 10, 5 BYN")
            print("Введите 0 для того чтобы закончить")
            bb = input("Введите купюру : ")
            lst = []
            while bb != "0":
                if bb in [str(i) for i in [200, 100, 50, 20, 10, 5]]:
                    lst.append(int(bb))
                    print(f"Введено {sum(lst)} BYN")
                else:
                    print("Ошибка. Такая купюра не принимается")
                bb = input("Введите купюру : ")

            # print(lst)
            self.pull_transaction(lst)

    def transaction_ans(self, trans):
        if trans == False:
            print("Ошибка недостаточно купюр или нет купюр нужного наминала :-(")
            self.more()
        elif trans == None:
            print("Ошибка транзакции")
            self.more()
        else:
            print("Выберите купюры которые хотите получить ->")
            length = -1
            for i, v in enumerate(trans):
                print(f"{i+1} : ", end="")
                for j in v:
                    print(f"{j[0]}-BYN {j[1]}-шт,", end=" ")
                print()
                length += 1

            try:
                choice = int(input("Введите : ")) - 1
                choice = (choice if (choice > -1 and choice <= length) else None)
            except:
                print("Ошибка транзакции. Не верное указание данных :-(")
                choice = None
                self.more()

            if choice == None:
                print("Ошибка транзакции. Не верное указание данных ((")
                self.more()
            else:
                self.transaction_finish(choice)

    def transaction_finish(self, choice):
        do = cash.do_transfer(choice)
        if do:
            print("Транзакция прошла успешно, возьмите ваши деньни")
            bs = bank.get_banknotes()
            print(bs)
        else:
            print("Ошибка транзакции :-(")
        bank.set_amount(None)
        self.more()

    def pull_transaction(self, lst):
        ans = cash2.get_transfer(lst)
        if ans == False:
            print("Ошибка попленения (")
        else:
            print("Баланс поплнен успешно")
            bs = bank.get_banknotes()
            print(bs)
        self.more()


inter = Interface()
