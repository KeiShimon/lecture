# %% [markdown]

# ## データの集計 part 1

# ここからはデータの集計を行っていきます。
#
# ### 状況
#
# 実験参加者のデータを集計していることを想像してください。
#
# - 実験
#   - 参加者は，Yes/No で答えられる問題60問に回答しました
#   - さらに，40問から成る特性質問紙に回答しました。
# - 質問紙
#   - 特性質問紙の各項目は，短文での質問に1から7のリッカート尺度で回答を求める形式でした。
#   - 特性質問紙で，抑うつ，攻撃性，人間関係，不安の4つの尺度を測定しました。
#   - それぞれの尺度の得点は，10個の質問への回答の合計得点とします。
#
#
# これからあなたは，この参加者のデータの，Yes選択率と，各尺度の得点を求めたいです。


# %%

# とりあえずインポート

import pandas as pd

# %%

# 比較的きれいなデータの場合
# data フォルダ内の 01.csv を読み込む。

clean_data = pd.read_csv('data/01.csv')

# 全体を表示
clean_data

# %%

# Yes 選択率を計算してみる

# 分母は60ということは実験デザインからわかっているが，データから60と取得する方法も紹介しておく。
# action が yesno である場合が，参加者のYes/No の選択の機会の総数である

# まず，True/False を出力させることができるのを思い出そう

clean_data['action'] == 'yesno'


# %%

# True は 1 ，False は 0 として扱うことを利用すると，
# その列の合計を求めることで，True の数がわかる

total_cases = sum(clean_data['action'] == 'yesno')
total_cases

# %%

# Yes の回答数についても，Yes/No の回答が 1/0 で保存されているので，合計を利用する。
# sum メソッドを使うパターンでやってみる。

yes_cases = clean_data[clean_data['action'] == 'yesno']['answer'].sum()
yes_cases

# %%

# 次に，特性質問紙の集計をする。

# aggression, anxiety, relationship, depression の4つしかないことがわかっているので，
# それらのグループに分けることができる。
# groupby メソッドが使える。

grouped = clean_data.groupby(clean_data['category'])

grouped

# %%

# DataFrameGroupBy object とはなんぞや？
# https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html

# sum() count() mean() indices groups あたりは登場頻度が高そうなので紹介する。

print(grouped.groups)  # グループに属する要素のインデックスラベル
print()
print()

print(grouped.indices)  # グループに属する要素のインデックス（今回はラベルとインデックスが等しい）
print()
print()

print(grouped.sum())
print()
print()

print(grouped.count())
print()
print()

print(grouped.mean())
print()
print()

# %%

# 今回欲しいのは，合計のデータ。
# 転置した形の方が扱いやすいので，転置させたデータを保管する。

summary = grouped.sum().T

# output
summary

# category 列は，インデックス列名と，インデックスラベルである点に注意


# %%

# summary に， yes 選択率のデータを追加する。

# summary['yes_ratio'] = [yes_cases / total_cases]
# これでも追加できるけど，一番右に追加される。

# 一番右でなく，特定の位置にデータを挿入したい場合は， insert メソッドを用いる。
# 今回は，aggression の左に，yes_ratio という列を作成し，データを追加したいとする。

# まず，aggression が何番目のインデックスか知る必要がある。(今回は明らかに0だけど）


# %%

# 列名の一覧は，.columns で得られる。

summary.columns

# %%

# get_index でインデックス番号を得る。

summary.columns.get_loc('aggression')

# %%

# aggression の左にinsert する。
# つまり，新しいデータ列 yes_ratio を，本来 agression のあった位置に挿入し，
# もともとあったデータ列たちは右に押される。

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.insert.html

summary.insert(0, 'yes_ratio', [yes_cases/total_cases])

# show
summary

# %%

# これで1人分のデータをまとめることができた！
# 複数のファイルで同じ操作を繰り返し，1つの .csv ファイルにまとめる方法は後ほど...
