import pandas as pd
import numpy as np
import GDAX
import csv
import time

publicClient = GDAX.PublicClient()
publicClient = GDAX.PublicClient(product_id="BTC-USD")
rates = []
stime = 1455870900
incrementval = 60000
etime = stime + incrementval

while (stime < time.time()):
    rates = rates + publicClient.getProductHistoricRates(granularity=300)
    stime = etime
    etime = stime + incrementval
    time.sleep(1)
    dfrates = pd.DataFrame(rates)
    dfrates.columns = ['ts', 'l', 'h', 'o', 'c', 'v']
    openvals = dfrates[['ts','o']]
    print(openvals)
    openvals.to_csv('gdaxBTCData.csv')

#dfrates = pd.DataFrame(rates)
#dfrates.columns = ['ts', 'l', 'h', 'o', 'c', 'v']
#openvals = dfrates['o']
#print(openvals)
#openvals.to_csv('gdaxBTCData.csv')

