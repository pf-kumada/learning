
import os
import sys


# 引数にテキストファイル名を指定しテキストファイル取得
path = sys.argv[1]
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


# 辞書のキーをリストに取り出す
file_charlist = list(file_char.keys())
fc = file_charlist


# 辞書の値ををリストに取り出す
file_valuelist = list(file_char.values())
fv = file_valuelist


# 要素番号の0番目とそれ以降を一つずつ比較し、先頭に最大の値が来るようにする
i = 0
while i < len(fv):
	j = 1

	while j < len(fv) - i:
		if fv[i] < fv[i+j]:
			cmtpval = fv[i]
			cmtpkey = fc[i]
			fv[i] = fv[i+j]
			fc[i] = fc[i+j]
			fv[i+j] = cmtpval
			fc[i+j] = cmtpkey
			j += 1
		else:
			j += 1

	i += 1


# 結果出力
for i in range(len(fc)):
	print(fc[i] + ":" + str(fv[i]))
