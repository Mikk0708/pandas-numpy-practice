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
data.isnull().sum()

#數據清洗
#刪除缺失值
data.dropna(inplace=True)
#填補缺失值
data.fillna(0, inplace=True)
#刪除重複數據
data.drop_duplicates(inplace=True)

#基礎數據分析
#計算銷售總額
data["Total_Sales"] = data["Price"]*data["Quantity"] 
ts = data["Total_Sales"].sum()
print(f"銷售總額為：{round(ts)}")
#計算每個產品的銷售總額
product_sales = data.groupby("Product")["Total_Sales"].sum().reset_index()
print(product_sales)
#找出銷售最高的產品
best_selling_p = product_sales.sort_values("Total_Sales", ascending=False).iloc[0]
print(f"最熱銷的是：{best_selling_p["Product"]}, 總額為：{round(best_selling_p["Total_Sales"])}")

#數據篩選與排序
#篩選出銷售額大於2500的訂單
big_sales = data[data["Total_Sales"] > 2500]
print(big_sales)
#將訂單按Total Sales降序排列 並顯示前6筆
sort_sales = data.sort_values(by= "Total_Sales", ascending=False)
print(sort_sales.head(6))