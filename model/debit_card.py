class CardFather:
    """банковская карта, пин код,
    операция просмотра остатка денег на карте"""

    __card_lst = {
        "8600": {
            "num": "8600",
            "card_holder": "IVANOV VOLODYA",
            "pin": "1234",
            "cvv": "333",
            "balance": 4500
        },
        "8611": {
            "num": "8611",
            "card_holder": "KIM RUSLAN",
            "pin": "1111",
            "cvv": "334",
            "balance": 6500
        },
        "8634": {
            "num": "8634",
            "card_holder": "IRINA KAYRATOVNA",
            "pin": "5000",
            "cvv": "335",
            "balance": 5000
        }

    }

    __current_card = None

    def __init__(self):
        pass

    def get_card_by_num(self, card_num):
        return self.__card_lst[card_num] if card_num in self.__card_lst else False

    def get_current_card(self):
        return self.__current_card

    def set_current_card(self, details):
        self.__current_card = details

    def set_balance(self, card_num, amount):
        self.__card_lst[card_num]["balance"] = amount


card = CardFather()
