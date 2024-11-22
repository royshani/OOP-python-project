from Company import Company
import copy

class CompanyNode(Company):

    _comparison_type = "net value"

    def __init__(self, name, stocks_num, stock_price, comp_type):
        Company.__init__(self, name, stocks_num, stock_price, comp_type)
        self.__children = []
        self.__parent = None

    def get_parent(self):
        return self.__parent

    def get_children(self):
        return self.__children

    def __len__(self):
        return len(self.__children)

    def is_leaf(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    def add_child(self, child):
        if type(child) == CompanyNode:
            if self >= child:
                self.__children.append(child)
                child.__parent = self
                return True
            else:
                return False
        else:
            return False

    def total_net_worth(self):
        tree_worth_sum = self.net_worth()
        for child in self.__children:
            tree_worth_sum += child.total_net_worth()
        return tree_worth_sum

    def test_node_order_validity(self):
        for child in self.__children:
            if self < child:
                return False
            else:
                child.test_node_order_validity()
        if self.__parent != None:
            if self <= self.__parent:
                return self.__parent.test_node_order_validity()
            else:
                return False
        return True

    def is_ancestor(self, other):
        for child in self.__children:
            if child == other:
                return True
            child.is_ancestor(other)
        return False

    def remove_ancestor(self, other):
        for child in self.__children:
            if child == other:
                self.__children.remove(other)
            child.remove_ancestor(other)
        return

    def change_comparison_type(cls, comparison_type):
        if comparison_type == "stock num" or "stock price" or "net value" or "total sum":
            cls._comparison_type = comparison_type
            return True
        else:
            return False

    def __repr__(self):
        children_repr = [child.__repr__() for child in self.__children]
        return "[" + Company.__repr__(self) + ", [" + ", ".join(children_repr) + "]]"

    def __add__(self, other):
        if other.is_ancestor(self) is True:
            raise ValueError("oops other is an ancestor")
        new_company_worth = self.net_worth() + other.net_worth()
        new_stocks_num = self.stocks_num + other.stocks_num
        new_stock_price = new_company_worth / new_stocks_num
        self_new_children = copy.deepcopy(self.get_children())
        other_new_children = copy.deepcopy(other.get_children())
        new_parent = copy.deepcopy(self.__parent)
        merged_companynode = CompanyNode(self.name, new_stocks_num, new_stock_price, self.comp_type)
        merged_companynode.__children = []
        merged_companynode.__parent = new_parent
        for child in self_new_children:
            merged_companynode.add_child(child)
        for child in other_new_children:
            merged_companynode.add_child(child)
        merged_companynode.remove_ancestor(other)
        if merged_companynode.test_node_order_validity() is False:
            raise ValueError("oops you cant merge 2 companies which do not follow the famous company rule")
        return merged_companynode

    def set_stocks_num(self, stocks_num):
        if type(stocks_num) is int and stocks_num >= 0:
            self.stock_price = self.net_worth() / stocks_num
            self.stocks_num = stocks_num
            return self.test_node_order_validity()
        else:
            return False

    def update_net_worth(self, net_worth):
        if type(net_worth) is int or float:
            if net_worth > self.net_worth():
                return False
            else:
                self.set_stock_price(net_worth / self.stocks_num)
                return self.test_node_order_validity()

        else:
            return False

    def set_stock_price(self, stock_price):
        if type(stock_price) is (int or float) and stock_price >= 0 and stock_price < self.stock_price:
            if (stock_price * self.stocks_num) > self.net_worth():
                return False
            else:
                self.stock_price = stock_price
                self.stocks_num = round(self.net_worth() / self.stock_price)
                net_worth = self.stock_price * self.stocks_num
                return self.update_net_worth(self, net_worth)

    def add_stocks(self, number):
        if type(number) is int and self.stocks_num + number > 0:
            self.stocks_num = self.stocks_num + number
            self.stock_price = self.net_worth() / self.stocks_num
            return self.test_node_order_validity()
        else:
            return False

    def __lt__(self, other):
        if type(other) == CompanyNode:
            if super().__lt__(Company(other.name, other.stocks_num, other.stock_price, other.comp_type)):
                return True
            if self._comparison_type == "total sum":
                return self.total_net_worth() < other.total_net_worth()
        else:
            return False

    def __gt__(self, other):
        if type(other) == CompanyNode:
            if super().__gt__(Company(other.name, other.stocks_num, other.stock_price, other.comp_type)):
                return True
            if self._comparison_type == "total sum":
                return self.total_net_worth() > other.total_net_worth()
        else:
            return False

    def __eq__(self, other):
        if type(other) == CompanyNode:
            if super().__eq__(Company(other.name, other.stocks_num, other.stock_price, other.comp_type)):
                return True
            if self._comparison_type == "total sum":
                return self.total_net_worth() == other.total_net_worth()
        else:
            return False

    def __ne__(self, other):
        if type(other) == CompanyNode:
            if super().__ne__(Company(other.name, other.stocks_num, other.stock_price, other.comp_type)):
                return True
            if self._comparison_type == "total sum":
                return self.total_net_worth() != other.total_net_worth()
        else:
            return False

    def __ge__(self, other):
        if type(other) == CompanyNode:
            if super().__ge__(Company(other.name, other.stocks_num, other.stock_price, other.comp_type)):
                return True
            if self._comparison_type == "total sum":
                return self.total_net_worth() >= other.total_net_worth()
        else:
            return False

    def __le__(self, other):
        if type(other) == CompanyNode:
            if super().__le__(Company(other.name, other.stocks_num, other.stock_price, other.comp_type)):
                return True
            if self._comparison_type == "total sum":
                return self.total_net_worth() <= other.total_net_worth()
        else:
            return False