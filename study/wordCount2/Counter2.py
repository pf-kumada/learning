import glob

print("------------------------------------------------------------------------------------")

# 指定したフォルダ内において、txtファイル一覧を取得
path_list = glob.glob("C:/Users/user/Documents/learning/study/wordCount2/*.txt")
print(path_list)

"""
# 取得したファイル一覧を一行ずつ表示
for file in path_list:
    print(file)



    file_word = dict(zip(char))
    print(file_word)
"""
file_word = {}
tmp = ""

# フォルダ内のファイルを全て取得する(with使わない)
for i in range(len(path_list)):
    with open(path_list[i], encoding="utf-8") as file:
        file_data = file.read()




# ファイルの中身を1文字ずつ取り出す
    for char in file_data:
# スペースだった場合、スペースまでのcharを1つの単語にして、file_wordのキーに設定し、値に1を加算する。
        if(char == " " or char == "," or char == ":" or char == "\n" or char == "、" or char == "。" or char == ";"):
            if(tmp in file_word):
                    file_word[tmp] = [file_word[tmp][0] + 1, {file_word[tmp][1]}.add(path_list[i])]

            else:
                    file_word[tmp] = [1, {file_word[tmp][1]}.add(path_list[i])]
            tmp = ""            
        else:
                tmp += char        
    if not tmp == "":
        if(tmp in file_word):
            file_word[tmp] = [file_word[tmp][0] + 1, {file_word[tmp][1]}.add(path_list[i])]
            tmp = ""  
        else:
            file_word[tmp] = [1, {file_word[tmp][1]}.add(path_list[i])]
            tmp = ""     


# 辞書のキーをリストに取り出す
file_keylist = list(file_word.keys())
fk = file_keylist


# 辞書の値ををリストに取り出す
file_valuelist = list(file_word.values())
fv = file_valuelist


# 使用頻度の多い順にソートする
# 要素番号の0番目とそれ以降を一つずつ比較し、先頭に最大の値が来るようにする
i = 0
while i < len(fv):
    j = 1

    while j < len(fv) - i:
        if fv[i] < fv[i+j]:
            cmtpval = fv[i]
            cmtpkey = fk[i]
            fv[i] = fv[i+j]
            fk[i] = fk[i+j]
            fv[i+j] = cmtpval
            fk[i+j] = cmtpkey
            j += 1
        else:
            j += 1

    i += 1


# 結果出力
for i in range(len(fk)):
	print(fk[i] + ":" + str(fv[i]))

# 各単語に対してどのファイルから吐き出されたものなのかそれぞれ出力する
