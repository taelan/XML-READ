import pandas as pd
import numpy as np
df = pd.read_excel(r'C:\Users\41223\课件\26号机销售数据.xlsx')
#print(df)

df1 = df[df['标签'].str.contains('编号')]
df2 = df[df['标签'].str.contains('支付方式')]
df3 = df[df['标签'].str.contains('名称')]
df4 = df[df['标签'].str.contains('销售数量')]
df5 = df[df['标签'].str.contains('单价')]
df6 = df[df['标签'].str.contains('金额')]

df4['内容'] = df4['内容'].astype('int')
df5['内容'] = df5['内容'].astype('int')
df6['内容'] = df6['内容'].astype('int')

#df7 = df.loc['单价']
df.set_index(['标签','内容'])

df7 = df.T
#转置

print(df)