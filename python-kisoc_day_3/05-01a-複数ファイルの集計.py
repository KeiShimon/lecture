# %% [markdown]

# 複数ファイルの集計をしていく。
#
# 複数のデータを，1つのDataFrame に要約する方法は，主に2通りあるので，両方紹介する。
#
# 1. 1人分のデータをたくさん用意して，最後に複数の行を1つにまとめる
#    - concat メソッドを用いる
# 2. 必要な統計量を人数分まとめた列を必要なだけ用意して，最後に複数の列をまとめる
#    - DataFrame を ディクショナリで生成する

# %% [markdown]

# ## 1人分のデータをたくさん用意して，最後に複数の行を1つにまとめる

# %%

# 複数人のデータを順番に読んで，同じ処理をすればよい。
# 複数のデータを順番にDataFrame として読むには，
# 読む対象のファイル名を変えていけばよい。

# たとえば，以下の例については，
# df = pd.read_csv('data/psysiological_00', index_col='time')
# 00 の部分を順番に増やしていけばよいだろう。

# 文字列に変数を埋め込む，ということをする。つまり，
# 'data/psysiological_{}'
# の，{} の中を，適切に埋めればよい。

# f 文字列 というものを使う。
# 普通の文字列 '' に， f をつけるだけ。
# さらに {} の中に，埋め込みたい変数を記す。

id = 12
file_name = f'data/psysiological_{id}'

file_name

# %%

# 1桁の場合はちょっと困る

id = 3
file_name = f'data/psysiological_{id}'

file_name

# %%

# 必要な桁数に達するまで 0埋めをする。
# zfill メソッドを用いる。

str(id).zfill(2)

# %%

# zfill をした場合のファイル名。

file_name = f'data/psysiological_{str(id).zfill(2)}'
file_name

# %%

# ファイル名を変えて，データを順番に読み込んでみる

# import
import pandas as pd

# consecutive reading
for id in range(20):
    df = pd.read_csv(f'data/psysiological_{str(id).zfill(2)}')
    print(df.head(2))  # show only 2 rows

# %% [markdown]

# サマリを作成する操作は全てのデータに対して共通なので，
# for ブロックの中で，サマリを作成するアルゴリズムを書けばよい。
#
# 前回と同様に，正中線上における，90 ms から 110 ms の振幅の平均値を求めたいとしよう。
# さらに，正中線各部位の平均も求めたい。

# %%

# 人数分のサマリを作成する。

centers = ['CPz', 'Pz', 'Oz', 'POz', 'Fz', 'FCz', 'Cz', 'AFz']

for id in range(20):
    df = pd.read_csv(f'data/psysiological_{str(id).zfill(2)}')
    summary = df.loc[90:110, centers].mean().to_frame().T
    summary.insert(0, 'average', [df.loc[90:110, centers].mean().mean()])

    print(summary)


# %%

# 個別にできたサマリを，1つの DataFrame にまとめる。

summaries = []

for id in range(20):
    df = pd.read_csv(f'data/psysiological_{str(id).zfill(2)}')
    summary = df.loc[90:110, centers].mean().to_frame().T
    summary.insert(0, 'average', [df.loc[90:110, centers].mean().mean()])

    summaries.append(summary)

summary_all = pd.concat(summaries)

summary_all

# %%

# インデックスをリセットしたい。

summary_all = pd.concat(summaries, ignore_index=True)
summary_all

# %%

# 保存する。
# インデックスの列が今は無名なので，保存時に名前を指定する。

summary_all.round(4).to_csv('saves/summary_psysiological.csv', index_label='id')

# %%

# %% [markdown]

# ## 必要な統計量を人数分まとめた列を必要なだけ用意して，最後に複数の列をまとめる

# %% [markdown]

# 必要な列は，
# 'average', 'CPz', 'Pz', 'Oz', 'POz', 'Fz', 'FCz', 'Cz', 'AFz'。
#
# 各列，人数分のデータを格納したうえで，最後に DataFrame にまとめる。

# %%

# データ格納庫を定義する

columns = ['average', 'CPz', 'Pz', 'Oz', 'POz', 'Fz', 'FCz', 'Cz', 'AFz']

psysiological_data = dict()
for c in columns:
    psysiological_data[c] = []

# 上は，以下のコードと同値。
# psysiological_data = {col: [] for col in columns}

# show
psysiological_data

# %%

