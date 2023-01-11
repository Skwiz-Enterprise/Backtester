from fastquant import get_stock_data, backtest
df = get_stock_data("TSLA", "2020-01-01", "2021-01-01")
print(df.head())
backtest('bbands', df, period=20, devfactor=2.0)
