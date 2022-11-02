import webbrowser
import pyautogui as au
import time
num = input("number phone of reciver : ")
msg = input("message text : ")
url ="https://web.whatsapp.com/send?phone={}&text=%20".format(num)
rep = input("number of repetitions : ")
wait = input("wait before starting (s)>10  : ")
input(" tap  > enter <  to continue ...")
webbrowser.open_new_tab(url)# https://web.whatsapp.com/send?phone=+212629854115&text=%20
time.sleep(int(wait))
for r in range(int(rep)):
    au.write(msg)
    au.press('enter')
print('program finnesh')
