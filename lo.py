# coding=utf-8
# created by Tn.Sad Boy

import os, sys, time, random

# =warna cuy
a="\033[1;30m"
m="\033[1;31m"
b="\033[1;34m"
c="\033[1;36m"
n="\033[0m"


z='''
{}Welcome {}tools {}cracked
{}pergunakan sebaik mungkin ya cok..
Salam Tn.Sad Boy{}
'''.format(a,b,m,c,n)

def type(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
type(z)
time.sleep(5)
os.system("clear")

logo='''
{} _________                       __
{} \_   ___ \____________    ____ |  | __
{} /    \  \/\_  __ \__  \ _/ ___\|  |/ /
{} \     \____|  | \// __ \\  \___|    <
{}  \______  /|__|  (____  /\___  >__|_ \     {}V 1.0
{}         \/            \/     \/     \/  {}./{}Black{}Hat
{}⚇───────────────────────────────────────────────────⚇
                {}✖ {}𝙉𝙤 𝙎𝙮𝙨𝙩𝙚𝙢 𝙄𝙨 𝙎𝙖𝙛𝙚 {}✖
{}⚇───────────────────────────────────────────────────⚇
'''.format(m,m,m,m,m,c,m,a,b,m,c,m,b,m,c)

print logo
