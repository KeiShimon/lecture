# %% [markdown]

# ## 時系列データを変換する
#
# -100秒から400秒の間の脳波データがあると想定する。測定部位は64ヵ所。
#
# data フォルダ内の psysiological から始まるファイルが各参加者のデータに該当する。
#
# 正中線上における，90 ms から 110 ms の振幅の平均値を求めたいとしよう。
# さらに，正中線各部位の平均も求めたい。

# %%

# import
import pandas as pd

# read
df = pd.read_csv('data/psysiological_00', index_col='time')
df

# %%

# 正中線 のデータは，column 名に 'z' を含む
centers = ['CPz', 'Pz', 'Oz', 'POz', 'Fz', 'FCz', 'Cz', 'AFz']

# %%

# 切り出し対象は
# インデックスラベルが 90 - 110 かつ，
# 列名が ['CPz', 'Pz', 'Oz', 'POz', 'Fz', 'FCz', 'Cz', 'AFz'] 。

df.loc[90:110, centers]

# %%

# 平均が欲しい。

df.loc[90:110, centers].mean()

# %%

# ちなみに，時系列ごとの平均が欲しければ，軸の方向を変えることで実現できる。

df.loc[90:110, centers].mean(axis=1)

# %%

# 時系列プロットを見たければ， plot メソッドを呼ぶだけで描画できる。

df.loc[90:110, centers].mean(axis=1).plot()

# %%

# 平均データは，Series ではなく，DataFrame として欲しい。
# to_frame メソッドを用いる。

df.loc[90:110, centers].mean().to_frame()

# %%

# 行列転置。

df.loc[90:110, centers].mean().to_frame().T

# %%

# 各部位の平均は，平均の平均。

df.loc[90:110, centers].mean().mean()


# %%

# サマリの DaraFrame を作成しよう。

summary = df.loc[90:110, centers].mean().to_frame().T
summary.insert(0, 'average', [df.loc[90:110, centers].mean().mean()])

summary

# %% [markdown]

# これで1人分のデータを要約できた。次は，複数のデータを1つの DataFrame にまとめていく。
