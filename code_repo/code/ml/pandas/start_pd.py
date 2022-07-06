import numpy as np
import pandas as pd

# ------------------------------------------------------ #
# 创建对象的方法
# 通过传递一个list对象创建一个Series，默认整型索引
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# 通过传递一个array数组，时间索引以及列标签创建一个dataframe
# 创建时间索引
dates = pd.date_range("20130101", periods=6)
print(dates)
# 创建列标签
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
# ------------------------------------------------------ #
# 查看数据
# 头部数据
print(df.head(), df.head(10))
# 尾部数
print(df.tail(), df.tail(10))
# 显示索引、列和底层的数值数据(以numpy array数组的形式展现)
print(df.index)
print(df.columns)
print(df.values)
# 描述性统计
print(df.describe())
# 转置
print(df.T)
# 按轴进行排序
print(df.sort_index(axis=1, ascending=False))
# 按值排序
print(df.sort_values(by="B"))
# ------------------------------------------------------ #
# 选择
# 选择单独的某列Series
print(df["A"])
# 切片
print(df[1: 3], df["20130102":"20130104"])
# loc标签
# 通过标签获取交叉区域
print(dates[0], df.loc[dates[0]])
# 通过标签在多个轴上进行选择
print(df.loc[:, ["A", "B"]])
# 标签切片
print(df.loc["20130102":"20130104", ["A", "B"]])
# 标签定位
print(df.loc["20130102", "A"])
# iloc位置选择
# 通过数值选择行
print(df.iloc[3])
# 通过数值进行切片
print(df.iloc[2:4, 0:2])
# 指定位置
print(df.iloc[[1, 2, 4], [0, 2]])
# 对行切片
print(df.iloc[1:3, :])
# 对列切片
print(df.iloc[:, 1:3])
# ------------------------------------------------------ #
# 布尔索引
print(df[df.A > 0])
# ------------------------------------------------------ #
# 增加新列
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130101", periods=6))
df["F"] = s1
print(df)
# ------------------------------------------------------ #
# 缺失值处理
# reindex()
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
print(df1)
df1.loc[dates[0]:dates[1], "E"] = 1
print(df1)
# 去掉包含缺失值的行
df2 = df1.dropna(how="any")
print(df2)
# 对缺失值进行填充
df3 = df1.fillna(value=3)
print(df3)
# ------------------------------------------------------ #
# apply函数
df4 = df.apply(lambda x: x.max() - x.min())
print(df4)

# ------------------------------------------------------ #
# 合并
df1 = pd.DataFrame(np.random.randn(5, 4), index=pd.date_range("20130101", periods=5), columns=list("ABCD"))
df2 = pd.DataFrame(np.random.randn(5, 4), index=pd.date_range("20180101", periods=5), columns=list("ABCD"))
df = pd.concat([df1, df2], ignore_index=True)
print(df)
