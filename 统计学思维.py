import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Peter/Desktop/Aviation-Data-Analysis/data/FixedDelayedFlights.csv", low_memory=False)

# 1. 三个统计量
print('平均值:', df['ArrDelay'].mean())
print('中位数:', df['ArrDelay'].median())
print('标准差:', df['ArrDelay'].std())
print('最大值:', df['ArrDelay'].max())
print('最小值:', df['ArrDelay'].min())

# 2. 相关性
print(df[['DepDelay', 'ArrDelay']].corr())

plt.figure(figsize=(12, 8))
plt.scatter(df['DepDelay'], df['ArrDelay'],color='red',alpha=0.6)
plt.title('correlation')
plt.xlabel('DepDelay', fontsize=20)
plt.ylabel('ArrDelay', fontsize=20)
plt.savefig('C:/Users/Peter/Desktop/Aviation-Data-Analysis/images/dep_arr_corr.png', dpi=150)
plt.show()