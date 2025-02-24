import numpy as np
#多維陣列運算

# 1.逐元運算 elementwise
#建立兩個多維陣列(兩陣列內容規格需相同)
data1 = np.array([21,-5,33,92])
data2 = np.array([-3,50,-14,8])
#逐一元素運算
a = data1 + data2
print("加法",a)
b = data1 * data2
print("乘法",b)
c = data1 > data2
print("大於",c)
d = data1 == data2
print("是否相等", d)


# 2.矩陣運算 matrix
#建立兩個多維陣列
data3 = np.array([
    [1,2,3],
    [4,5,6]
]) #2*3
data4 = np.array([
    [7,8,9],
    [-1,-2,-3],
    [-4,-5,-6]
]) #3*3
#第一個矩陣的列數需等於第二個矩陣的行數
#data3 的列數（第 2 維，即 dim 1）必須等於 data4 的行數（第 1 維，即 dim 0）
#內積
e = data3.dot(data4)
print("內積：",e)
# 也可寫成data3@data4
#外積
f = np.outer(data3,data4) 
print("外積：",f)


# 3.統計運算 statistics
#建立一個多維陣列
data5 = np.array([
    [2,17,57],
    [34,-5,-8],
    [28,-33,5]
])
data5.sum() #全部加總
data5.sum(axis=0) #colum加總(欄)
data5.sum(axis=1) #row加總(列)
data5.min() #全部最小值
data5.cumsum() #逐值累加
data5.mean() #平均數
data5.std() #標準差 
