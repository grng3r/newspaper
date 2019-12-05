#!/bin/python3
"""
Developed by : gr@ng3r
This software is developed for personal use and educational purposes.
It is free to be downloaded, modified and developed however you wish.
"""
import sys
import requests
import os
from bs4 import BeautifulSoup

from datetime import datetime
from colorama import Fore as fcolors
from colorama import Back as bcolors
from colorama import Style

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

#Tech News
def HackerNews():
    result = requests.get('https://news.ycombinator.com', headers=header)
    print(result.status_code)

    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup.title.string)
    print("\n\n")
    news_bar = soup.find('table', {'class': 'itemlist'})
    links = news_bar.find_all("a", {'class': 'storylink'})
    for link in links:
        print(link.text)
        print(link.get('href'))
        print('\n')



def DefCon():
    result = requests.get('https://www.defcon.org/html/links/dc-news.html', headers=header)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup.title.string)
    print("\n")
    
    articles = soup.find_all('div', {'class': 'nine columns alpha'})[0:5]
    for article in articles:
        print(article.text)
        links = article.find_all('a')
        for link in links:
            print(link.get('href'))
            print('\n')
    



def BlackHat():
    result = requests.get('https://www.blackhat.com/html/press.html', headers=header)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup.title.string)
    print("\n")

    news_bar = soup.find_all('ul', {'class': 'blue-bottom'})[0]
    
    articles = news_bar.find_all('li')[0:6]
    for article in articles:
        print(article.text)
        links = article.find_all('a')
        for link in links:
            print(link.get('href'))
            print('\n')


#TODO poprav
def ProjectZero():
    result = requests.get('https://googleprojectzero.blogspot.com', headers=header)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup.title.string)
    print("\n")

    #news_bar = soup.find_all('div', {'styl': 'font-size: large;'})
    #for articles in news_bar:
      #  print(articles)
    articles = soup.find_all('ul')

    for article in articles:
        li = article.find_all('li')
    
        for links in li:
            link = links.find_all('a', {'class': 'post-count-link'})
            
    
    
    #TODO extract first years from javascript 


#Project work news
def NODE():
    result = requests.get('https://n-o-d-e.net', headers=header)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src,'lxml')
    print(soup.title.string)
    print("\n")
    links = soup.find_all('a')
    
    for link in links[0:5]:
        print(link.text)
        print("https://n-o-d-e.net/"+ link.get('href'))

    print("\n")

    for link in links[5:12]:
        print(link.text)
        print("https://n-o-d-e.net/"+ link.get('href'))
        print("\n")



def LiveOverflow():
    result = requests.get('https://liveoverflow.com', headers=header)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup.title.string)
    print("\n")

    links = soup.find_all('a')

    for link in links[1:7]:
        print(link.text)
        print(link.get('href'))
    
    print("\n")

    for link in links[8:24]:
        print(link.text)
        print("https://liveoverflow.com"+link.get('href'))
        print("\n")



def g0hwc():
    result = requests.get('http://www.g0hwc.com/raspberry-pi-ham-radio.html', headers=header)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup.title.string)
    print("\n")
    
    projects = soup.find_all('tr')[3:8]

    for project in projects:
        print(project.text)
        links = project.find_all('a')
        for link in links:
            print(link.get('href'))
        print("\n")




#sport news
def Telesport():
    result = requests.get('https://telesport.telegram.hr', headers=header)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup.title.string)
    print("\n")

    news_bar = soup.find_all('div', {'class': 'page-content'})
    for articles in news_bar:
        article = articles.find_all('article', {'class': 'article-half'})
        
        for links in article:
            link = links.find_all('a')[2:]
            
            for www in link:
                print(www.text)
                print(www.get('href'))
                print("\n")
     


def bbcsport():
    result = requests.get('https://www.bbc.com/sport/rugby-union', headers=header)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup.title.string)
    print("\n")

    
    news_bar = soup.find_all('article')[:7]
    for articles in news_bar:
        article = articles.find_all('a', {'class': 'faux-block-link__overlay'})
        for links in article:
            link = links.get('href')
            print("https://www.bbc.com"+link)
            print('\n')

    titles = soup.find_all('h3', {'class': 'lakeside__title faux-block-link__target gel-pica-bold'})[:7]
    for title in titles:
        print(title.text)




#news world and country
def bbc():
    result = requests.get('https://www.bbc.com/news/world', headers=header)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup.title.string)
    print("\n")

    top_stories = soup.find_all('div', {'aria-label': 'Top Stories'})
    for titles in top_stories:
        title = titles.find_all('h2')[0]
        print(title.text)
    for news_bar in top_stories:
        links = news_bar.find_all('a')
        for link in links:
            print(link.text)
            print("www.bbc.co.uk/"+link.get('href'))
            print("\n")


def index():
    result = requests.get('https://www.index.hr', headers=header)
    print(result.status_code)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup.title.string)
    print("\n")

    news_bar = soup.find_all('div', {'id': "tab-content-latest-vijesti"})
    for articles in news_bar:
        article = articles.find_all('ul')
        
        for lis in article:
            li = lis.find_all('li')
            
            for links in li:
                link = links.find_all('a')
                for www in link:
                    print(www.text)
                    print(www.get('href'))



#menus

def news_menu():
    print(fcolors.RED+"Pritisni b za nazad, m za naslovnicu ili q za izac...\n")
    print(fcolors.BLUE+"_______MAINSTREAM_NEWS_______\n\n\n")
    
    odabir = input(fcolors.YELLOW+"1. BBC\n"+"2. INDEX.hr\n")

    if odabir == "1":
        bbc()
        

    if odabir == "2":
        index()
    
    if odabir == "q":
        sys.exit()

    if odabir == "b":
        menu()

    if odabir == "m":
        naslovna()

    else:
       odabir2 =  input("Odaberi nesto iz menia ili izadi, za kaznu korak nazad...\n")

       menu()


def sportnews_menu():
    print(fcolors.RED+"Pritisni b za nazad, m za naslovnicu ili q za izac...\n")
    print(fcolors.BLUE+"_______SPORTS_NEWS_______\n\n\n")
    
    odabir = input(fcolors.YELLOW+"1. BBC rugby\n"+"2. Telesport\n")

    if odabir == "1":
        bbcsport()
        

    if odabir == "2":
        Telesport()
    
    if odabir == "q":
        sys.exit()

    if odabir == "b":
        menu()

    if odabir == "m":
        naslovna()

    else:
       odabir2 =  input("Odaberi nesto iz menia ili izadi, za kaznu korak nazad...\n")

       menu()




def technews_menu():
    print(fcolors.RED+"Pritisni b za nazad, m za naslovnicu ili q za izac...\n")
    print(fcolors.BLUE+"_______TECH_NEWS_______\n\n\n")
    
    odabir = input(fcolors.YELLOW+"1. DefCon\n"+"2. BlackHat\n"+"3. ProjectZero\n"+"4. N_O_D_E\n"+"5. g0hwc\n"+"6. LiveOverflow\n"+"7. HackerNews\n")

    if odabir == "1":
        DefCon()
        

    if odabir == "2":
        BlackHat()


    if odabir == "3":
        ProjectZero()
        

    if odabir == "4":
        NODE()

    if odabir == "5":
        g0hwc()

    if odabir == "6":
        LiveOverflow()

    if odabir == "7":
        HackerNews()
    
    if odabir == "q":
        sys.exit()

    if odabir == "b":
        menu()

    if odabir == "m":
        naslovna()

    else:
       odabir2 =  input("Odaberi nesto iz menia ili izadi, za kaznu korak nazad...\n")

       menu()



#TODO Weather report
def menu():
    print(fcolors.RED+"Pritisni b za nazad ili q za izac...\n")

    os.system('clear')
    print(fcolors.BLUE+"__________MENU_________\n\n\n")
    print(fcolors.YELLOW+"Sta te zanima?\n")

    odabir = input("1. Tech vijesti?\n"+"2. Sportske vijesti?\n"+"3. Opcenito ono vijesti brate, svit, politika, ekonomija....\n\n")
    if odabir == "1":
        os.system('clear')
        technews_menu()
    
    if odabir == "2":
        os.system('clear')
        sportnews_menu()

    if odabir == "3":
        os.system('clear')
        news_menu()

    if odabir == "q":
        sys.exit()

    if odabir == "b":
        naslovna()

    else:
       odabir2 =  input("Odaberi nesto iz menia ili izadi, za kaznu korak nazad...\n")

       menu()



def naslovna():
    os.system('clear')
    date_time = datetime.now()
    today = date_time.strftime("%a, %d %m %y")
    print("\n")
    print(fcolors.BLUE+today)
    print('\n')
    print(fcolors.YELLOW+"L0 4nd b3h0ld gr@ng3r\n\n")

    print(fcolors.BLACK+"OpenSource ==> OpenWorld")
    
    answer = input(fcolors.RED+"Kakav si za vijesti?\n\n")
    if answer == "y":
        menu()
    else:
        sys.exit()
    
    print(Style.RESET_ALL)



def main():
    naslovna()

main()
