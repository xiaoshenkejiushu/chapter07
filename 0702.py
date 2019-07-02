# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series


#data = DataFrame(np.arange(6).reshape((2, 3)),
#                 index=pd.Index(['Ohio', 'Colorado'], name='state'),
#                 columns=pd.Index(['one', 'two', 'three'], name='number'))
#
#print(data)
#
#result = data.stack()#将列变为层次化
#print(result)
#
#print(result.unstack())#第一层索引为行，第二层索引为列
#
#print(result.unstack(0))#第一层索引为列，第二层索引为行
#
#
#
#
#s1 = Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
#s2 = Series([4, 5, 6], index=['c', 'd', 'e'])
#data2 = pd.concat([s1, s2], keys=['one', 'two'])
#
#print(data2)
#print(data2.unstack())
#print(data2.unstack().stack(dropna = False))




# 将“长格式”旋转为“宽格式”
ldata = pd.read_csv('./macrodata.csv')
ldata.head()


date =pd.PeriodIndex(year=ldata.year, quarter=ldata.quarter, freq='Q')
ldata['date'] = date.asfreq('M', 'e').asfreq('H', 's').values
ldata = ldata.loc[:, ['date', 'realgdp', 'infl', 'unemp']]
ldata = pd.melt(ldata, id_vars = ['date'], value_vars=['realgdp', 'infl', 'unemp'], var_name='item') # melt与pivot正好对应
print(ldata)


pivoted = ldata.pivot('date','item','value')
print(pivoted.head())

ldata['value2'] = np.random.randn(len(ldata))
print(ldata.head())


pivoted = ldata.pivot('date', 'item')
print(pivoted.head())












