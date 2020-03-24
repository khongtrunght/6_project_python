import random
from os import system, name

a = ['Búa', 'Kéo', 'Giấy']
print('Trò chơi búa kéo giấy!!!')
def may():
    print("Máy win!!")
    exit()

def nguoi():
    print("Người win!!")
    exit()

while True:
    H_pick = input('Mời bạn chọn Búa, Kéo, Giấy: ')
    C_pick_number = random.randint(0,2)
    H_pick_number = a.index(H_pick)
    if (H_pick_number == C_pick_number):
        print("Hoà! Mời bạn chọn lại. ")
    else:
        if H_pick_number == 0 :
            if C_pick_number == 3:
                may()
            else:
                nguoi()
        elif C_pick_number == 0:
            if H_pick_number == 3:
                nguoi()
            else:
                may()
        elif C_pick_number == 1:
            nguoi()
        else:
            may()



