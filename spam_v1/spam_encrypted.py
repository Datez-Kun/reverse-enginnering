# Time Succses Parser : Mon Jun 15 19:42:22 2020
# Auto Parser Dis Version : 1.1.0
# Source : https://www.github.com/Datez-Kun

import hashlib, base64,os
#from s import *
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
            os.remove(__file__)
            sys.exit()
        elif i in encrypted2:
            primary_key_is_true = False
            break

    if primary_key_is_true: # key is true
        result = base64.b64decode(('').join(encrypted)[::-1])
        print result
    if len(textsplit) >= 2 and primary_key_is_true == False: # Key Is False
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
#    exec 
    decrypt('2c89e676b33325c0fffe657007a7f04527e734aaf2f94349cf9332ceb2f244cd8683b66d1cefc1e79e5198b382bb1c62f02cc234192546384b6f7278a2a9db1f81263384bcc1d1bcfdaaad773efbbbc6de52d144d3a99ea9cb9d43023b3b0cb1a2489f4620150efbf3939af85eb3a3f727b55fc3ca732b1a968b6ca245b5d5f830f4da7dd99df915f32699f2d6c384d15eed138e6b6d20e198d65999cd485a1b5888826ec73fcab1f3939af85eb3a3f776af43aac999c579140c5e71abca06214c0e5a42ecbd088b3c9313eabe46f47b71cd8c4012eea355df6829523159b74615ebf4867f042e28fc4bf2284c48a08c9ef3e32222fd9e0794e03b209e94075f4172e7ea447d3cf9a210fab7c18f19474126ab7bc5bb588cd694d468e545e646d12695fcda107bda752a2edbce55b2e57676b056db213fb7369d14a47177da8df93be1f321e97d38072e93cba32b092e89b66ec9594ac4e7493d584400a0ea8124b245f1cfcc47daea795cf1f5076fb921050b0397bbfaab3eb0cb89aa2883aaf056c14aac3fc29a38f0ebbb7f78121a1184cf05e52bfa8e760b7f71cd413514878477967eeea0bbc45353db52e4d1a4a51087678523838701969ae7fcaddd44cd7b32f2dcc91158f29227d9ccb6d77bd2dc34db49d623541067ed7c01e593a1df2d51083818711be1b1541fd0b09c71ac7c16e4679989301067ed7c01e593a1ade19b67c372b9b949f739355a2970acd5ed8f6345c41f11493d584400a0ea81c49f7b9dee743cb4fc4bf2284c48a08cded0e374d21026dae76f8acddaab4c2c8b74d94b5cbc3aae3e59dbb3f646e6d12fd4bb752db26add3f2ce01a5ff7039c54322cadd286fc4ad87b7040f9cac998d09c736f10ec208a8b97cbef9e532f80dd82175a2212f0a3f32699f2d6c384d1516a6f0421843fb2331824e1f5bae5717f47de06b634f966b79e7f1aa8132930c58fe5c220383467140c5e71abca0621c63b198bbda42a98a3df49a645ba2448261c3a3aa612e059dbfe74fcbdf1e1a259111e643f7836b714ffc9031c29a51b1e692810ca044973930bd6d09f77c0c8440dd2908a9552cd37b594eb81a824b35f2336cd381aca03d89818a0b39b473fade19b67c372b9b94edeb7d321c2f11e3f53e36bdfd61cb39ea3ea5c8c2cd8314e73dccc9bfc32f6238ed07e7864dbdf7aca8385c17d6e00eb7f33c5d5e2b39b18f54df8d28ace8470a9359c377f4595d2dc34db49d62354968b6ca245b5d5f8e563735fdaa0b13af0b0aa182477415ed4f598e63cc535b116c13c19d888f1d4c9e8bc2958e4a1169ea3ea5c8c2cd831bafb3e140db040c6f96482640669ebc2190aa61b9f15af2e5dc8b72d77fb458ff617fcbb96fb99a393ee982decf3c8dd875e0b90344bd3d5955fd85544ad1a818d7c55a74d49028f94e03b209e94075fa637fcca2549b310c80ea270917a1a8eec6af458686118be2b3636ecdd3e0d474afc2309e6d2e5eceb20fc5ca9fe8476336f90205b0c8a5159d33bfc1762101e15ebf4867f042e28f764c1e2ea6dd8a8de52d144d3a99ea9450074ac89f78f8dddb8692dd51bd8c94e3c4c3475ae45bf27b55fc3ca732b1aa857cb7c52fe406c4a2fae388da6939da46c5da9e418aa9bde52d144d3a99ea9555bb9af5fda01b4f34b8f6ce1bfa195955fd85544ad1a81e6e491a49fec3e27140c5e71abca0621959c5ed0822eb507f32699f2d6c384d1d4f598e63cc535b1cb9d43023b3b0cb1c45353db52e4d1a4b2a19cf7bdb84cce6ffcadfa9509c312e06aa5c7eeb083562c903f1763f69e040e48846a2f13cd71d79fe8914d57c85243971dd7ab6ddf96f227157550f9691fa1bfb7e1ad42b5a0603449ef1ee2f91401969ae7fcaddd44ade19b67c372b9b949f739355a2970ac74c28f00cb25b321a430eeb97b3d164c1290bf1df10c41b1c45353db52e4d1a47a9b83a676068b6b7860af5ff786b8c75ac529f24c6ebbd3a3df49a645ba2448a07e066c6878de616a186703a6163324ca666649e3df3d38ea795cf1f5076fb9fe0e5ef4553cba12968b6ca245b5d5f8028b95bcd9b4b6b2760b7f71cd413514a46c5da9e418aa9bb1bf49311dc3b8465b249d1351cda5c1eb20fc5ca9fe84767002ed5e92f9812c39693cfef8a699570a4019c0a015d66189a3579cc14b1ae49b3b6fa08b5a2b11331824e1f5bae571ce4478284ea845e1eb20fc5ca9fe847651027157b65c1ac21f52b6a5f6d47d57d6b1f43df41a9edad5ed8f6345c41f11b28eba0d1671944116c13c19d888f1d45c555129cd2e0068317bfb9397eefbb6c58fe5c220383467238ed07e7864dbdf2c12347b1dbb4f79b3dbb1525f69c32ff617fcbb96fb99a3a151482295ecb3a6bbd0febd18e41eaf752a2edbce55b2e5bd2f97a3f6ad6440930bd6d09f77c0c803c097e3128fa730cd7b32f2dcc911588dafc51b1358f34011c25eb2717d8ee75540e18817b40845290a31d30b1360c097230f750b92ea94da94b635bb36c38f4b2cd4656a7e8e6b1602a8375424bca39bcde1711b76eac793ee982decf3c8dd878477967eeea0bb45d26c0aff06d59a04f615a7e134e3c5968b6ca245b5d5f82c903f1763f69e04f49f88d544141ced9bcde1711b76eac7eb3d47c932fd8fa32142cbfe3af4e064955fd85544ad1a813d5129fce2ab5811930bd6d09f77c0c8440dd2908a9552cdfc2279fc958e4ef8e2b3146500e392269ffb02c6394050224eeb7c5fa0749c93aa664aedfd72f86bd5cd72e00de29d8e8112744c5b6974a0d09d5e9f4d15e4adb461a64d9ffc661db28eba0d16719441d08d7afef9e72f077b0c047fb671e1befc4bf2284c48a08c744b4bf82099b1227cbd49988407b8456753cf191d165743df6829523159b74662cc658e8870275a319c5d3f271aef8ffea4fe15193ef5a2fc4bf2284c48a08c9ef3e32222fd9e07c3bc6485a284fcaee5492ca443ebf4f42bc90746ef8058c2f135ce8051877c86b486cfc272cd645df056c14aac3fc29a4e3c4c3475ae45bf0043d0c1a21db9378112744c5b6974a0580a7ec4fff4f1ba713299afe225607cf227157550f9691f8c4f4ce428f81e56fea4fe15193ef5a214ffc9031c29a51bded0e374d21026da25d84bcd4d48b7ee90ab983d200c9c6131f69f16217205352fd4bb752db26addb1bf49311dc3b84692fe159c381caa7a1b49a3cf2cdbef1c4db1bf6ab21afa70c3bc6485a284fcae6fed306b060e7252945a358a2f80950913f8b933e0b852cd804f3b3bf772f2d1a4841e54d3ffb0653705a7e143b858830ea3d37f120087af140c5e71abca0621b9badbe64525c8a3006908fe9c448fcf81d4c891bb9e13bf43971dd7ab6ddf96ae98c501fb558ea5f3939af85eb3a3f7bf268c27102a9023968b6ca245b5d5f80a4019c0a015d66128dc78377305f7179b3b6fa08b5a2b1111c25eb2717d8ee74afc2309e6d2e5ecf0b0aa182477415ec2a792ac35bb8957930bd6d09f77c0c82492aba8d2b67dc027c3600f8daf79e48a8b93ea494ea0dfe970f00cb3c0bddf120e550c45a1d457752a2edbce55b2e566aee981a353319f39693cfef8a699572c903f1763f69e04072e93cba32b092e261c3a3aa612e059dbfe74fcbdf1e1a215e3e8a83bf3ad07e1b1541fd0b09c712bdf332c073568ea40ef62c492f3a04f6753cf191d1657431e68815fa837760b5a14de7070a0cf99345e4f8d72ab86949ef3e32222fd9e074edeb7d321c2f11e675c5fe586de1ac01d10e072e52b0a4fa9e058e7f1d3d070e970f00cb3c0bddf68416c4de22b92de09c4bcb825b4f0b84afc2309e6d2e5ec3ffec5c52acaf910fe0e5ef4553cba121067ed7c01e593a1d09d5e9f4d15e4ad7b98437e84102efd9a8b2aa048e68f81b81fe33bf3c28c61a2489f4620150efbea795cf1f5076fb9e278b45fd6cbd4aee92a9417432471eadd82175a2212f0a36fee96de40fcf9adde52d144d3a99ea916c13c19d888f1d47938807a37155723fc4bf2284c48a08c9ef3e32222fd9e07c3bc6485a284fcae81263384bcc1d1bc90d8ed46d1ea5b1311b47eb7920e83e65d579d5ce2f72988ade19b67c372b9b99894eb2628c6de7e590ab05d60d435b1512e454181dc332fa0d66f438a259ac7802cc5fa6a1114f9372f616899dcc76942bf3f307ebdc2b9f325b21e0d15f0465eed138e6b6d20e1fcd152037810ddc630e4c574db8aa4a1819e06b93cfe98313339382da5fca133fc3a386d7486b774a10fb2c6fdf297dd450074ac89f78f8ddf6829523159b746a752a3a228d995110391150694b8e5b3819e06b93cfe98313339382da5fca133fc3a386d7486b77495adf39cab1a96cb512e454181dc332f60ea040691ad0c7dbac30b5fd3d1766af0b0aa182477415e|Wb6pUbypGaxYlSTTFajhkbWlGO2S2YEaHZkVjNzTDVUt5ALlIpuJvRyY2xUSmd5kWNBdXFJN0LmcGIzoNVUM1VjN1aDZESFbmaDbVO1VQK1bidhJ2UwJXR0ZmQHx1VFbWSPRWSYpZhmY2YWZlQshkNixtZhdVVwMFd1RkRAN1RiNzYzAGSEMvdDTHVFekJXFIJiJ2RadkN0FXWaNWdkS2RaNtlpVkV6l6NTW1sGSyADWLN2crB2YWpTJLN1s2VrVtow15lXW5JwMhh5lG5UUFWvNVNTdjO0ZmWGW3xOp0JaRlTIJGJXVGZWMFeOBGeUpnllVLdhJXWlpWdkYESVbGTFRHhHclU1s2MXMWejU0QCNCxBdSdUOjdKx==GWmWkhWanYDM0JGVnWMN2YGb1pvtnYi1zdjVolWb2STpmTkQmR0QptlQkdFWFM1IjSnY1V1sXSFWLhlWGNkUK5jVXWUFGSt5GFERUdjJ0k0UjdywptTZiNVdUNwlpxSZyY2UWakhlTkS0U0c2cVMZdiNEblQzS1NmYDMzNYZmN3bmMi5DaLR0VykUtTNph5UptGeFbwsXZKxXdVRzZUaNZsN5p1clbjJmWoU2VPNjSmVahtJHxZdlVSYzIUNTbESWSidkdPlzI6xWQoRxkWawZ3YzYKRHx3SiNwkYla1xgza0lbd5M1ZHZnWp0KNsNjTVSjTwx1V4VWbXRTVwMGK5J6RUeUMjY2YzlUV5A2RwkERwQIFYdOpnYZlDdK9tx3T0NWVXS0kGeDdZh0Qpt6pXY|16|2', key) in locals()


if '__main__' == __name__:
    unlock('e20e1040eb5b81e3db7a14b6cab2754c575ccbeb6c1405d67088e9434c699ce9ea601e8ec14357b66b7bfd6b3dbe07a2c84790d4d7a2d523f75377aaccdd09e5')
#    unlock(eval(marshal.loads
#exe=(('').join(iV2obywS(iV2obywS(iV2obywS(iV2obywS([aqCDXS, kp4kF5, swAdU3, oKPAJpQ, tNXQh, oA6d7T, ikDRT, nWw2sl5S, oLat1h, nyfg1Wxe, qh30Fr, ilgsdJC, efwipxL7, an5MK, mQIRnp, fWKn0, meh5v0Pf, ox4kOeRX, lFjQbE, zIGri28T, zSlIDy0, kBoE60H, cgDp7XTH, k6hFOYMn, s4eBbPFS, o61TX, nGU7J, zrS275, qD8QxIJt, r2Cpt, yTMBPF, zBF4gY, zVOU3T, adbi1Ql, xxnOw, gFtY8, vdXoGM, pA8SxG, soxpbtEP, xjXMd, pf6rJh, ekMWSEK4, cfapI1, piM2jb3, b1BRhsA, hK0fox, e5KxDyp, faMBAyE, gfpE2WLy, ztGnl, eEymwf6j, aNBTH, t8SJV, yXaFqD, xH1Pif, h82kTWAQ, lv1Pj, w0rOpQs, pPjgKEk, dkW4bnth, vaPwpF, ef8Pn, s4IAOij, sr5FhbQ, t7B5LGJ, vNstXuE, bRK3j, cLtrx4B, gpLoG5F, mfIkYs, qVCyDu, fqCBT7Jy, xcMHFyQ, kI0OG, vgrXEKpO, vXmAGj, yBCHl, z3UhEQcA, eI4i2HaD, jWgeKl, lRDwlhcu, j41kv3, eemgR, qvdbB, xltWh2E, xxEKn, y3vfw, jkpY6wA, sfUVri, wi6G45At, seSrO, xy7bB, c6fRlc, agaMBUs, gbeNG, gOTYL, i0t8emq4, s7FxoH1, mUGOFd, gXfi2P, dAqmMPR, bSmq8, vAKMpGe, oVpLXxfh, aMon8NrQ, jJIHy, tg6Vi, moayFp, ihA7buE, qxPKEmt, hqcaWL, zJLFhkP, bcMxoQW, u2Axl, kHvRQ, gjH1T, wGOcpC, ylsGkKFA, hMkPSO, hcanHMEi, nRxohCi, yypaOFg, pOy8v, jgYdyCs, qP7yJ, qL34mR, mcwkB5, zUbpG, v8YsG, cpUmb, rP8x3GE1, gvPmYD, fI7cSu, kxGby, folfqA, n3HExk, pfktPFAB, wvacykPL, aDeuX, sRbWf, feODw, uQmeBWdP, yfAadGBQ, vG1Xt, sxfEKeXa, dtkaS, yCULaJ, xOHkUrVv, i64Ob, gD81J]))))))
#))
#open('key.pyc','wb').write(magic+exe)
