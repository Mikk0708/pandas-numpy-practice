import numpy as np
import pandas as pd

#資料篩選練習 Series
data1 = pd.Series([20,30,40])
condition1 = [True, False, True]
new_data1 = data1[condition1]
#print(new_data1)

data2 = pd.Series([10,30,50,70,90])
condition2 = data2 > 60 #透過比較運算篩選
new_data2 = data2[condition2]
#print(new_data2)

data3 = pd.Series(["Mike", "Pinky", "Penny", "Julia", "James"])
condition3 = data3.str.contains("J")  #字串篩選
new_data3 = data3[condition3]
#print(new_data3)

#資料篩選練習 DataFrame
data4 = pd.DataFrame({
    "Name":["Mike", "Martin", "Apple", "Alice", "Tom"],
    "Age": [25,30,21,32,36]
}) #兩欄五列的資料
condition4 = data4["Age"] > 28
new_data4 = data4[condition4]
#print(new_data4)

data5 = pd.DataFrame({
    "Name":["Mike", "Martin", "Apple", "Alice", "Tom"],
    "Age":[25,30,21,32,36],
    "Salary":[35000,40000,53000,28000,60000],
    "Department":["Sales","Finance","Sales","Finance","Legal"]
}) #三欄五列的資料
#求 薪資>50000 且 名字含有”M“ 的資料 
condition5 = (data5["Salary"] > 50000) & (data5["Name"].str.contains("T")) #pandas需要用& 不能用and
new_data5 = data5[condition5]
#print(new_data5)

data5.sort_values(by="Age", ascending = True, inplace = True)
print(data5)



