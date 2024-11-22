class Company:

    _comparison_type = "net value"

    def __init__(self, name, stocks_num, stock_price, comp_type):
        if type(name) is not str or len(name) < 2 or not name[0].isupper() or "  " in name:
            for i in name:
                if not (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or ord(i) == 32):
                    raise ValueError("oops you have a name problem")
        else:
            self.name = name
        if type(stocks_num) is not int or stocks_num < 0:
            raise ValueError("oops your stocks num is not valid")
        else:
            self.stocks_num = stocks_num
        if not (isinstance(stock_price, int) or isinstance(stock_price, float)) or stock_price < 0:
            raise ValueError("oops your stock price is not valid")
        else:
            self.stock_price = stock_price
        if type(comp_type) is not str or len(comp_type) < 2 or not comp_type[0].isupper() or "  " in comp_type:
            raise ValueError("oops you have a company type problem")
        else:
            self.comp_type = comp_type

    def net_worth(self):
        return self.stocks_num * self.stock_price

    def set_name(self, name):
        for i in name:
            if not (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or ord(i) == 32):
                return False
        if type(name) is str and len(name) >= 2 and name[0].isupper() and "  " not in name:
            self.name = name
            return True
        else:
            return False

    def set_stocks_num(self, stocks_num):
        if type(stocks_num) is int and stocks_num >= 0:
            self.stock_price = self.net_worth() / stocks_num
            self.stocks_num = stocks_num
            return True
        else:
            return False

    def set_stock_price(self, stock_price):
        if type(stock_price) is (int or float) and stock_price >= 0:
            self.stocks_num = round(self.net_worth() / stock_price)
            self.stock_price = stock_price
            return True
        else:
            return False

    def set_comp_type(self, comp_type):
        if type(comp_type) is str and len(comp_type) > 2 and comp_type[0].isupper() and "  " not in comp_type:
            self.comp_type = comp_type
            return True
        else:
            return False

    def update_net_worth(self, net_worth):
        if (type(net_worth) is int or float) and net_worth > 0:
            if net_worth > self.net_worth():
                return False
            else:
                self.stock_price = (net_worth/self.stocks_num)
                return True
        else:
            return False

    def add_stocks(self, number):
        if type(number) is int and self.stocks_num + number > 0:
            self.stocks_num = self.stocks_num + number
            self.stock_price = self.net_worth() / self.stocks_num
            return True
        else:
            return False

    def __repr__(self):
        return "(" + self.name + ", " + str(self.stocks_num) + " stocks, Price: " + str(self.stock_price) + ", " + self.comp_type + ", Net Worth: " + str(self.net_worth()) + ")"

    def __str__(self):
        return "(" + self.name + ", " + str(self.stocks_num) + " stocks, Price: " + str(self.stock_price) + ", " + self.comp_type + ", Net Worth: " + str(self.net_worth()) + ")"

    def change_comparison_type(cls, comparison_type):
        if comparison_type == "stock num" or "stock price" or "net value":
            cls._comparison_type = comparison_type
            return True
        else:
            return False

    def __lt__(self, other):
        if type(other) == Company:
            if self._comparison_type == "stock num":
                if self.stocks_num < other.stocks_num:
                    return True
                else:
                    return False
            if self._comparison_type == "stock price":
                if self.stock_price < other.stock_price:
                    return True
                else:
                    return False
            if self._comparison_type == "net value":
                if self.net_worth() < other.net_worth():
                    return True
                else:
                    return False
        return False

    def __gt__(self, other):
        if type(other) == Company:
            if self._comparison_type == "stock num":
                if self.stocks_num > other.stocks_num:
                    return True
                else:
                    return False
            if self._comparison_type == "stock price":
                if self.stock_price > other.stock_price:
                    return True
                else:
                    return False
            if self._comparison_type == "net value":
                if self.net_worth() > other.net_worth():
                    return True
                else:
                    return False
        return False

    def __eq__(self, other):
        if type(other) == Company:
            if self._comparison_type == "stock num":
                if self.stocks_num == other.stocks_num:
                    return True
                else:
                    return False
            if self._comparison_type == "stock price":
                if self.stock_price == other.stock_price:
                    return True
                else:
                    return False
            if self._comparison_type == "net value":
                if self.net_worth() == other.net_worth():
                    return True
                else:
                    return False
        return False

    def __ne__(self, other):
        if type(other) == Company:
            if self._comparison_type == "stock num":
                if self.stocks_num != other.stocks_num:
                    return True
                else:
                    return False
            if self._comparison_type == "stock price":
                if self.stock_price != other.stock_price:
                    return True
                else:
                    return False
            if self._comparison_type == "net value":
                if self.net_worth() != other.net_worth():
                    return True
                else:
                    return False
        return False

    def __ge__(self, other):
        if type(other) == Company:
            if self._comparison_type == "stock num":
                if self.stocks_num >= other.stocks_num:
                    return True
                else:
                    return False
            if self._comparison_type == "stock price":
                if self.stock_price >= other.stock_price:
                    return True
                else:
                    return False
            if self._comparison_type == "net value":
                if self.net_worth() >= other.net_worth():
                    return True
                else:
                    return False
        return False

    def __le__(self, other):
        if type(other) == Company:
            if self._comparison_type == "stock num":
                if self.stocks_num <= other.stocks_num:
                    return True
                else:
                    return False
            if self._comparison_type == "stock price":
                if self.stock_price <= other.stock_price:
                    return True
                else:
                    return False
            if self._comparison_type == "net value":
                if self.net_worth() <= other.net_worth():
                    return True
                else:
                    return False
        return False

    def __add__(self, other):
        new_company_worth = self.net_worth() + other.net_worth()
        new_stocks_num = self.stocks_num + other.stocks_num
        new_stock_price = new_company_worth / new_stocks_num
        merged_company = Company(self.name, new_stocks_num, new_stock_price, self.comp_type)
        return merged_company
