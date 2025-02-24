import pandas as pd
import numpy as np

#自訂索引 pd.Series(資料列表 ,index = 索引列表)
data1 = pd.Series([3,5,-8,12,4],index = ["a","b","c","d","e"])

# dtype型態
print(data1.dtype)
# size數量
print(data1.size)
# index索引
print(data1.index)
#取得資料 根據順序 根據索引
data1[2]  #根據順序 取得第三筆資料
data1["a"] #根據索引 取得第一筆資料

#數字運算
data1.sum() #加法總和
data1.max() #最大值
data1.prod() #乘法總和
data1.mean() #算術平均數
data1.median() #中位數
data1.std() #標準差
data1.nlargest() #取前n大
data1.nsmallest() #取前n小

#字串相關
data2 = pd.Series(["Mike","Vicky","James","Julia","Daniel"],index = ["a","b","c","d","e"])

data2.str.lower() #全轉為小寫
data2.str.upper() #全轉為大寫
data2.str.len() #取得每個字串長度
data2.str.cat(sep = "-") #每個字串用"-"串接成一個字串
data2.str.contains("J") #是否包含"J"
data2.str.replace("Mike","Ray") #取代

print(data2.str.replace("Mike","Ray"))
print(data2.str.cat(sep="-"))
print(data2.str.contains("J"))

