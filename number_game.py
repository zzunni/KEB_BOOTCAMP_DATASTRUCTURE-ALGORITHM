import random

num = random.randint(0,100)
chance = 10
print(f"숫자맞추기 게임을 시작합니다. 주어진 기회는 {chance}번 입니다.")

while chance > 0:
    mynum = int(input("숫자를 맞춰보세요: "))
    if mynum < num:
        chance=chance-1
        print(f"정답보다 작은 값을 입력하셨습니다. 남은 기회는 {chance}번 입니다.")


    elif mynum > num:
        chance=chance-1
        print(f"정답보다 큰 값을 입력하셨습니다. 남은 기회는 {chance}번 입니다.")


    elif mynum == num:
        chance=chance-1
        print(f"정답을 {chance}번 만에 맞추셨습니다. ")
        break

    if chance == 0:
        print(f"찬스를 모두 소진하셨습니다. 답은 {num}이었습니다. 프로그램을 종료합니다.")
        break