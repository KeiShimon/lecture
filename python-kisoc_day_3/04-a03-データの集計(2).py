# %% [markdown]

# ## 得られたデータが汚かった場合
#
# 往々にして，もともとのデータは汚い。
# うまくデータを取り出す方法をいくつかのケースについて紹介する。


# %% [markdown]

# ## 数値としてデータが記述されていない場合
#
# data/02.csv が該当。

# %%

import pandas as pd

# %%

# read data

dirty_data = pd.read_csv('data/02.csv')
dirty_data

# %%

# Yes 選択率を集計する。
# Yes が選択されたケースは，
# 'action' 列の値が 'yesno' かつ 'answer' の値が 'y'のとき。

yes_cases = len(dirty_data[(dirty_data['action'] == 'yesno') & (dirty_data['answer'] == 'y')])
yes_cases

# %% [markdown]

# 特性質問紙はかなり曲者。
# 選択肢はいくつかあるが，手間の小さい順に
#
# 1. データを書き換える
# 2. ラムダ式を用いる
# 3. 列ずつループさせて頑張る
#
# 今回は，後学のために 3. 1列ずつループさせて頑張る の方法でやる。

# %%

# DataFrame を一列ずつ取り出すのに，iterrows メソッドを使う。
# インデックスラベルと，行データを順番に取り出す for ループが書ける。

for i, row in dirty_data.loc[:5, :].iterrows():
    print('i:', i)
    print('row: ')
    print()
    print(row)
    print()


# %%

# ループしながらスコアの合計を求める

depression_score = 0
relationship_score = 0
aggression_score = 0
anxiety_score = 0
total_cases = 0

for i, row in dirty_data[dirty_data['action'] == 'subjective'].iterrows():
    total_cases += 1
    if row['category'] == 'depression':
        depression_score += int(row['answer'][1])
    elif row['category'] == 'relationship':
        relationship_score += int(row['answer'][1])
    elif row['category'] == 'anxiety':
        anxiety_score += int(row['answer'][1])
    elif row['category'] == 'aggression':
        aggression_score += int(row['answer'][1])
    else:
        # スペルミスを検出するために，上の条件のどれにもあてはまらない場合はエラーを起こすようにする
        # スペルミスが無ければ，このブロックにはたどり着かない
        raise ValueError

print(depression_score, relationship_score, aggression_score, anxiety_score)

# %%

# DataFrameに変換する

summary = pd.DataFrame({
    'yes_ratio': [yes_cases/total_cases],
    'relationship': [relationship_score],
    'anxiety': [anxiety_score],
    'aggression': [aggression_score],
    'depression': [depression_score],
})

# %% [markdown]

# ## 練習 最も汚いデータの部類の集計をする。
#
# data/03.csv ファイル内の，Yes 選択率を求めよう！
#
# data/03.csv の Yes/No 選択において，Yes が左側に呈示された場合は category 列の値が ly，
# Yes が右側に呈示された場合は ry となる。
# そして，answer 列には，参加者の選択が左右どちらだったがが示されている。

# %%

# data/03.csv ファイル内の，Yes 選択率を求めよう。

dirtiest_data = pd.read_csv('data/03.csv')

total_cases = 0
yes_cases = 0

for i, row in dirtiest_data[dirtiest_data['action'] == 'yesno'].iterrows():
    total_cases += 1
    yes_cases += (row['category'] == 'ly' and row['answer'] == 'l')\
        or (row['category'] == 'ry' and row['answer'] == 'r')

print(yes_cases, total_cases)

# %%

# %%

# ### 特性質問紙の集計をする。
#
# groupby を用いることは可能だが，ループで求める方法でやってみる。
#
# 文字列の，endswith メソッドで，その文字列の末尾が一致するかを求めることができる。
#
# 'Hello World'.endswith('World')
#
# の実行結果は，True になるし，
#
# 'Hello World'.endswith('xxxxx')
#
# の実行結果は，False になる。

# %%

# 今回のデータは，末尾に尺度の名前がついている。

'4-anxiety'.endswith('anxiety')


# %%

# ループしながら各尺度の合計点数を求める。

depression_score = 0
relationship_score = 0
aggression_score = 0
anxiety_score = 0
total_cases = 0

for i, row in dirtiest_data[dirtiest_data['action'] == 'subjective'].iterrows():
    total_cases += 1
    if row['category'].endswith('depression'):
        depression_score += int(row['answer'])
    elif row['category'].endswith('relationship'):
        relationship_score += int(row['answer'])
    elif row['category'].endswith('anxiety'):
        anxiety_score += int(row['answer'])
    elif row['category'].endswith('aggression'):
        aggression_score += int(row['answer'])
    else:
        # スペルミスを検出するために，上の条件のどれにもあてはまらない場合はエラーを起こすようにする
        # スペルミスが無ければ，このブロックにはたどり着かない
        raise ValueError

print(depression_score, relationship_score, aggression_score, anxiety_score)


# %%