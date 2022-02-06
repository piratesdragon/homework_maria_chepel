#Парсинг статей из книжного раздела Афиши Daily (https://daily.afisha.ru/series/180-knigi/) 

! pip3 install requests
! pip3 install beautifulsoup4 
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
n=1
dataset ={}
def new_info(url):
  global n
  page = rq.get(url) 
  page.text
  soup = BeautifulSoup(page.text, 'html.parser')
  for x in soup.find_all("h1", class_ = "article-head__title js-article-title"):
      title = x.text
  for y in soup.find_all("h3"):
      inside_text = y.text
  for headings in soup.find_all("div", class_= 'article-paragraph js-mediator-article'):
      inside_text += headings.text 
  for z in soup.find_all('span', class_ = 'article-head__datetime'):
      time = z.text
  dataset.update({n:[url, time, title, inside_text]})
  n+=1
  


new_info("https://daily.afisha.ru/brain/22296-ot-psihbolnicy-do-krugosvetki-kak-nelli-blay-stala-legendoy-zhurnalistiki/")
new_info("https://daily.afisha.ru/brain/22252-v-ozhidanii-rasstrela-kak-ustroen-novyy-roman-ot-avtora-cheloveka-iz-podolska/")
new_info("https://daily.afisha.ru/brain/22232-zhenschina-ne-muzhchina-i-tleyuschiy-ogon-dva-otlichnyh-novyh-romana/")
new_info("https://daily.afisha.ru/brain/22090-chto-chitala-redakciya-afishi-daily-v-2021-godu/")
new_info("https://daily.afisha.ru/brain/21955-7-luchshih-knig-2021-goda-vybor-egora-mihaylova/")
new_info("https://daily.afisha.ru/brain/21978-akuly-vo-dni-spasateley-i-my-nachinaem-v-konce-esche-dve-knigi-kotorye-stoit-prochitat/")
new_info("https://daily.afisha.ru/brain/21837-rutu-modan-yumor-eto-prosto-odin-iz-sposobov-smotret-na-sereznye-temy/")
new_info("https://daily.afisha.ru/brain/21792-lyubimye-knigi-kventina-tarantino/")
new_info("https://daily.afisha.ru/brain/21769-lyubov-v-shotlandii-i-chuma-v-anglii-dva-novyh-romana-kotorye-stoit-prochitat-zimoy/")
new_info("https://daily.afisha.ru/brain/21705-zachem-snyatsya-sny-stoit-li-chitat-dvorec-snovideniy-ismailya-kadare/")

dat = pd.DataFrame.from_dict(dataset,columns=["источник", "дата", "заголовок", "текст"], orient="index")

display(dat)

dat.to_csv('books.csv')
