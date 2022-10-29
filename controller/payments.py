from model.debit_card import card
from model.bank_model import bank


class Payments:
    """Операция оплаты телевидения,
    операция оплаты телефона"""

    def __init__(self, name,  account):
        self.name = name
        self.account = account

    def pay(self, card_num, place, amount):

        if self.if_enough(card_num, amount):
            # print("Взять деньги с card в размере amount положить в place")
            try:
                if place in bank.get_accounts(self.name):
                    now_amount = card_num["balance"] - int(amount)
                    # print("# Запись в историю куда оправились деньги")
                    card.set_balance(card_num=card_num["num"], amount=now_amount)
                    card.set_current_card(card.get_card_by_num(card_num["num"]))
                    return True
                else:
                    return None
            except:
                return None

        else:
            return False

    def if_enough(self, card_num, amount):
        return True if (card_num["balance"] >= int(amount)) else False


pay_tv = Payments("tv", 112233)
pay_mob = Payments("mob", 223344)


class Payments2(Payments):

    def pay2(self, card_num, place, amount):

        if self.if_enough(card_num, amount):
            # print("Взять деньги с card в размере amount положить в place")
            try:
                if place in bank.get_accounts(self.name):
                    now_amount = card_num["balance"] - int(amount)
                    # print("# Запись в историю куда оправились деньги")
                    card.set_balance(card_num=card_num["num"], amount=now_amount)
                    card.set_current_card(card.get_card_by_num(card_num["num"]))
                    return True
                else:
                    return None
            except:
                return None

        else:
            return False


pay_fine = Payments2("fine", 334455)
