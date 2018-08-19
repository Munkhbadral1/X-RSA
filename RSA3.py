import sys
import platform,os
from urllib2 import *
from platform import system
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

clear = ""
if "Windows" in platform.system():
	clear = "cls"
if "Linux" in platform.system():
	clear = "clear"
os.system(clear)
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def banner():
    print("""%s

_____       ________________                  _____      _____
\    \     /    /\          \            _____\    \   /      |_
 \    |   |    /  \    /\    \          /    / \    | /         \\
  \    \ /    /    |   \_\    |        |    |  /___/||     /\    \\
   \    |    /     |      ___/      ____\    \ |   |||    |  |    \\
   /    |    \     |      \  ____  /    /\    \|___|/|     \/      \\
  /    /|\    \   /     /\ \/    \|    |/ \    \     |\      /\     \\
 |____|/ \|____| /_____/ |\______||\____\ /____/|    | \_____\ \_____\\
 |    |   |    | |     | | |     || |   ||    | |    | |     | |     |
 |____|   |____| |_____|/ \|_____| \|___||____|/      \|_____|\|_____|
  %s%s
[ Version : 0.1 ]\033[92m
[ Author  : X-Vector ]\033[96m
[ Github  : github.com/X-Vector ]\033[93m
[ Twitter : twitter.com/@XVector11 ]\033[95m
[ Facebook: facebook.com/X.Vector1 ]\033[95m
[ GreeteZ : Karem Ali ]\033[94m

    """ % (R, W,R))
banner()


#c = 37209877026138824302301697292319328185824059912506644719041273895972747926698556612194455367172368277268883774102719113194850674012999971337550561061697826458468363574428378679179721672530515881761949297613967812683948622068020382771205609975220407119022966600675469044732891210789248284410739482876937857726026431593283960162298707892143970513804892248370427455318472402011536095802255121284911517882268092785246985981687913310965628793178703498961617628661113277249071490584774764571170891391355080033791745662119139170834529306548644716069025161989103880671580075279656495472299747401794635781847901588156099495017
#n = 43210326036290106251088810298667915702007744567467854988107937233622821671752930583378558808381197036542903396534337305723496107154050324953536530993744267386008120658910242143992656773360792182698142273761182047011119261779988377408208858109503177413194541524543447827777831409903664749520527375514748678462101261445039900408999429969510786960471887158957679337190091527913340383310225813322177657695256994315048270952315001100548949554323965404643005206732777361386623591544461533797263652780595639288158892122219626720481472616420118039436680647298714768071797941290307081010086729667552569828323354008441335674251
#d = 36745622940545343875759976434157197886755506358760982257308567037006074391719705315666781200065625116203199598633622026070492775743618607966652393996419663853350085914252797887742782661594880295499227386075929594641556658033207382848075073319786244161193801795105901007640174254798831863226544268004149920625395925259715625248417078457317167458592444532825039828013768181860349705192246622240475711133444054985367520564542488697167606480838294747710396401026533820191299116891186474240520253953309474166963956334430798860084072450328931700881244717326902973061667440442315315084591766881188371668945135391290476758145
#e = 65537
#phi = 43210326036290106251088810298667915702007744567467854988107937233622821671752930583378558808381197036542903396534337305723496107154050324953536530993744267386008120658910242143992656773360792182698142273761182047011119261779988377408208858109503177413194541524543447827777831409903664749520527375514748678461684001179681025836243272641520046001108394411608315423967170123709569701951917513847951924936347574671212789694222728087028519090194131250999358518159691864169187723815719657688598576820104123456547706995794001020837756695923476582226622677087727699446323459489485731800382017980557710365098279949382831681952

c = input(">>> c = ")
n = input(">>> n = ")
d = input(">>> d = ")
e = input(">>> e = ")
phi = input(">>> phi = ")


try:
    slowprint("\n[+] Please Wait ... \033[95m\n")
    n = hex(pow(c,d,n))[2:]
    decode = (n.replace('L','')).decode("hex")
    slowprint("[+] The PlainText = ")
    print decode
except:
    slowprint("[-] False Attack !! ")
