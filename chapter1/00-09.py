
# coding: utf-8

# In[1]:

# 00.
s = 'stressed'
s[-1::-1]


# In[2]:

# 01.
s = 'パタトクカシーー'
s[1::2]


# In[3]:

# 02.
p = 'パトカー'
t = 'タクシー'
s = ''
for i in range(4):
    s += p[i]+t[i]
s


# In[4]:

# 03.
s = "Now I need a drink, alcoholic of course,     after the heavy lectures involving quantum mechanics."
sl = list(map(len, s.split()))
sl


# In[5]:

# 04.
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine.    New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sd = {}
for i, w in enumerate(list(s.split())):
    j = i+1
    if j in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        sd[w[:1]] = j
    else:
        sd[w[:2]] = j
sd


# In[6]:

# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
# 引数：文字列かリスト
# 戻り値：単語bi-gram、文字bi-gram
def ngram(sequence, n = 2, sep = ''):
    #リストなら単語区切り、文字列なら単語が来ると想定
    seq = list(sequence[:])
    # print(seq)
    i = 0
    while i < len(seq) - n + 1:
        print(sep.join([seq[i],seq[i+1]]))
        i += 1

s = "I am an NLPer"
ngram(s.split(), sep='-'); print()
for w in s.split():
    ngram(w); print()
ngram(s); print()


# In[7]:

def ngram(sequence, n = 2, sep = ''):
    #リストなら単語区切り、文字列なら単語が来ると想定
    seq = list(sequence[:])
    rtn = []
    for i in range(0,len(seq)-n+1):
        rtn.append(sep.join([seq[i],seq[i+1]]))
    return rtn

x="paraparaparadise"
y="paragraph"
# 和集合，積集合，差集合を求めよ．
# 'se'というbi-gramがXおよびYに含まれるかどうかを調べよ
X = set( ngram(x) )
Y = set( ngram(y) )
print(X|Y)
print(X&Y)
print(X-Y, Y-X, X^Y)


# In[8]:

# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
def ps(x,y,z):
    print("{0}時の{1}は{2}".format(x,y,z))
    return
ps(12,'気温',22.4)


# In[9]:

# 関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．
def cipher(w):
    r = ''
    for c in w[:]:
        if c.islower():
            c = chr( 219 - ord(c) )
        r += c
    return r

cipher('Hello world!')
cipher(cipher('Hello world again!'))


# In[10]:

# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
from random import shuffle
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
# を与え，その実行結果を確認せよ．
def shuffleWord(sentence):
    sts = sentence.split()
    result = []
    for i in sts:
        if len(i) > 4:
            mid = list(i[1:-1])
            shuffle(mid)
            i = i[0] + ''.join(mid) + i[-1]
        result.append(i)
    return ' '.join(result)

shuffleWord(s)


# In[ ]:



