

# 로그인 관련
class LoginManager:
    def __init__(self, correct_id, correct_pw, max_attempts=3):
        self.correct_id = correct_id
        self.correct_pw = correct_pw
        self.max_attempts = max_attempts

    def login(self):
        for count in range(self.max_attempts):
            user_id = input("ID를 입력하세요: ")
            user_pw = input("PASSWORD를 입력하세요: ")

            if user_id == self.correct_id and user_pw == self.correct_pw:
                print("로그인 되었습니다.")
                return True
            else:
                print("아이디 또는 비밀번호가 틀렸습니다.")

        print("로그인 3회 실패로 프로그램을 종료합니다.")
        return False



# 전체 프로그램
class App:
    def __init__(self):
        self.login_manager = LoginManager("admin", "1234")
        from random_dice import Ranom_dice_history
        self.history_board = Ranom_dice_history()
        from random_dice import DiceGame
        self.DiceGame = DiceGame()
        from 제로게임 import zerogame
        self.zerogame = zerogame()
        from ThreeSixNine_game import ThreeSixNine
        self.ThreeSixNineGame = ThreeSixNine()

    def print_menu(self):
        print()
        print("1. 주사위 게임")
        print("2. 제로 게임")
        print("3. 369 게임")
        print("4. 홀짝 게임")        
        print("5. 게임 종료")

    def input_menu(self):
        while True:
            try:
                menu = int(input("메뉴를 선택하세요: "))
                return menu
            except ValueError:
                print("숫자만 입력해주세요.")

    def run(self):
        if not self.login_manager.login():
            return

        while True:
            self.print_menu()
            menu = self.input_menu()

            if menu == 1:
                print("1. 주사위 게임 시작")
                print("2. 주사위 게임 기록보기")

                choose = input("메뉴를 선택해주세요: ")

                if choose == "1":
                    success = self.DiceGame.play()

                    nickname = input("닉네임을 입력하세요: ")

                    if success:
                        self.history_board.add_record(nickname, "성공")
                    else:
                        self.history_board.add_record(nickname, "실패")

                elif choose == "2":
                    self.history_board.show_result()

                else:
                    print("잘못된 메뉴선택입니다.")
                    
            elif menu == 2:
                print("1. 제로게임 시작")
                print("2. 제로게임 기록보기")
                choose=input("메뉴를 선택해주세요:")
                if choose == "1":
                    self.zerogame.zero()
                elif choose == "2":
                    self.zerogame.read_history()
                else:
                    print("잘못된 메뉴선택입니다.")

            elif menu == 3:
                print("1. 369게임 시작")
                print("2. 369게임 기록보기")
                choose=input("메뉴를 선택해주세요:")
                if choose == "1":
                    self.ThreeSixNineGame.play_game()
                elif choose == "2":
                    # print("서비스 준비중")
                    self.ThreeSixNineGame.show_result(cut=10)   # 10개 history 출력
                else:
                    print("잘못된 메뉴선택입니다.")

            elif menu == 4:
                game = "홀짝게임"

            elif menu == 5:
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 메뉴입니다.")


app = App()
app.run()

