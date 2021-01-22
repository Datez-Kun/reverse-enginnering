# Time Succses Parser : Tue Jun 16 00:42:06 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import hashlib, base64
from var_data import *

def hasher(text, length, key):
    if length > 64:
        raise ValueError('hash length should be lower than 64')
    result = hashlib.sha256(text + key + text).hexdigest()[:length][::-1]
    return result


def separator(text, length):
    return [ text[i:i + length] for i in range(0, len(text), int(length)) ]


def decrypt(text, key):
    textsplit = text.split('!-!')
    encrypted, shuffled, hash_length, separate_length = textsplit[0].split('|')
    encrypted = separator(encrypted, int(hash_length))
    encrypted2 = separator(('').join(encrypted), int(hash_length))
    shuffled = separator(shuffled, int(separate_length))
    primary_key_is_true = True
    for i in shuffled:
        hashed = hasher(i, int(hash_length), key)
        if hashed in encrypted:
            encrypted[encrypted.index(hashed)] = i

    for i in encrypted:
        if i in encrypted2 and len(textsplit) == 1:
            os.remove(__file__) # return deleting file
            sys.exit()
        elif i in encrypted2:
            primary_key_is_true = False #if key is false
            break

    if primary_key_is_true: # if key is true 
        result = base64.b64decode(('').join(encrypted)[::-1]) # return exec file
        print result
    if len(textsplit) >= 2 and primary_key_is_true == False:
        master_key = separator(textsplit[1], int(hash_length))
        master_key2 = separator(('').join(master_key), int(hash_length))
        for i in shuffled:
            hashed = hasher(i, int(hash_length), key)
            if hashed in master_key:
                master_key[master_key.index(hashed)] = i

        for i in master_key:
            if i in master_key2:
                os.remove(__file__)
                sys.exit()

        result = base64.b64decode(('').join(master_key)[::-1])
    return result


def unlock(key):
#    exec  # dont run script
    decrypt('467c7e6986ec0859b8f917b9fed960986c35417ae954b2d5ca4f7b0ac28f79889937fa27d89b3a23ec677b6c894914f0b0e91268fb1f5e1fa0a1f5be67de8e7b94ebde08709e45534a892d90f39db430cfe6cb72d765cafdecc1fc08212a02d1d4875922f7f4746e3310779461a50497811ab1b08bb0ef77edc8f1a79b1e7356ae1322a99a938b5b334c303fc1daea0909de5c01fab91e53fc38cd07bd214f290a08c6571fc6cc3e002ea7ec1c998bb0ba0cf84a05751bfa817c37a9e7bbfd5c82dc87552f03627253efe8183fa0240ebab485e320950650b8a3c364d325d35989c49f040fb20ce96cf8297a071dc2ffae3009b696e8fada7e109d5176f76be2acef92855f2c48fb2ae016d41a91b116cfd27f6f5685ebfc9d2ca7ef33d6ac2e402843a65b1c061f07a48b0ff041e1c9ec4971e16a9c3d40d921febe8379afe9b454212ee69c5f0be935f4384e3aeb4b26683655bdf66dd66d09078273735b7044df9d444ee1e1747111732aa3cf2e83bf74657e16eadef084690f404ad8e1afe57bf828c1222822f5a4d0273e3eaa1f00f9c12f298274837cc7113fb0b65aac3c04037f2ce7e47f29489cf333c5bde6dfcdd3a3876946b1314b72b47ad1a7a26b5611bce6bcd09eeaaad5ba9488cec6201b6a00c31ceefc49ae0278a7453c3f93f25e1ddcb9cb465209fffb5a34090dc9b897f29cfecde457ba2e548b66953951a703e08dbb1b70ac3f796321e25dd053f06cf2771606d6ddfb1c8f00f482eea347e5d8462e7852cf8d891b0f2f0a0c94c5b2f8535019566f076b029e1773c91fe43af71a9e6b1f8acf3d1de6e9f378708211440692d843689c3b70aafb4cc341adfdf86c68346ece5b4115bebb847e05c3dc261f71a049c401d4630862d542bf59ab0e82165653987493d426c19d38b4e1428bb25b735e7edc00c3bb7196ec54c7d433ef7d6310f6d15c5882a4609b71e100ee219faeed00db40f121670eb6b297cc227853fb8c8602552235579ec9872a07c380de68c5781e8e1ef3d6649e14e1fde9dac3db013963ffb7be5d90ee3c532c307fbcb5bc8601ca037036086e963673d770baafbef3693c42707fa198815aeb09437db4ca106f4ad88bdf57a02626cb7fc02be2a4e621d5bfe9e5aec71ebbf56bae659149156dc734db790ac907cf6df786eac92d7660cfeffcdcbb452fbf5082c9616d40604f944feb28bcf1fed127e4e1081feb085988fea1b75f89a60644de03443403156dc734db790ac90257f9a7b3ee090466ebb071f83bd50b12fe7675d4e236628f7ee2697e734c1c7ad409caf9120299620a96e9360aee9464c74a8e73522b988d037c532693b26d62ca1ff3d7e6a0f70c338a0154e6b35258dc7c27e0fe4ed7da316d2970f9c6392c9c9b79dff3bdf088f533349194a72142f8ae2616f3d4de5ad070c389cc2c2458ad1cbdf005d7e2a148e0da4c4529b79345369bf923b5a077ee791b3867ae48402d3667c3a1cba8a26ae017a81ada9303476bbb7ac24ba43df9cda574ac0de5f54f08492843d7e44bd1b9a66331f0fa5cfd46e49cc0986d045b4c22ff1992d8f0f04a835a8e77f033284c99a3f44f1aa699a1b5ff298aa658c94d8699bd60224e34f83efd23c1f337a10f9fcc57a4f1f315f852365167930ba26120bd1b757333980275e9c897780df32eccb7689e6c8310e380f86aa748cce7947f55c73d27c50d4efa8c82ddc04751cf0820a0d765558535b64b428fce3ce0250f64f4512e273214842866a0d9e7b2c31c07a713cc9ffc2e40e650dfef33d7fbdad6e476a552796e45893614d9ce0f159889e9b506ca2c099934a0a2fdb28308a2442c6727e13f31d909ed50d3a26ae017a81ada9301555565e507b63368ac9e4cf0550c6f42b6556cc39f9287c1fe4e2eab80d64d8b2fefa4301618695f384ea68dd3d70a|LN0Zv1zJoUGZvNWRnFlM5Q3YHZEM3QpF0ZJNkQ2NWeXVVdjJDespFWB9ndmUHxmchhlSwJ65EdU1WO0J2MJdsN2Qnp3SRBndjlJlnQGJ2VKxmWHJDWGhnZYZ0dnFlbGVXSE92ZKl3aLR2RoFTWpFUOJdEa2VzdmYXZVekhlTkaNBXSB9maJZEdjNkQyJ2MKlWWXRDJkZYlHOnZ2QBdKBnYuF1ZKJDZwR3dWTEFkNORVW202ShdVWnJWb582YYJleZhlQ3lERwcmNkQ4wUeBZXSGhUeZdVNup1UnhXTGhnZYlHemZmR5gWTUNneNdVMUR2VWZXV0ZWdkVzl1VDa3lERwc2YtZ0MmZDJEOYNzdnhlR2QtxGdjdUO5R2QY1UdahFawR2QnBBdWSDF0ZJNUQnlnpUM4RTTXpkYNRwQGSCp3TphjdaJB9WTDRDeLF1bnlDF0ZJNUQnlESSBnh1R1gDWzc3ZJNsN2Qnh3SRBXdiJql0dNRUU5l0RKhYlnQmlkR5YWSGhUN2J2V5kXSIJFbzZJNkQmlkR5YGW2chJGI0J3bw1Wa2UIF0ZTJTO5lVbXhHMMNkQCNGSJd2YlRkRpdleFdTT2RsRnWTVjeidkVidVV1NmM4xmWYF5F0ZYFDOnh1M3dXN3V2UjB3QnBXb5J0QahlSpl1VohOZnWHV1ZNlGNzM2YyY1aJdUO1lESidkV3JmM042QpFXN6VGWOBjWXBzbkQjhlR5YGWzgnZmZDJkZYlnQjJmbnN2RWlHZY5EahlJl1VOJnWYlkbD5kRpdleFdTT6JFdoN2MWJXYyYUdJdi12anh1R0cGWIdpkSXx0iO6s1JJlneNJTMXFGWKFzYFSnhXWsNHePpXTYJDb1NGSWBzSDRnQxIWbOZnYYJUNVNjVpNmMOlXYXp4ZGW5J0YYNUQvhEe2plM4s0YIpEcCZ3Y5d3ZkdEb0pkTqNWbsdHZDJEc1UCtEZY5EMRNlQmUwJ2VVV3YygHblV5RGWOhWY5J0b0wkaBVnT5F0bhhDbwEGSWlGTt5kdwo1Vw8mSy40cadRp1VxkGZXZEMJZWO09UaCFVZYJ1bilXQ5k0QKNWZEZlMohmYtVDbiNkQ5F2V1ATSDR2YlR1c650Rw4WSDN3ZEciJDNn1Ue0MDTjSpl1V042QuJFcmYyQzZZ5Gbwo1VENJNEarp1VahGZ2UCJnWTFkbJN0c2RsRnWTVjeidkVTdMlGN1p0dvdWS0MCVDZHhmdipWSHRzZYFTOmhVeBdUSDF0ZJNUQnl0QCBTYXFDbM5mTzp0QBdWSDF0ZJhkQBd3TUt2dNl2YLRmNUQnlkR4NGWxg2V1ATSDR2YlRkRqF0SJlnQRVGWS9VeCNGWDFkbYFTOKJjTzp1VGlnS5t0bNl2aLNGSKBnYrd2UuZlekVkRJliNTSnF2UCBnYpJkUwMGSNZDT5hzSWTDRTeLF1bnl0QiNVOxRGWOBTWXhnYXVVdjJDespFWpNkbClXYXVDMJdWTql0ZNpWQ510QWZkRjNi5CN2U2ckQmlkR4NWSGljZXdmNUQnhVM4YXSlR5pUertkYHljbHVDaidVV2k0RS5GJXWXRzZkdVNwQHZVekhlToFWejt1VWd3SEFUdNl2asZHZYJVMZ1WVnB3F2V4xmWDJUbj1BdWSDF0ZJhkQ5FCd3YtxWdkNUQuRGaZJDdsNmbNZ3YWWyQHbjl2YLNGSVBXMjNjUClURohEF0dNRUQ3tEVvtEci5WUnpUMk9WWhdlSzp1UCJkYtJVUwZ3Y5VjelhlTWSDF0ZJNUQnl0Q1oXZY5EMadFMvpnlkR4cGWHVDOJN3dmZGhDcJNEOnhEbJVEcxM2MSJUSFhGaZJDdsNWajtpdleFdTT6ZEdUdidUVykESax2Yu5oFWeC92YDJkciNKpXWzoEcZ1WVnF0YIpEci5WUnp0MUSDF0ZJNUQnl0QJZEe000VKJWTUNi5WUnpUM4RTTXpzcYNDemhVM4YHW0ZJNkQ2NWe1oXZXYTJ0ahdFZxIWb0QBdWSDF0ZJNUQahVQv50Urt0YIp2R5MnYyUjbJdUMUOmZ2Q4cGWyE0ZDVDcjJjRzN2Roh2SDtmNDlWQnl0QiJDNn1Ua0MDTqVUaXpXR30keoRHW5J2Ujd2S5JkekhmTqlENPRVW00ka0ZJNUQnlESSBnYUaNdmUHZlaiJTM4kES3dmZDFkdJZJpnTEllePREbqtVeiJDbrl0QnFTTIFFMNdmTDRTeMpi1WOvNWQvdWSDF1VOJnWYl0ZYdEN1M3dmZDF0ZJR0duJldiJDe6l0RsV0UCRkYHZUdalXQhJGKjVGelpAN2UCd3YtxWdkNUQuhuF1ZKFDe000VKJGeZx2c49keNJjYFbaNkQtF2V4xWSkYNR1c61kMxMmYUSvF2Urd2S5Fkb|16|14', key) in locals()


if '__main__' == __name__:
    unlock('7f84926b65ef83a2d8d13219e5d8ee8ccf1557f0558159945a26561efd8d044fd2bf46e5df351074af71e2eb9c0da569925683fd3e54f31bed836529d7e7ba1a')
#    unlock(eval(marshal.loads
#exe=(('').join(bun2lIWo(bun2lIWo(bun2lIWo(bun2lIWo([wnH30Y, tSwcv0, uDTsgaW, tqxIPO, nlEwp, xOjMbct, sIsrnq, ppHcE8, nL6vGQEs, pudy4, k4Bra7e, vhTeanrR, sL3dAs, wTIWdXK, hiWY8, ujQoAd, uTE6mLjr, tgAD5B, o1fv4, ftiQ1gy, eHKFV, ojcexX8C, lD3n7F, uIhuEMq, ayosDYR, vd6gV, vJgYWsH, hcWp6, pklr5YtH, gKbur, rmLFd7G, i1uaedU, xHA5PXV, zKrWXlTm, joA7lK, oc3is, g1Kje, eJ6VD3kL, tU7V3, vTCwVP, tKG3lNxY, tIDKnPMu, x567sj, zolRa5, jysgx, kpWc0, cGA67nR, aJ3BSPip, lOaWPK1M, cWxa52, di5OE, i147g, y7OMmenI, aawlyqH, nXsTE, pXcFs, vFiu81, lbloxT, a6cVy, kpKCI, wP8c0h, xjCPy, j1StBON, cByEX, kOb8t56, z0jXWUrR, avtfx8, f4g7bTWv, juhGDx7R, bAaFUqi, pXSIt, lQRsfm, aYn1P, g0Clc2, sHVjF6W4, oDUEWw5N, yqXt1ons, pt3BjHFv, o5Xmysg, iVnKNY8, glV2RE4o, ydrMk, awQemKlk, iHQrEVgj, t6SLU, qkS6B, gaXS3wR, uAJnk, d1Rnw6j, rSXcFev, dyX1C8, tPanbJ, geBJX0I, cb2o34, bCOQFv, fvOm1R, r3QPhq07, vevJGnt, oKfmJyDq, an7NMK0t, gc4KFI, cVqwUK, vhU6bKXC, z8DmMy, tKM8itC, r5ICNE, wSOcq, c1nBHl, pRmC3, bMmwC3, bUPAMX, beflX, ltjdY, hks3y8q, uvsCKhl, n4OcB, uG5cL, qPF1nf, yoqQ4Sh, xwtIy, stK46, u8Uq6, edhsXF3f, sQxUM, jdN8yYMb, y2J1I5, pbiWU, gwBaLn, hvDfnR, v0o5e4hA, qv3pbM, zQHbn0, eVqIGL01, bGdhHI, msOhJ7b, wQhtO, gHPcvY, kis6lNLP, qK3PB, pXp1s, n25tSJDR, p6Wun7K, i4Ld3qQY, na6GK2, hmCcF, dqU7WwGM, aWeOY, z0mHV, lhq3TM, i8TtYX]))))))
#))
#open('key.pyc','wb').write(magic+exe)
