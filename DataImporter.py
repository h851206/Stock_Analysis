# TODO:
# 1. Figure out some stocks (numbers) I am interested in.
# 2. Dig into the method of making prediction
# 3. Create a dashboard for visualization

# web: https://finmind.github.io/  and  https://twstock.readthedocs.io/zh_TW/latest/prepare.html
import pandas as pd
import twstock
stock = twstock.Stock('2330')
print(stock.sid)