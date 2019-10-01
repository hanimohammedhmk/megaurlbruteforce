#! /usr/bin/python3

import requests
import urllib
import strgen
def main(): 
 #version check
 print ('         _    __')         
 print ('  /\  /\/_\  / _\  /\  /\ ')
 print (' / /_/ //_|\ \ \  / /_/ /')
 print ('/ __  /  _  \_\ \/ __  / ') 
 print ('\/ /_/\_/ \_/\__/\/ /_/  ')
                         
 #print(requests.__version__)
 #print(requests.__copyright__)
 print('url mega bruteforce written by hanihmk#')
 print('requirement: python module StringGenerator install using cmd \'pip install StringGenerator\' ')
 #input url
 print('Enter $ to bruteforcing area')
 url = input("Enter the url for bruteforcing random string patterns : ") 
 print('Entered url:',url)
 url = str(url)
 if (url.find('$')==-1):
     print('bruteforcing point not specified ($) will not work !!!')
 #url = 'https://anonfile.com/'
 
 
 
 #concatenate pattern+/
 #pattern = 'K2wbm2t6nc'
 n=0
 template = input('Enter template of string pattern (find more about template at https://pypi.org/project/StringGenerator/ ): ')
 template = str(template)
 #template =  '[A-Z]{1}[\d]{1}[\c]{3}[0-9]{1}[a-z]{1}[0-9]{1}[\c]{2}'
 while(1) :
   
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
     if (statuscode == 200 or 301 or 300):
        n=n+1
        print(statuscode, '-- got ', n ,' urls')
        foundedurls = open('output.txt','a')
        foundedurls.write(url2)
        foundedurls.write('\n')
        foundedurls.close()
     connection.close() 
   #except urllib.request.HTTPError or urllib.error.URLError as e:
   except urllib.error.URLError as e:
     print(e.reason)
    

if __name__ == '__main__':
	main()
	
