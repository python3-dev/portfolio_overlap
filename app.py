import json
import sys

from main import Stock, Fund, Portfolio

STOCK_DATA_LOCATION = "stock_data.json"


def initialise():
    with open(STOCK_DATA_LOCATION, "r") as file_data:
        stock_data = json.load(file_data)

    master_portfolio = Portfolio()
    master_fund = Fund('MASTER')

    for fund_data in stock_data['funds']:
        fund = Fund(fund_data['name'])
        for stock_name in fund_data['stocks']:
            stock = Stock(stock_name)
            fund.add_stock(stock)
            if not(stock_name in master_fund.get_stock_names()):
                master_fund.add_stock(stock)
        master_portfolio.add_fund(fund)

    return(master_portfolio, master_fund)


MASTER_PORTFOLIO, MASTER_FUND = initialise()


def getinput(input_file_name=None):
    """
    Reads inputs from commandline argument or
    optionally, from an input file (for testing).

    Args:
        input_file_name (str, optional): Optionally reads input file
        (used only for testing). Defaults to None.
    """
    if not(input_file_name):
        input_file_name = sys.argv[-1]

    with open(input_file_name, "r") as input_file:
        for _line in input_file.readlines():
            if _line.startswith('CURRENT_PORTFOLIO'):
                fund_names = _line.replace(
                    'CURRENT_PORTFOLIO', '').strip().split()
                current_portfolio = create_portfolio(fund_names)
            elif _line.startswith('CALCULATE_OVERLAP'):
                fund_name = _line.strip().split()[-1]
                compute_overlap(fund_name, current_portfolio)
            elif _line.startswith('ADD_STOCK'):
                fund_name, stock_name = _line.replace(
                    'ADD_STOCK', '').strip().split()
                add_stock(fund_name, stock_name)


def create_portfolio(fund_names):
    portfolio = Portfolio()
    for fund_name in fund_names:
        for fund in MASTER_PORTFOLIO.get_fund_list():
            if fund_name == fund.fund_name:
                portfolio.add_fund(fund)
    return(portfolio)


def compute_overlap(fund_name, current_portfolio):
    for fund in MASTER_PORTFOLIO.get_fund_list():
        if fund.get_fund_name() == fund_name:
            for current_fund in current_portfolio.get_fund_list():
                print(f"{fund.get_fund_name()} {current_fund.get_fund_name()} {current_fund.overlap(fund):.2f}%")


def add_stock(fund_name, stock_name):
    for fund in MASTER_PORTFOLIO.get_fund_list():
        if fund.get_fund_name() == fund_name:
            if stock_name in MASTER_FUND.get_stock_names():
                for stock in MASTER_FUND.get_stocks():
                    if stock.get_stock_name() == stock_name:
                        fund.add_stock(stock)
            else:
                new_stock = Stock(stock_name)
                MASTER_FUND.add_stock(new_stock)
                fund.add_stock(new_stock)
    return('a')


def main():
    getinput('input1.txt')


if __name__ == "__main__":
    main()
