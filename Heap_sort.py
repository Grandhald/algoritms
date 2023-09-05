from random import randint as rnd

def sub_value_list(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]



def binary_wood(lst_number, end_pos):
    index = end_pos - 1
    while index != 0:
        if index % 2 == 0:
            if lst_number[index] > lst_number[(index-2)//2]:
                sub_value_list(lst_number, index, (index-2)//2)
        else: 
            if lst_number[index] > lst_number[(index-1)//2]:
                sub_value_list(lst_number, index, (index-1)//2)
        index -= 1


def heap_sort(list_number):
    start_pos, end_pos = 0, len(list_number)
    while start_pos < end_pos:
        binary_wood(list_number, end_pos)
        sub_value_list(list_number, start_pos, end_pos - 1)
        end_pos -=1
    
     
     
     
        
        
list_num = [rnd(-10,10) for i in range(10)]
heap_sort(list_num)
print()
print(list_num)