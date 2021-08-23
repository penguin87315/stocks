# -*- coding: utf-8 -*-
import finnhub
import requests

fh_ac = finnhub.Client(api_key="c4ftrqqad3i9aff8egdg")
amd = float(fh_ac.quote('AMD')['c'])
amd_dp = float(fh_ac.quote('AMD')['dp'])
nvda = float(fh_ac.quote('NVDA')['c'])
nvda_dp = float(fh_ac.quote('NVDA')['dp'])

a_price, a_ps = 111.05, 31.72
n_price, n_ps = 199.09, 21.06
earn = (amd - a_price) * a_ps + (nvda - n_price) * n_ps


bark = requests.post('https://api.day.app/iGTyQntufxFVjXu6UrcCFA/美股/' 
	+ 'AMD目前價格是:' + str(amd) + ' 漲幅:'+ str(round(amd_dp,2))+ '%' 
	+'\nNVDA目前價格是:' + str(nvda) + ' 漲幅:'+ str(round(nvda_dp,2)) + '%' 
	+'\n目前利潤是:' + str(round(earn,2)))


