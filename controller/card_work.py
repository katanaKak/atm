from model.debit_card import card
from model.bank_model import bank


class ControllFather:

    def __int__(self):
        pass

    def check_card(self, num, pin):
        item = card.get_card_by_num(num)

        black = bank.get_blk()

        if isinstance(item, dict):
            if item["pin"] == pin and black.count(num) < 3:
                # Сохраняет данные карты используемык в этот момент
                card.set_current_card(item)
                bank.blk_cls(num)
                return True
            elif black.count(num) >= 3:
                return None
            else:
                bank.blk_add(num)
                return False
        elif item == False:
            return False

    def get_balance(self):
        try:
            crd = card.get_current_card()
            return crd["balance"]
        except:
            print("Не удалось получить текущую карту")


card_controll = ControllFather()
