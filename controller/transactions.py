from model.debit_card import card
from model.bank_model import bank
from controller.bank_work import bank_controll


class Transactions:

    def __init__(self, action):
        self.action = action

    def transfer(self, place, amount):
        if self.action == "get":
            ava = bank_controll.if_available(amount)
            return ava if (ava != False) else False

        elif self.action == "post":
            try:
                now_amount = place["balance"] + int(amount)
                card.set_balance(card_num=place["num"], amount=now_amount)
                card.set_current_card(card.get_card_by_num(place["num"]))
                return amount
            except:
                return None

    def do_transfer(self, choice):
        amount = bank.get_amount()
        ava = bank_controll.if_available(amount)

        try:
            place = card.get_current_card()
            now_amount = place["balance"] - int(amount)
            card.set_balance(card_num=place["num"], amount=now_amount)
            card.set_current_card(card.get_card_by_num(place["num"]))

            for i in ava[choice]:
                bank.banknote_minus(i)
            else:
                return True
        except:
            return False

    def get_transfer(self, lst):
        try:
            amount = sum(lst)
            place = card.get_current_card()
            now_amount = place["balance"] + int(amount)
            card.set_balance(card_num=place["num"], amount=now_amount)
            card.set_current_card(card.get_card_by_num(place["num"]))

            for i in lst:
                bank.banknote_plus(i)
            else:
                return True
        except:
            return False

    def if_enough(self, card_num, amount):
        return True if (card_num["balance"] >= int(amount)) else False


cash = Transactions("get")


class Transactions2(Transactions):

    def get_transfer(self, lst):
        try:
            amount = sum(lst)
            place = card.get_current_card()
            now_amount = place["balance"] + int(amount)
            card.set_balance(card_num=place["num"], amount=now_amount)
            card.set_current_card(card.get_card_by_num(place["num"]))

            for i in lst:
                bank.banknote_plus(i)
            else:
                return True
        except:
            return False


cash2 = Transactions("get")
