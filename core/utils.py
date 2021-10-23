import json
from core.models import Stock, Fund, Portfolio

STOCK_DATA_LOCATION = "stock_data.json"
CURRENT_PORTFOLIO = "CURRENT_PORTFOLIO"
CALCULATE_OVERLAP = "CALCULATE_OVERLAP"


def initialise():
    """
    Initialise the program by reading the given stock_data.json and
    creating Stock, Fund and Portfolio instances from it.

    Returns:
        master_portfolio (Portfolio): Master portfolio instance of all
        mutual funds listed in stock_data.json
        master_fund (Fund): Master fund instance of all stocks listed
        in stock_data.json
    """
    with open(STOCK_DATA_LOCATION, "r") as file_data:
        stock_data = json.load(file_data)

    master_portfolio = Portfolio()
    master_fund = Fund("MASTER")

    for fund_data in stock_data["funds"]:
        fund = Fund(fund_data["name"])
        for stock_name in fund_data["stocks"]:
            stock = Stock(stock_name)
            fund.add_stock(stock)
            if (master_fund.find_stock(stock_name) is None):
                master_fund.add_stock(stock)
        master_portfolio.add_fund(fund)

    return (master_portfolio, master_fund)


def create_portfolio(fund_names):
    """
    Create Portfolio instance from input data

    Args:
        fund_names (list): Fund name strings from input data.

    Returns:
        portfolio (Portfolio): Portfolio instance from given data.
    """
    portfolio = Portfolio()
    for fund_name in fund_names:
        fund = MASTER_PORTFOLIO.find_fund(fund_name)
        portfolio.add_fund(fund)
    return portfolio


def calculate_overlap(fund_name, current_portfolio):
    """
    Determine the overlap for the given fund with the current portfolio.

    Args:
        fund_name (str): Name of the fund for which overlap
        should be determined.
        current_portfolio (Portfolio): Current portfolio to which
        the fund must be compared.

    Returns:
        overlap (float): Percentage of overlap between two funds.
    """
    fund = MASTER_PORTFOLIO.find_fund(fund_name)
    if (fund is None):
        print("FUND_NOT_FOUND")
    else:
        for current_fund in current_portfolio.get_fund_list():
            overlap = current_fund.overlap(fund)
            if overlap > 0:
                print(
                    f"{fund.get_fund_name()} {current_fund.get_fund_name()} {overlap:.2f}%"
                )


def add_stock(fund_name, stock_name):
    """
    Adds a given stock to a given fund.

    Args:
        fund_name (str): Name of the fund to which stock must be added.
        stock_name (str): Name of the stock to be added.
    """
    fund = MASTER_PORTFOLIO.find_fund(fund_name)
    stock = MASTER_FUND.find_stock(stock_name)
    if (stock is None):
        new_stock = Stock(stock_name)
        MASTER_FUND.add_stock(new_stock)
        fund.add_stock(new_stock)
    else:
        fund.add_stock(stock)


def split_command(line_):
    """
    Helper function to split command and input data.

    Args:
        command (str): Input command.
        line_ (str): Input line.

    Returns:
        fund_name, stock_name (str, str): Fund name and stock (for ADD_STOCK)
    """
    first_space = line_.find(" ")
    second_space = line_.find(" ", first_space + 1)
    fund_name = line_[first_space:second_space].strip()
    stock_name = line_[second_space:].strip()
    return (fund_name, stock_name)


MASTER_PORTFOLIO, MASTER_FUND = initialise()
