import glob


# 指定したフォルダ内において、txtファイル一覧を取得
path_list = glob.glob("C:/Users/user/Documents/learning/study/wordCount2/*.txt")
print(path_list)

"""
# 取得したファイル一覧を一行ずつ表示
for file in path_list:
    print(file)
"""

# フォルダ内のファイルを全て取得する
for i in range(len(path_list)):
    with open(path_list[i], encoding="utf-8") as file:
        file_data = file.read()

file_word = {}
tmp = ""
# ファイルの中身を

for char in file_data:
    if(char = " "):
        file_word[char] = char
        if(char in file_char):
                file_word[char] += 1
        else:
                file_word[char] = 1
    else:
            tmp += char


# 使用頻度の多い順にソートする



# 各単語に対してどのファイルから吐き出されたものなのかそれぞれ出力する
