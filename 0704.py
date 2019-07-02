# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series
import re

val = 'a,b,  guido'
print(val.split(','))

pieces = [x.strip() for x in val.split(',')]
print(pieces)

','.join(pieces)
print(pieces)

print('guido' in val)

print(val.index(','))

print(val.index(','))

print(val.count(','))

print(val.replace(',','::'))


#正则表达式

text = "foo   bar\t baz  \tqux"
print(re.split('\s+', text))
print(text.split(' '))


regex = re.compile('\s+')
print(regex.split(text))
print(regex.findall(text))


text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE) # 忽略大小写
print(regex.split(text))
print(regex.findall(text))


m = regex.search(text)
print(m)
print(text[m.start():m.end()])

#替换
print(regex.sub('REDACTED',text))


print(regex.match(text)) # 返回None，因为它只匹配出现在字符串开头的模式。


pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})' # 用()包含group
regex = re.compile(pattern, flags=re.IGNORECASE)
m = regex.match('wesm@bright.net')
print(m.groups())

print(regex.findall(text))

print(text)

print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))

# pandas中矢量化的字符串函数

data = {'Dave': 'dave@google.com',
        'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com',
        'Wes': np.nan}
data = Series(data)
print(data)
data.str.contains('gmail')

pattern = '([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\\.([A-Z]{2,4})'
data.str.findall(pattern, flags=re.IGNORECASE)


print(data.str[:5])
















































