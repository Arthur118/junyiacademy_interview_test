def select_num(num):

    num_list = []           # 儲存1~使用者輸入的數字
    multiples_of_3 = []     # 儲存3的倍數
    multiples_of_5 = []     # 儲存5的倍數
    multiples_of_3_5 = []   # 儲存3和5的公倍數
    rest_num = []           # 儲存剩下的數字

    for i in range(1, num+1):
        num_list.append(i)
    if __name__ == '__main__':  # 加上這行是為了不在unittest中顯示
        print(f'所有的數字是: {str(num_list).strip("[]")}')

    for i in num_list:
        if i % 3 == 0 and i % 5 == 0:   # 取3和5的公倍數
            multiples_of_3_5.append(i)
            rest_num.append(i)
        elif i % 3 == 0:                # 取3的倍數
            multiples_of_3.append(i)
        elif i % 5 == 0:                # 取5的倍數
            multiples_of_5.append(i)
        else:                           # 取剩下的數字
            rest_num.append(i)

    if __name__ == '__main__':  # 加上這行是為了不在unittest中顯示
        print(f'其中{str(multiples_of_3).strip("[]")}被剔除;'
              f'{str(multiples_of_5).strip("[]")}被剔除;'
              f'但是{str(multiples_of_3_5).strip("[]")}被保留\n'
              f'所以剩下的數字是:{str(rest_num).strip("[]")} 因此')

    return f'Output:{len(rest_num)}'  # 做為unittest判斷準則


if __name__ == '__main__':  # 加上這行是為了不在unittest中詢問使用者
    print(select_num(int(input("input:"))))
