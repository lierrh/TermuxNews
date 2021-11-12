from GoogleNews import GoogleNews
from colorama import Fore, Back, Style

googleNews=GoogleNews()

googleNews=GoogleNews (lang='tr', period='7d') 

googleNews.search('Türkiye')

Sonuc=googleNews.result()

for i in Sonuc:
  
  print(Back.WHITE + Fore.RED)
  print("Başlık: ",i['title'])
  
  print(Back.WHITE + Fore.GREEN)
  print("Zaman: ",i['date'])
  
  print(Back.WHITE + Fore.BLACK)
  print("Açıklama: ",i['desc'])
  
  print(Back.WHITE + Fore.MAGENTA)
  print("Haber linki: ",i['link'])
  
  print(Style.RESET_ALL)