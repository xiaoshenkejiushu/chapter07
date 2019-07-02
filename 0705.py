# -*- coding: utf-8 -*-

# 示例：USDA食品数据库
import json
import numpy as np
import pandas as pd
from pandas import DataFrame, Series


db = json.load(open('./usda_food/database.json'))#list中包含无数的字典
print(len(db))

print(db[0].keys())

print(db[0]['nutrients'][0])

nutrients = DataFrame(db[0]['nutrients']) # 根据第0条记录的营养成本构造一个DataFrame
nutrients.head()


info_keys = ['description', 'group', 'id', 'manufacturer']
info = DataFrame(db, columns=info_keys) # 根据指定的列构造DataFrame
info.head()

info.info()


pd.value_counts(info.group) # 查看group这列各个值的出现次数


nutrients = []
# 把每条记录的营养成分单独拿出来做一个DataFrame，同时用id匹配原记录。
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)
nutrients = pd.concat(nutrients, ignore_index=True)
nutrients.head()

print(nutrients.duplicated().sum())#t统计有重复的行数总和


nutrients = nutrients.drop_dulicates()

col_mapping = {'description': 'food', 'group': 'fgroup'}
info = info.rename(columns=col_mapping, copy=False) # 列重命名
info.info()

col_mapping = {'description': 'nutrient', 'group': 'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)
nutrients.info()


ndata = pd.merge(nutrients, info, on='id', how='outer') # 做一个全连接
print(ndata.head())
print(ndata.info())



# 根据营养成分和食物种类分组，quantile(0.5)自动计算中位数。
result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5) 
result['Zinc, Zn'].sort_values().plot(kind='barh') # 各种食物锌含量的中位数




get_maximum = lambda x: x.xs(x.value.idxmax()) # 根据最大值的位置选择一行
get_minimum = lambda x: x.xs(x.value.idxmin())
by_nutrient = ndata.groupby(['nutgroup', 'nutrient'])
max_foods = by_nutrient.apply(get_maximum)[['value', 'food']] # 每个营养种类里，对应每个营养成分，含量最高的食物。
max_foods.head()





























































