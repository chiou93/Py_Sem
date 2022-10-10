# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def list_random_nums(count):
   if count < 0:
      print("Negative value of the number of numbers!")
      return []

   list_nums = sample(range(1, count * 2), count)
   return list_nums

def prod_pairs(list_nums: list):
   res_list = []
   len_list = len(list_nums)

   for i in range(len_list // 2):
      res_list.append(list_nums[i] * list_nums[len_list - i - 1])

   if len_list % 2:
        res_list.append(list_nums[len_list // 2])
   return res_list

all_list = list_random_nums(int(input("Enter the number of numbers: ")))
print(all_list)
print(prod_pairs(all_list))


