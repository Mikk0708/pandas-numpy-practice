import pandas as pd
import numpy as np

# 以列表資料為底 建立Series(單維度)
data1 = pd.Series([2,4,6,8,10]) #pd.Series(列表)
data1.max() #找最大值
data1.median() #計算中位數
data1 = data1 * 2 #放大兩倍
#print("Max",data1.max())
#print("Median",data1.median())


# DataFrame(二維度) pd.DataFrame(字典)
data2 = pd.DataFrame({
    "name":["Mike","Julia","Tom","Pinky"],
    "age":[24,26,29,20],
    "salary":[20000,40000,8000,90000]
}) 
print(data2)
#取得特定欄 data["欄位名稱"]
data2["name"]
#取得特定列 data.iloc[列編號]
data2.iloc[2]

