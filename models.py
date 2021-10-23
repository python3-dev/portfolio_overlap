class Stock():
    counter = 0

    def __init__(self, stock_name):
        self.id = Stock.counter
        self.stock_name = self.__normalise(stock_name)
        Stock.counter += 1

    def __normalise(self, _stock_name):
        def single_spacer(name):
            if "  " in name:
                name = name.replace("  ", " ")
                single_spacer(name)
            else:
                return(name.strip())
        return(single_spacer(_stock_name))

    def get_stock_name(self):
        return(self.stock_name)


class Fund():
    counter = 0

    def __init__(self, fund_name):
        self.id = Fund.counter
        self.fund_name = fund_name
        self.stock_list = []
        Fund.counter += 1

    def get_fund_name(self):
        return(self.fund_name)

    def add_stock(self, stock):
        self.stock_list.append(stock)

    def get_stock_names(self):
        stocknames = []
        for stock in self.stock_list:
            stocknames.append(stock.stock_name)
        return(stocknames)

    def get_stocks(self):
        return(self.stock_list)

    def overlap(self, other):
        total_stocks = len(self.get_stocks()) + len(other.get_stocks())
        common_stocks = len(set(self.get_stock_names()).intersection(other.get_stock_names()))
        overlap_ = round(2*(common_stocks/total_stocks)*100, 2)
        return(overlap_)


class Portfolio():
    def __init__(self):
        self.fund_list = []

    def add_fund(self, fund):
        self.fund_list.append(fund)

    def get_fund_list(self):
        return(self.fund_list)

    def get_fund_names(self):
        fund_names = []
        for fund in self.fund_list:
            fund_names.append(fund.get_fund_name())
        return(fund_names)
