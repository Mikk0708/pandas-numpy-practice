#numpy合併操作
import numpy as np

arr1 = np.array([
    [3,4,5],
    [6,7,8]
]) #2*3
arr2 = np.array([
    [7,8,9],
    [10,1,2]
]) #2*3
#合併第一個維度 np.vstack((陣列一,陣列二,...)) = 4*3
result1 = np.vstack((arr1,arr2))
print(result1)

#合併第二個維度 np.hstack((陣列一,陣列二,...)) = 2*6
result2 = np.hstack((arr1,arr2))
print(result2)

#numpy切割操作
arr3 = np.array([
            [1,2,3,4],
            [4,5,6,7]
]) #2*4

#根據第一個維度切割 np.vsplit(陣列,切割數量)
ans1 = np.vsplit(arr3,2)
print(ans1)
#[[1,2,3,4]] 1*4
#[[4,5,6,7]] 1*4
 
#根據第二個維度切割 np.hsplit(陣列,切割數量)
ans2 = np.hsplit(arr3,2)
print(ans2)
#[[1,2],[3,4]] 2*2
#[[4,5],[6,7]] 2*2

