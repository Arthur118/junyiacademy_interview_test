def sentence_reverse(input_data):

    elements = []       # 儲存句子中的每個單字
    sentence = []       # 儲存字母以構成單字
    out_sentence = []   # 儲存已顛倒過的單字

    input_data += " "  # 為句尾最後一個單字做出間格
    for i in input_data:

        # 當遇到間格時，儲存單字
        if i == ' ':
            elements.append(''.join(map(str, sentence)))  # 將element list中添加以組合好的單字
            sentence = []
        # 否則繼續往sentence list裡添加元素
        else:
            sentence.append(i)

    for i in range(len(elements)):  # 開始分別處理element list中的每個單字
        string = list(elements[i])
        rev_string = []  # 用來儲存顛倒後的元素

        # 將單字顛倒過來
        for j in range(len(string) - 1, -1, -1):
            rev_string.append(string[j])

        # 最後將已經顛倒過來的字母串成單字，添加到out sentence list當中
        out_sentence.append(''.join(map(str, rev_string)))

    return ' '.join(map(str, out_sentence))  # 以空格分開單字與單字以形成句子


if __name__ == '__main__':  # 加上這行是為了不在unittest中詢問使用者
    print(sentence_reverse(input("Enter a sentence: ")))
