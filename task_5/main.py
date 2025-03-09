input_ls = [1,2,3,4,5,1,6,9,12]



def unique(ls):
  return f"Количество уникальных чисел: {len(list(set(ls)))}"

print(unique(input_ls))

def second_max_ls(ls):
    maximum = max(ls)
    for i in ls:
        if i == maximum:
            ls.remove(i)
    return f"Второе по велечине число: {max(ls)}"

print(second_max_ls(input_ls))

def numbers(ls):
    ls_num = []
    for i in ls:
        if i % 3 == 0:
            ls_num.append(i)
    return f"Числа делящиеся на 3: {ls_num}"


print(numbers(input_ls))