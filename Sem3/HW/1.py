# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def list_random_nums(count: int):
   if count < 0:
      print("Negative value of the number of numbers!")
      return []

   list_nums = sample(range(1, count * 2), count)
   return list_nums

def sum_odd_nums(list_nums: list):
   sum_nums = 0
   for i in range(0, len(list_nums), 2):
      sum_nums += list_nums[i]
   return sum_nums

all_list = list_random_nums(int(input("Enter the number of numbers: ")))
print(all_list)
print(sum_odd_nums(all_list))