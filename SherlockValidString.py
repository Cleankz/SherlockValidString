def SherlockValidString(s):
    str_to_list = list(s)
    count_array = []
    index = []
    min = 0
    max = 0
    norm = 0 
    other = 0
    for str in s:
        count = s.count(str)
        count_array.append(count)
    sum = 0
    for j in range(len(count_array) -1):
        sum +=count_array[j]
    mid = sum / len(s)
    m = (mid % 1) * 10
    if m >= 5:
        m = (sum // len(s)) + 1
    else:
        m = (sum // len(s))
    for i in range(len(s)):
        if s.count(s[i]) < m:
            min +=1
        elif s.count(s[i]) > m:
            max += 1
        elif s.count(s[i]) == m:
            norm += 1
    if   min == 0 and max == 0 :
        return True
    elif min == 1 and max == 0 or max == 1 and min == 0:
        return True
    elif norm - min == 1 or norm - max == 1:
        return True
    elif min - norm == 1 and max == 0:
        return True
    elif max - norm == 1 and min == 0:
        return True
    else:
        return False