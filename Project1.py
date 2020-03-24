# Hangman game
import csv
import random
import googletrans

words = csv.reader(open("dictionary.csv", "r"))
words = list(words)

class tu_can_doan():
    guess = 0
    isWin = False
    do_kho = [10,8,6]
    def __init__(self, tu, kho):
        self.tu = tu[0]
        self.l = len(self.tu)
        temp = {}
        for i in self.tu:
            temp[i] = False
        self.chu_cai = temp
        self.sai_cho_phep = self.do_kho[int(kho)-1]


def getword():
    return random.choice(words)


# trả lại một xâu với chữ bình thường nếu đoán đúng và * nếu chưa đoán được
def sau_khi_doan(word):
    temp = "".join([i if word.chu_cai[i] == True else "*" for i in word.tu])
    return temp

# nếu win thì is_Win = true
def check_win(word):
    if all(word.chu_cai.values()):
        word.isWin = True

def main():
    print("Trò chơi Hangman đoán từ!!!")
    print("Bắt đầu: ")
    while True:
        kho = input("Mời bạn chọn độ khó 1-3 : ")
        word = tu_can_doan(getword(), kho)
        print("Đây là từ có {} chữ cái : {}".format(word.l, word.l * "*"))
        while not (word.isWin):
            doan = input("Mời bạn đoán chữ cái: ")

            if doan in word.chu_cai.keys():
                print("Bạn đã đoán đúng")
                word.chu_cai[doan] = True
            else:
                word.guess += 1
                print("Bạn đoán sai rồi, bạn còn {} lần đoán sai".format(word.sai_cho_phep - word.guess))
            print("Từ : {}".format(sau_khi_doan(word)))
            check_win(word)
            if word.sai_cho_phep - word.guess < 0 :
                break

        if (word.isWin):
            print("Bạn đã chiến thắng rồi!!!")
        else:
            print("Rất tiếc bạn đã thua!!, chữ cái là : {}".format(word.tu))
            tran = googletrans.Translator()
            print(tran.translate(word.tu,dest="vi").text)

        conti = input("Bạn có muốn chơi tiếp (y/n) : ")
        if conti != 'y':
            exit()
        else:
            clear()

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

main()