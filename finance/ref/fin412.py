import numpy as np
import FundamentalAnalysis as fa
import pandas_datareader as pd

symbol = ['TSLA','AAPL']

comp1 = 'TSLA'


# print(fa.summary('TSLA'))

# print(fa.summary(symbol))

# balance_sheet = fa.balance_sheet(symbol)



# print(balance_sheet)


#  balance_sheet[comp1].to_csv("BalanceSheet_TSLA.csv")

# fa.balance_sheet_analysis(balance_sheet, symbol, log=False)


#  income_statement = fa.income_statement(comp1)

# print(income_statement)

# income_statement[comp1].to_csv("IncomeStatement_TSLA.csv")

# same using cashflows

# ratios = fa.ratios(comp1)

# print(ratios)

stock_data = fa.stock_data(2015,2016,comp1)

# print(stock_data)


print(stock_data[comp1].describe())
