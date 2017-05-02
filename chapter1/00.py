
# coding: utf-8

# In[20]:

# 00.
s = 'stressed'
s[-1::-1]


# In[21]:

# 01.
s = 'パタトクカシーー'
s[1::2]


# In[36]:

p = 'パトカー'
t = 'タクシー'
s = ''
for i in range(4):
    s += p[i]+t[i]
s


# In[39]:

s = "Now I need a drink, alcoholic of course,     after the heavy lectures involving quantum mechanics."
sl = list(map(len, s.split()))
sl


# In[48]:

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine.    New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sd = {}
for i, w in enumerate(map(lambda a: a[:2], s.split())):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        sd[w[:1]] = i
    sd[w] = i
sd


# In[73]:

# http://d.hatena.ne.jp/jetbead/20110904/1315147133
def biGram(sorl):
    if type(sorl) == str:
        sl = sorl.split()
        if type(sl) != list:
            sl = [sl]
    else:
        sl = sorl
    print(sl)
    word_biGram = set()
    sent_biGram = set()
    i = 0
    while i < len(sl):
        if i != len(sl)-1: #not last one. cuz until n-1;
            word_biGram.add(sl[i]+'-'+sl[i+1])
        j = 0
        while j < len(sl[i])-1:
            sent_biGram.add(sl[i][j]+sl[i][j+1])
            j += 1
        i += 1
    return {'w': word_biGram, 's': sent_biGram}

biGram("I am an NLPer")


# In[74]:

s1 = "paraparaparadise"
s2 = "paragraph"
biGram(s1)
X = biGram(s1)['w']
Y = biGram(s2)['w']
# print(X, Y)
# print(X or Y)


# In[ ]:



