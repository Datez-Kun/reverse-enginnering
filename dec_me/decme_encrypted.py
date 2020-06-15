import getpass
import hashlib
import base64
import os
from deco import *

def hasher(text, length, key):
    if length > 64:
        raise ValueError('hash length should be lower than 64')
    result = hashlib.sha256(text + key + text).hexdigest()[:length][::-1]
    return result


def separator(text, length):
    return [ text[i:i + length] for i in range(0, len(text), int(length)) ]


def decrypt(text, key):
    textsplit = text.split('!-!')
    (encrypted, shuffled, hash_length, separate_length) = textsplit[0].split('|')
    encrypted = separator(encrypted, int(hash_length))
    encrypted2 = separator(''.join(encrypted), int(hash_length))
    shuffled = separator(shuffled, int(separate_length))
    primary_key_is_true = True
    for i in shuffled:
        hashed = hasher(i, int(hash_length), key)
        if hashed in encrypted:
            encrypted[encrypted.index(hashed)] = i
            continue
    for i in encrypted:
        if i in encrypted2 and len(textsplit) == 1:
            os.remove(__file__)
            sys.exit()
            continue
        if i in encrypted2:
            primary_key_is_true = False
            break
            continue
    if primary_key_is_true: #key is true
        result = base64.b64decode(''.join(encrypted)[::-1])
        print result
    if len(textsplit) >= 2 and primary_key_is_true == False:
        master_key = separator(textsplit[1], int(hash_length))
        master_key2 = separator(''.join(master_key), int(hash_length))
        for i in shuffled:
            hashed = hasher(i, int(hash_length), key)
            if hashed in master_key:
                master_key[master_key.index(hashed)] = i
                continue
        for i in master_key:
            if i in master_key2:
                os.remove(__file__)
                sys.exit()
                continue
        result = base64.b64decode(''.join(master_key)[::-1])
        print result
    return result


def unlock(key):
    decrypt('9434d06d3dc90b2392b3fa738d01e2783fcfee2594db74b77902bf07bef7578773d525cd369aa475a39a9d231f9fbc5624aae0fa2fc9c73c6fbd7376c485b65f3d79e2faf58ca0cfb25b635a2aeb71eea2f1f4ca0911b1498b1c7660a6597ad83a045631799980295c8e0f317daa7f8c9d7a5c7887ecf356e4e51b44c594bad226c287f4d760ce0498a809ec5c06bfb42ca8a2b90703ba6963dbe8c3383ca56c1a1371b063a93abd1b559f09c6567a1979a1027353b71813939f7fcbd90442926458f365a6303eb045156ee473d1f8ce69aa6787b07774b323c3b7b8a86ad0fe8de8db826c796705c809168cd43fda4185c4683d1f9eeb21d1e97f64d33baa41454896181c1107fbab293ed96d4833791049cfc232e68b95e7d2187c76f05d51c49dbaa0fee50ed376cbd3a0a44d6bf6e4cf47d625a2c4fc0e88e6b8e7ee50a992f3d11361a4b66e88e922b662d4b7f9105d2783949e2fc3f1f282968bbed57ca33699e297abf7ccc04dc00380a552eff3d157e6735a0666|GRmciFDZ1R2R4c2SXVTcZh1atxWdkZUOoUGZvNWZ2l0QoBjW2U2chJGKwoFWoBzS2l0QnlWWyQndWJDdrp1VZd2YYhGMLF1bIpEci5mUjVGelpANtZFMkhlSDJ0dj1GbpkSXx0iOzlFWOpXS1lESSxWZyJmevtUSYhGMLR1btR2V1oGZkRjNi5CNmhVeB92YHxmdidGcnl0QBd2YywWdhhlUHxGdjdUOyY1calGeU92SJNUQptUUv1zJ2U2chJGIIJUehdVNIJFblhUU6s1Ja5mSDF0ZJdkULl0QBdWS2J2UCZGW5R2QCd3Ynl0QBdWSyoVMkhkV0J3bw1Wawk0QoBjWIF1SD1mT5plV5YWSspVaCZGWwN0ZvtkV|16|8', key) in locals()

if '__main__' == __name__:
    unlock('4aa252092dd8a794c1d1442c414acb906874b0d17cd417f54c96c4fc2c59111025130da0c3d6bd58732426d5c9b189efa18d0a0de8491b96dddf4e1c6d23217b')
#<---return hashlib.sha512(__file__).hexdigest()--->
'''
    unlock(eval(marshal.loads(''.join(r7MmIDN1(r7MmIDN1(r7MmIDN1(r7MmIDN1([
        lEYxK,
        sLIS0fhA,
        p6Ht5Kf,
        qBoegIN,
        yFSEga5,
        i7mWHw,
        uqyYLA,
        xeAVU1dQ,
        vufhYi,
        rme53kt,
        tUsIN,
        mt1oFUV,
        dlhqL,
        dL8vyfDG,
        oPcLk,
        vuI0mw,
        nmvrw,
        pnmodyR,
        x1ue4awl,
        tuf4jk,
        mEnxKk7,
        s7fG2,
        tKnugU0S,
        j65wypi3,
        vX2Mw,
        zhJBm,
        oSr32,
        oNhUFaD0,
        hPklUy,
        oHICeB,
        dVcGu,
        leVjQk,
        xDNC2xW,
        lacAh6,
        k1oqSdT,
        kcaO0hmr,
        dXKPTc,
        cNE5ngP,
        j1Hjcl,
        t6bIQH,
        p3l2PR,
        lH3D1n,
        viMY7rK,
        llkXTy,
        pxyd5,
        qAURJoiB,
        poELm,
        gLlmv5W,
        onsDkbOS,
        oHamjtK,
        gUdgMmvx,
        jeq7GsVl,
        yYBTFys8,
        k8uWp,
        qIcrUw7O,
        mfG2AIET,
        bKQo1EkJ,
        dyOEGt,
        oEvA1,
        jMiGbaHe,
        pPnvs,
        cKdWgn,
        axw1r8hi,
        vnyqR,
        vB8tuqb,
        tBrp0oOQ,
        oDxCUg,
        dyi7b3,
        ov0liC7,
        kscl03,
        oCMxK0,
        qgquW,
        uj15WNP,
        qyVinF4,
        hL4ln52,
        sPVRQ7,
        wWEAVl,
        uECsA,
        aub2mT,
        hsgBShPa,
        buQ8k7Mx,
        vkLyWI,
        lMhN2q,
        vH8bJRg,
        gn7CO8Uc,
        oNeswPkR,
        pvnWfd8,
        rYB6WA1,
        pC3Boq,
        pDtI3,
        zm7oQ,
        lCYMPa,
        ljdqH8D,
        qpweKUc6,
        aSsm0ar2,
        fCE7Q,
        hdmPJi,
        pksxbBA,
        m5uOAbU,
        e2bakQq,
        ks8Od7tF,
        eOnj6pQ,
        s53NTRA,
        fYuHK1,
        d2Vm8H,
        uprmF,
        cDjacG,
        iGOeygl,
        dKXkNpPi,
        nIk705g,
        dlfgSkx,
        tFfroyXd,
        gnVUg,
        nKr4qW3G,
        mMvmp,
        q4wMxX1s,
        zS0QbmYM,
        sD16y2lO,
        iOPex,
        s1spI,
        eKSbvDWY,
        kIk3C,
        grSuN6,
        sjq6V4,
        bTiFf,
        zSu7Um,
        o5JSr,
        vHDbu,
        ie7aE4J,
        xqg1GQS,
        hl3Dk,
        jtdbxsy,
        nph8oPO,
        mN1T5,
        zDA2wid,
        lkFVCYnE,
        tuRWI7,
        xA74SFl,
        svJw8xWj,
        rXVAb,
        duFIUW,
        kqAOa,
        zVRGS,
        jiuvI,
        h5pWmUE,
        iDuFnEWI,
        d4Yi5n,
        pHq8X,
        bh57w,
        kMm4tGnj]))))))))
'''
