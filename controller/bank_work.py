from model.bank_model import bank


class BankControll:

    def __init__(self):
        pass

    def if_available(self, amount):
        amount = int(amount)
        d = bank.get_banknotes()
        total = 0
        for i, v in d.items():
            total += i * v

        if 5 <= amount <= total:
            total_res = []
            not_lst = []

            for key, val in d.items():
                am_c = amount
                res = []

                for i, v in d.items():
                    c = am_c // i if (v > 0) else 0
                    c = c if c <= v else v

                    if c != 0 and i not in not_lst:
                        res.append([i, c])
                        am_c -= i*c
                    # elif c != 0 and v >= 1 and i not in not_lst:
                    #     res.append([i, c])
                    #     am_c -= i * c

                not_lst.append(key)
                s = [i*v for i, v in res]
                if amount == sum(s) and res not in total_res:
                    total_res.append(res)
                    # print(res)

            # print(total_res)
            return total_res if len(total_res) > 0 else False

        else:
            return False


bank_controll = BankControll()
