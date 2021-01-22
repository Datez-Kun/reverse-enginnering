# Decompiled At :  Tue Mar 17 15:33:48 2020
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:25:46) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
""" Ga kesusun rapih ? Ya maap gan [+] wa.me/+628978125962 """
import os, urllib, requests, time, sys
try:
    os.mkdir('Images')
except:
    pass

logo = '\x1b[1;31m\n    (\xc2\xaf`\xc2\xb7.\xc2\xb8\xc2\xb8.\xc2\xb7\xc2\xb4\xc2\xaf`\xc2\xb7.\xc2\xb8\xc2\xb8.\xc2\xb7\xc2\xb4\xc2\xaf)\n    ( \\                / )\n   ( \\ )    \x1b[1;32mRemove\x1b[1;31m    ( / )\n  ( ) (   \x1b[1;33mBackground\x1b[1;31m   ) ( )\n   ( / )    \x1b[1;32mImages\x1b[1;31m    ( \\ )\n    ( /                 \\ )\n     (_.\xc2\xb7\xc2\xb4\xc2\xaf`\xc2\xb7.\xc2\xb8\xc2\xb8.\xc2\xb7\xc2\xb4\xc2\xaf`\xc2\xb7.\xc2\xb8_)'
author = '\x1b[1;36mAllviyan'
github = '\x1b[1;36mHttps://github.com/Al2VyN'

def main():
    """ Input Image File / Url """
    os.system('clear')
    print logo
    print '\x1b[1;0mAuthor :', author
    print '\x1b[1;0mGithub :', github
    img = raw_input('\n\x1b[1;0m[\x1b[1;32m+\x1b[1;0m] Image File / Url : \x1b[1;32m')
    if 'https' in img or 'http' in img:
        try:
            image = urllib.urlopen(img)
            if image.headers.maintype == 'image':
                image_url(img)
            else:
                print '\x1b[1;0m[\x1b[1;31m+\x1b[1;0m]\x1b[1;0m Error Url Image Not Found'
                time.sleep(2)
                main()
        except:
            print '\x1b[1;0m[\x1b[1;31m+\x1b[1;0m]\x1b[1;0m Error Url Image Not Found'
            time.sleep(2)
            main()

    else:
        image_file(img)


def image_url(url):
    """ Process Image From Url """
    print '\x1b[1;0m[\x1b[1;32m+\x1b[1;0m] Starting Remove Background'
    sys.stdout.write('\x1b[1;0m[\x1b[1;32m+\x1b[1;0m] \x1b[1;0mProgress\x1b[1;32m 0\x1b[1;0m%')
    sys.stdout.flush()
    out = url.split('/')[(-1)].split('.')[0] + '_remove-bg.png'
    req = requests.post('https://api.remove.bg/v1.0/removebg', data={'image_url': url, 'size': 'auto'}, headers={'X-Api-Key': 'JvBniboyxaCf8BXNifX2edkH'})
    get_image(req.content, out)


def image_file(file):
    """ Process Image From File """
    try:
        image = open(file, 'rb').read()
    except:
        print '\x1b[1;0m[\x1b[1;31m+\x1b[1;0m]\x1b[1;0m Error Image Not Found'
        time.sleep(2)
        main()

    print '\x1b[1;0m[\x1b[1;32m+\x1b[1;0m] Starting Remove Background'
    sys.stdout.write('\x1b[1;0m[\x1b[1;32m+\x1b[1;0m] \x1b[1;0mProgress\x1b[1;32m 0\x1b[1;0m%')
    sys.stdout.flush()
    out = file.split('.')[0] + '_remove-bg.png'
    req = requests.post('https://api.remove.bg/v1.0/removebg', files={'image_file': image}, data={'size': 'auto'}, headers={'X-Api-Key': 'JvBniboyxaCf8BXNifX2edkH'})
    get_image(req.content, out)


def get_image(image, filename):
    """ Output Image From File/Url """
    size = len(str(image))
    if size != 0:
        for i in range(0, int(size)):
            percent = int(1.0 * i / int(size) * 100)
            sys.stdout.write(('\r\x1b[1;0m[\x1b[1;32m+\x1b[1;0m] \x1b[1;0mProgress \x1b[1;32m{}\x1b[1;0m%').format(str(percent)))
            sys.stdout.write('\r\x1b[1;0m[\x1b[1;32m+\x1b[1;0m] \x1b[1;0mProgress \x1b[1;32m100\x1b[1;0m%')
            sys.stdout.flush()

        print '\n\x1b[1;0m[\x1b[1;32m+\x1b[1;0m]\x1b[1;0m Done'
        open('Images/' + filename, 'wb').write(image)
        time.sleep(1)
        print ('\x1b[1;0m[\x1b[1;32m+\x1b[1;0m]\x1b[1;0m File Saved : Images/{}').format(filename)
    else:
        print "\n\x1b[1;0m[\x1b[1;31m+\x1b[1;0m]\x1b[1;0m Error Can't Remove Background Image"


main()