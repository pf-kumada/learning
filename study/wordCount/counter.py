
import os
import sys
from collections import Counter


# 引数にテキストファイル名を指定しテキストファイル取得
path = "C:/Users/user/Documents/study/wordCount/sample.txt"
fileName = os.path.basename(path)

# ファイルの中身の文字列を取得
with open(fileName, encoding="utf-8") as file:
	file_data = file.read()


# ファイルの中身を格納する辞書を定義
file_char = {} 


# 変数charにファイルの中身を出力し、ファイルから取得したキーが重複している場合、値に1を加算する
for char in file_data:
	if (char in file_char):
		file_char[char] += 1

	else:
		file_char[char] = 1


# 辞書のキーをリストに変換して、要素数文回す
for file_charlist in file_char.keys():
	print(file_charlist + ":" + str(file_char[file_charlist]))
