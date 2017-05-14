
# coding: utf-8

# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
# 
# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
# 
# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
# 
# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
# 
# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

# In[1]:

with open('hightemp.txt') as io:
    print(len(list(io)))


# In[2]:

import re
with open('hightemp.txt') as io:
    for line in io:
#         line = re.sub(r"\t+", " ", line)
        line = line.split()
        print(line)


# In[3]:

import re
with open('hightemp.txt') as io:
    for line in io:
        line = re.sub(r"\t+", " ", line)
        cols = line.split()
        for i in [1,2]:
            with open('col{0}.txt'.format(i), 'a') as io1:
                io1.write(cols[i-1]+'\n')


# In[4]:

with open('col1.txt') as c1, open('col2.txt') as c2, open('col1&2.txt', 'w') as c12:
    for i, j in zip(c1, c2):
        c12.write('{0}\t{1}\n'.format(i[:-1],j[:-1]))

15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
# In[5]:

# 15.py


# In[7]:

# 16
N = int(input('Enter N > '))
spl = ['']*N
with open('hightemp.txt') as f:
    for idx, line in enumerate(f.readlines()):
        i = idx%3
        spl[i] += line
    for i in range(N):
        print(i, ":\n", spl[i])


# In[7]:

# 17
with open('hightemp.txt') as f:
    lines = f.readlines()
    lines = list(map(lambda s: s.split(), lines))
    result = set(map(lambda i:i[0], lines))
    print(result)


# In[17]:

# 18
import pandas as pd
df = pd.read_csv('hightemp.txt', sep='\t', header=None)
result = df.sort_values(by=2)
# result


# In[28]:

# 19
import pandas as pd
df = pd.read_csv('hightemp.txt', sep='\t', header=None)
pref = list(df[0])
freq = dict()
for p in pref:
    if p in freq:
        freq[p] += 1
    else:
        freq[p] = 1
result = sorted(list(freq.items()), key=lambda i: -i[1])
for i in result:
    print(i[0])


# In[ ]:



