# 1
# a = int(input())
# b = int(input())
# operation = input()
# def calc():
#     if operation == "+":
#         print(a+b)
#     elif operation == "-":
#         print(a-b)
#     elif operation == "*":
#         print(a*b)
#     elif operation == "/":
#         print(a/b)
#     else:
#         print("Операция не поддерживается")
#
# calc()
#2
# lst=[2, 3, 45, 5, 4, 10, 12, 13, 15, 17]
# for i in lst:
#     if i==13:
#         break
#     elif i%2!=0:
#         print(i)

#4
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# sum = 0
# for i in lst:
#     if i<30 and i%3:
#         print(i, end='\t')
#     else:
#         sum += i
# print(sum)

#3
# a = list(reversed(range(2, 22, 4)))
# print(a)

#6
# a = 'Hello World'
# b = a.split(' ')
# c = b[1]+' '+b[0]
# print(c)

#5
# def month_to_season(m):
#     s = {
#         (12,1,2):"Winter",
#         (3,4,5):"Spring",
#         (6,7,8):"Summer",
#         (9,10,11):"Autumn"
#     }
#     sen = None
#     for key, val in s.items():
#         if m in key:
#             sen = val
#             break
#     return sen
#
# print(month_to_season(10))