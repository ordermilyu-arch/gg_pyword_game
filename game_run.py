#게임 실행하는 앱
from func_wordsgame import wordLoad, gameRun,scorePrint

words = wordLoad()
# - 워드 게임 실행하는 기능 모듈화 : gameRun()
elapsed_time,countC,cor_answer = gameRun(words)
# - 게임 결과 출력 : scorePrint
scorePrint(countC, elapsed_time)