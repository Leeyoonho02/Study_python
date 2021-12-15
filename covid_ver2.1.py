from bs4 import BeautifulSoup
import urllib.request
#import time

webpage = urllib.request.urlopen("https://corona-live.com/")
soup = BeautifulSoup(webpage,"html.parser")
#now = time.localtime()

korea = soup.select_one("#root > div.c-bZXDba > div.c-gmUTjU > div.c-gmRZqw > div > div > section:nth-child(1) > div > div.c-ftcwwt.c-ftcwwt-bpRjqJ-color-red > div.c-yYoNH").get_text()
daegu = soup.select_one("#root > div.c-bZXDba > div.c-gmUTjU > div.c-gmRZqw > div > div > section:nth-child(4) > div > div.c-iCTXjZ > div > table > tbody > tr:nth-child(15) > td.c-fWUTTQ.c-fWUTTQ-fYeKAw-shadow-true.c-fWUTTQ-cOWTvr-centered-true.c-fWUTTQ-ibxIhnQ-css > a > div > div > div.c-hPkbyn").get_text()
daegu_today = soup.select_one("#root > div.c-bZXDba > div.c-gmUTjU > div.c-gmRZqw > div > div > section:nth-child(4) > div > div.c-iCTXjZ > div > table > tbody > tr:nth-child(15) > td.c-fWUTTQ.c-fWUTTQ-fYeKAw-shadow-true.c-fWUTTQ-cOWTvr-centered-true.c-fWUTTQ-igvBJoE-css > a > div > div > div.c-hPkbyn").get_text()

#print(f"----------Todays ({time}시 기준) Covid19 status----------")
#print("--------------Todays (%04d/%02d/%02d %02d:%02d:%02d시 기준) Covid status---------------" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
print(f"전국 누적 확진자 : {korea} 명")
print(f"대구 누적 확진자 : {daegu} 명")
print(f"대구 신규 확진자 : {daegu_today} 명")
print("-------------------------------------------------------------")