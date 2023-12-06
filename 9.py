#  1
# try:
#     a = int(input())
#     c = int(input())
#     print(a +c)
# except ValueError:
#     print('несоответствующее значения')
#  2
# while True:
#     try:
#         a = int(input())
#         c = int(input())
#         print(a +c)
#         break
#     except ValueError:
#         print('несоответствующее значения')
#  3
# try:
#     a = int(input())
#     c = int(input())
#     print(a / c)
# except ZeroDivisionError:
#     print('несоответствующее значения')
#  4
# try:
#     a = int(input())
#     c = int(input())
#     print(a / c)
# except (ValueError, ZeroDivisionError):
#     print('несоответствующее значения')
#  5
try:
    a = int(input())
    c = int(input())
    print(a / c)
except (ValueError, ZeroDivisionError):
    print('несоответствующее значения')
finally:
    print('выход из программы')
