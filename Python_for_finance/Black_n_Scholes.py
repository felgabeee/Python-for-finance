import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def bs_call_price(s, k, sigma,r, t,q):
    d1 = (1 / (sigma * t**0.5)) * (np.log(s / k) + (r-q+sigma**2)/2 * t)
    d2 = d1 - sigma*np.sqrt(t)
    call_price = stats.norm.cdf(d1)*s - (k*np.exp(-(r-q)*t)*stats.norm.cdf(d2))
    return call_price

def bs_put_price(s, k, sigma,r, t,q):
    d1 = (1 / (sigma * t**0.5)) * (np.log(s / k) + (r-q+sigma**2)/2 * t)
    d2 = d1 - sigma*np.sqrt(t)
    put_price = k*np.exp(-(r-q)*t)*stats.norm.cdf(-d2) - stats.norm.cdf(-d1)*s 
    return put_price

def call_from_put(put_price,s,k,r,t):
    call = put_price - k*np.exp(-r*t) + s
    return call

def put_from_call(call_price,s,k,r,t):
    put = call_price + k*np.exp(-r*t) - s
    return put
  
    


