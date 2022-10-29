class BankFather:

    def __init__(self):
        pass

    __banknotes = {
        200: 0,
        100: 2,
        50: 25,
        20: 25,
        10: 25,
        5: 0
    }

    __accounts_lst = {
        "tv": ["1234", "2345", "3456", "4567", "5678", "6789"],
        "mob": ["+375255555555", "+375333333333", "+375299999999"],
        "fine": [["777", "777"], ["5000", "808"]]
    }
    __amount = None

    __black_lst = []

    def get_accounts(self, id):
        return self.__accounts_lst[id]

    def get_banknotes(self):
        return self.__banknotes

    def banknote_minus(self, lst):
        new = self.__banknotes[lst[0]] - lst[1]
        if new >= 0:
            self.__banknotes[lst[0]] = new
        else:
            raise ValueError

    def banknote_plus(self, i):
        self.__banknotes[i] += 1

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def get_blk(self):
        return self.__black_lst

    def blk_add(self, card):
        self.__black_lst.append(card)

    def blk_cls(self, card):
        self.__black_lst = [i for i in self.__black_lst if i != card]


bank = BankFather()
