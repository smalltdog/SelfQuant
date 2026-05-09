import pandas as pd
import os

csv_path = os.path.join(os.getcwd(), "dataget/data", "tu_data.csv")
df = pd.read_csv(csv_path)
line_num = df.shape[0]
df = df[df['name'].str.contains('ST|\\*ST') == False]
df = df[df['list_date'] <= 20180101]
line_num_after = df.shape[0]
print(f"总行数: {line_num}, 去除ST后行数: {line_num_after}, 去除比例: {(line_num - line_num_after) / line_num:.2%}")
df.to_csv(csv_path.replace("tu_data.csv", "tu_data_cleaned.csv"), index=False)