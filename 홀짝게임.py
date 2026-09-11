import random


class EvenOddGame:

    def __init__(self):

        self.nickname = ""

        self.history = []  # 게임 결과를 저장할 리스트

    # 1. 숫자 입력받는 함수

    def get_user_number(self):

        while True:

            try:

                num = int(input("1~100 사이의 숫자를 입력하세요: "))

                if 1 <= num <= 100:

                    return num

                print("1에서 100 사이의 숫자를 입력해주십시오.")

            except ValueError:

                print("숫자로만 입력해주십시오.")

    # 2. 홀 / 짝 예측 입력받는 함수

    def get_user_choice(self):

        while True:

            choice = input(
                "두 수의 합은 무엇일까요? ('홀' 또는 '짝' 입력): "
            ).strip()

            if choice in ["홀", "짝"]:

                return choice

            print("'홀' 또는 '짝' 중에서 정확히 입력해주십시오.")

    # 3. 홀짝 게임 진행 함수

    def play_game(self):

        print("\n==================================")

        print("홀짝 게임을 시작합니다.")

        computer_num = random.randint(1, 100)

        user_num = self.get_user_number()

        sigma = computer_num + user_num

        q = sigma % 2

        if q == 0:

            answer = "짝"

        else:

            answer = "홀"

        ans = self.get_user_choice()

        if answer == ans:

            result = "승리"

        else:

            result = "패배"

        # 결과 출력

        print("\n[게임 결과]")

        print(
            f"컴퓨터의 숫자: {computer_num} / "
            f"내가 입력한 숫자: {user_num}"
        )

        print(f"두 수의 합: {sigma} ({answer})")

        print(f"👉 {self.nickname}님, {result}하셨습니다!")

        # history에 nickname과 result 저장

        record = f"{self.nickname},{result}"

        self.history.append(record)

        # txt 파일에 결과 바로 추가

        with open("EO_history.txt", "a", encoding="utf-8") as file:

            file.write(record + "\n")

    # 4. txt 파일에서 history 불러오는 함수

    def load_history(self):

        try:

            with open("EO_history.txt", "r", encoding="utf-8") as file:

                for line in file:

                    record = line.strip()

                    if record:

                        self.history.append(record)

        except FileNotFoundError:

            pass

    # 5. nickname별 개인 기록 조회

    def view_personal_history(self):

        search_nickname = input(
            "\n조회할 닉네임을 입력해주세요: "
        ).strip()

        print("\n==================================")
        print(f"[{search_nickname}님의 개인 기록]")
        print("==================================")

        personal_history = []

        try:

            with open("EO_history.txt", "r", encoding="utf-8") as file:

                for line in file:

                    record = line.strip()

                    if record:

                        data = record.split(",")

                        # nickname이 같은 기록만 가져오기

                        if data[0] == search_nickname:

                            personal_history.append(data[1])

        except FileNotFoundError:

            print("아직 저장된 기록 파일이 없습니다.")
            print("==================================")
            return

        if len(personal_history) == 0:

            print("해당 nickname의 게임 기록이 없습니다.")
            print("==================================")
            return

        win_count = 0
        loss_count = 0

        for i in range(len(personal_history)):

            result = personal_history[i]

            print(f"{i + 1}번째 게임 : {result}")

            if result == "승리":

                win_count += 1

            else:

                loss_count += 1

        print("----------------------------------")

        print(
            f"총 전적 : "
            f"{len(personal_history)}전 "
            f"{win_count}승 "
            f"{loss_count}패"
        )

        print("==================================")

    # 6. 게임 메뉴 실행 함수

    def start(self):

        print("\n==================================")

        print("홀짝 게임에 오신 것을 환영합니다!")

        # nickname 입력

        while True:

            self.nickname = input(
                "닉네임을 입력해주세요: "
            ).strip()

            if self.nickname:

                break

            print("nickname을 한 글자 이상 입력해주세요.")

        # 게임 메뉴를 반복

        while True:

            try:

                print("\n==================================")

                print(f"{self.nickname}님 1, 2, 3번 중에 입력해주세요")

                print("1번 : 홀짝 게임 시작")

                print("2번 : 개인 기록 조회")

                print("3번 : 게임 종료")

                menu = int(input("번호를 입력하세요: "))

                if menu == 1:

                    self.play_game()

                elif menu == 2:

                    self.view_personal_history()

                elif menu == 3:

                    print("\n홀짝 게임을 종료합니다.")

                    break

                else:

                    print("1, 2, 3번 중에서 선택해주세요.")

            except ValueError:

                print("숫자로 입력해주십시오.")


