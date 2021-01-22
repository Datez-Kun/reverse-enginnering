# Decompiled At : Thu May  7 15:17:31 WIB 2020
# From Python2.7.17
import os, sys, subprocess

def install():
    """Install Module"""
    lime = '\x1b[1;92m'
    tutup = '\x1b[0m'
    os.system('clear')
    print tutup + ('[ Dark-FB ]v1.8').center(44)
    print ' Ingin membeli api-key bisa hubungi kami melalui : '
    print ' Wa : ' + lime + '+62 8978125962\n' + tutup
    raw_input('[>] Masukkan API KEY : ')
    raw_input('Enter untuk hubungi saya ...')
    os.system('clear')
    subprocess.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=+628978125962&text=Buy+license+Dark-Fb+1.8'])


install()
