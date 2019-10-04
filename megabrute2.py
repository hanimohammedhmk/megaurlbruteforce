#! /usr/bin/python3

import requests
import urllib
import strgen
from bs4 import BeautifulSoup
def megabrute():
    #version check
    print ('         _    __')
    print ('  /\  /\/_\  / _\  /\  /\ ')
    print (' / /_/ //_|\ \ \  / /_/ /')
    print ('/ __  /  _  \_\ \/ __  / ')
    print ('\/ /_/\_/ \_/\__/\/ /_/  ')
    print("\n\n")
    #print(requests.__version__)
    #print(requests.__copyright__)
    print('URL Mega Bruteforce written by hanihmk#')
    print('requirement: python module StringGenerator install using cmd \'pip install StringGenerator\' \n')
    #input url
    print('Enter $ to bruteforcing area')
    url = input("Enter the url for bruteforcing random string patterns : ")
    print('Entered url:',url)
    url = str(url)
    if (url.find('$')==-1):
        print('bruteforcing point not specified ($) will not work !!!')
        exit()
        #url = 'https://anonfile.com/'
    while(1):
        print("\n")
        print ("######Available Bruteforce Methods######")
        print ("1.Word List or Dictionary BruteForcing \n2.Random String generated brute forcing \n3.exit ")
        print("\n")
        method = int(input("Enter the method of bruteforcning (1/2/3): "))
        if (method == 2):
            n=0
            template = input('Enter template of string pattern (find more about template at https://pypi.org/project/StringGenerator/ ): ')
            template = str(template)
            print("BruteForcing with given pattern......(to stop press 'Ctrl+C')")
            try :
                while(1):
                    pattern = strgen.StringGenerator(template).render()
                    #pattern = 'K2wbm2t6nc'
                    url2 = url.replace("$",pattern)
                    #url2 = "%s%s/"%(url,pattern)
                    print('Checking ------ ',url2)
                    #finding status code
                    try:
                        req = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
                        connection = urllib.request.urlopen(req)
                        #connection = urllib.request.urlopen(url2)
                        statuscode = connection.getcode()
                        #statuscode = urllib.urlopen(url2).getcode()
                        print(type(statuscode),statuscode)
                        if(statuscode == 200 or 301 or 300):
                            n=n+1
                            print(statuscode, '-- got ', n ,' urls')
                            soup = BeautifulSoup(urllib.request.urlopen(url2),"lxml")
                            title = soup.title.string
                            foundedurls = open('output.txt','a')
                            foundedurls.write(url2)
                            foundedurls.write(title)
                            foundedurls.write('\n')
                            foundedurls.close()
                            connection.close()
                            #except urllib.request.HTTPError or urllib.error.URLError as e:
                    except urllib.error.URLError as e:
                            print(e.reason)
            except KeyboardInterrupt:
                print('interrupted!')
        if (method == 3):
            exit()
        if (method == 1):
            n=0
            print("Enter word list path")
            path = input("path = ")
            try:
                wordlist = open (path,"r")
                word = wordlist.readlines()
                wordlist.close()
                #print(word)
                count = len(word)
            except IOError:
                print("Could not read file:", path)
                exit()
            i=0
            try :
                print("BruteForcing with given wordlist/Dictionary......(to stop press 'Ctrl+C')")
                for x in word:
                    while ( i < count):
                        pattern = (word[i]).rstrip()
                        #print(pattern,"\n",type(pattern))
                        i=i+1
                        url2 = url.replace("$",pattern)
                        #url2 = "%s%s/"%(url,pattern)
                        print('Checking ------ ',url2)
                        #finding status code
                        try:
                            req = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
                            connection = urllib.request.urlopen(req)
                            #connection = urllib.request.urlopen(url2)
                            statuscode = connection.getcode()
                            #statuscode = urllib.urlopen(url2).getcode()
                            print(type(statuscode),statuscode)
                            if(statuscode == 200 or 301 or 300):
                                n=n+1
                                print(statuscode, '-- got ', n ,' urls')
                                soup = BeautifulSoup(urllib.request.urlopen(url2),"lxml")
                                title = soup.title.string
                                foundedurls = open('output.txt','a')
                                foundedurls.write(url2)
                                foundedurls.write(title)
                                foundedurls.write('\n')
                                foundedurls.close()
                                connection.close()
                                #except urllib.request.HTTPError or urllib.error.URLError as e:
                        except urllib.error.URLError as e:
                            print(e.reason)
                print("WordList Bruteforcing successfull!!! URLs with status code 200 are saved to output.txt")
            except KeyboardInterrupt:
                print('interrupted!')

        else:
            print("invalid no of method provided")

def main():
    megabrute()


if __name__ == '__main__':
	main()
