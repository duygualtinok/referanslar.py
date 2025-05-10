# en dizideki en buyuk kelimeyi bulmak *****************
"""def longest(strings:list):
    enbuyuk=strings[0]
    for kelime in strings:
        if len(enbuyuk)<len(kelime):
            enbuyuk=kelime
    return enbuyuk


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))"""

#----------- referanslarr---------------------------------

"""def double_items(numbers:list):
    new_list=[]
    for item in numbers:
        new_list.append(item*2)
    return new_list
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)"""

#------------------------------------------------------


"""def remove_smallest(numbers:list):
    enkucuk=min(numbers)
    numbers.remove(enkucuk)
if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)"""

#-----------------------------------------------

"""def add_item(my_list:list):
    new_item=10
    my_list_copy=my_list[:]
    my_list_copy.append(new_item)
    return my_list_copy

numbers = [1, 2, 3]
numbers2 = add_item(numbers)

print("original list:", numbers)
print("new list:", numbers2)"""

#-----------------------------------------------

"""def augment_all(my_list:list):
    new_list=[]
    for item in my_list:
        new_list.append(item+10)
    my_list=new_list
numbers = [1, 2, 3]
print("in the beginning:", numbers)
augment_all(numbers)
print("after the function is executed:", numbers) # gene aynı olur hiç bir şey değişmez çünkü 
# orjinal liste değişmemiş  my_list=new_list bu satırdan dolayı ikiside aynı olur """



#-------------------------------------------------
"""def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print("Orijinal matris:")
for row in matrix:
    print(row)
    
transpose(matrix)  # Fonksiyon matrisi doğrudan değiştirir
    
print("\nTranspozu alınmış matris:")
for row in matrix:
    print(row)"""

#----------------------------------------------------