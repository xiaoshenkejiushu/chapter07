# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series

data = DataFrame({'k1':['one']*3+['two']*4,
                  'k2':[1,1,2,3,3,4,4]})
print(data)

print(data.duplicated())
data.drop_duplicates()
print(data)

#去除指定列的重复
data['v1'] = range(7)
print(data.drop_duplicates(['k1']))


print(data.drop_duplicates(['k1','k2'],keep = 'last'))


#利用函数或者映射进行数据转换

data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                           'corned beef', 'Bacon', 'pastrami', 'honey ham',
                           'nova lox'],
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

print(data)


meat_to_animal = {'bacon': 'pig',
                  'pulled pork': 'pig',
                  'pastrami': 'cow',
                  'corned beef': 'cow',
                  'honey ham': 'pig',
                  'nova lox': 'salmon'} # 动物来源

data['animal'] = data['food'].map(str.lower)

print(data)

data['food'].map(lambda x:meat_to_animal[x.lower()])
print(data)


data = Series([1., -999., 2., -999., -1000., 3.])

data.replace(-999,np.nan)

print(data.replace([-999,-1000],np.nan))

print(data.replace([-999, -1000], ['JJJ', 'Thousand']))

print(data.replace({-99:'JJJ', -1000:'Thousand'}))



data = DataFrame(np.arange(12).reshape((3, 4)),
                 index=['Ohio', 'Colorado', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data.index.map(str.upper)
data.index = data.index.map(str.upper)

print(data.rename(index=str.upper, columns=str.title))
print(data)


print(data.rename(index = {'OHIO':'hcq'},columns = {'one':'sw'}))

data.rename(index = {'OHIO':'hcq'},inplace = True)
print(data)


#离散化处理
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages,bins)
print(cats)
print(cats.codes)

cats_hcq = pd.cut(ages, [18, 26, 36, 61, 100], right=False) # right设置开闭区间
print(cats_hcq)


group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior'] # 每个区间的名字
cats = pd.cut(ages,bins,labels = group_names)
print(cats)


data = np.random.rand(20)
cats =pd.qcut(data,4)#产生四分位数的区间
print(cats)

print(pd.value_counts(cats))

#检测和过滤异常值
np.random.seed(12345)
data = DataFrame(np.random.randn(1000,4))
print(data.describe())

col = data[3]
print(col[np.abs(col)>3])

print(data[(np.abs(data)>3).any(1)])


data[np.abs(data)>3] = 0
print(data[np.abs(data)>3])


df = DataFrame(np.arange(5 * 4).reshape(5, 4))
sampler = np.random.permutation(5)
print(df)
print(sampler)

print(df.take(sampler))

print(df.take(np.random.permutation(len(df))[:3]))

bag = np.array([5, 7, -1, 6, 4])
sampler = np.random.randint(0,len(bag),size = 10)
print(sampler)
print(bag.take(sampler))


df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                'data1': range(6)})
print(pd.get_dummies(df['key']))

dummies = pd.get_dummies(df['key'],prefix = 'key')
print(dummies)

df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)



mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('./ml-1m/movies.dat',
                       sep='::',
                       header=None,
                       names=mnames)
movies.head()


genre_iter = (set(x.split('|')) for x in movies.genres)
print(genre_iter)
genres = sorted(set.union(*genre_iter))
print(genres)


dummies = DataFrame(np.zeros((len(movies),len(genres))),columns = genres)
print(dummies.head())


for i, gen in enumerate(movies.genres):
    dummies.loc[i, gen.split('|')] = 1 # 给每部电影打标签

print(dummies.head())

movies_windic = movies.join(dummies.add_prefix('Genre_'))
print(movies_windic.head())


values = np.random.rand(10)
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]

print(pd.cut(values,bins))
print(pd.get_dummies(pd.cut(values,bins)))


























