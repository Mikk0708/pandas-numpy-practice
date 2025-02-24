import pandas as pd
import numpy as np

# DataFrame(二維度資料)
data1 = pd.DataFrame({
    "name":["Mike","Julia","Pinky","Mini","Vic"],
    "age":[24,26,18,32,40],
    "salary":[40000,60000,100000,20000,45000]
},index=["a","b","c","d","e"])

print(data1)

#觀察資料
print("資料數量", data1.size)
print("資料形狀", data1.shape)
print("資料索引", data1.index)
print("資料欄位",data1.columns)

#取得列(row)
print("取得第二列",data1.iloc[1], sep="\n")
print("==============================")
print("取得第b列",data1.loc["b"], sep="\n")
print("==============================")

#取得欄(column)
print("取得name欄",data1["name"], sep="\n")
print("==============================")

#將名字轉為大寫
new_name = data1["name"] # 取出name變為Series
print(new_name.str.upper(),sep="\n")

#計算salary平均值
new_salary = data1["salary"]
print("平均薪資為:",new_salary.mean())

#獲得基本統計數據
print(data1.describe())

#建立新欄位
data1["sex"] = ["M","F","F","F","M"] #以列表建立
data1["revenue"] = pd.Series([200000,400000,600000,80000,90000], index=["a","b","c","d","e"]) #以Series建立
#欄位之間運算結果 建立新欄位
data1["cp"] = data1["revenue"]/data1["salary"]
print(data1)



