import random
import requests,os,json,uuid,secrets
from datetime import datetime, time
from json import dumps
from time import sleep
from colorama import Fore,Style
from user_agent import generate_user_agent

# Not responsible for any improper use of this program !
# FREE Tool By @O0Dev (Telegram channel)
# All rights reserved for @O0Dev (Telegram channel) 2022 | Coder : Osama A.M.Y 

class IGBoxO0Dev():
    def __init__(self):
        self.t = requests.get('https://o7aa.pythonanywhere.com/?id=7238',headers={'user_agent':generate_user_agent()}).json()['telegram']
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('color')
        self.x = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.s = 0
        self.p = 0
        self.m = 0
        self.n = 0
        self.r = 0
        self.w = 0
        self.g = 0
        self.k = 0
        self.ix = uuid.uuid4()
        self.b0 = Style.RESET_ALL
        self.b1 = Fore.YELLOW + '['
        self.b2 = Fore.YELLOW + ']'
        self.b3 = Fore.GREEN + '-'
        self.b4 = Fore.RED + '!'
        self.b5 = Fore.LIGHTCYAN_EX + '+'
        self.bb = (Fore.LIGHTYELLOW_EX+"""

   ____________          
  /  _/ ___/ _ )___ __ __
 _/ // (_ / _  / _ \\ \ /
/___/\___/____/\___/_\_\ v7
                         
        """)

    def CheckFiles(self):
        if os.path.exists(f'story.txt') == False:
            open('story.txt','a')
        if os.path.exists(f'accounts.txt') == False:
            open('accounts.txt','a')
        if os.path.exists(f'combo.txt') == False:
            open('combo.txt','a')

        self.HomeScreen()

    def HomeScreen(self):
        self.x = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.s = 0

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.bb)
            print(f'{self.b1}{self.b3}{self.b2}{self.b0} Coded By Osama A.M.Y || Tele {self.t}')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print(f"""
{self.b1}1{self.b2}{self.b0} Start Report [Profile]
{self.b1}2{self.b2}{self.b0} Auto Follow User From list
{self.b1}3{self.b2}{self.b0} Auto Comment
{self.b1}4{self.b2}{self.b0} Auto Watch Stories
{self.b1}5{self.b2}{self.b0} Auto Instagram Post
{self.b1}6{self.b2}{self.b0} Get Users From Words
{self.b1}7{self.b2}{self.b0} Get Users From User
{self.b1}8{self.b2}{self.b0} Delete Following
{self.b1}9{self.b2}{self.b0} Delete Posts
{self.b1}10{self.b2}{self.b0} Delete chat
{self.b1}11{self.b2}{self.b0} Cheack Email Linked
{self.b1}12{self.b2}{self.b0} Get Public email
{self.b1}13{self.b2}{self.b0} Switch Accounts type
{self.b1}14{self.b2}{self.b0} Change Password From list
{self.b1}15{self.b2}{self.b0} Sort Combo
{self.b1}16{self.b2}{self.b0} Increase real followers
{self.b1}17{self.b2}{self.b0} Post a New Note 
{self.b1}99{self.b2}{self.b0} exit
        """)
            tool = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Num of Tool > ')
            if tool == '1':
                self.vip_Report()
            elif tool == '2':
                self.Auto_follow()
            elif tool == '3':
                self.Auto_comment()
            elif tool == '4':
                self.Auto_stories()
            elif tool == '5':
                self.Auto_post()
            elif tool == '6':
                self.users_word()
            elif tool == '7':
                self.users_user()
            elif tool == '8':
                self.del_flow()
            elif tool == '9':
                self.del_post()
            elif tool == '10':
                self.del_chat()
            elif tool == '11':
                self.cheack_email()
            elif tool == '12':
                self.public_email()
            elif tool == '13':
                self.convert_acc()
            elif tool == '14':
                self.change_pass()
            elif tool == '15':
                self.sort_combo()
            elif tool == '16':
                self.real_fllow()
            elif tool == '17':
                self.post_note()
            elif tool == '99':
                print(f'{self.b1}{self.b3}{self.b2}{self.b0} I wish u a happy day :)')
                sleep(3)
                exit()
            else:
                print(f'{self.b1}{self.b4}{self.b2}{self.b0} Bad Number')
                sleep(1.5)
                IGBoxO0Dev().HomeScreen()

    def Insta_login(self, user, pasw):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        url = "https://www.instagram.com/accounts/login/ajax/"
    
        head = {
            'accept':'*/*',
            'accept-encoding':'gzip,deflate,br',
            'accept-language':'en-US,en;q=0.9,ar;q=0.8',
            'content-length':'269',
            'content-type':'application/x-www-form-urlencoded',
            'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
            'origin':'https://www.instagram.com',
            'referer':'https://www.instagram.com/',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'user-agent': generate_user_agent(),
            'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
            'x-ig-app-id':'936619743392459',
            'x-ig-www-claim':'0',
            'x-instagram-ajax':'8a8118fa7d40',
            'x-requested-with':'XMLHttpRequest',
        }
        time_now = int(datetime.now().timestamp())
        data = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pasw}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }
        login = requests.post(url, headers=head, data=data)

        if 'userId' in login.text:
            logincookies = login.cookies
            return logincookies
            # FREE Tool By @O0Dev (Telegram channel)

        elif 'challenge_required' in login.text:
            loginjson = login.json()
            logincookies = login.cookies
            MyPATH = loginjson['challenge']['api_path']
            url_api = 'https://i.instagram.com/api/v1' + MyPATH
            Secure = requests.get(url_api, headers=head, cookies=logincookies).json()
            mode = []
            try:
                if ('email') in Secure['step_data']:
                    mode.append('[1] Email')
                elif ('phone_number') in Secure['step_data']:
                    mode.append('[0] Phone')
                else:
                    print(f'{self.b1}{self.b4}{self.b2}{self.b0} Error, Try Again')
                    sleep(3)
                    IGBoxO0Dev().HomeScreen()
            except:
                print(f'{self.b1}{self.b4}{self.b2}{self.b0} Error, Try Again')
                sleep(3)
                IGBoxO0Dev().HomeScreen()

            for modes in mode:
                print(modes)
            myMode = input(f"{self.b1}{self.b5}{self.b2}{self.b0} Enter your Mode : ")
            SecureData = {
                'choice': myMode,
                '_uuid': self.ix,
                '_uid': self.ix,
                '_csrftoken': 'missing'
            }

            Send_Mode = requests.post(url_api, headers=head, data=SecureData, cookies=logincookies).json()
            Contact = Send_Mode['step_data']['contact_point']
            print(f'{self.b1}{self.b3}{self.b2}{self.b0} Done Sending The Code To » {Contact}')
            myCode = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Your Code : ')
            CodeData = {
                'security_code': myCode,
                '_uuid': self.ix,
                '_uid': self.ix,
                '_csrftoken': 'missing'
            }
            Send_Code = requests.post(url_api, headers=head, data=CodeData, cookies=logincookies).text
            if 'logged_in_user' in Send_Code:
                return logincookies
            else:
                print(f'{self.b1}{self.b4}{self.b2}{self.b0} Error Code')
                sleep(3)
                IGBoxO0Dev().HomeScreen()

        else:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} Error in Login with ur Account')
            print(login.text)
            sleep(3)
            IGBoxO0Dev().HomeScreen()

    def get_id(self,user):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        url = f"https://www.instagram.com/{user}/?__a=1&__d=dis"

        head = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'gzip,deflate,br',
            'accept-language':'en-US,en;q=0.9,ar;q=0.8',
            'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
            'user-agent': generate_user_agent(),
        }

        idd = requests.get(url,headers=head).json()['logging_page_id'].split('_')[1]
        return str(idd)

    def vip_Report(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)

        special_users = ['r6r9','o.7a','oo']

        username = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter UserName : ')
        password = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Password : ')
        
        login = IGBoxO0Dev().Insta_login(username,password)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)

        reportis = 0

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.bb)
            self.m = 0
            self.n = 0

            reportType = input(f"""
{self.b1}1{self.b2}{self.b0} Spam
{self.b1}2{self.b2}{self.b0} Suicide Or Self Injury
{self.b1}3{self.b2}{self.b0} Sale Of Illegal Goods
{self.b1}4{self.b2}{self.b0} Scam Or Fraud
{self.b1}5{self.b2}{self.b0} Nudity Or Pornography
{self.b1}6{self.b2}{self.b0} Violence Or Dangerous Activity
{self.b1}7{self.b2}{self.b0} Hate Speech
{self.b1}8{self.b2}{self.b0} Bullying
{self.b1}99{self.b2}{self.b0} Back to Home Screen

{self.b1}{self.b5}{self.b2}{self.b0} Enter Report type : """)

            if reportType == '1':
                reportis = 1
            elif reportType == '2':
                reportis = 2
            elif reportType == '3':
                reportis = 3
            elif reportType == '4':
                reportis = 4
            elif reportType == '5':
                reportis = 5
            elif reportType == '6':
                reportis = 6
            elif reportType == '7':
                reportis = 7
            elif reportType == '8':
                reportis = 8
            else:
                sleep(3)
                IGBoxO0Dev().HomeScreen()

            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.bb)

            Target = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Target : ')
            if str(Target) in special_users:
                sleep(3)
                IGBoxO0Dev().HomeScreen()
            else:
                pass

            try:
                idd = IGBoxO0Dev().get_id(Target)
            except:
                print(f'{self.b1}{self.b4}{self.b2}{self.b0} Error in find @{Target} on instagram')
                sleep(3)
                IGBoxO0Dev().HomeScreen()

            try:
                num_Report = int(input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Number of Report : '))
            except:
                num_Report = 10

            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.bb)

            coo = login.get_dict()
            cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"
            for i in range(num_Report):
                data = {'source_name':'',f'reason_id':reportis,'frx_context':''}
                head = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54",
                    "Host": "i.instagram.com",
                    'cookie': cookie ,
                    "X-CSRFToken": f"{login.get_dict()['csrftoken']}",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                }
                try:
                    start = requests.post(f"https://www.instagram.com/users/{idd}/report/", headers=head, data=data)
                    if 'ok' in start.text:
                        self.m +=1
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.m}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {self.n}')
                    elif start.status_code == 404:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(self.bb)
                        print(f'{self.b1}{self.b3}{self.b2}{self.b0} Account @{Target} Banned successfuly') 
                        sleep(10)
                        IGBoxO0Dev().HomeScreen()
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(self.bb)
                        print(f'{self.b1}{self.b4}{self.b2}{self.b0} Account Action Blocked, Please wait')
                        sleep(300)
                except:
                    self.n +=1
                    
                    print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.m}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {self.n}')

    def Auto_follow(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)

        target = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Target : ')

        try:
            accs = open('accounts.txt','r').read().splitlines()
        except:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} accounts.txt Not Found here')
            sleep(3)
            IGBoxO0Dev().HomeScreen()

        for acc in accs:
            user = acc.split(':')[0]
            pasw = acc.split(':')[1]
            login = IGBoxO0Dev().Insta_login(user,pasw)

            coo = login.get_dict()
            cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"
            idd = IGBoxO0Dev().get_id(target)

            url2 = f'https://i.instagram.com/api/v1/web/friendships/{idd}/follow/'

            head2 = {
                'accept':'*/*',
                'accept-encoding':'gzip,deflate,br',
                'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                'content-length':'0',
                'content-type':'application/x-www-form-urlencoded',
                'cookie': cookie,
                'origin':'https://www.instagram.com',
                'referer':f'https://www.instagram.com/{target}/',
                'sec-fetch-dest':'empty',
                'sec-fetch-mode':'cors',
                'sec-fetch-site':'same-origin',
                'user-agent': generate_user_agent(),
                'x-asbd-id': '437806',
                'x-csrftoken': coo['csrftoken'],
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9Rcy',
                'x-instagram-ajax': '0019e974ed32',
                'x-requested-with':'XMLHttpRequest',
            }
            try:
                follow = requests.post(url2,headers=head2,cookies=coo).text

                if '"status":"ok"' in follow:
                    self.a +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.a}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {self.b}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad Acc : {self.c}\n{self.b1}{self.b5}{self.b2}{self.b0} Error : {self.d}')
                else:
                    self.b +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.a}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {self.b}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad Acc : {self.c}\n{self.b1}{self.b5}{self.b2}{self.b0} Error : {self.d}')
            except:
                self.d +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.a}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {self.b}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad Acc : {self.c}\n{self.b1}{self.b5}{self.b2}{self.b0} Error : {self.d}')
        else:
            self.c +=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.a}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {self.b}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad Acc : {self.c}\n{self.b1}{self.b5}{self.b2}{self.b0} Error : {self.d}')
            sleep(3)

    def Auto_comment(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)

        target = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Post Link : ')
        post = f'{target}?__a=1&__d=dis'

        try:
            accs = open('accounts.txt','r').read().splitlines()
        except:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} accounts.txt Not Found here')
            sleep(3)
            self.HomeScreen()

        self.a = 0
        self.b = 0
        self.c = 0

        for acc in accs:
            user = acc.split(':')[0]
            pasw = acc.split(':')[1]
            login = IGBoxO0Dev().Insta_login(user,pasw)

            coo = login.get_dict()
            cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"
            head = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-length": "0",
                "content-type": "application/x-www-form-urlencoded",
                "cookie": cookie,
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                "x-csrftoken": coo['sessionid'],
                "x-ig-app-id": "936619743392459",
                "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFqSx",
                "x-instagram-ajax": "d3d3aea32e75",
                "x-requested-with": "XMLHttpRequest"
            }
            x = requests.get(post,headers=head).json()
            post_id = int(x['items'][0]['pk']) # FREE Tool By @O0Dev (Telegram channel)
            comment_text = input(f'{self.b1}{self.b4}{self.b2}{self.b0} Enter The Comment : ')

            url_post = f"https://www.instagram.com/web/comments/{post_id}/add/"

            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-length": "39",
                "content-type": "application/x-www-form-urlencoded",
                "cookie": cookie,
                "origin": "https://www.instagram.com",
                "referer": target,
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "x-csrftoken": coo['csrftoken'],
                "x-ig-app-id": "936619743392459",
                "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                "x-instagram-ajax": "d3d3aea32e75",
                "x-requested-with": "XMLHttpRequest"
            }
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                try:
                    response = requests.request("POST", url_post, headers=headers, data=f"comment_text={comment_text}&replied_to_comment_id=".encode('utf-8'))
                    if response.status_code == 200:
                        self.a +=1
                        print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.a}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {self.b}\n{self.b1}{self.b5}{self.b2}{self.b0} Error : {self.c}')
                        sleep(6)
                    else:
                        self.b +=1
                        print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.a}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {self.b}\n{self.b1}{self.b5}{self.b2}{self.b0} Error : {self.c}')
                        sleep(3)
                except:
                    self.c +=1
                    print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.a}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {self.b}\n{self.b1}{self.b5}{self.b2}{self.b0} Error : {self.c}')
                    sleep(3)

    def Auto_stories(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Ur UserName : ')
        pasw = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Ur Password : ')
        login = IGBoxO0Dev().Insta_login(user,pasw)

        coo = login.get_dict()
        csrf = coo['csrftoken']
        cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"

        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        print(f"""
{self.b1}1{self.b2}{self.b0} Watch From list
{self.b1}2{self.b2}{self.b0} Watch My Following Stories
{self.b1}3{self.b2}{self.b0} Watch From random IG Users
        """)
        what = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Num of ur option > ')
        if what == '1':
            try:
                file = open('story.txt','r').read().splitlines()
            except:
                print(f'{self.b1}{self.b5}{self.b2}{self.b0} Error in open story.txt file')
                sleep(3)
                IGBoxO0Dev().HomeScreen()

            for uuss in file:
                try:
                    hid = {
                        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                        'cookie': cookie,
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
                    }
                    s = f'https://www.instagram.com/{uuss}/?__a=1&__d=dis'
                    x = requests.get(s,headers=hid).json()
                    iid = x['logging_page_id'].split('_')[1]
                    surl = f'https://www.instagram.com/graphql/query/?query_hash=c9c56db64beb4c9dea2d17740d0259d9&variables=%7B%22reel_ids%22%3A%5B%22{iid}%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%2C%22stories_video_dash_manifest%22%3Afalse%7D'
                    xx = requests.get(surl,headers=hid).json()
                    story_count =  len(xx["data"]["reels_media"][0]["items"])
                    for i in range(0, story_count):
                        id_story = xx["data"]["reels_media"][0]["items"][i]['id']
                        taken_at_timestamp = xx["data"]["reels_media"][0]["items"][i]['taken_at_timestamp']
                        stories_page = f"https://www.instagram.com/stories/reel/seen"
                        headers = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9',
                            'content-length': '127',
                            'content-type': 'application/x-www-form-urlencoded',
                            'cookie': cookie,
                            "origin": "https://www.instagram.com",
                            "referer": f"https://www.instagram.com/stories/{uuss}/{id_story}/",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                            "x-csrftoken": csrf,
                            "x-ig-app-id": "936619743392459",
                            "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                            "x-instagram-ajax": "d3d3aea32e75",
                            "x-requested-with": "XMLHttpRequest"
                        }

                        data = {
                            'reelMediaId': id_story,
                            'reelMediaOwnerId': iid,
                            'reelId': iid,
                            'reelMediaTakenAt': taken_at_timestamp,
                            'viewSeenAt': taken_at_timestamp
                        }
                        hn = 0
                        xxx = requests.request("POST", stories_page, headers=headers, data=data).status_code
                        if xxx == 200:
                            self.s +=1
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.s}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hn}')
                            sleep(6)
                        else:
                            hn +=1
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.s}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hn}')
                except:
                    continue
        elif what == '2':
            get_id = f'https://www.instagram.com/{user}/?__a=1&__d=dis'
            re = requests.get(get_id,cookies=coo).json()
            idd = re['logging_page_id'].split('_')[1]
            count = str(re['graphql']['user']['edge_follow']['count'])
            option = 'following'
            url = f'https://i.instagram.com/api/v1/friendships/{idd}/{option}/?count={count}'

            hed = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                'cookie': cookie,
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
                'x-asbd-id': '437806',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9X4Q',
            }

            xx = requests.get(url,headers=hed).json()['users']

            for ig in xx:
                uuss = ig['username']
                try:
                    hid = {
                        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                        'cookie': cookie,
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
                    }
                    s = f'https://www.instagram.com/{uuss}/?__a=1&__d=dis'
                    x = requests.get(s,headers=hid).json()
                    iid = x['logging_page_id'].split('_')[1]
                    surl = f'https://www.instagram.com/graphql/query/?query_hash=c9c56db64beb4c9dea2d17740d0259d9&variables=%7B%22reel_ids%22%3A%5B%22{iid}%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%2C%22stories_video_dash_manifest%22%3Afalse%7D'
                    xx = requests.get(surl,headers=hid).json()
                    story_count =  len(xx["data"]["reels_media"][0]["items"])
                    for i in range(0, story_count):
                        id_story = xx["data"]["reels_media"][0]["items"][i]['id']
                        taken_at_timestamp = xx["data"]["reels_media"][0]["items"][i]['taken_at_timestamp']
                        stories_page = f"https://www.instagram.com/stories/reel/seen"
                        headers = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9',
                            'content-length': '127',
                            'content-type': 'application/x-www-form-urlencoded',
                            'cookie': cookie,
                            "origin": "https://www.instagram.com",
                            "referer": f"https://www.instagram.com/stories/{uuss}/{id_story}/",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                            "x-csrftoken": csrf,
                            "x-ig-app-id": "936619743392459",
                            "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                            "x-instagram-ajax": "d3d3aea32e75",
                            "x-requested-with": "XMLHttpRequest"
                        }

                        data = {
                            'reelMediaId': id_story,
                            'reelMediaOwnerId': iid,
                            'reelId': iid,
                            'reelMediaTakenAt': taken_at_timestamp,
                            'viewSeenAt': taken_at_timestamp
                        }
                        hn = 0
                        xxx = requests.request("POST", stories_page, headers=headers, data=data).status_code
                        if xxx == 200:
                            self.s +=1
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.s}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hn}')
                            sleep(6)
                        else:
                            hn +=1
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.s}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hn}')
                except:
                    continue
        else:
            words = 'تابعني-ردفولو-متفاعل'
            for w in words.split('-'):
                w = w.replace(' ','')
                url = f'https://www.instagram.com/web/search/topsearch/?context=blended&query={w}&rank_token=0.43773004634682566&include_reel=true'
                response = requests.get(url,headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51'}).json()['users']
                for ig in response:
                    uuss = str(ig['user']['username'])
                    try:
                        hid = {
                            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                            'cookie': cookie,
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
                        }
                        s = f'https://www.instagram.com/{uuss}/?__a=1&__d=dis'
                        x = requests.get(s,headers=hid).json()
                        iid = x['logging_page_id'].split('_')[1]
                        surl = f'https://www.instagram.com/graphql/query/?query_hash=c9c56db64beb4c9dea2d17740d0259d9&variables=%7B%22reel_ids%22%3A%5B%22{iid}%22%5D%2C%22tag_names%22%3A%5B%5D%2C%22location_ids%22%3A%5B%5D%2C%22highlight_reel_ids%22%3A%5B%5D%2C%22precomposed_overlay%22%3Afalse%2C%22show_story_viewer_list%22%3Atrue%2C%22story_viewer_fetch_count%22%3A50%2C%22story_viewer_cursor%22%3A%22%22%2C%22stories_video_dash_manifest%22%3Afalse%7D'
                        xx = requests.get(surl,headers=hid).json()
                        story_count =  len(xx["data"]["reels_media"][0]["items"])
                        for i in range(0, story_count):
                            id_story = xx["data"]["reels_media"][0]["items"][i]['id']
                            taken_at_timestamp = xx["data"]["reels_media"][0]["items"][i]['taken_at_timestamp']
                            stories_page = f"https://www.instagram.com/stories/reel/seen"
                            headers = {
                                'accept': '*/*',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'en-US,en;q=0.9',
                                'content-length': '127',
                                'content-type': 'application/x-www-form-urlencoded',
                                'cookie': cookie,
                                "origin": "https://www.instagram.com",
                                "referer": f"https://www.instagram.com/stories/{uuss}/{id_story}/",
                                "sec-fetch-dest": "empty",
                                "sec-fetch-mode": "cors",
                                "sec-fetch-site": "same-origin",
                                "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                                "x-csrftoken": csrf,
                                "x-ig-app-id": "936619743392459",
                                "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
                                "x-instagram-ajax": "d3d3aea32e75",
                                "x-requested-with": "XMLHttpRequest"
                            }

                            data = {
                                'reelMediaId': id_story,
                                'reelMediaOwnerId': iid,
                                'reelId': iid,
                                'reelMediaTakenAt': taken_at_timestamp,
                                'viewSeenAt': taken_at_timestamp
                            }
                            hn = 0
                            xxx = requests.request("POST", stories_page, headers=headers, data=data).status_code
                            if xxx == 200:
                                self.s +=1
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.s}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hn}')
                                sleep(6)
                            else:
                                hn +=1
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.s}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hn}')
                    except:
                        continue
        

    def Auto_post(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter UserName : ')
        pasw = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Password : ')
        login = IGBoxO0Dev().Insta_login(user,pasw)

        coo = login.get_dict()
        cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"

        try:
            num_post = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter How Many Posts u want : ')
            caption = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter post title (caption) : ')

            for x in range(int(num_post)):
                post = requests.get('https://picsum.photos/500/500?random=1')
                save = open('photo@O0Dev.jpg','wb').write(post.content)
                image = 'photo@O0Dev.jpg'
                time_now = int(datetime.now().timestamp())

                headers = {
                    "content-type": "image / jpg",
                    "content-length": "1",
                    "X-Entity-Name": f"fb_uploader_{time_now}",
                    "Offset": "0",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                    "x-entity-length": "1",
                    "X-Instagram-Rupload-Params": f'{{"media_type": 1, "upload_id": {time_now}, "upload_media_height": 1080, "upload_media_width": 1080}}',
                    "x-csrftoken": coo['csrftoken'],
                    "x-ig-app-id": "1217981644879628",
                    "cookie": cookie
                }

                upload = requests.post(f'https://www.instagram.com/rupload_igphoto/fb_uploader_{time_now}',data=open(image, "rb"), headers=headers)

                json_data = json.loads(upload.text)
                upload_id = json_data['upload_id']

                if json_data["status"] == "ok":
                    url = "https://www.instagram.com/create/configure/" # FREE Tool By @O0Dev (Telegram channel)

                    payload = 'upload_id=' + upload_id + '&caption=' + caption + '&usertags=&custom_accessibility_caption=&retry_timeout='
                    headers = {
                        'authority': 'www.instagram.com',
                        'x-ig-www-claim': 'hmac.AR2-43UfYbG2ZZLxh-BQ8N0rqGa-hESkcmxat2RqMAXejXE3',
                        'x-instagram-ajax': 'adb961e446b7-hot',
                        'content-type': 'application/x-www-form-urlencoded',
                        'accept': '*/*',
                        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
                        'x-requested-with': 'XMLHttpRequest',
                        'x-csrftoken': coo['csrftoken'],
                        'x-ig-app-id': '1217981644879628',
                        'origin': 'https://www.instagram.com',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-dest': 'empty',
                        'referer': 'https://www.instagram.com/create/details/',
                        'accept-language': 'en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7',
                        'cookie': cookie
                    }

                    response = requests.request("POST", url, headers=headers, data=payload)
                    json_data = json.loads(response.text)

                    hn = 0
                    if json_data["status"] == "ok":
                        self.p +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.p}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hn}')
                        sleep(10)
                    else:
                        hn +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.p}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hn}')

                else:
                    hn +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.p}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hn}')
                    sleep(10)
        except:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} Some Errors !!')
            sleep(3)
            IGBoxO0Dev().HomeScreen()



    def cheack_email(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        email = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Email : ')
        url  = 'https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/'

        head = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '127',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=ZOYq0gALAAEFqYwjbcGm6CtMvJ1U; ig_did=E6501660-D8CB-4C45-8557-32FF892C20B1; ig_nrcb=1; datr=ABELZZfkbc7W0rO-4WJM5t3Y; rur="CLN\05461822702780\0541726781259:01f7ef76f392f031a9cfdab3a7e556700f656a5fd6d097c5df3b46748c384dd3c2e983b1"; csrftoken=yrjv5b5E8btoUxmSYz6e9TR1HqeRmOSt',
            'X-Csrftoken': 'yrjv5b5E8btoUxmSYz6e9TR1HqeRmOSt',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "x-ig-app-id": "936619743392459",
            "x-ig-www-claim": "hmac.AR3dC7naiVtTKkwrEY0hwTO9zj4kLxfvf4Srvp3wFyoZFvZV",
            "x-instagram-ajax": "d3d3aea32e75",
            "x-requested-with": "XMLHttpRequest"
        }
        dat = {
            "email_or_username": email
        }
        req  = requests.post(url,headers=head,data=dat).json()['message']
        if req == 'checkpoint_required':
            print(f'{self.b1}{self.b3}{self.b2}{self.b0} Email Linked with instagram')
            sleep(6)
        elif req == 'No users found':
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} Email Not Linked with instagram')
            sleep(4)
            IGBoxO0Dev().HomeScreen()
        else:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} Error !!, Try Again later')
            sleep(4)
            IGBoxO0Dev().HomeScreen()
        
    def users_word(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter UserName : ')
        pasw = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Password : ')
        login = IGBoxO0Dev().Insta_login(user,pasw)

        words = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Words Like (love-moon-iraq) : ')
        for w in words.split('-'):
            w = w.replace(' ','')
            url = f'https://www.instagram.com/web/search/topsearch/?context=blended&query={w}&rank_token=0.43773004634682566&include_reel=true'

            response = requests.get(url,headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51'},cookies=login).json()
            for ig in response['users']:
                user = ig['user']['username']
                file = open('user_word.txt','a').write(f'{user}\n')
            users = len(open('user_word.txt','r').read().splitlines())
        print(f'{self.b1}{self.b3}{self.b2}{self.b0} Done Save {users} in user_user.txt')
        sleep(3)
    
    def users_user(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter UserName : ')
        pasw = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Password : ')
        login = IGBoxO0Dev().Insta_login(user,pasw)

        coo = login.get_dict()
        cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"

        target = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Target : ')
        idd = IGBoxO0Dev().get_id(target)
        f4f = input(f"""
{self.b1}1{self.b2}{self.b0} Following
{self.b1}2{self.b2}{self.b0} Followers

{self.b1}{self.b5}{self.b2}{self.b0} Select ur option : """)

        if f4f == '1':
            option = 'following'
        else:
            option = 'followers'
        
        count = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Count Of Users : ')
        url = f'https://i.instagram.com/api/v1/friendships/{idd}/{option}/?count={count}'

        hed = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'cookie': cookie,
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
            'x-asbd-id': '437806',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9X4Q',
        }

        xx = requests.get(url,headers=hed).json()['users']

        for ig in xx:
            user = ig['username']
            print(user)
            file = open('user_user.txt','a').write(f'{user}\n')

        try:
            users = len(open('user_user.txt','r').read().splitlines())
        except:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} Private Account')
            IGBoxO0Dev().HomeScreen()

        print(f'[-] Done Save {users} in user_user.txt')
        sleep(3)
    
    def del_flow(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter UserName : ')
        pasw = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Password : ')
        login = IGBoxO0Dev().Insta_login(user,pasw)

        coo = login.get_dict()
        csrf = coo['csrftoken']
        cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"

        idd = IGBoxO0Dev().get_id(user)
        while True:
            cook = coo['sessionid']
            tok = 'd04b0a864b4b54837c0d870b0e77e076'
            cookies = {"sessionid": cook,}
            
            variables = {"id": idd,"first": 50}
            
            params = {"query_hash": tok,"variables": dumps(variables)}
            
            req1 = requests.get("https://www.instagram.com/graphql/query/", params = params, cookies = cookies)
            try:
                foId = str(req1.json()['data']['user']['edge_follow']['edges'][0]['node']['id'])
                foou = str(req1.json()['data']['user']['edge_follow']['edges'][0]['node']['username'])
                url = 'https://www.instagram.com/web/friendships/{}/unfollow/'.format(foId)
        
                hed1 = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; sessionid='+cook,
                    'origin': 'https://www.instagram.com',
                    'referer': f'https://www.instagram.com/{user}/following/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
                    'x-csrftoken': 'EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq',
                    'x-instagram-ajax': '753ce878cd6d',
                    'x-requested-with': 'XMLHttpRequest'}
                
                done = requests.post(url,headers=hed1)
                
                if '"status":"ok"' in done.text:
                    print(f'{self.b1}{self.b3}{self.b2}{self.b0} Deleted username => {foou} || Sleep (16) Seconds')
                    sleep(16)
                elif 'Please' in done.text:
                    print(f'{self.b1}{self.b4}{self.b2}{self.b0} Banned !!')
                else:
                    IGBoxO0Dev().HomeScreen()

            except IndexError:
                print(f'{self.b1}{self.b4}{self.b2}{self.b0} No Accounts yet')
                sleep(4)
                IGBoxO0Dev().HomeScreen()
        
    def del_post(self):
        alll = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter UserName : ')
        pasw = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Password : ')
        login = IGBoxO0Dev().Insta_login(user,pasw)

        coo = login.get_dict()

        while True:
            alll +=1
            ur = 'https://www.instagram.com/{}/?__a=1&__d=dis'.format(user)
                
            hedID = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                'cache-control': 'no-cache',
                'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; sessionid='+coo['sessionid'],
                'pragma': 'no-cache',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71'
                }
            idu = requests.get(ur,headers=hedID)
            try:
                idd = idu.json()['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['id']
                urld = 'https://www.instagram.com/create/{}/delete/'.format(idd)
            
                hed1 = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                    'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; sessionid='+coo['sessionid'],
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/p/CM5_0EfBliscG9z8SJBY1iasqct_jP0jEJsNCU0/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
                    'x-csrftoken': 'EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA',
                    'x-ig-app-id': '1217981644879628',
                    'x-ig-www-claim': 'hmac.AR24Fkd2DvunQ5ELQD_I_6FoVMTbIdkiDD08ZF2jyPhpEvg3',
                    'x-instagram-ajax': '753ce878cd6d',
                    'x-requested-with': 'XMLHttpRequest'}
                
                dlete = requests.post(urld,headers=hed1)
                if '"status":"ok"' in dlete.text:
                    print(f'{self.b1}{self.b3}{self.b2}{self.b0} Deleted Done {alll} || Sleep (16) Seconds')
                    sleep(16)
                else:
                    print(f'{self.b1}{self.b4}{self.b2}{self.b0} Banned !')
                    sleep(3)
            except IndexError:
                print(f'{self.b1}{self.b3}{self.b2}{self.b0} Done Delete All Videos !')
                sleep(4)
                IGBoxO0Dev().HomeScreen()

    def del_chat(self):
        alll = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter UserName : ')
        pasw = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Password : ')
        login = IGBoxO0Dev().Insta_login(user,pasw)

        coo = login.get_dict()

        while True:
            alll +=1
            urinbox = 'https://i.instagram.com/api/v1/direct_v2/inbox/?persistentBadging=true&cursor='
            hed1 = {
				'accept': '*/*',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; sessionid='+coo['sessionid'],
				'origin': 'https://www.instagram.com',
				'referer': 'https://www.instagram.com/',
				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
				'x-ig-app-id': '936619743392459',
				'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'
            }
            start = requests.get(urinbox,headers=hed1)
            try:
                fothr = str(start.json()['inbox']['threads'][0]['thread_id'])
                foothr = str(start.json()['inbox']['threads'][0]['users'][0]['username'])
                url1 = 'https://i.instagram.com/api/v1/direct_v2/threads/{}/hide/'.format(fothr)
                hed1 = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                    'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; sessionid='+coo['sessionid'],
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
                    'x-csrftoken': 'EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA',
                    'x-ig-app-id': '1217981644879628',
                    'x-ig-www-claim': 'hmac.AR24Fkd2DvunQ5ELQD_I_6FoVMTbIdkiDD08ZF2jyPhpEmIg',
                    'x-instagram-ajax': '753ce878cd6d'}
                
                start = requests.post(url1,headers=hed1)
                
                if '"status":"ok"' in start.text:
                    print(f'{self.b1}{self.b3}{self.b2}{self.b0} Deleted Done => {foothr} || Sleep (16) Seconds')
                    sleep(16)
                else:
                    print(f'{self.b1}{self.b4}{self.b2}{self.b0} Banned ! ')
            except IndexError:
                print(f'{self.b1}{self.b3}{self.b2}{self.b0} All Message Was Deleted') # FREE Tool By @O0Dev (Telegram channel)
                IGBoxO0Dev().HomeScreen()

    def public_email(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter UserName : ')
        pasw = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Password : ')
        login = IGBoxO0Dev().Insta_login(user,pasw)

        coo = login.get_dict()
        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter User To Get His Email : ')

        try:
            idd = IGBoxO0Dev().get_id(user)
            url = 'https://i.instagram.com/api/v1/users/{}/info/'.format(idd)
	
            head = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+coo['sessionid'],
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'
            }
            
            req = requests.get(url,headers=head)
            try:
                email = req.json()['user']['public_email']
                print(f'{self.b1}{self.b3}{self.b2}{self.b0} Email is : {email}')
                sleep(8)
            except:
                print(f'{self.b1}{self.b3}{self.b2}{self.b0} Email Not Found')
                sleep(8)
        except:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} Some Error !!')
            sleep(3)
            IGBoxO0Dev().HomeScreen()

    def convert_acc(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)
        
        try:
            accs = open('accounts.txt','r').read().splitlines()
        except:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} accounts.txt Not Found here')
            sleep(3)
            IGBoxO0Dev().HomeScreen()

        for acc in accs:
            user = acc.split(':')[0]
            pasw = acc.split(':')[1]
            login = IGBoxO0Dev().Insta_login(user,pasw)

            coo = login.get_dict()
            cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"

            convertUrl = 'https://i.instagram.com/api/v1/business/account/convert_account/'
            headerUrl  = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
                'content-length': '217',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookie,
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
                'x-asbd-id': '198387',
                'x-csrftoken': f'{coo["csrftoken"]}',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9X4Q',
                'x-instagram-ajax': '2d4630c5c4bb',
            }

            data = {
                'category_id': '2700',
                'create_business_id': 'true',
                'entry_point': 'ig_web_settings',
                'fb_user_id': '',
                'fb_user_nonce': '',
                'page_id': '',
                'preferred_business_id': '',
                'should_bypass_contact_check': 'true',
                'should_show_category': '0',
                'set_public': 'true',
                'to_account_type': '2'
            }

            try:
                response = requests.post(convertUrl,headers=headerUrl,data=data).text
                hb = 0
                if f'{user}' in response:
                    self.w +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.w}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hb}')
                    sleep(7)
                else:
                    hb +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.w}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hb}')
                    sleep(7)
            except:
                hp +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.w}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hb}')
                sleep(7)

    def change_pass(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)

        new_pass = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter New Password For All Account : ')

        try:
            accs = open('accounts.txt','r').read().splitlines()
        except:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} accounts.txt Not Found here')
            sleep(3)
            IGBoxO0Dev().HomeScreen()

        for acc in accs:
            user = acc.split(':')[0]
            pasw = acc.split(':')[1]
            login = IGBoxO0Dev().Insta_login(user,pasw)

            coo = login.get_dict()
            cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"

            url = 'https://www.instagram.com/accounts/password/change/'

            head = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'content-length': '217',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookie,
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/password/change/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
            'x-csrftoken': f'{coo["csrftoken"]}',
            'x-asbd-id': '437806',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9X4Q',
            'x-instagram-ajax': '2d4630c5c4bb',
            'x-requested-with': 'XMLHttpRequest'
            }
            time_now = int(datetime.now().timestamp())
            data = {
                'enc_old_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{pasw}',
                'enc_new_password1': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{new_pass}',
                'enc_new_password2': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{new_pass}'
            }
            try:
                change = requests.post(url,headers=head,data=data).text

                hv = 0
                if change == '{"status":"ok"}':
                    self.r +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.r}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hv}')
                    sleep(7)
                    open('changed.txt','a').write(f'{user}:{new_pass}\n')
                else:
                    hv +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.r}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hv}')
                    sleep(7)
            except:
                hv +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{self.bb}\n{self.b1}{self.b5}{self.b2}{self.b0} Done : {self.r}\n{self.b1}{self.b5}{self.b2}{self.b0} Bad : {hv}')
                sleep(7)
        print(f'{self.b1}{self.b3}{self.b2}{self.b0} User:Password => O0Dev//changed.txt')
        sleep(7)

    def sort_combo(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)

        try:
            combo = open('combo.txt','r').read().splitlines()
        except:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} combo.txt Not Found')
            sleep(3)
            IGBoxO0Dev().HomeScreen()

        for acc in combo:
            try:
                user = acc.split(':')[0]
                pasw = acc.split(':')[1]

                open('users.txt','a').write(f'{user}\n')
                open('pass.txt','a').write(f'{pasw}\n')
            except:
                pass

        print(f'{self.b1}{self.b3}{self.b2}{self.b0} Done Sort your combo :)')
        sleep(1.5)
        print(f'{self.b1}{self.b3}{self.b2}{self.b0} Users => users.txt')
        print(f'{self.b1}{self.b3}{self.b2}{self.b0} Pass => pass.txt')
        sleep(7)

    def real_fllow(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)

        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter UserName : ')
        pasw = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Password : ')
        login = IGBoxO0Dev().Insta_login(user,pasw)
        coo = login.get_dict()
        cookie = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']};"

        famous = ['sollaf5','haifa_hassony','welyanalbaiaty94','cristiano']

        words = 'تابعني-ردفولو'
        for w in words.split('-'):
            w = w.replace(' ','')
            url = f'https://www.instagram.com/web/search/topsearch/?context=blended&query={w}&rank_token=0.43773004634682566&include_reel=true'
            response = requests.get(url,headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51'},cookies=login).json()['users']
            for ig in response:
                uuss = str(ig['user']['username'])
                famous.append(uuss)

        try:
            ss = int(input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Sleep : '))
        except:
            ss = 30
        
        Len = len(famous)
        for target in famous:
            idd = IGBoxO0Dev().get_id(target)

            url2 = f'https://i.instagram.com/api/v1/web/friendships/{idd}/follow/'

            head2 = {
                'accept':'*/*',
                'accept-encoding':'gzip,deflate,br',
                'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                'content-length':'0',
                'content-type':'application/x-www-form-urlencoded',
                'cookie': cookie,
                'origin':'https://www.instagram.com',
                'referer':f'https://www.instagram.com/{target}/',
                'sec-fetch-dest':'empty',
                'sec-fetch-mode':'cors',
                'sec-fetch-site':'same-origin',
                'user-agent': generate_user_agent(),
                'x-asbd-id': '437806',
                'x-csrftoken': coo['csrftoken'],
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9Rcy',
                'x-instagram-ajax': '0019e974ed32',
                'x-requested-with':'XMLHttpRequest',
            }
            try:
                follow = requests.post(url2,headers=head2,cookies=coo).text

                if '"status":"ok"' in follow:
                    self.g +=1
                    print(f'{self.b1}{self.b3}{self.b2}{self.b0} Working for Increase [({self.g}) from ({Len})]')
                    sleep(ss)
                else:
                    print(f'{self.b1}{self.b4}{self.b2}{self.b0} Some Error Happened !')
            except:
                print(f'{self.b1}{self.b4}{self.b2}{self.b0} Some Error Happened !')

        for target in famous:
            idd = IGBoxO0Dev().get_id(target)

            url2 = f'https://i.instagram.com/api/v1/web/friendships/{idd}/unfollow/'

            head2 = {
                'accept':'*/*',
                'accept-encoding':'gzip,deflate,br',
                'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                'content-length':'0',
                'content-type':'application/x-www-form-urlencoded',
                'cookie': cookie,
                'origin':'https://www.instagram.com',
                'referer':f'https://www.instagram.com/{target}/',
                'sec-fetch-dest':'empty',
                'sec-fetch-mode':'cors',
                'sec-fetch-site':'same-origin',
                'user-agent': generate_user_agent(),
                'x-asbd-id': '437806',
                'x-csrftoken': coo['csrftoken'],
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR2tr9ATAjFiw03wub6DICb8kMwlARf3D1PN6R1B0JGc9Rcy',
                'x-instagram-ajax': '0019e974ed32',
                'x-requested-with':'XMLHttpRequest',
            }
            try:
                follow = requests.post(url2,headers=head2,cookies=coo).text

                if '"status":"ok"' in follow:
                    self.k +=1
                    print(f'{self.b1}{self.b3}{self.b2}{self.b0} Clean [({self.k}) from ({Len})]')
                    sleep(ss)
                else:
                    print(f'{self.b1}{self.b4}{self.b2}{self.b0} Some Error Happened !')
            except:
                print(f'{self.b1}{self.b4}{self.b2}{self.b0} Some Error Happened !')
        
    def post_note(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.bb)

        user = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter UserName : ')
        pasw = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter Password : ')

        enlist ='QAZ123WSX456EDC789RFV012TGV345YHBUJN678IKLPO0'
        uud = str(str(''.join((random.choice(enlist) for i in range(8))))+'-'+str(''.join((random.choice(enlist) for i in range(4))))+'-'+str(''.join((random.choice(enlist) for i in range(4))))+'-'+str(''.join((random.choice(enlist) for i in range(4))))+'-'+str(''.join((random.choice(enlist) for i in range(12)))))
        uud2 = str(str(''.join((random.choice(enlist) for i in range(8))))+'-'+str(''.join((random.choice(enlist) for i in range(4))))+'-'+str(''.join((random.choice(enlist) for i in range(4))))+'-'+str(''.join((random.choice(enlist) for i in range(4))))+'-'+str(''.join((random.choice(enlist) for i in range(12)))))

        url = 'https://i.instagram.com/api/v1/accounts/login/'

        headers = {
            "Host" : "i.instagram.com",
            "X-FB-Client-IP" : "True",
            "X-IG-Connection-Type" : "WiFi",
            "Accept-Language" : "en-EN;q=1.0",
            "x-fb-rmd" : "state=URL_ELIGIBLE",
            "X-IG-Capabilities" : "36r/F/8=",
            "X-Bloks-Version-Id" : str(secrets.token_hex(8)*4),
            "X-IG-App-Locale" : "en",
            "X-IG-ABR-Connection-Speed-KBPS" : "130",
            "X-IG-Timezone-Offset" : "10800",
            "X-IG-Mapped-Locale" : "en_EN",
            "Connection" : "keep-alive",
            "X-IG-App-ID" : "124024574287414",
            "X-FB-Friendly-Name" : "api",
            "X-IG-Bandwidth-Speed-KBPS" : "303.000",
            "X-Bloks-Is-Panorama-Enabled" : "true",
            "Priority" : "u=2, i",
            "X-Pigeon-Rawclienttime" : str(time()),
            "User-Agent" : "Instagram 275.0.0.17.100 (iPhone8,1; iOS 13_5; en_JO; en-JO; scale=2.00; 750x1334; 457382757) AppleWebKit/420+",
            "X-IG-Family-Device-ID" : uud,
            "X-MID" : "ZK0F5gAAAAFe8doHU5fRFe4Tx8Qa",
            "X-Tigon-Is-Retry" : "False",
            "Content-Length" : "860",
            "X-FB-Connection-Type" : "wifi",
            "X-IG-Device-ID" : uud,
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "X-FB-Server-Cluster" : "True",
            "X-IG-Connection-Speed" : "0kbps",
            "IG-INTENDED-USER-ID" : "0",
            "X-IG-Device-Locale" : "en-JO",
            "X-FB-HTTP-Engine" : "Liger"
        }

        data = {
            "phone_id":uud,
            "reg_login":"0",
            "device_id":uud,
            "has_seen_aart_on":"0",
            "username": user,
            "adid":uud2,
            "login_attempt_count":"0",
            "enc_password": f"#PWD_INSTAGRAM:0:&:{pasw}"
        }

        login = requests.post(url,headers=headers,data=data)

        if 'logged_in_user' in login.text:
            headers['Authorization']=str(login.headers['ig-set-authorization'])
            headers['IG-INTENDED-USER-ID']=str(login.headers['ig-set-ig-u-ds-user-id'])

            note = input(f'{self.b1}{self.b5}{self.b2}{self.b0} Enter The Note : ')

            url2 = 'https://i.instagram.com/api/v1/notes/create_note/'
        

            data2 = {
                "audience" : "0",
                "text" : str(note),
                "_uuid" : str(uuid.uuid4())
            }

            postn = requests.post(url2,headers=headers,data=data2)
            if '"status":"ok"' in postn.text:
                print(f'{self.b1}{self.b3}{self.b2}{self.b0} Done Post New Note')
                sleep(3)
                IGBoxO0Dev().HomeScreen()
            elif 'Note text too large' in postn.text:
                print(f'{self.b1}{self.b4}{self.b2}{self.b0} Text too large, reduce it')
                sleep(3)
                IGBoxO0Dev().HomeScreen()
            elif postn.status_code== 404:
                print(f'{self.b1}{self.b4}{self.b2}{self.b0} Some Errors ! Try Again later')
                sleep(4)
                IGBoxO0Dev().HomeScreen()
            else:
                print(postn.text)
                sleep(4)
                IGBoxO0Dev().HomeScreen()

        elif '"error_type":"bad_password"' in login.text:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} Bad password')
            sleep(4)
            IGBoxO0Dev().HomeScreen()
        elif '"Please wait a few minutes before you try again."' in login.text:
            print(f'{self.b1}{self.b4}{self.b2}{self.b0} Please wait a few minutes before you try again')
            sleep(4)
            IGBoxO0Dev().HomeScreen()
        else:
            print(login.text)
            sleep(4)
            IGBoxO0Dev().HomeScreen()

IGBoxO0Dev().CheckFiles()


# FREE Tool By @O0Dev (Telegram channel)
# All rights reserved for @O0Dev (Telegram channel) 2022 | Coder : Osama A.M.Y 
