import unittest

from core.utils import (
    initialise,
    create_portfolio,
    add_stock,
    split_command,
    CURRENT_PORTFOLIO,
    ADD_STOCK,
    CALCULATE_OVERLAP,
    MASTER_PORTFOLIO,
    MASTER_FUND
)

from core.models import Stock, Fund, Portfolio


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.stock0 = Stock("PVR")
        self.stock1 = Stock("TCS")
        self.stock2 = Stock("Netflix")
        self.stock3 = Stock("Amazon")
        self.stock4 = Stock("Microsoft")
        self.stock5 = Stock("Alphabet")
        self.stock6 = Stock("Apple")
        self.stock7 = Stock("Big Basket")
        self.stock8 = Stock("Wipro")
        self.stock9 = Stock("Intel")

        self.fund0 = Fund("ABC Mutual Fund")
        self.fund1 = Fund("DEF Mutual Fund")
        self.fund2 = Fund("GHI Mutual Fund")
        self.fund3 = Fund("JKL Mutual Fund")
        self.fund4 = Fund("MNO Mutual Fund")

        self.portfolio0 = Portfolio()
        self.portfolio1 = Portfolio()

        self.app0 = initialise()
        self.app1 = create_portfolio(
            [
                "ICICI_PRU_NIFTY_NEXT_50_INDEX",
                "PARAG_PARIKH_CONSERVATIVE_HYBRID"
            ]
        )
        return super().setUp()

    def test_get_stock_name_0(self):
        stock_name = self.stock0.get_stock_name()
        self.assertTrue(stock_name == "PVR")

    def test_get_stock_name_1(self):
        stock_name = self.stock1.get_stock_name()
        self.assertTrue(stock_name == "TCS")

    def test_get_stock_name_2(self):
        stock_name = self.stock2.get_stock_name()
        self.assertTrue(stock_name == "Netflix")

    def test_get_stock_name_3(self):
        stock_name = self.stock3.get_stock_name()
        self.assertTrue(stock_name == "Amazon")

    def test_get_stock_name_4(self):
        stock_name = self.stock4.get_stock_name()
        self.assertTrue(stock_name == "Microsoft")

    def test_get_stock_name_5(self):
        stock_name = self.stock5.get_stock_name()
        self.assertTrue(stock_name == "Alphabet")

    def test_get_stock_name_6(self):
        stock_name = self.stock6.get_stock_name()
        self.assertTrue(stock_name == "Apple")

    def test_get_stock_name_7(self):
        stock_name = self.stock7.get_stock_name()
        self.assertTrue(stock_name == "Big Basket")

    def test_get_stock_name_8(self):
        stock_name = self.stock8.get_stock_name()
        self.assertTrue(stock_name == "Wipro")

    def test_get_stock_name_9(self):
        stock_name = self.stock9.get_stock_name()
        self.assertTrue(stock_name == "Intel")

    def test_get_fund_name_0(self):
        fund_name = self.fund0.get_fund_name()
        self.assertTrue(fund_name == "ABC Mutual Fund")

    def test_get_fund_name_1(self):
        fund_name = self.fund1.get_fund_name()
        self.assertTrue(fund_name == "DEF Mutual Fund")

    def test_get_fund_name_2(self):
        fund_name = self.fund2.get_fund_name()
        self.assertTrue(fund_name == "GHI Mutual Fund")

    def test_get_fund_name_3(self):
        fund_name = self.fund3.get_fund_name()
        self.assertTrue(fund_name == "JKL Mutual Fund")

    def test_get_fund_name_4(self):
        fund_name = self.fund4.get_fund_name()
        self.assertTrue(fund_name == "MNO Mutual Fund")

    def test_add_stock_0(self):
        self.fund0.add_stock(self.stock0)
        self.fund0.add_stock(self.stock1)
        self.fund0.add_stock(self.stock2)
        self.fund0.add_stock(self.stock3)
        self.fund0.add_stock(self.stock4)
        self.assertEqual(len(self.fund0.get_stocks()), 5)

    def test_add_stock_1(self):
        self.fund1.add_stock(self.stock0)
        self.fund1.add_stock(self.stock1)
        self.fund1.add_stock(self.stock2)
        self.fund1.add_stock(self.stock3)
        self.fund1.add_stock(self.stock4)
        self.assertEqual(len(self.fund1.get_stocks()), 5)

    def test_add_stock_2(self):
        self.fund2.add_stock(self.stock0)
        self.fund2.add_stock(self.stock1)
        self.fund2.add_stock(self.stock2)
        self.fund2.add_stock(self.stock3)
        self.fund2.add_stock(self.stock4)
        self.assertEqual(len(self.fund2.get_stocks()), 5)

    def test_add_stock_3(self):
        self.fund3.add_stock(self.stock0)
        self.fund3.add_stock(self.stock1)
        self.fund3.add_stock(self.stock2)
        self.fund3.add_stock(self.stock3)
        self.fund3.add_stock(self.stock4)
        self.assertEqual(len(self.fund3.get_stocks()), 5)

    def test_add_stock_4(self):
        self.fund4.add_stock(self.stock0)
        self.fund4.add_stock(self.stock1)
        self.fund4.add_stock(self.stock2)
        self.fund4.add_stock(self.stock3)
        self.fund4.add_stock(self.stock4)
        self.assertEqual(len(self.fund4.get_stocks()), 5)

    def test_add_fund_0(self):
        self.portfolio0.add_fund(self.fund0)
        self.portfolio0.add_fund(self.fund1)
        self.portfolio0.add_fund(self.fund2)
        self.portfolio0.add_fund(self.fund3)
        self.portfolio0.add_fund(self.fund4)
        self.assertTrue(len(self.portfolio0.get_fund_list()) == 5)

    def test_add_fund_1(self):
        self.portfolio1.add_fund(self.fund0)
        self.portfolio1.add_fund(self.fund1)
        self.portfolio1.add_fund(self.fund2)
        self.portfolio1.add_fund(self.fund3)
        self.portfolio1.add_fund(self.fund4)
        self.assertTrue(len(self.portfolio1.get_fund_list()) == 5)

    def test_app0(self):
        portfolio, fund = self.app0
        self.assertTrue(isinstance(portfolio, Portfolio))
        self.assertTrue(isinstance(fund, Fund))

    def test_app1(self):
        self.assertTrue(isinstance(self.app1, Portfolio))

    def test_app2(self):
        self.assertTrue(
            len(self.app1.get_fund_list()) == len(self.app1.get_fund_names())
        )

    def test_overlap(self):
        portfolio_1 = create_portfolio(["AXIS_BLUECHIP"])
        portfolio_2 = create_portfolio(["MIRAE_ASSET_EMERGING_BLUECHIP"])
        fund_1 = portfolio_1.get_fund_list()[0]
        fund_2 = portfolio_2.get_fund_list()[0]
        self.assertAlmostEqual(fund_1.overlap(fund_2), 38.3)

    def test_add_stock_00(self):
        portfolio_1 = create_portfolio(["AXIS_BLUECHIP"])
        fund_1 = portfolio_1.get_fund_list()[0]
        fund_1_name = fund_1.get_fund_name()
        add_stock(fund_1_name, "TCS")
        self.assertTrue("TCS" in fund_1.get_stock_names())

    def test_add_stock_01(self):
        portfolio_1 = create_portfolio(["AXIS_BLUECHIP"])
        fund_1 = portfolio_1.get_fund_list()[0]
        fund_1_name = fund_1.get_fund_name()
        add_stock(fund_1_name, "ACC LIMITED")
        self.assertTrue("ACC LIMITED" in fund_1.get_stock_names())

    def test_split_command_1(self):
        result = split_command(CURRENT_PORTFOLIO, "CURRENT_PORTFOLIO A B C")
        self.assertEqual(len(result), 3)

    def test_split_command_2(self):
        result = split_command(CALCULATE_OVERLAP, "CALCULATE_OVERLAP A")
        self.assertEqual(len(result), 1)

    def test_split_command_3(self):
        fund_name, stock_name = split_command(ADD_STOCK, "ADD_STOCK A B")
        self.assertTrue(type(fund_name), str)
        self.assertTrue(type(stock_name), str)

    def test_find_fund_0(self):
        fund = MASTER_PORTFOLIO.find_fund("AXIS_BLUECHIP")
        self.assertTrue(isinstance(fund, Fund))

    def test_find_fund_1(self):
        fund = MASTER_PORTFOLIO.find_fund("ABC")
        self.assertTrue(fund is None)

    def test_find_stock_0(self):
        stock = MASTER_FUND.find_stock("INFOSYS LIMITED")
        self.assertTrue(isinstance(stock, Stock))

    def test_find_stock_1(self):
        stock = MASTER_FUND.find_stock("ABCDEF123")
        self.assertTrue(stock is None)
