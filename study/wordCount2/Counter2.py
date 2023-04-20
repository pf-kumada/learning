import glob

print("------------------------------------------------------------------------------------")

# 指定したフォルダ内において、txtファイル一覧を取得する
path_list = glob.glob("*.txt")
print(path_list)

# ループ内で使用する変数を定義する
file_word = {}
tmp = ""
file_first = set()
file_escape = set()

# フォルダ内のファイルを全て取得する
"""
# withを使用する場合
for i in range(len(path_list)):
   with open(path_list[i], encoding="utf-8") as file:
    file_data = file.read()
"""
# withを使用しない場合
for i in range(len(path_list)):
    file = open(path_list[i], "r", encoding="utf-8")
    file_data = file.read()
    file.close()

    # ファイルの中身を1文字ずつ取り出す
    for char in file_data:

        # スペースだった場合、スペースまでのcharを1つの単語にして、file_wordのキーに設定し、値に1を加算する
        # 各単語に対してどのファイルから吐き出されたものなのかそれぞれ辞書の値（リスト）の[1]要素目に出力する
        if(char == " " or char == "," or char == ":" or char == "\n" or
           char == "、" or char == "。" or char == ";" or char == "[" or char == "'"):
            if(tmp in file_word):
                # 返り値None(file_wordの中には追加はされている)
                file_word[tmp][1].add(path_list[i])
                file_word[tmp][0] = file_word[tmp][0] + 1
            # 半角スペースが二回以上続いた場合を考慮する
            elif(tmp == ""):
                continue
            # 単語が一回目の出現の場合
            else:
                file_first.add(path_list[i])
                file_escape = file_first.copy()
                file_word[tmp] = [1, file_escape]
            # 文字を格納する為のtmp、一回目の単語が出現したファイル名を格納するfile_firstの中身を空にする
            tmp = ""
            file_first.discard(path_list[i])

        # tmpに一文字追加する
        else:
            tmp += char

    # 改行などが入っていない場合、ファイルが連結されてしまうのでファイル単位で区切るようにする
    if not tmp == "":
        if(tmp in file_word):
            file_word[tmp][1].add(path_list[i])
            file_word[tmp][0] = file_word[tmp][0] + 1
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




# 完成までに足らないもの
# ・単語の区切りの条件式を手動で限定しない（半角英数字、ハイフン、アンダースコア以外で判別（バイトコード使う））
# ・出力の表示結果の変更
# ・関数にまとめる