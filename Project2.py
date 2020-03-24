# Guess the number
import random
from os import system, name

a = {
    "0": 20,
    "1": 40,
    "2": 80
}
so_lan_max = 6


def main():
    print("Trờ chơi đoán số!!!")
    do_kho = input("Mời bạn chọn độ khó (0-2): ")

    try:
        num = random.randint(0, a[do_kho])
    except:
        num = random.randint(0, a['2'])
        do_kho = '2'

    dem = 0
    while True:
        guess_num = int(input("Mời bạn đoán một số giữa 0 và {}: ".format(a[do_kho])))
        if guess_num == num:
            print("Chúc mừng bạn đã chiến thắng !!")
            break
        else:
            if guess_num > num:
                print("Lớn hơn số cần đoán!")
            else:
                print("Nhỏ hơn số cần đoán!")
            dem = dem + 1
        if dem >= so_lan_max:
            print("Bạn đã dùng hết số lượt đoán! Vẫn không đoán được!")
            break


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


while True:
    main()
    con = input("Bạn có muốn chơi tiếp (y/n): ")
    if con != 'y':
        exit(0)
    else:
        clear()
