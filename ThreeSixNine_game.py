
########## 3, 6, 9게임

class ThreeSixNine:

    def __init__(self):
        self.history = []
        self.filename = "ThreeSixNine_history.txt"

    def check_369(self, number):
        number = str(number)
        count = 0
        for n in number:
            if n in ["3", "6", "9"]:
                count += 1
        if count > 0:
            return "짝"*count
        else:
            return number

    def input_answer(self):
        while True:
            try:
                answer = input("당신의 차례입니다: ")
                return answer
            except ValueError:
                print("잘못 입력했습니다.")

    def add_record(self, nickname, result):
        result = { "id": nickname, "result": result }
        self.history.append(result)

    def save_history(self, history, filename):
        with open(filename, "a", encoding="utf-8") as file:
            for record in history:
                line = f"{record["id"]}, {record["result"]}\n"
                file.write(line)

    def play_game(self, start_num=1, end_num=50):

        correct_answer_list = []  # 정답 리스트
        for number in range(start_num, end_num+1):
            correct_answer = self.check_369(number)
            correct_answer_list.append(correct_answer)

        how_many_turn = 0
        for turn in range(len(correct_answer_list)):
            correct_answer = correct_answer_list[turn]

            # 사용자가 먼저 시작하는 것으로 고정하자 -> 홀수 턴이 사용자가 입력하는 차례가 됨
            if turn%2 != 0 :
                print()
                user_answer = self.input_answer()
                if user_answer == correct_answer:
                    how_many_turn += 1
                    continue
                else:
                    print(f"틀렸습니다. 정답은 {correct_answer}입니다.")
                    break
            else:
                print()
                print(f"컴퓨터 차례입니다: {correct_answer}")
                how_many_turn += 1
                continue

        if how_many_turn == end_num:
            print()
            print("성공하셨습니다!")
            result = "성공"
        else:
            print()
            print("실패하셨습니다!")
            result = "실패"
        
        nickname = input("닉네임을 입력하세요: ")
        self.add_record(nickname, result)

        self.save_history(self.history, self.filename)





    




# app = ThreeSixNine()
# app.play_game(start_num=1, end_num=50)

        






        
            
        


        

