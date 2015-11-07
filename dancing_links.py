sudoku = [[8,0,0,0,0,0,0,0,0],
          [0,0,3,6,0,0,0,0,0],
          [0,7,0,0,9,0,2,0,0],
          [0,5,0,0,0,7,0,0,0],
          [0,0,0,0,4,5,7,0,0],
          [0,0,0,1,0,0,0,3,0],
          [0,0,1,0,0,0,0,6,8],
          [0,0,8,5,0,0,0,1,0],
          [0,9,0,0,0,0,4,0,0]]

dancing_links = []

def get_dancing_links():
    first_links = [0 for i in range(324)]
    dancing_links.append(first_links)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                dancing_links[0][i * 9 + j] = 1
                dancing_links[0][80 + i * 9 + sudoku[i][j]] = 1
                dancing_links[0][161 + j * 9 + sudoku[i][j]] = 1
                num_row = i / 3
                num_col = j / 3
                dancing_links[0][242 + (num_row * 3 + num_col) * 9 +sudoku[i][j]] = 1
    for i in range(9):
        for j in range(9):
            if dancing_links[0][i * 9 + j] == 0:
                num_row = i / 3
                num_col = j / 3
                for k in range(9):
                    if dancing_links[0][81 + i * 9 + k] == 0:
                        if dancing_links[0][162 + j * 9 + k] == 0:
                            if dancing_links[0][243 + (num_row * 3 + num_col) * 9 + k] == 0:
                                first_links = [0 for m in range(325)]
                                first_links[i * 9 + j] = 1
                                first_links[80 + i * 9 + k + 1] = 1
                                first_links[161 + j * 9 + k + 1] = 1
                                first_links[242 + (num_row * 3 + num_col) * 9 + k + 1] = 1
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
            mark_succ = True
            for j in range(aim_num):
                if dancing_links[i][j] == 1:
                    if dancing_links[0][j] == 1:
                        mark_succ = False
                        break
                    change_col_list.append(j)
                    dancing_links[0][j] = 1
                    for k in range(1, link_len):
                        if dancing_links[k][j] == 1:
                            if dancing_links[k][aim_num] == 0:
                                dancing_links[k][aim_num] = 1
                                change_row_list.append(k)
            if mark_succ == True:
                mark_succ = use_dancing_links(num_node + 1, aim_num)
                if mark_succ == True:
                    position_x = change_col_list[0] / 9
                    position_y = change_col_list[0] % 9
                    num = (change_col_list[1] - 81) - position_x * 9 + 1
                    sudoku[position_x][position_y] = num
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
mark_succ = use_dancing_links(0, 324)
for i in range(len(sudoku)):
    print sudoku[i]