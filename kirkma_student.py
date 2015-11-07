dancing_links = []

ans_set = [[],[],[],[],[],[],[]]

def get_dancing_links():
    first_links = [0 for i in range(330)]
    for i in range(0, 330, 23):
        first_links[i] = 1
    dancing_links.append(first_links)
    for i in range(15):
        for j in range(i + 1, 15):
            for k in range(j + 1, 15):
                for l in range(7):
                    first_links = [0 for m in range(331)]
                    num1 = i * 22
                    num2 = j * 22
                    num3 = k * 22
                    first_links[num1 + j] = 1
                    first_links[num1 + k] = 1
                    first_links[num1 + l + 15] = 1
                    first_links[num2 + i] = 1
                    first_links[num2 + k] = 1
                    first_links[num2 + l + 15] = 1
                    first_links[num3 + i] = 1
                    first_links[num3 + j] = 1
                    first_links[num3 + l + 15] = 1
                    dancing_links.append(first_links)

def use_dancing_links(num_node, aim_num):
    if num_node == aim_num:
        return True
    if dancing_links[0][num_node] == 1:
        return use_dancing_links(num_node + 1, aim_num)
    link_len = len(dancing_links)
    change_col_list = []
    change_row_list = []
    for i in range(1, link_len):
        if dancing_links[i][num_node] == 1 and dancing_links[i][aim_num] == 0:
            dancing_links[i][aim_num] = 1
            sample_succ = True
            for j in range(aim_num):
                if dancing_links[i][j] == 1:
                    if dancing_links[0][j] == 1:
                        sample_succ = False
                        break
                    change_col_list.append(j)
                    dancing_links[0][j] = 1
                    for k in range(1, link_len):
                        if dancing_links[k][j] == 1:
                            if dancing_links[k][aim_num] == 0:
                                dancing_links[k][aim_num] = 1
                                change_row_list.append(k)
            if sample_succ == True:
                sample_succ = use_dancing_links(num_node + 1, aim_num)
                if sample_succ == True:
                    person1 = change_col_list[0] / 22
                    person2 = change_col_list[0] % 22
                    person3 = change_col_list[1] % 22
                    weekday = change_col_list[2] % 22 - 15
                    ans_set[weekday].append([person1, person2, person3])
                    return True
            for item in change_col_list:
                dancing_links[0][item] = 0
            for item in change_row_list:
                dancing_links[item][aim_num] = 0
            change_row_list = []
            change_col_list = []
            dancing_links[i][aim_num] = 0
    return False

get_dancing_links()
mark_succ = use_dancing_links(0, 330)
for i in range(7):
    print ans_set[i]