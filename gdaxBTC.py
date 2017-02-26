import pandas as pd
import numpy as np
import urllib2
import datetime as dt
import csv
#import matplotlib.pyplot as plt
 
def get_google_data(symbol, period, window):
    url_root = 'http://www.google.com/finance/getprices?i='
    url_root += str(period) + '&p=' + str(window)
    url_root += 'd&f=d,o,h,l,c,v&df=cpct&q=' + symbol
    response = urllib2.urlopen(url_root)
    data = response.read().split('\n')
    #actual data starts at index = 7
    #first line contains full timestamp,
    #every other line is offset of period from timestamp
    parsed_data = []
    anchor_stamp = ''
    end = len(data)
    for i in range(7, end):
        cdata = data[i].split(',')
        if 'a' in cdata[0]:
            #first one record anchor timestamp
            anchor_stamp = cdata[0].replace('a', '')
            cts = int(anchor_stamp)
        else:
            try:
                coffset = int(cdata[0])
                cts = int(anchor_stamp) + (coffset * period)
                parsed_data.append((dt.datetime.fromtimestamp(float(cts)), float(cdata[1]), float(cdata[2]), float(cdata[3]), float(cdata[4]), float(cdata[5])))
            except:
                pass # for time zone offsets thrown into data
    df = pd.DataFrame(parsed_data)
    df.columns = ['ts', 'o', 'h', 'l', 'c', 'v']
    #df.index = df.ts
    #del df['ts']
    df2 = df['o']  #should take only the open price columns
    return df2

stock1 = get_google_data('INX', 300, 1200)
print(stock1)
stock1.to_csv('stock1.csv')

stock2 = get_google_data('FB', 300, 1200)
print(stock2)
stock2.to_csv('stock2.csv')

stock3 = get_google_data('JPM', 300, 1200)
print(stock3)
stock3.to_csv('stock3.csv')

stock4 = get_google_data('INTC', 300, 1200)
print(stock4)
stock4.to_csv('stock4.csv')

stock5 = get_google_data('GOLD', 300, 1200)
print(stock5)
stock5.to_csv('stock5.csv')

stock6 = get_google_data('LODE', 300, 1200)
print(stock6)
stock6.to_csv('stock6.csv')

stock7 = get_google_data('C', 300, 1200)
print(stock7)
stock7.to_csv('stock7.csv')

stock8 = get_google_data('F', 300, 1200)
print(stock8)
stock8.to_csv('stock8.csv')

stock9 = get_google_data('WMT', 300, 1200)
print(stock9)
stock9.to_csv('stock9.csv')

stock10 = get_google_data('TSLA', 300, 1200)
print(stock1)
stock10.to_csv('stock10.csv')




