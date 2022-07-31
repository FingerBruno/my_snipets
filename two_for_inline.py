lst = [[1,2,3], [4,5,6], [7,8,9]]

square_numbers_list = []
for number in lst:
    for n in number:
        square_numbers_list.append(n**2)


better_square_number_lst = [n**2 for number in lst for n in number]
print(better_square_number_lst)