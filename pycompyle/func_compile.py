
__all__ = ['compile']

import __builtin__
import imp
import marshal
import os.path
import base64

def compile(py_file):
    useless_code = base64.decodestring('wcHkh5Or4c/n1MuBzsijwcHkjpSBh46rh8zq1Y62h56kl6Srh46rxc/5h5Orl4G7rQ==')
    find_data = base64.decodestring('svSJp8qLp8qLpw==')
    replace_data = base64.decodestring('svSJpyqepyqKpw==')
    ___ = lambda x, y: ''.join([chr(ord(x[i]) ^ ord(y[(lambda x, y: (x % y if x % y >= 0 else y))(i, len(y))])) for i in range(len(x))])
    with open(py_file, 'U') as f:
        source_code = f.read()
    source_code = ___(useless_code, base64.decodestring((lambda x, y: x(x, y))(lambda x, y: y and chr(y%256) + x(x, y//256) or "", 1278621296))) + source_code
    codeobject = __builtin__.compile(source_code, py_file, 'exec')
    py_file = os.path.join(os.path.dirname(py_file), os.path.splitext(os.path.basename(py_file))[0] + '.pyc')
    with open(py_file, 'wb') as f:
        f.write(base64.decodestring('QQAAAA=='))
        f.write(__import__('random').choice([ base64.decodestring(z) for z in ('kJ0A/w==', 'kJ3//w==', 'kJ1//w==', 'kJ2A/w==')]))
        marshal.dump(codeobject, f)
        f.flush()
        f.seek(0, 0)
        f.write(imp.get_magic())
    source_code = open(py_file, 'rb').read()
    start_offset = len(find_data) + len(imp.get_magic())
    end_offset = source_code.find(___(find_data, base64.decodestring((lambda x, y: x(x, y))(lambda x, y: y and chr(y%256) + x(x, y//256) or "", 1278621296))))
    source_code = source_code.replace(___(find_data, base64.decodestring((lambda x, y: x(x, y))(lambda x, y: y and chr(y%256) + x(x, y//256) or "", 1278621296))), ___(replace_data, base64.decodestring((lambda x, y: x(x, y))(lambda x, y: y and chr(y%256) + x(x, y//256) or "", 1278621296))))
    with open(py_file, 'wb') as f:
        f.write(source_code)
    return (end_offset - start_offset)

