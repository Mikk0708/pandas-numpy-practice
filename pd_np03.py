# ndarray維度 形狀操作
#資料形狀確認 .shape
#資料轉置 .T.shape
#產生扁平化資料 多維度變一維 .ravel
#重塑資料形狀 資料總數需一樣 .reshape
import numpy as np

data = np.array([
    [
        [2,4,0,7],[6,8,1,7],[5,2,0,3]
    ],
    [
        [1,3,5,3],[5,7,9,8],[8,6,3,4]
    ]
]) #2*3*4

print(data.shape) 

data2 = data.T
print(data2.shape)

data3 = data.ravel()
print(data3)

data4 = data.reshape(2,2,6)
print(data4)

#資料索引 切片
print(data[0,1,3]) #7
print(data[:,2,2]) #[0,3]
#多維度
print(data[1,1:3,2:4]) #[9,8] [3,4]