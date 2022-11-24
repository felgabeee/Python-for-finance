import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from Python_for_finance.Black_n_Scholes import bs_call_price,bs_put_price
plt.style.use('fivethirtyeight')


def implied_volatility(option_price,s,k,r,t,q,call=True):
    sigma =0.01
    price = bs_call_price(s, k, sigma, r,t,q)
    while abs(option_price - price) > 0.05:
        if call :
            price = bs_call_price(s, k, sigma,r, t,q)
            sigma+=0.001
        else :
            price = bs_put_price(s, k, sigma,r, t,q)
            sigma+=0.001
    print(sigma)
    return sigma

#Compute implied volatility from a call price
implied_volatilities = []
for i in np.arange(8,100,1):
    volatility = implied_volatility(i,104,100,0.03,1,0,call=True)
    implied_volatilities.append(volatility)
implied_volatilities



plt.figure(figsize=(12,8))
plt.plot([i for i in np.arange(8,100,1)], implied_volatilities)
plt.title('Implied volatilities deducted from option prices', fontsize=24)
plt.xlabel('Implied volatility', fontsize=22)
plt.ylabel('Option Price', fontsize=22)
plt.show()