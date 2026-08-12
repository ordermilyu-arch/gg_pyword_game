#랜덤?모듈
import random

#음성 모듈
from pygame import mixer
mixer.init() 

#csv 모듈
import csv

#시간 모듈
import time


#클래스 정의 
class Wordgame:
    #클래스의 속성과 매서드로 구분

    def __init__(self):
            self.words= []
            self.elapsed_time =()
            self.countC = 0
            self.count = 1
            self.cor_answer = []
            
    
    def wordLoad(self):
        path = "data/word.txt"

        with open(path,"r",encoding="UTF8")as file:
            read_words = file.readlines()

            for word in read_words:
                word = word.strip()
                self.words.append(word)

        print(self.words)
        return self.words



    def gameRun(self):
        input("준비? 엔트를 입력하세요.")
        start_time = time.time()



        ##words 를 가지고와서 질문으로 프린트 하여 보여주기
        while self.count <6:
            question = random .choice(self.words)
            print(f"Question #{self.count}")
            print(question)
            
            answer = input()
            ##input받기
            #print(answer)
                

        ##input 받은 단어와 질문을 대조하여 답변 출력하기

            if answer == question:
                print("정답입니다.")
                #음성파일 출력
                mixer.music.load('assets/good.wav')
                mixer.music.play()
                self.countC = self.countC+1
                self.cor_answer.append(answer)

                

            else :
                print("오답입니다.")
                #음성파일 출력
                mixer.music.load('assets/bad.wav')
                mixer.music.play()

            self.count = self.count+1
            #print(count)

        #시험종료 시간종료
        end_time = time.time()
        self.elapsed_time = int(end_time-start_time)

    #최종 합격 여부 판별하기
    def scorePrint(self):
        if self.countC < 3:
            print("불합격입니다")
        else:
            print("합격입니다.")

        print(f"게임 종료:{self.countC}개 맞추었습니다.")
        print(f"총{self.elapsed_time}초 동안 플레이 하였습니다.")


    def run(self):
        self.wordLoad()
            # - 워드 게임 실행하는 기능 모듈화 : gameRun()
        self.gameRun()
        # - 게임 결과 출력 : scorePrint
        self.scorePrint()


if __name__ == "__main__":
    #게임 객체화
    wg=Wordgame()
    wg.run()

#csv에 입력하기
f=open('word_game_socre.csv','a')
writer = csv.writer(f)
writer.writerow(wg.cor_answer)
writer.writerow([f"{wg.elapsed_time}초 동안 플레이 하였습니다."])
writer.writerow([f"{wg.countC}개 맞추었습니다."])
f.close()
