import akshare as ak
import os

df = ak.stock_zh_a_hist(symbol="all", period="daily", start_date="20100101", end_date="20251231", adjust="qfq")
save_path = r"D:\zzr\Quant\SelfQuant\dataget\data"
df.to_csv(os.path.join(save_path, "ak_data.csv"), index=False)