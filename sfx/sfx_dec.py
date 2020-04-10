# uncompyle6 version 3.6.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <Nanta_ID>
import os, sys, time, random
lg = '\n  ________________________  ___\n /   _____/\\_   _____/\\   \\/  /\n \\_____  \\  |    __)   \\     /\n /        \\ |     \\    /     \\\n/_______  / \\___  /   /___/\\  \\\n        \\/      \\/          \\_/\niPhone PUBGM for Android\ncoded by R3DB0T\n'

def clear():
    os.system('clear')


def jaja(g):
    for h in g + '\n':
        sys.stdout.write(h)
        sys.stdout.flush()
        time.sleep(0.01)


core = '[SoundQuality]\n+CVars=2A160C171D280C1815100D002D00091C4448'

def main():
    clear()
    print lg
    if checkBackup == True:
        cb = '\x1b[0;92mOK\x1b[0;39m'
    else:
        cb = '\x1b[0;91mNO\x1b[0;39m'
    print '[ Backup status : ' + cb + ' ]'
    print '[1] Install'
    print '[2] Backup UserSettings.ini'
    print '[0] Exit'
    q = raw_input('  ==> ')
    if q == '1':
        con = raw_input('[!] Warn! If you not need your config deleted,\n[!] Please backup first\n[*] Type y/Y then ENTER to continue\n[*] Type n/N then ENTER to close\n  ==> ')
        if con in ('n', 'N'):
            main()
        else:
            install()
    elif q == '2':
        backup()
    else:
        exit('[ Thanks for download & use! ]')


def install():
    jaja('========================')
    print "[*] Installing, don't close/exit while procces is done"
    time.sleep(random.choice([1, 2, 3, 4, 5]))
    with open('/storage/emulated/0/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserSettings.ini', 'w') as (put):
        put.write(core)
    exit('[*] Done.')


def backup():
    jaja('========================')
    print "[*] Backuping UserSettings.ini, don't close/exit while procces is done"
    os.system('cp -r /storage/emulated/0/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserSettings.ini /storage/emulated/0/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserSettings.ini.backup')
    exit('[*] Done, named to UserSettings.ini.backup')


if __name__ == '__main__':
    os.system('termux-setup-storage')
    checkApp = os.path.exists('/data/user/0/com.tencent.ig')
    if checkApp != True:
        exit('[!] Your PUBGM not installed')
    if os.path.exists('/storage/emulated/0/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserSettings.ini.backup') == True:
        checkBackup = True
    else:
        checkBackup = False
    main()