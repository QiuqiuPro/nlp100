#!/usr/bin/env python3
import sys
# 末尾のN行を出力 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
# supposed usage
#$ py 15.py 13 #=> N=13
N = int(sys.argv[1])
with open('./hightemp.txt') as io:
    for i in range(N):
        print(io.readline()[:-1])
