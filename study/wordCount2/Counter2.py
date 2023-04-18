import glob

print("------------------------------------------------------------------------------------")

# 指定したフォルダ内において、txtファイル一覧を取得
path_list = glob.glob("C:/Users/user/Documents/learning/study/wordCount2/test*.txt")
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
file_set = set()
file_first = set()
file_escape = set()
# フォルダ内のファイルを全て取得する(with使わない)
for i in range(len(path_list)):
   with open(path_list[i], encoding="utf-8") as file:
    file_data = file.read()
    
    file_set.add(path_list[i]) #返り値None(file_setの中には追加はされている)
    # file_word[tmp][1].add(path_list[i])

# ファイルの中身を1文字ずつ取り出す
    for char in file_data:
# スペースだった場合、スペースまでのcharを1つの単語にして、file_wordのキーに設定し、値に1を加算する。
# 各単語に対してどのファイルから吐き出されたものなのかそれぞれ辞書の値（リスト）の[1]要素目に出力する
        if(char == " " or char == "," or char == ":" or char == "\n" or char == "、" or char == "。" or char == ";" or char == "[" or char =="'"):
            if(tmp in file_word):
                    file_word[tmp] = [file_word[tmp][0] + 1, file_set] 

            else:
                    file_first.add(path_list[i])
                    file_escape = file_first.copy()
                    file_word[tmp] = [1, file_escape]
            tmp = ""            
            file_first.discard(path_list[i])
        else:
                tmp += char        
# 改行などが入っていない場合、ファイルが連結されてしまうのでファイル単位で区切るようにする
    if not tmp == "":
        if(tmp in file_word):
            file_word[tmp] = [file_word[tmp][0] + 1, file_set]
            tmp = ""  
        else:
            file_first.add(path_list[i])
            file_escape = file_first.copy()
            file_word[tmp] = [1, file_escape]
            tmp = ""
            file_first.discard(path_list[i])

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


