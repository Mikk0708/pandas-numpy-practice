import pandas as pd
import numpy as np

# 固定隨機種子以保證結果一致
np.random.seed(42)

# 模擬電商銷售數據
data = {
    "Order ID": range(1001, 1051),  # 訂單編號
    "Product": np.random.choice(["Laptop", "Smartphone", "Tablet", "Headphones", "Monitor"], size=50),
    "Category": np.random.choice(["Electronics", "Accessories"], size=50),
    "Order Date": pd.date_range(start="2024-01-01", periods=50, freq="D"),
    "Quantity": np.random.randint(1, 10, size=50),
    "Price": np.random.uniform(100, 1000, size=50).round(2)  # 單價為浮點數
}

# 計算總銷售額
data["Total Sales"] = (data["Quantity"] * data["Price"]).round(2)

# 引入一些缺失值
random_indices = np.random.choice(range(50), size=5, replace=False)
for idx in random_indices:
    data["Price"][idx] = np.nan

# 創建 DataFrame
df = pd.DataFrame(data)

# 將數據保存為 CSV 文件
file_path = "sales_data.csv"
df.to_csv(file_path, index=False)
print(f"數據已保存至 {file_path}")