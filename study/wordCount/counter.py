
import os
from collections import Counter


# 引数にテキストファイル名を指定しテキストファイル取得
path = "C:/Users/user/Documents/study/wordCount/sample.txt"
fileName = os.path.basename(path)

# ファイルの中身の文字列を取得
with open(fileName, encoding="utf-8") as file:
	file_data = file.read()


# 文字列がどんな文字でできているか、カウント(重複含む)
myword = file_data
mycounter = Counter(myword)


# 結果出力
print(mycounter)

