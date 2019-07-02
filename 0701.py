# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
import sys
#01 合并数据集

#1.01
#df1 = DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1':range(7)})
#df2 = DataFrame({'key':['a', 'b', 'd'],'data2':range(3)})
#
##df_merge = pd.merge(df1,df2)#如果未指定，则将重叠列当作主键,默认inner，即两边都有的才会保留
#df_merge = pd.merge(df1,df2,on=['key'])
#df_merge.to_csv(sys.stdout,sep = ' ')


df1 = DataFrame({'key1':['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1':range(7)})
df2 = DataFrame({'key2':['a', 'b', 'd'],'data2':range(3)})

#df_merge = pd.merge(df1,df2)#如果未指定，则将重叠列当作主键
df_merge = pd.merge(df1,df2,left_on=['key1'],right_on =['key2'],how = 'outer')#相等于两个求并集
df_merge.to_csv(sys.stdout,sep = ' ')

#merge相当于是做了笛卡尔乘积
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                 'data1': range(6)})
df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                 'data2': range(5)})
pd.merge(df1, df2, on='key', how='left') # left join，c会出现，data2自动填充NA。



#左边的key列和右边的索引列进行合并
left1 = DataFrame({'key':['a', 'b', 'a', 'a', 'b', 'c'],'value':range(6)})
right1 = DataFrame({'group_val': [3.5, 7]},index = ['a','b'])
print(left1)
print(right1)

df_merge = pd.merge(left1,right1,left_on = ['key'],right_index = True)
print(df_merge)


#层次化的索引数据
left = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                  'key2': [2000, 2001, 2002, 2001, 2002],
                 'data': np.arange(5.)})
right = DataFrame(np.arange(12).reshape((6, 2)),
                  index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                         [2001, 2000, 2000, 2000, 2001, 2002]],
                  columns=['event1', 'event2'])
print(left)
print(right)
df_merge = pd.merge(left,right,left_on = ['key1','key2'],right_index = True)
print(df_merge)


#轴向链接
arr = np.arange(12).reshape(3,4)
arr_con = np.concatenate([arr,arr],axis=1)
print(arr_con)


s1 = Series([0,1],index=['a','b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
a = pd.concat([s1,s2,s3])
print(a)


s4 = pd.concat([s1 * 5, s3])
#print(pd.concat([s1, s4], axis=1))# 默认的轴向连接是内连接
#print(pd.concat([s1, s4], axis=1, join='inner')) # 两个Series沿着列合并变成2列

print(pd.concat([s1, s4], axis=1, join_axes = [['a','c','b','e']])) 

result = pd.concat([s1,s1,s3],keys = ['one','two','three'])
print(result)

print(result.unstack())


pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']) # 沿着列的方向合并，keys变成columns。

df1 = DataFrame(np.arange(6).reshape(3, 2),
                index=['a', 'b', 'c'],
                columns=['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape(2, 2),
                index=['a', 'c'],
                columns=['three', 'four'])
pd.concat([df1, df2], axis=1, keys=['level1', 'level2']) # level1/2分别对应df1/2的列


pd.concat({'level1': df1, 'level2': df2}, axis=1) # 字典的key对应多重索引的列名

df1 = DataFrame(np.random.randn(3,4),columns = ['a','b','c','d'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
pd.concat([df1,df2])


a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b = Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
print(a)
print(b)
np.where(pd.isnull(a), b, a) # 如果a对应索引为空就取b的值









































