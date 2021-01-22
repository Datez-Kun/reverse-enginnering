import types
import marshal

print '[#] Rebuilding bytecode !!!'
aa = marshal.loads(open('3.pyc').read()[8:])

# method ClAss
cu = aa.co_consts[8]
# method __init__
doki = cu.co_consts[0]
code_3 = types.CodeType(
doki.co_argcount, 
doki.co_nlocals, 
doki.co_stacksize, 
doki.co_flags, 
doki.co_code[6:], # --> fix code patch :v
doki.co_consts, 
doki.co_names,
doki.co_varnames, 
doki.co_filename, 
doki.co_name, 
doki.co_firstlineno, 
doki.co_lnotab, 
doki.co_freevars, 
doki.co_cellvars,
)
# method DaTez_Kun
pico = cu.co_consts[1]
code_4 = types.CodeType(
pico.co_argcount, 
pico.co_nlocals, 
pico.co_stacksize, 
pico.co_flags, 
pico.co_code[6:], # --> fix code patch :v
pico.co_consts, 
pico.co_names,
pico.co_varnames, 
pico.co_filename, 
pico.co_name, 
pico.co_firstlineno, 
pico.co_lnotab, 
pico.co_freevars, 
pico.co_cellvars,
)
# method ReturN
xo = cu.co_consts[2]
code_5 = types.CodeType(
xo.co_argcount, 
xo.co_nlocals, 
xo.co_stacksize, 
xo.co_flags, 
xo.co_code[6:], # --> fix code patch :v
xo.co_consts, 
xo.co_names,
xo.co_varnames, 
xo.co_filename, 
xo.co_name, 
xo.co_firstlineno, 
xo.co_lnotab, 
xo.co_freevars, 
xo.co_cellvars,
)
# ClAss Consts
const_ClAss = (
code_3,
code_4,
code_5,
)
# ClAss Method
puki = cu.co_code[:6] + cu.co_code[15:] # -->Error Fix
code_2 = types.CodeType(
cu.co_argcount, 
cu.co_nlocals, 
cu.co_stacksize, 
cu.co_flags, 
cu.co_code[12:],
const_ClAss, 
cu.co_names,
cu.co_varnames, 
cu.co_filename, 
cu.co_name, 
cu.co_firstlineno, 
cu.co_lnotab, 
cu.co_freevars, 
cu.co_cellvars,
)

#open('out.pyc','wb').write('\x03\xf3\r\n\x8f\xf6\xe0^' + marshal.dumps(code_2))
sili = aa.co_code[9:]
code = types.CodeType(
aa.co_argcount, 
aa.co_nlocals, 
aa.co_stacksize, 
aa.co_flags,
sili, # --> fix code patch :v 
aa.co_consts, 
aa.co_names, 
aa.co_varnames, 
aa.co_filename,
aa.co_name, 
aa.co_firstlineno, 
aa.co_lnotab, 
aa.co_freevars, 
aa.co_cellvars,
)
import dis
#dis.dis(code)
open('analyze.pyc','wb').write('\x03\xf3\r\n\x8f\xf6\xe0^' + marshal.dumps(code))
