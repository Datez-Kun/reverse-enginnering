# FileName : None
# Python Bytecode : 3.8
# Time Succses Decompiled : Wed Aug 26 23:13:34 2020
# Timestamp In Code: 2020-06-27 04:07:18

import websocket
from websocket import create_connection
import json, time, datetime
from datetime import datetime
try:
    import thread
except ImportError:
    import _thread as thread
else:
    import time, requests, random
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import os, sys
    token = [
     '247448f9ff3bce363bf2e996688cf440c119ddd5',
     'fb7cde5a98798f046848a703f5703694df9da3f5',
     'e7efd338b1adb91fe6e0ce0ad4ad9830b4a61ba6',
     '5df024c2e294a471980f602bac32b93c7a091be3',
     'a3c8789943abf28f8a81fe810039a7beb8d1383b',
     '8fe0ea72f3805d305483940fb56b0044b89a1d9a',
     '610273d5ab3321a9f5f6d7357c85e19918bfd1bf',
     '2bff84708b54dfedf5672305f1b91b28bafb5d21',
     '36cd412dd0b6d68cb3a632aaa51d3f24df481f26',
     'b7b2fb70c5376718931b558cda457f683e70e2bb',
     'dad817b84de3e8ae8d8b33759649f0e5ef8765da',
     '15d53c09a9a8b23866869a93b0b8fa759d90ed61',
     'a9394db8696e262889f2e3e07faa27b35e52985f',
     '8fe0ea72f3805d305483940fb56b0044b89a1d9a',
     '6745249d89855c002eef8f889dd72278e5023acf',
     '2c0dfa2ff9a0d5877175eb5d0a600afdc598073b',
     '0c6057e4ce16672256169846ffc9c5e34c893f40',
     'eac7cedbfd40570493c446225d1284a32827c94b',
     'ceec5a55cc095182bcb770e734124d4aed40bdb8',
     '10a3a958ef940441f2be554c578c8f85ea6e8da7',
     'e5cb891b335f7f162f059c48071393ec1db361a4',
     'a82c51d126608211bd4681fc0514dbb33cab1120',
     'bb7e53d33a2da7b34b987ce58f0cecf8c56a883f',
     '47e6188ebff00c850e76a6f2aa870cd7c7e340f1',
     '2c0dfa2ff9a0d5877175eb5d0a600afdc598073b',
     '44cd0e5f7f44bdd40ccc490c6951c90929cc0e69',
     '91e5c61f2e4a1af756f9d747d085204233f09626',
     '0aa830daf61f0749363132948b6c698c72214f95',
     '4800b8983097cc3bd6b6fbee1e05024cb8d69a5a',
     '9152f08748578466df7ebfaea3996583f78a723f',
     '6fe0edb1852bfeb8326f2702e18baf04a8e6dd39',
     '3cfc91f40115cc11a8a2b2fc3e11b95d0f56de5e',
     'a294fd44213b8ebf4b0c1bd856f6af22f4e07170',
     '4d8b4f27d7e8fe0c2e28c4c0a0e5459926117564',
     '821d6f4df73d2684db634306c9231d7490f2b269',
     '53751de76ef873e1836b3c168a18dba1bf65f90b',
     '922a4730130ad4ceedbc74623419e43ebfa15fae',
     'f3b13523fc68dec4952c8ea191257c2daddc3360',
     '46492e24867969a2ecb3fa49b9852efc5aa82339',
     '24777c252d2b9beaece91f95735d5017a8329f10',
     'aa551af641839f3d39a5d323a92e3778b74ebbb0',
     'b50e20226b2523093ecda51ca5cdb701bed1bf54',
     '2d31e3629644d9b8e3f52a68e2df421b146bc389',
     '436ea6ec379044ba004b4a1f7fb412b264bfd415',
     '5f69e76aa68df24e90c9e2bec93587c970848d78',
     '8c05b03af799ea4f84319d45936b91402b3da693',
     '533eee48caa39650f9bbfebe6957d47c76289f6b',
     'c8ed5186f6ef64552376535a61a6eb1f7ad55b05',
     '1f91a7f90f7c60ba82ebbbb5987ec8b48386f15a',
     'b31d890f2513a57993e638bc45dbd24f4b9ec8c7                               ',
     'a4efc86e880602d304268e21de5c0bb54949c115',
     '91fa9adb4b7046d18ceeb6e13cfd8c782900cbd9',
     '1032dbc2587012658ae420f201a26056e9bf7cdb',
     'e811d3e7fa2aad93df931ce0f4c533391ad520ff',
     'e0893e0fcdd28a11924445c2ded61492b868007a',
     '5fa56416902456c6c3c96991189e5b93dd172dda',
     '961f2cbbebcaf757b32e362d645ec7ccba9ee6ad',
     '1f760f807591e6ef5a6436e542e34b216e38bb75',
     'ef0d40af1c132b55f5bef1c4368b1aa8a00097d1',
     'f4a241e912803e719668878482768aea07356abd',
     '9fcb7e8af9e925b2c5dfb56baea24c649c9733de',
     '82589fb39dbcbd394cb2763d6cfdf982636db99b',
     '662e763803adea0eace2027d50a3af3eee6c00c8',
     '68d97ad6bcdcca33cf8ded93b4cb07ca6bda433f',
     '9450fcb7da39f6799f66d49d5d4b5ec983d4decc',
     '0c39e1a98ad9e892e61ae6828e3d2a315c2b03d4',
     '3fde52e0a35193b82c09eea8178b7804a1d664b5',
     '89d83c68ba3ae9607c471acb416d43ff24fc49f3',
     'c32ff9b0f5123fe5fab2f891a78e59f9ac44c618',
     '5d7a35ae391caa124085aed670c49b3c3019c680',
     '27e8c2b2c1709f7813e6f1c5784c2b20bd44a9ef',
     'fa8f79dda57556ec1a57d71ce64c99684270cbed',
     'a8b52a929cdf5a2edc0bf043fb1706df2535890f',
     '5a6262049b9b2dd3821ec60fc4a8cbab6a01fa8f',
     'ed8e8a0c4d1e1c8acf7a31c808836542e9effbf9',
     '57acb40639a224595533a96465e710cb72ac5204',
     '335cba7b161af69423e809bf1e6ee70ba9c6513a',
     '6bd2a9ea129fffac24d87c7b09cd2fd386ef7284',
     '719b4f5f23a44c47df58ea85715c2742a30fa79d',
     '0daf82c0ee85d4dcede11748e07fb4fe00a5731e',
     '0958bdf41c60a8517441a7781dd3683fabd1e569',
     '9912decdd8a6b7664f4268b520b21817e137bac2',
     'bca6b642b18fc777d450714cdc37c6a8e63e7a5b',
     '5dbd83c9730302acd287ad8061635cbff40f7b9e',
     'abe5e994658533204ee9150957be2ef2e6fd7b7a',
     '769142c01bdb8e2e21cfa8a837428dcd24eba0e1',
     '9ad87b8b98b3cfff0fe6e0ebcb29dc0b6b2f90b7',
     '81bf7ffc3a273f0424412971f8b2b0cdec43c6b8',
     'f6a52af6f5af3f081aa7ee121eb0db721830a587',
     'a59dd850a75bf735adc079d6aeb468cfbd8cc2f1',
     'e6104239e8d53d133f9b79b3536234b5d577187b',
     '8c65e50923c60c3df05ef048256d27b0d20f3c12',
     '7fb03337e72dc351209c69fd88d4eb8b8513c0b1',
     '83ec91d286d5a9aa961864905fa04249d13d494b',
     '0d0038c514400df8f54222f1b1d237e53301d444',
     '75b67e43e118f7c057123c559a1e368bbadb7a8d',
     'a94b13c143335570b9e7c2dfa3e5aa8c61d807aa',
     'ce7c9a02baaace428dd3dbf37d3c13570b10f636',
     '35e803edd263e4aab29b260dba27c0d6c7fbe9ce',
     '310d117daf03dfb57fd347d2769db7ed3bcea79f',
     'e695f2a1a88a1e415b0a69b209ca4a538cf18df5',
     '205aea8a7233425c029276abe6224e4df7170e85',
     '0eaa409eba6759c9303741b32638d509a97311e2',
     '01a3da48645562b0a1e2e0d50ac5ad7986f6f804',
     'c32ff9b0f5123fe5fab2f891a78e59f9ac44c618',
     'ba6290507f2d01197cd23c9335424159e7caec67',
     '7c1f3082db36dda7f1c4194c7b8794006f939cf8',
     'c9fb296a62a3dfb00e2d27becebef95a7822ebe4',
     'be21b9fa029107d6131296b9198ad7195b33ffc4',
     '953539ae7e63f1727092982540902cabb8cedd46',
     '4946a492fec793132de02298c5877c4046831c48',
     '0985828b3f66ad9d008151699331e7d4b7dec151',
     'e64bac7fb45eedd1aa826cc4b0838639107fd56a',
     '8a00d32178fd553153f6d7a767a239fbca1886cf',
     '9246c55a551d67c2462108141f0e5bac4991a517',
     '6fcd13983a0142ae804573e34b00904550f574e3',
     '2d34a278494f58a5ebb3e67e5a3e12db43b5034b',
     'c0ecb8b04d88d5eb49b2373bc16c923ced29c524',
     '0eadf1894c07a97244f7ccf84cec1b132cba976c',
     '32a0eed4f28e961715feae1ce208c0d07f46c735',
     '0ee869c0712c42ad6c8662c17aaecd19fcdf8dd1',
     'b7c77a59171502e39c4bf386246384372d47043c',
     '46b67351e331fe86331ab097d794cb1589a4a830',
     '8b346293305e25699daebf95d14543600cfcbe05',
     'a97b4fedec07580b1b3a9c1f9cc00e2e4b7ce4e8',
     'cb92f75c76602dae7478fa7519022512deaae9d4',
     '440b33dad96b0e7f1be7054076f2cb5179032686',
     '7fdee01317e66764629b44627674074cd578d242',
     '69e42c08f4995d9ccb539f8ec4bcbcb0da719e3b',
     '6057322086bbcac056b1220abe2cba40c56aa611',
     '35e09792313363e7da3e0a0d64c987ab81fc43c5',
     '6aad3d237c2bb89d2421945afec76ebd1e45f951',
     'fb259d300a1e0b4f414d78d571b3a4dfa8a7f1f5',
     'c0e830cd6db1d67f83d62a54a675598af3d45591',
     '667ea1931450552c34bcf40f9e5c3085bafab416',
     '8921300150827e6b58aebb786e0d0f7fa1225f0e',
     'f6fdf91cff0c63b909c45a0b3519c54f5fe3eb65',
     'ca353f6ca3b9b4f1a5b12f4e875e61478682fca9',
     '44eb50e19d565eff8cc9490a54269bfe2b2e35f5',
     '1748ea2ed743bb30dabd3ad781ac43aa675c0070',
     '3a23ba9f94eda441a41022923ae758f108b5b0cb',
     'bfc497beafb62e5daa6f46e3fbbeec9b9a1932b1',
     '23008ab0165eca0e22ac3edf2ef99f6c4c1673fe',
     '234ff63cdc5db19a4d8c7ebc4fc1814918c2fe94',
     '1a620e8563dc1c7b05d3d92a1b41daefb16a721b',
     '0ca359d8f14fcec9a9fc1f6d9e5334706e260438',
     '5b1665a5166c3e8151cb359be5b9e5f52d1c33ff',
     'd2cad024e4efae0d62d3243c132044bb57efe38f',
     '8a10ad00ac70cea5c403725c6376ab61e1c263da',
     '4be632cefd894ef37a93605383389d1693648e76',
     'ea6fce6d0d9d47573123d44ab2726b2bb661dccc',
     'e0a73368d1cfe253f5112c42518a197706d879f2',
     'a273d745616c65b33cbd48e2f40fbe9fa51a0193',
     'faf5e91f391565d0a96c5f8399ae04a97c7a2d90',
     '35504899a6a87d63de8410a416e9d6288c9ead60',
     'bfd7e29e08b8ca6628f0db6a90ecef5d8ccf3121',
     '1d5e3136981b32ecb2949d84a0f930a92a9f8891',
     'dcde4de30c7899321308defda0a70fe7d922921d',
     '1868c239787d73e3d2740899a45ce6f5a1450bf9',
     '582265366196ef856292ce52caa4403e53f1fa35',
     'f1455b00d12b5419a9b580fcfd028cce998056e4',
     'a0683f0f3fc91ebacb08c993b440392b2d225689',
     '9899ac8c90cf0e5bc9b3bb327160e438a6b6214f',
     'ee0db639f8b3e74ddea3e45c1bfa3bf7bfcaed24',
     '8898066bd789638d4bdfc5e3cbdb4bbaa0972104',
     '68e6f10a7ac0ce82e25007b3118a224ef6e4b4a1',
     '7c279d694095c68035f7f365f284d73923bade0e',
     'f50009bfc0ad907f6eda4aa52d96f737caf53be5',
     'fb9b218b2b72ff05f5bebad334a7f80b5cdfafa4',
     '752cba16e82b5a97822b81f72e3fc2b33fd9b99f',
     'b674226dfae89b236add16b2c7df259df380ccc7',
     'd467cc6b0bff0054b63b165b24f8af3d0af9602f',
     'dc9c9d6c9ed226e02b84115618ab99512bdc77ca',
     '90c5cc0880c7dd04a20c6a5e2a197f3a01a99d74',
     '1099c25fa3b5d607ea1c18165f4b64a72322c440',
     '840b720f7c3f3a0e41d04cf2b700bb891805c91d',
     '4c31294dc67b5d0669ce1df42fc01362b1b371ab',
     'a3297d55064ae46ed06892133c342e91df724cb5',
     'ee64427066f50170293ea1102fd37b4d035282fb',
     '1845ef553445aafe2fcee7bac5005b84044b9db7',
     '56cc8c8f42e17523d1baf6efb400b8e9d5e1a1c4',
     '4fe8d359aae539007b08888a47dd22e92aa46780',
     '4ce1e3cdcfd21ec5ca57148d1ccb3e90c7d51e54',
     '8aba4c81ad709b20944c4ee2363d13a7bd9dcebc',
     '7d55a161732b472aeb054807b091783654386009',
     '3e6065a767e9e8aa5d0b560fe5d6a4b8f3e3b7bb',
     '6d1a8a2fd2d154dc1eb97e61ba356635b8c4aac7',
     '3570107f623c545f6053acbc1479538f9518d652',
     'cf3231fb3dc2e1bfee17f0a48b333f99889692c6',
     'b9bd71ae4b6714cc9cfa2edd1ebf21077a9efc16',
     '2632f430e3313782b2174d61aae30c3b01e64d2a',
     'a28494e7770f062d8f641d8e3c13ecd68a43ade1',
     '8fe2d160c20bc3b782f84952e43ad9cc251dea87',
     'f2631bbdd75355ca9872ddad1119a2fc9738050a',
     'f96916bcc4d2b5b3d2ddf282f763a4908aa11cac',
     '1faf226217de0f5dd95dea38c951f46715167338',
     'bd8aefe8ac2c917d9a9c8698c866207880d9f43b']
    idbot = [
     '210952568',
     '211666779',
     '211666796',
     '210986817',
     '211666926',
     '210991267',
     '211928532',
     '212155151',
     '212155171',
     '212155195',
     '212155336',
     '212155447',
     '212155476',
     '211932351',
     '211932300',
     '211891521',
     '211926810',
     '212276640',
     '212276652',
     '212276660',
     '212276667',
     '212276680',
     '212088228',
     '212216426',
     '212216471',
     '212216525',
     '212216607',
     '211739827',
     '212216666',
     '211928155',
     '212218056',
     '212284374',
     '212284401',
     '212284411',
     '212284456',
     '212284472',
     '212284478',
     '212284488',
     '211666796',
     '212284559',
     '212284612',
     '212284634',
     '212284655',
     '212284674',
     '212284685',
     '212284753',
     '212284880',
     '212284888',
     '212288338',
     '212288348',
     '212288356',
     '212288369',
     '212288379',
     '212288396',
     '212288421',
     '212288432',
     '211524168',
     '211524205',
     '211492108',
     '211495701',
     '211495753',
     '211495795',
     '211467950',
     '211468011',
     '211468342',
     '211468440',
     '211468476',
     '211468500',
     '211469937',
     '211454531',
     '211454565',
     '211454712',
     '211421338',
     '211421764',
     '211421443',
     '211421932',
     '211421943',
     '211651986',
     '211652047',
     '211652083',
     '211652104',
     '211652109',
     '211652380',
     '211652225',
     '211652394',
     '211652434',
     '211652446',
     '211652469',
     '211652487',
     '211652696',
     '211652938',
     '211653001',
     '211460000',
     '210887962',
     '211460128',
     '210814565',
     '210888121',
     '210888136',
     '211460167',
     '211460246',
     '211653281',
     '211653744',
     '211653734',
     '211655322',
     '211655459',
     '211655379',
     '211651970',
     '211651988',
     '211652010',
     '211652025',
     '211652040',
     '211651933',
     '211651944',
     '211652086',
     '211652107',
     '211652139',
     '211652218',
     '211652247',
     '211652259',
     '211655690',
     '211652277',
     '211652335',
     '211654301',
     '211654391',
     '211654449',
     '211510287',
     '211655771',
     '211511379',
     '211660668',
     '211660710',
     '210946801']
    uproom = True
    botout = True
    xz = 1
    status = 'tidur'
    nama = 'xyx'
    judul = 'xyz'
    timeh = datetime.today()
    response3 = '{"div":"hai"}'
    createdl = datetime.today()
    ranke = []
    totid = []
    countr = 15
    nurut = False
    vocer = 3
    vocer2 = 1
    json2 = 'jsjaj'
    inccountr = True
    listlagu = ['lagu', 'lagu', 'lagu', 'lagu']
    lagucountr = 0
    ngeup = False
    ciddd = ''
    tiru = False
    tokenl = ''
    iddd = ''
    cou = 1
    namal = 'xyz'
    judull = 'xwx'
    timehl2 = datetime.today()

    def signa():
        os.system('clear')
        print('\x1b[1;33;42mDibuat Oleh Wibu :v yang suka oppai')
        print('with love ❤')
        print('CP : 085155415154\n')
        print(datetime.now())
        print('VERSI : vvvip')
        print('\x1b[1;37;40m\n')


    def sign(pess):
        os.system('clear')
        print('\x1b[1;34;42mDibuat Oleh Wibu Tachi Dayo :v')
        print('with love ❤')
        print('CP : 085155415154\n')
        print(datetime.now())
        print('VERSI : Onii Chan~ (~￣▽￣)~')
        print(pess)
        print('\x1b[1;37;40m\n')


    def Remove(duplicate):
        final_list = []
        for num in duplicate:
            if num not in final_list:
                final_list.append(num)
            return final_list


    def slowprint(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.09)


    def on_message(ws, message):
        global cou
        global iddd
        chat = json.loads(message)
        print(cou)
        cou += 1
        uid = chat['data']['author']['id']
        nick = chat['data']['author']['nickname']
        evn = chat['event']
        if evn == 'live_present':
            print(chat['data']['sticker'])
            gift = chat['data']['sticker']
            kado = gift[8:]
            if kado == 'myheart':
                kado = 'kado balon'
        if evn == 'live_message':
            psn = chat['data']['message']
            tag = chat['data']['author']['tag']
        if evn == 'live_block':
            iddd = chat['data']['author']['id']
            print(iddd)
            if str(iddd) in idbot:
                ws.close()
        pesan2 = '{"appversion":"4.3.16","event":"live_message","token":"ce5c43e71af39a1d73ccdd82b1fa89b6feb65454","useragent":"Android","message":"' + pesanspam + '"}'
        ws.send(pesan2)


    def on_error(ws, error):
        print(error)


    def on_close(ws):
        print('### closed ###')


    def on_open(ws):

        def run(*args):
            global slink
            global tokenl
            pesan = '{"live_id":' + slink + ',"token":"' + tokenl + '","event":"live_' + joinmode + 'join","appversion":"4.3.16","useragent":"Android"}'
            ws.send(pesan)
            print('====')

        thread.start_new_thread(run, ())
        print('aaa')


    def multiucing(tokett):
        global tokenl
        tokenl = tokett
        headers = {'User-Agent':'Mozilla/5.0',  'Authorization':'Token ' + tokett}
        ress = requests.post(('https://id-api.spooncast.net/lives/' + slink + '/' + 'join' + '/'), params=params, headers=headers)
        stts = ress.json()['status_code']
        if stts == 200:
            websocket.enableTrace(False)
            ws = websocket.WebSocketApp(('wss://id-heimdallr.spooncast.net/' + slink), on_message=on_message, on_error=on_error, on_close=on_close)
            ws.on_open = on_open
            ws.run_forever()
        else:
            print('loading')


    if __name__ == '__main__':
        kode = 0
        print('sedang mengecek ...')
        print('sedang memuat ...')
        print('pastikan internet aman ...')
        zz = requests.get('https://diveot.site/spoon/kode8.json')
        os.system('clear')
        print('sedang memuat ...')
        pess = requests.get('https://diveot.site/spoon/pesan.txt').text
        aktivasi = zz.json()['kode']
        if os.path.exists('../wibu/js.gm') == False:
            signa()
            file = open('../wibu/js.gm', 'w+')
            abc = random.randint(100000, 999999)
            file.write(str(abc))
            file.close()
            f = open('../wibu/js.gm', 'r')
            kod = int(f.read())
            print('KODE AKTIVASI = ' + str(kod))
            if os.path.exists('../sepun/johnson.div') == True:
                g = open('../sepun/johnson.div', 'r')
                kod = int(g.read())
                print('KODE AKTIVASI SEPUN7 = ' + str(kod))
                g.close()
            f.close()
            exit()
        else:
            f = open('../wibu/js.gm', 'r')
            kod = int(f.read())
            kode = kod * 50
            if kode in aktivasi:
                os.system('clear')
                print('status:sudah aktivasi')
            else:
                signa()
                print('status:belum aktivasi')
                print('KODE AKTIVASI = ' + str(kod))
                if os.path.exists('../sepun/johnson.div') == True:
                    g = open('../sepun/johnson.div', 'r')
                    kod = int(g.read())
                    print('KODE AKTIVASI SEPUN7 = ' + str(kod * 50 + 5))
                    g.close()
                exit()
            f.close()
        pw = zz.json()['password']
        slowprint('SELAMAT DATANG')
        time.sleep(0.5)
        os.system('clear')
        slowprint('enjoy')
        sign(pess)
        token = Remove(token)
        params = {'cv': 'heimdallr2'}
        txtid = input('masukkan link spoon: ')
        pesanspam = input('masukkan isi pesan: ')
        headers = {'User-Agent':'Mozilla/5.0',  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
        response = requests.get(txtid)
        url = response.url
        slink = url[34:-59]
        response2 = requests.get('https://id-api.spooncast.net/lives/' + slink)
        json2 = response2
        joinmode = ''
        random.shuffle(token)
        processes = []
        with ThreadPoolExecutor(max_workers=5) as (executor):
            for toket in token:
                processes.append(executor.submit(multiucing, toket))
