from bs4 import BeautifulSoup
import urllib.request

webpage = urllib.request.urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=")
soup = BeautifulSoup(webpage,"html.parser")

time = soup.select_one("#content > div > div.timetable > p > span").get_text()
korea = soup.select_one("#mapAll > div > ul > li:nth-child(5) > div:nth-child(2) > span").get_text()
daegu = soup.select_one("#main_maplayout > button:nth-child(3) > span.num").get_text()
daegu_today = soup.select_one("#main_maplayout > button:nth-child(3) > span.before").get_text()

print(f"----------Todays ({time}시 기준) Covid19 status----------")
print(f"전국 누적 확진자 : {korea} 명")
print(f"대구 누적 확진자 : {daegu} 명")
print(f"대구 신규 확진자 : {daegu_today[2:5]} 명")
print("-------------------------------------------------------------")