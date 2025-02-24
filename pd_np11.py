import pandas as pd
import numpy as np

#載入與檢查
#讀取數據 pd.read_csv, pd.read_excel, pd.read_sql
data = pd.read_csv('sales_data.csv')
# #顯示前五筆資料
data.head()
#顯示基本統計訊息
data.describe()
#查看列名表
data.columns
#查看索引列
data.index
#查看每列數據類型
data.dtypes
#檢查缺失值
print(data.isnull().sum())

#數據清洗
#填補缺失值
data.fillna(0, inplace=True)
#刪除缺失值
data.dropna(inplace=True)
#刪除重複數據
data.drop_duplicates(inplace=True)

#確保所有欄位數據類型正確



#基礎數據分析
#計算每個產品銷售總額
#找出銷售最高的產品和類別
#按月份統計銷售額並繪製折線圖

#數據篩選與排序
#篩選出銷售額大於1000的訂單
#將訂單按Total Sales將序排列 並顯示前10筆
