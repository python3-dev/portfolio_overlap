class Stock:
    """
    Stock model

    Attributes:
        stock_name (str): Name of the stock

    """

    counter = 0

    def __init__(self, stock_name) -> None:
        """
        Initialises Stock Model

        Arguments:
            stock_name (str): Name of the stock
        """
        self.id = Stock.counter
        self.stock_name = self.__normalise(stock_name)
        Stock.counter += 1

    def __normalise(self, _stock_name):
        """
        Normalises the stock names.

        Remove double and trailing spaces from stock names.

        Arguments:
            _stock_name (str): Name of the stock.

        Returns:
            (str): Normalised stock name
        """

        def single_spacer(name):
            """
            Recursively removes double spaces from the name string

            Args:
                name (str): Input name string.

            Returns:
                (str): String with all double spaces removed.
            """
            if "  " in name:
                name = name.replace("  ", " ")
                single_spacer(name)
            else:
                return name.strip()
            return(name)

        return single_spacer(_stock_name)

    def get_stock_name(self):
        """
        Stock name getter function.

        Returns:
            (str): Name of the stock
        """
        return self.stock_name


class Fund:
    """
    Fund model

    Attributes:
        fund_name (str): Name of the mutual fund
    """

    counter = 0

    def __init__(self, fund_name) -> None:
        """
        Initialises the Fund model

        Args:
            fund_name (str): Name of the fund.
        """
        self.id = Fund.counter
        self.fund_name = fund_name
        self.stock_list = []
        Fund.counter += 1

    def get_fund_name(self):
        """
        Getter function for name of Fund instance.

        Returns:
            (str): Name of the fund.
        """
        return self.fund_name

    def add_stock(self, stock):
        """
        Adding a Stock instance to a fund.

        Args:
            stock (Stock): Stock instance to be added.
        """
        self.stock_list.append(stock)

    def get_stock_names(self):
        """
        Getter function for names of Stock instances listed under
        a Fund instance.

        Returns:
            (list): List of stock names listed under a Fund instance.
        """
        stocknames = []
        for stock in self.stock_list:
            stocknames.append(stock.stock_name)
        return stocknames

    def get_stocks(self):
        """
        Getter function for Stock instances listed under a Fund instance.

        Returns:
            (list): List of Stock instances listed under a Fund instance.
        """
        return self.stock_list

    def overlap(self, other):
        """
        Compute and return the overlap percentage rounded off to
        two significant digits.

        Args:
            other (Fund): Fund instance to which overlap must be computed.

        Returns:
            overlap_ (float): Overlap percentage rounded off to
            two significant digits.
        """
        total_stocks = len(self.get_stocks()) + len(other.get_stocks())
        common_stocks = len(
            set(self.get_stock_names()).intersection(other.get_stock_names())
        )
        overlap_ = round(2 * (common_stocks / total_stocks) * 100, 2)
        return overlap_

    def find_stock(self, stock_name):
        """
        Find Stock instance from a Fund instance by stock name.

        Args:
            stock_name (str): Name of the stock to be retrieved.

        Returns:
            stock (Stock): Instance of stock if found else None.
        """
        if stock_name in self.get_stock_names():
            for stock in self.get_stocks():
                if stock.get_stock_name() == stock_name:
                    return(stock)
        else:
            return(None)


class Portfolio:
    """
    Portfolio model.
    """

    def __init__(self) -> None:
        """
        Initialises the Portfolio model.
        """
        self.fund_list = []

    def add_fund(self, fund):
        """
        Add a Fund instance to Portfolio model.

        Args:
            fund (Fund): Fund instance to be added to a Portfolio instance.
        """
        self.fund_list.append(fund)

    def get_fund_list(self):
        """
        Getter function for Fund instances listed under a Portfolio instance.

        Returns:
            (list): List of Fund instances of a given Portfolio instance.
        """
        return self.fund_list

    def get_fund_names(self):
        """
        Getter function for names of Fund instances listed
        under a Portfolio instance.

        Returns:
            (list): List of names of Fund instances of a Portfolio instance.
        """
        fund_names = []
        for fund in self.fund_list:
            fund_names.append(fund.get_fund_name())
        return fund_names

    def find_fund(self, fund_name):
        """
        Find Fund instance from a Portfolio instance by fund name.

        Args:
            fund_name (str): Name of the Fund instance to be retrieved.

        Returns:
            fund (Fund): Fund instance if found, else None.
        """
        if not (fund_name in self.get_fund_names()):
            return(None)
        for fund in self.get_fund_list():
            if fund.get_fund_name() == fund_name:
                return(fund)


class ResultMatrix():
    def __init__(self, current_portfolio, other_fund) -> None:
        self.other_fund = other_fund
        self.current_portfolio = current_portfolio
        self.overlap_matrix = {}
        self.__store_overlap()

    def __store_overlap(self):
        if not(self.other_fund is None):
            for current_fund in self.current_portfolio.get_fund_list():
                self.overlap_matrix[
                    current_fund.get_fund_name()
                    ] = current_fund.overlap(
                        self.other_fund
                        )

    def fetch(self):
        return(self.overlap_matrix)

    def get_other_fund_name(self):
        return(self.other_fund.get_fund_name())
