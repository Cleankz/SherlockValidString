def SherlockValidString(input_str): # s - input_str
    str_to_list = list(input_str)
    count_array = []
    index = []
    count_of_min_num = 0 # min - count_of_min_num
    count_of_max_num = 0 # max - count_of_max_num
    count_of_equal_num = 0 # norm - count_of_equal_num
    count_of_other_num = 0 # other - count_of_other_num
    for str in input_str:
        count_of_symb = input_str.count(str) # count - count_of_symb
        count_array.append(count)
    count_symb = 0 # sum - count_symb
    for j in range(len(count_array) -1):
        count_symb +=count_array[j]
    mid_of_str = sum / len(input_str) # mid - mid_of_str
    m = (mid_of_str % 1) * 10
    if m >= 5:
        m = (sum // len(input_str)) + 1
    else:
        m = (sum // len(input_str))
    for i in range(len(input_str)):
        if input_str.count(input_str[i]) < m:
            count_of_min_num +=1
        elif input_str.count(input_str[i]) > m:
            count_of_max_num += 1
        elif input_str.count(input_str[i]) == m:
            count_of_equal_num += 1
    if   count_of_min_num == 0 and count_of_max_num == 0 :
        return True
    elif count_of_min_num == 1 and count_of_max_num == 0 or count_of_max_num == 1 and count_of_min_num == 0:
        return True
    elif count_of_equal_num - count_of_min_num == 1 or count_of_equal_num - count_of_max_num == 1:
        return True
    elif count_of_min_num - count_of_equal_num == 1 and count_of_max_num == 0:
        return True
    elif count_of_max_num - count_of_equal_num == 1 and count_of_min_num == 0:
        return True
    else:
        return False
