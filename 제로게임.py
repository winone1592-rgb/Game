import random

class zerogame:
    def zero(self):
        result = self.game()
        name = input("닉네임을 입력해주세요: ")
        self.save(name, result)

    def game(self):
        computer = random.randint(0, 2)
        
        user, user_ans = self.enter()
        if computer+user == user_ans:
            result = "성공"
        else:
            result = "실패"
        print(f"맞추기에 {result}하셨습니다")

        return result

    def enter(self):
        while True :
            print("들어올릴 엄지 손가락 수와 전체 맞출 수를 입력해주세요")
            print("0, 0 형태로 입력해주세요")
            print("e.g. 1, 3 을 입력하면 하나의 엄지손가락을 들었고, 상대가 2개의 엄지손가락을 들었을 것으로 예상한 것입니다.")
            inp = input("(0,1,2중 입력 가능, 0,1,2,3,4 중 입력가능):")
            inpt = inp.strip().split(",")
            if int(inpt[0]) not in {0, 1, 2}:
                print("들어올릴 엄지 손가락의 수는 0, 1, 2 중에서 선택해주세요")
            elif int(inpt[1]) not in {0, 1, 2, 3, 4}:
                    print("추측할 값으로는 0, 1, 2, 3, 4 만 가능합니다.")
            else :
                break

        return int(inpt[0]), int(inpt[1])

    def save(self, n, r):
        with open("zero_history.txt","a",encoding="utf-8")as file:
            file.write(f"{n}, {r}")


# from 제로게임 import zerogame
# a=zerogame()
# a.zero()