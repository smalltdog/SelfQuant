import tushare as ts
import os

ts.set_token('39af2cbc772dc465379eab77d945b93f2206bd32dcd97ffcd457ab61')
pro = ts.pro_api()
df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
save_path = r"D:\zzr\Quant\SelfQuant\dataget\data"
df.to_csv(os.path.join(save_path, "tu_data.csv"), index=False)