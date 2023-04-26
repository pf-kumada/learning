import os
import sys

print("------------------------------------------------------------------------------------")

# 指定したフォルダ名を変数pathに格納する
#path = sys.argv[1]
path = "C:/Users/user/Documents/learning/study/wordCount2text"

# ループ内で使用する変数を定義する
file_word = {}
tmp = ""
file_first = set()
file_escape = set()

# 辞書の値を設定する関数定義（初回）
def add_first(file_first, current_dir, files_list, i, file_escape, file_word, tmp):
    file_first.add(os.path.join(current_dir,files_list[i]))
    file_escape = file_first.copy()
    file_word[tmp] = [1, file_escape]

# 辞書の値を設定する関数定義（二回目以降）
def add_second(file_word, tmp, current_dir, files_list, i):
    file_word[tmp][1].add(os.path.join(current_dir,files_list[i]))
    file_word[tmp][0] = file_word[tmp][0] + 1

# フォルダ内、サブフォルダ内のファイルを全て取得する
"""
# withを使用する場合
for i in range(len(path_list)):
   with open(path_list[i], encoding="utf-8") as file:
        file_data = file.read()
"""

# withを使用しない場合
for current_dir, sub_dirs, files_list in os.walk(path):
    for i in range(len(files_list)):
        base, ext = os.path.splitext(files_list[i])
        if ext == ".txt":
            file = open(os.path.join(current_dir,files_list[i]), encoding="utf-8")
            file_data = file.read()
            file.close()
            print(os.path.join(current_dir,files_list[i]))


    # ファイルの中身を1文字ずつ取り出す
            for char in file_data:

                x = ord(char)
                # スペースだった場合、スペースまでのcharを1つの単語にして、file_wordのキーに設定し、値に1を加算する
                # 各単語に対してどのファイルから吐き出されたものなのかそれぞれ辞書の値（リスト）の[1]要素目に出力する
                if(x != 45 and x <= 47 or 58 
                <= x <= 64 or 91 <= x <= 94 or x == 96 or 123 <= x <= 127):
                    if(tmp in file_word):
                        add_second(file_word, tmp, current_dir, files_list, i)
                    # 半角スペースが二回以上続いた場合を考慮する
                    elif(tmp == ""):
                        continue
                    # 単語が一回目の出現の場合
                    else:
                        add_first(file_first, current_dir, files_list, i, file_escape, file_word, tmp)
                    # 文字を格納する為のtmp、一回目の単語が出現したファイル名を格納するfile_firstの中身を空にする
                    tmp = ""
                    file_first.discard(os.path.join(current_dir,files_list[i]))

                # tmpに一文字追加する
                else:
                    tmp += char

            # 改行などが入っていない場合、ファイルが連結されてしまうのでファイル単位で区切るようにする
            if not tmp == "":
                if(tmp in file_word):
                    add_second(file_word, tmp, current_dir, files_list, i)
                    tmp = ""
                else:
                    add_first(file_first, current_dir, files_list, i, file_escape, file_word, tmp)
                    tmp = ""
                    file_first.discard(os.path.join(current_dir,files_list[i]))

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
    print("[単語]:" + fk[i] + "[出現回数]:" + str(fv[i][0]))
    for pathname in fv[i][1]:
        print("    [ファイル名]:" + pathname)