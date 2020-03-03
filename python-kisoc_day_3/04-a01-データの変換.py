# %% [markdown]

# # 集計する

# いよいよデータの変換・集計の時間です！

# ここからは，DataFrame の有用なメソッドを紹介しながら，Python を使った集計を体験します。

# ## 目標

# - Python を用いてデータを変換・集計する
# - DataFrame の便利なメソッドを知り，ループを回せるようになる

# ここからは，ライブコードを写しながら進めます。

# %%
# まずはインポート

import pandas as pd

# %% [markdown]

# ## シンプルなケース： 単位の変換

# 運動と身体のデータを用いて，データの変換のしかたを学ぶ。

# %%

# まずは運動と身体のデータをもう一度読み込んでみよう。
# データは，同じフォルダ内の excercise.csv に用意したので，これを読み込む。
# csv ファイルの読み込みには，read_csv メソッドを用いる。

df_exercise = pd.read_csv('excercise.csv')
df_exercise.head()

# %%

# Waist はインチ表示なので，センチメートルに変換したい。(2.54)
# Weight はポンド表示なので，キログラムに変換したい。(0.453592)

INCH_TO_CM = 2.54
POUND_TO_KG = 0.453592

# %%

# でも，元データは元データで残しておくのが望ましい。

# 列名に単位をつけて，インチもセンチメートルも両方残せばよい！
# 列名を変更するメソッド rename を用いて，列名に単位をつける。

df_exercise = df_exercise.rename(columns={'Weight': 'Weight_pound',
                                          'Waist': 'Waist_inch'})

df_exercise.head()

# %%

# Weight を変換したいので，Weight の列に係数をかけてみよう。

df_exercise.Weight_pound * POUND_TO_KG

# 列への演算は，全ての要素に適用される！ （ループを回さなくても良い）

# %%

# Weightに係数を掛けた列を追加する。

df_exercise['Weight_kg'] = df_exercise.Weight_pound * POUND_TO_KG
df_exercise.head()

# 追加の方法がディクショナリと同じことに気づいた？

# %%

# 練習
# Waist をセンチメートルに変換した列を追加してみよう。

df_exercise['Waist_cm'] = df_exercise.Waist_inch * INCH_TO_CM
df_exercise.head()

# %%

# 保存して終了する。
# to_csv メソッドを用いる。

# インデックスの有無に気を付ける
df_exercise.to_csv('excercise_modified.csv', index=None)

# %%

# 小数点が汚い！
# round メソッドで綺麗にしてから保存する。
df_exercise.round(4).to_csv('excercise_modified.csv', index=None)


# %%
