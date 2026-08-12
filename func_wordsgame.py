#랜덤?모듈
import random

#음성 모듈
from pygame import mixer
mixer.init() 

#csv 모듈
import csv

#시간 모듈
import time

def wordLoad():
    path = "data/word.txt"
    words = [] # txt파일에서 꺼낸거를 단어로 저장

    with open(path,"r",encoding="UTF8")as file:
        read_words = file.readlines()

        for word in read_words:
            #각 단어의 공백 및 뉴라인 문자 제거
            word = word.strip()
            #각 단어를 words 리스트에 저장
            words.append(word)

    # 리스트 잘들어갔나 확인
    print(words)
    return words


#게임시작하기
def gameRun(words):
    input("준비? 엔트를 입력하세요.")
    start_time = time.time()



    count =int(1)
    countC = int()
    cor_answer = []


    ##words 를 가지고와서 질문으로 프린트 하여 보여주기
    while count <6:
        question = random .choice(words)
        print(f"Question #{count}")
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
            countC = countC+1
            cor_answer.append(answer)

            

        else :
            print("오답입니다.")
            #음성파일 출력
            mixer.music.load('assets/bad.wav')
            mixer.music.play()

        count = count+1
        #print(count)

    #시험종료 시간종료
    end_time = time.time()
    elapsed_time = int(end_time-start_time)
    return elapsed_time,countC,cor_answer

#최종 합격 여부 판별하기
def scorePrint(elapsed_time,countC):
    if countC < 3:
        print("불합격입니다")
    else:
        print("합격입니다.")

    print(f"게임 종료:{countC}개 맞추었습니다.")
    print(f"총{elapsed_time}초 동안 플레이 하였습니다.")

if __name__ == "__main__":
    # print(__name__)s
    # - 워드 파일을 로딩하여 words 리스트에 대입하는 기능 모듈화 : wordLoad()
    words = wordLoad()
    # - 워드 게임 실행하는 기능 모듈화 : gameRun()
    elapsed_time,countC,cor_answer = gameRun(words)
    # - 게임 결과 출력 : scorePrint
    scorePrint(countC, elapsed_time)

#csv에 입력하기
f=open('word_game_socre.csv','a')
writer = csv.writer(f)
writer.writerow(cor_answer)
writer.writerow([f"{elapsed_time}초 동안 플레이 하였습니다."])
writer.writerow([f"{countC}개 맞추었습니다."])
f.close()
