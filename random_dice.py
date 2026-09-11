# 랜덤주사위
import random

# 랭킹 관련
class Ranom_dice_history:
    def __init__(self):
        self.records = []

    def add_record(self, nickname, result):
        record = {"name": nickname, "result": result}

        self.records.append(record)

        with open("random_dice_history.txt", "a", encoding="utf-8") as file:
            file.write(f"{nickname} , {result}\n")

    def show_result(self):
        if len(self.records) == 0:
            print("기록이 없습니다.")
            return

        print("===== 게임 기록 =====")

        for record in self.records:
            print(record["name"], ",", record["result"])


# 주사위 게임
class DiceGame:
    def __init__(self):
        self.player = 0
        self.computer = 0

    def play(self):
        print()
        print("===== 주사위 대결 =====")

        input("Enter를 누르면 주사위를 굴립니다.")

        self.player = random.randint(1, 6)
        self.computer = random.randint(1, 6)

        print("플레이어 주사위: ", self.player)
        print("컴퓨터 주사위: ", self.computer)

        if self.player > self.computer:
            print("플레이어 성공!")
            return True

        elif self.player < self.computer:
            print("플레이어 실패!")
            return False

        else:
            print("무승부!")
            return False

