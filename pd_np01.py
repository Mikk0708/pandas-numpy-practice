#pandas/numpy學習

#驗證pandas是否安裝
import pandas as pd
print("Pandas 已成功安裝 版本：", pd.__version__)
#驗證numpy是否安裝
import numpy as np
print("Numpy 已成功安裝 版本：", np.__version__)

#利用陣列代替列表 處理多維度資料
#根據列表list 建立ndarray物件
np_array = np.array([1,2,3,4])
print(np_array) #把資料印出來
print(np_array.size) #取得資料的數量

##一維陣列##
#建立一個一維陣列
data_1 = np.array([2,4,6,8])
#print(data_1)
#創造一個有四個資料的一維陣列 資料未指定
data_2 = np.empty(4)
#print(data_2)
#創造一個有三個資料的一維陣列 資料都是0
data_3 = np.zeros(3)
#print(data_3)
#創造一個有三個資料的一維陣列 資料都是1
data_4 = np.ones(3)
#print(data_4)
#創造一個有五個資料的一維陣列 資料為0,1,2,3,4
data_5 = np.arange(5)
#print(data_5)

##二維陣列##
#創造一個2*2的二維陣列
data_6 = np.array([
    [1,3],
    [5,7]
])
#print(data_6)
#創造一個3*2的二維陣列 資料未指定
data_7 = np.empty([3,2])
#print(data_7)
#創造一個2*3的二維陣列 資料都是1
data_8 = np.ones([2,3])
#print(data_8)

##三維陣列##
#創造一個2*2*2的三維陣列
data_9 = np.array([
    [
        [87,45],[22,38]
    ],
    [
        [13,84],[74,9]
    ]
])
#print(data_9)
#創造一個2*3*4的三維陣列 資料未指定
data_10 = np.empty([2,3,4])
#print(data_10)
#創造一個2*3*3的二維陣列 資料都是1
data_11 = np.ones([2,3,3])
#print(data_11)

##高維陣列##(舉例四維)
#創造一個2*2*2*2的高維陣列
data_12 = np.array([
    [
        [
            [9,7]
        ]
    ],
    [
        [
            [4,8]
        ]
    ]
])
#print(data_12)
#創造一個2*1*2*2的四維陣列 資料未指定
data_13 = np.empty([2,1,2,2])
#print(data_13)
#創造一個1*2*2*1的四維陣列 資料都是1
data_14 = np.ones([1,2,2,1])
#print(data_14)