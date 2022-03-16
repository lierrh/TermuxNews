from GoogleNews import GoogleNews
from colorama import Fore, Back, Style

googleNews=GoogleNews()

googleNews=GoogleNews (lang='tr', period='7d') 

googleNews.search('Türkiye')

Sonuc=googleNews.result()

for i in Sonuc:

  print(Back.BLACK + Fore.WHITE)
  print("...............................")

  print(Back.BLACK + Fore.RED)
  print("Başlık: ",i['title'])
  
  print(Back.BLACK + Fore.GREEN)
  print("Zaman: ",i['date'])
  
  print(Back.BLACK + Fore.WHITE)
  print("Açıklama: ",i['desc'])
  
  print(Back.BLACK + Fore.MAGENTA)
  print("Haber linki: ",i['link'])
  
  print(Style.RESET_ALL)
