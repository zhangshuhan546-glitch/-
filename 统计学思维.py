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
#直方图
# bins 控制分成多少区间，range 控制只看 -60 到 180 分钟
n, bins, patches = plt.hist(df['ArrDelay'],
                            bins=100,            # 100 个区间，更细
                            range=(-60, 180),    # 只看主要范围，忽略极端值
                            color='steelblue',
                            edgecolor='white',
                            alpha=0.8)

# 添加平均线和中位线
plt.axvline(df['ArrDelay'].mean(), color='red', linestyle='--', linewidth=2, label=f'平均值 {df["ArrDelay"].mean():.1f}')
plt.axvline(df['ArrDelay'].median(), color='orange', linestyle='--', linewidth=2, label=f'中位数 {df["ArrDelay"].median():.1f}')

plt.title('到达延误分布直方图', fontsize=28)
plt.xlabel('延误（分钟）', fontsize=20)
plt.ylabel('航班数', fontsize=20)
plt.legend(fontsize=15)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('C:/Users/Peter/Desktop/Aviation-Data-Analysis/images/arrdelay_hist_detail.png', dpi=150)
plt.show()
# 箱线图：看中位数和异常值
plt.figure(figsize=(10, 6))
plt.boxplot(df['ArrDelay'])
plt.title('到达延误箱线图', fontsize=25)
plt.ylabel('延误（分钟）', fontsize=20)
plt.savefig('C:/Users/Peter/Desktop/Aviation-Data-Analysis/images/arrdelay_box.png', dpi=150)
plt.show()
