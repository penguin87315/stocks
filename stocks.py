import yfinance as yf
import pandas as pd
import numpy as np
import requests
amd_money = yf.download('AMD', period = '1d', interval = '1m')
df = pd.DataFrame(amd_money)
df_1 = df.round(2).tail(1)
al = np.array(df_1).tolist()
amd = al[0][4]

amd_price = 111.05
amd_position = 31.72

nvda_money = yf.download('NVDA', period = '1d', interval = '1m')
df_2 = pd.DataFrame(nvda_money)
nvda_df = df_2.round(2).tail(1)
nvda = np.array(nvda_df).tolist()
nvda = nvda[0][4]

nvda_price = 199.09
nvda_position = 21.06

earn_amd = amd_position * (amd - amd_price)
earn_nvda = nvda_position * (nvda - nvda_price)
total = earn_nvda + earn_amd
headers = {
        "Authorization": "Bearer " + "LsTV16WPkTS3wt9K3kfeywWboU5t1EYJz0pisEkWkDh",
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
params = {"message": "目前amd的價格是" + str(amd) + "元, nvda的價格是" + str(nvda) +"元, 利潤是" + str(round(total,2)) + "元"}

r = requests.post("https://notify-api.line.me/api/notify",
                  headers=headers, params=params)
print(r.status_code)  #200

