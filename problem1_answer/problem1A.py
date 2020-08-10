def reverse_string(input_str):

    string = list(input_str)  # 將輸入的字串分為一個一個元素
    rev_string = []           # 儲存顛倒後的元素
    # 顛倒元素們的順序
    for i in range(len(string)-1, -1, -1):
        rev_string.append(string[i])      # 加入每個顛倒後的元素到rev_string中

    return ''.join(map(str, rev_string))  # 組合每個顛倒後的元素


if __name__ == '__main__':  # 加上這行是為了不在unittest中詢問使用者
    print(reverse_string(input("Enter a string: ")))
