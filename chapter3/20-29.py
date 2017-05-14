
# coding: utf-8
第3章: 正規表現

Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．

1行に1記事の情報がJSON形式で格納される
各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される

20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．

22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．

25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
# In[12]:

# 20
import json
wikidata = list()
with open('jawiki-country.json') as wf:
    lines = wf.readlines()
    wikidata = list(map(json.loads, lines))

for wikiline in wikidata:
    if wikiline['title'] == 'エジプト':
        print(wikiline['text'])
        egypt = wikiline['text']


# In[18]:

egypt_l = egypt.split('\n')
categories = list()
for i in egypt_l:
    if 'Category' in i:
        print(i)
        categories.append(i)


# In[20]:

for i in categories:
    print(i[11:-2])


# In[24]:

for i in egypt_l:
    if i[0:2] == '==':
        n = len(i.split()[0])-1
        print(i, 'level:', n)


# In[42]:

import re
mediafiles = []
p = r'ファイル:[0-9a-zA-Z ,._-]*'
for i in egypt_l:
    if 'ファイル:' in i:
#         mediafiles.append(i)
        mediafiles.append(re.findall(p, i)[0])
with open('EgyptMediaFiles.md', 'w') as f:
    for i in mediafiles:
        f.write('['+i+'](https://ja.wikipedia.org/wiki/'+i+')  \n')


# In[59]:

# 25
# 26
import re
def removeMarkup(string):
#     p = r'(\{\{|\'\'|\"\"\"|\'\'\')(?P<result>.*)(\}\}|\'\'|\"\"\"|\'\'\')'
#     m = re.match(p, string)
#     result = m.group('result') if m else string
    result = re.sub(r'(\{\{|\}\}|\[\[|\]\]|\'\'|\"\"\"|\'\'\')', '', string)
    return result

def removeHTMLtag(string):
    p = r'<[a-zA-Z]+ .*/[a-zA-Z]*>'
    result = re.sub(p, '', string)
    return result

in_range = False
baseInfoCountry = {}
for i in egypt_l:
    if '{{基礎情報' in i:
        in_range = True
        continue
    if in_range:
        if i == '}}': break
        line = i.split(' =')
        s = ''.join(line[1:])
        s = removeMarkup(s)
        s = removeHTMLtag(s)
        baseInfoCountry[line[0][1:]] = s
        
baseInfoCountry


# In[61]:

flag_url = 'https://ja.wikipedia.org/wiki/ファイル:'+baseInfoCountry['国旗画像']
flag_url


# In[ ]:



