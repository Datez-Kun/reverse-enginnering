# FileNames : <zen_ezz>
# Python Bytecode : 3.8.5
# Selector visit In Line 144 file visit.pyc
# Timestamp In Code :  (2020-08-24 02:40:47)

# Method Name:       visit
# Filename:          <zen_ezz>
# Argument count:    0
# Position-only argument count: 0
# Keyword-only arguments: 0
# Number of locals:  16
# Stack size:        15
# Flags:             0x00000043 (NOFREE | NEWLOCALS | OPTIMIZED)
# First Line:        144
# Constants:
#    0: None
#    1: 5000000
#    2: '\r'
#    3: '                                                              '
#    4: '\x1b[1;35mSTATUS VISIT    : \x1b[1;36mGathering data ... !'
#    5: '/visit'
#    6: ('entity', 'message')
#    7: 2
#    8: 1
#    9: 0
#   10: ('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash')
#   11: 'Sorry, there are no new ads available'
#   12: -1
#   13: '\x1b[1;35mSTATUS VISIT    : \x1b[1;36m'
#   14: 15
#   15: True
#   16: ('headers', 'timeout', 'allow_redirects')
#   17: 'html.parser'
#   18: 'div'
#   19: 'g-recaptcha'
#   20: ('class_',)
#   21: 'headbar'
#   22: ('id',)
#   23: 'You must stay'
#   24: 'Please stay on'
#   25: '([\\d.]*\\d+)'
#   26: '\r\x1b[1;35mSTATUS VISIT    : \x1b[1;36mYou earned '
#   27: ' '
#   28: '\n'
#   29: 'container-fluid'
#   30: 'data-code'
#   31: 'data-timer'
#   32: 'data-token'
#   33: 'https://dogeclick.com/reward'
#   34: ('code', 'token')
#   35: ('data', 'headers', 'timeout', 'allow_redirects')
#   36: 'reward'
#   37: '                                                                '
#   38: '\x1b[1;35mSTATUS VISIT    : \x1b[1;36mCaptcha Detected'
#   39: ('data',)
#   40: '\r\x1b[1;35mSTATUS VISIT    : \x1b[1;36mSkip captcha ... !\n'
#   41: 3
# Names:
#    0: requests
#    1: Session
#    2: range
#    3: sys
#    4: stdout
#    5: write
#    6: flush
#    7: client
#    8: send_message
#    9: channel_entity
#   10: sleep
#   11: GetHistoryRequest
#   12: messages
#   13: message
#   14: find
#   15: reply_markup
#   16: rows
#   17: buttons
#   18: url
#   19: id
#   20: get
#   21: ua
#   22: BeautifulSoup
#   23: content
#   24: re
#   25: findall
#   26: tunggu
#   27: int
#   28: cr
#   29: find_all
#   30: post
#   31: json
#   32: loads
#   33: text
#   34: GetBotCallbackAnswerRequest
#   35: channel_username
#   36: data
# Varnames:
#	c, i, posts, url, id, r, soup, message, sec, messageres, reward, dat, code, timer, tokena, js
# Local variables:
#    0: c
#    1: i
#    2: posts
#    3: url
#    4: id
#    5: r
#    6: soup
#    7: message
#    8: sec
#    9: messageres
#   10: reward
#   11: dat
#   12: code
#   13: timer
#   14: tokena
#   15: js
145           0 LOAD_GLOBAL              0 (requests)
              2 LOAD_METHOD              1 (Session)
              4 CALL_METHOD              0
              6 STORE_FAST               0 (c)
c = requests.Session()

146           8 LOAD_GLOBAL              2 (range)
             10 LOAD_CONST               1 (5000000)
             12 CALL_FUNCTION            1
             14 GET_ITER
        >>   16 EXTENDED_ARG             4
             18 FOR_ITER              1044 (to 1064)
             20 STORE_FAST               1 (i)
for i in range(5000000):

147          22 LOAD_GLOBAL              3 (sys)
             24 LOAD_ATTR                4 (stdout)
             26 LOAD_METHOD              5 (write)
             28 LOAD_CONST               2 ('\r')
             30 CALL_METHOD              1
             32 POP_TOP
sys.stdout.write('\r')

148          34 LOAD_GLOBAL              3 (sys)
             36 LOAD_ATTR                4 (stdout)
             38 LOAD_METHOD              5 (write)
             40 LOAD_CONST               3 ('                                                              ')
             42 CALL_METHOD              1
             44 POP_TOP
sys.stdout.write('                                                              ')

149          46 LOAD_GLOBAL              3 (sys)
             48 LOAD_ATTR                4 (stdout)
             50 LOAD_METHOD              5 (write)
             52 LOAD_CONST               2 ('\r')
             54 CALL_METHOD              1
             56 POP_TOP
sys.stdout.write('\r')

150          58 LOAD_GLOBAL              3 (sys)
             60 LOAD_ATTR                4 (stdout)
             62 LOAD_METHOD              5 (write)
             64 LOAD_CONST               4 ('\x1b[1;35mSTATUS VISIT    : \x1b[1;36mGathering data ... !')
             66 CALL_METHOD              1
             68 POP_TOP
sys.stdout.write('\x1b[1;35mSTATUS VISIT    : \x1b[1;36mGathering data ... !')

151          70 LOAD_GLOBAL              3 (sys)
             72 LOAD_ATTR                4 (stdout)
             74 LOAD_METHOD              6 (flush)
             76 CALL_METHOD              0
             78 POP_TOP
sys.stdout.flush()

152          80 LOAD_GLOBAL              7 (client)
             82 LOAD_ATTR                8 (send_message)
             84 LOAD_GLOBAL              9 (channel_entity)
             86 LOAD_CONST               5 ('/visit')
             88 LOAD_CONST               6 (('entity', 'message'))
             90 CALL_FUNCTION_KW         2
             92 POP_TOP
client.send_message(entity=channel_entity, message='/visit')

153          94 LOAD_GLOBAL             10 (sleep)
             96 LOAD_CONST               7 (2)
             98 CALL_FUNCTION            1
            100 POP_TOP
sleep(2)

154         102 LOAD_GLOBAL              7 (client)
            104 LOAD_GLOBAL             11 (GetHistoryRequest)
            106 LOAD_GLOBAL              9 (channel_entity)
            108 LOAD_CONST               8 (1)
            110 LOAD_CONST               0 (None)
            112 LOAD_CONST               9 (0)
            114 LOAD_CONST               9 (0)
            116 LOAD_CONST               9 (0)
            118 LOAD_CONST               9 (0)
            120 LOAD_CONST               9 (0)
            122 LOAD_CONST              10 (('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash'))
            124 CALL_FUNCTION_KW         8
            126 CALL_FUNCTION            1
            128 STORE_FAST               2 (posts)
posts = client(GetHistoryRequest(
peer=channel_entity, 
limit=1, 
offset_date=None, 
offset_id=0, 
max_id=0, 
min_id=0, 
add_offset=0, 
hash=0))

155         130 LOAD_FAST                2 (posts)
            132 LOAD_ATTR               12 (messages)
            134 LOAD_CONST               9 (0)
            136 BINARY_SUBSCR
            138 LOAD_ATTR               13 (message)
            140 LOAD_METHOD             14 (find)
            142 LOAD_CONST              11 ('Sorry, there are no new ads available')
            144 CALL_METHOD              1
            146 LOAD_CONST              12 (-1)
            148 COMPARE_OP               3 (!=)
            150 POP_JUMP_IF_FALSE      160
if posts.messages[0].message.find('Sorry, there are no new ads available') != -1:

156         152 POP_TOP
            154 EXTENDED_ARG             4
            156 JUMP_ABSOLUTE         1064
            158 JUMP_ABSOLUTE           16

158     >>  160 EXTENDED_ARG             2
            162 SETUP_FINALLY          662 (to 826) 
try:

159         164 LOAD_FAST                2 (posts)
            166 LOAD_ATTR               12 (messages)
            168 LOAD_CONST               9 (0)
            170 BINARY_SUBSCR
            172 LOAD_ATTR               15 (reply_markup)
            174 LOAD_ATTR               16 (rows)
            176 LOAD_CONST               9 (0)
            178 BINARY_SUBSCR
            180 LOAD_ATTR               17 (buttons)
            182 LOAD_CONST               9 (0)
            184 BINARY_SUBSCR
            186 LOAD_ATTR               18 (url)
            188 STORE_FAST               3 (url)
url = posts.messages[0].reply_markup.rows[0].buttons[0].url

160         190 LOAD_GLOBAL              3 (sys)
            192 LOAD_ATTR                4 (stdout)
            194 LOAD_METHOD              5 (write)
            196 LOAD_CONST               2 ('\r')
            198 CALL_METHOD              1
            200 POP_TOP
sys.stdout.write('\r')

161         202 LOAD_GLOBAL              3 (sys)
            204 LOAD_ATTR                4 (stdout)
            206 LOAD_METHOD              5 (write)
            208 LOAD_CONST              13 ('\x1b[1;35mSTATUS VISIT    : \x1b[1;36m')
            210 LOAD_FAST                3 (url)
            212 FORMAT_VALUE             0
            214 BUILD_STRING             2
            216 CALL_METHOD              1
            218 POP_TOP
sys.stdout.write(f"\x1b[1;35mSTATUS VISIT    : \x1b[1;36m{url}")

162         220 LOAD_GLOBAL              3 (sys)
            222 LOAD_ATTR                4 (stdout)
            224 LOAD_METHOD              6 (flush)
            226 CALL_METHOD              0
            228 POP_TOP
sys.stdout.flush()

163         230 LOAD_FAST                2 (posts)
            232 LOAD_ATTR               12 (messages)
            234 LOAD_CONST               9 (0)
            236 BINARY_SUBSCR
            238 LOAD_ATTR               19 (id)
            240 STORE_FAST               4 (id)
id = posts.messages[0].id

164         242 LOAD_FAST                0 (c)
            244 LOAD_ATTR               20 (get)
            246 LOAD_FAST                3 (url)
            248 LOAD_GLOBAL             21 (ua)
            250 LOAD_CONST              14 (15)
            252 LOAD_CONST              15 (True)
            254 LOAD_CONST              16 (('headers', 'timeout', 'allow_redirects'))
            256 CALL_FUNCTION_KW         4
            258 STORE_FAST               5 (r)
r = c.get(url, headers=ua, timeout=15, allow_redirects=True)

165         260 LOAD_GLOBAL             22 (BeautifulSoup)
            262 LOAD_FAST                5 (r)
            264 LOAD_ATTR               23 (content)
            266 LOAD_CONST              17 ('html.parser')
            268 CALL_FUNCTION            2
            270 STORE_FAST               6 (soup)
soup = BeautifulSoup(r.content, 'html.parser')

166         272 LOAD_FAST                6 (soup)
            274 LOAD_ATTR               14 (find)
            276 LOAD_CONST              18 ('div')
            278 LOAD_CONST              19 ('g-recaptcha')
            280 LOAD_CONST              20 (('class_',))
            282 CALL_FUNCTION_KW         2
            284 LOAD_CONST               0 (None)
            286 COMPARE_OP               8 (is)
            288 EXTENDED_ARG             2
            290 POP_JUMP_IF_FALSE      540
            292 LOAD_FAST                6 (soup)
            294 LOAD_ATTR               14 (find)
            296 LOAD_CONST              18 ('div')
            298 LOAD_CONST              21 ('headbar')
            300 LOAD_CONST              22 (('id',))
            302 CALL_FUNCTION_KW         2
            304 LOAD_CONST               0 (None)
            306 COMPARE_OP               8 (is)
            308 EXTENDED_ARG             2
            310 POP_JUMP_IF_FALSE      540
if soup.find('div', class_='g-recaptcha') is None and soup.find('div', id='headbar') is None:

167         312 LOAD_GLOBAL             10 (sleep)
            314 LOAD_CONST               7 (2)
            316 CALL_FUNCTION            1
            318 POP_TOP
sleep(2)

168         320 LOAD_GLOBAL              7 (client)
            322 LOAD_GLOBAL             11 (GetHistoryRequest)
            324 LOAD_GLOBAL              9 (channel_entity)
            326 LOAD_CONST               8 (1)
            328 LOAD_CONST               0 (None)
            330 LOAD_CONST               9 (0)
            332 LOAD_CONST               9 (0)
            334 LOAD_CONST               9 (0)
            336 LOAD_CONST               9 (0)
            338 LOAD_CONST               9 (0)
            340 LOAD_CONST              10 (('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash'))
            342 CALL_FUNCTION_KW         8
            344 CALL_FUNCTION            1
            346 STORE_FAST               2 (posts)
posts = client(GetHistoryRequest(
peer=channel_entity, 
limit=1, 
offset_date=None, 
offset_id=0, 
max_id=0, 
min_id=0, 
add_offset=0, 
hash=0))

169         348 LOAD_FAST                2 (posts)
            350 LOAD_ATTR               12 (messages)
            352 LOAD_CONST               9 (0)
            354 BINARY_SUBSCR
            356 LOAD_ATTR               13 (message)
            358 STORE_FAST               7 (message)
message = posts.messages[0].message

170         360 LOAD_FAST                2 (posts)
            362 LOAD_ATTR               12 (messages)
            364 LOAD_CONST               9 (0)
            366 BINARY_SUBSCR
            368 LOAD_ATTR               13 (message)
            370 LOAD_METHOD             14 (find)
            372 LOAD_CONST              23 ('You must stay')
            374 CALL_METHOD              1
            376 LOAD_CONST              12 (-1)
            378 COMPARE_OP               3 (!=)
            380 EXTENDED_ARG             1
            382 POP_JUMP_IF_TRUE       408
            384 LOAD_FAST                2 (posts)
            386 LOAD_ATTR               12 (messages)
            388 LOAD_CONST               9 (0)
            390 BINARY_SUBSCR
            392 LOAD_ATTR               13 (message)
            394 LOAD_METHOD             14 (find)
            396 LOAD_CONST              24 ('Please stay on')
            398 CALL_METHOD              1
            400 LOAD_CONST              12 (-1)
            402 COMPARE_OP               3 (!=)
            404 EXTENDED_ARG             3
            406 POP_JUMP_IF_FALSE      822
if posts.messages[0].message.find('You must stay') != -1 or posts.messages[0].message.find('Please stay on') != -1:

171     >>  408 LOAD_GLOBAL             24 (re)
            410 LOAD_METHOD             25 (findall)
            412 LOAD_CONST              25 ('([\\d.]*\\d+)')
            414 LOAD_FAST                7 (message)
            416 CALL_METHOD              2
            418 STORE_FAST               8 (sec)
sec = re.findall('([\\d.]*\\d+)', message)

172         420 LOAD_GLOBAL             26 (tunggu)
            422 LOAD_GLOBAL             27 (int)
            424 LOAD_FAST                8 (sec)
            426 LOAD_CONST               9 (0)
            428 BINARY_SUBSCR
            430 CALL_FUNCTION            1
            432 CALL_FUNCTION            1
            434 POP_TOP
tunggu(int(sec[0]))

173         436 LOAD_GLOBAL             10 (sleep)
            438 LOAD_CONST               8 (1)
            440 CALL_FUNCTION            1
            442 POP_TOP
sleep(1)

174         444 LOAD_GLOBAL              7 (client)
            446 LOAD_GLOBAL             11 (GetHistoryRequest)
            448 LOAD_GLOBAL              9 (channel_entity)
            450 LOAD_CONST               7 (2)
            452 LOAD_CONST               0 (None)
            454 LOAD_CONST               9 (0)
            456 LOAD_CONST               9 (0)
            458 LOAD_CONST               9 (0)
            460 LOAD_CONST               9 (0)
            462 LOAD_CONST               9 (0)
            464 LOAD_CONST              10 (('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash'))
            466 CALL_FUNCTION_KW         8
            468 CALL_FUNCTION            1
            470 STORE_FAST               2 (posts)
posts = client(GetHistoryRequest(
peer=channel_entity, 
limit=2, 
offset_date=None, 
offset_id=0, 
max_id=0, 
min_id=0, 
add_offset=0, 
hash=0))

175         472 LOAD_FAST                2 (posts)
            474 LOAD_ATTR               12 (messages)
            476 LOAD_CONST               8 (1)
            478 BINARY_SUBSCR
            480 LOAD_ATTR               13 (message)
            482 STORE_FAST               9 (messageres)
messageres = posts.messages[1].message

176         484 LOAD_GLOBAL             24 (re)
            486 LOAD_METHOD             25 (findall)
            488 LOAD_CONST              25 ('([\\d.]*\\d+)')
            490 LOAD_FAST                9 (messageres)
            492 CALL_METHOD              2
            494 LOAD_CONST               9 (0)
            496 BINARY_SUBSCR
            498 STORE_FAST              10 (reward)
reward = re.findall('([\\d.]*\\d+)', messageres)[0]

177         500 LOAD_GLOBAL             10 (sleep)
            502 LOAD_CONST               7 (2)
            504 CALL_FUNCTION            1
            506 POP_TOP
sleep(2)

178         508 LOAD_GLOBAL              3 (sys)
            510 LOAD_ATTR                4 (stdout)
            512 LOAD_METHOD              5 (write)
            514 LOAD_CONST              26 ('\r\x1b[1;35mSTATUS VISIT    : \x1b[1;36mYou earned ')
            516 LOAD_FAST               10 (reward)
            518 FORMAT_VALUE             0
            520 LOAD_CONST              27 (' ')
            522 LOAD_GLOBAL             28 (cr)
            524 FORMAT_VALUE             0
            526 LOAD_CONST              28 ('\n')
            528 BUILD_STRING             5
            530 CALL_METHOD              1
            532 POP_TOP
            534 JUMP_FORWARD             0 (to 536)
sys.stdout.write(f"\r\x1b[1;35mSTATUS VISIT    : \x1b[1;36mYou earned {reward} {cr}\n")

180     >>  536 EXTENDED_ARG             1
            538 JUMP_FORWARD           282 (to 822)

181     >>  540 LOAD_FAST                6 (soup)
            542 LOAD_ATTR               14 (find)
            544 LOAD_CONST              18 ('div')
            546 LOAD_CONST              21 ('headbar')
            548 LOAD_CONST              22 (('id',))
            550 CALL_FUNCTION_KW         2
            552 LOAD_CONST               0 (None)
            554 COMPARE_OP               9 (is not)
            556 EXTENDED_ARG             2
            558 POP_JUMP_IF_FALSE      696
elif soup.find('div',id='headbar') is not None:

182         560 LOAD_FAST                6 (soup)
            562 LOAD_ATTR               29 (find_all)
            564 LOAD_CONST              18 ('div')
            566 LOAD_CONST              29 ('container-fluid')
            568 LOAD_CONST              20 (('class_',))
            570 CALL_FUNCTION_KW         2
            572 GET_ITER
        >>  574 FOR_ITER               118 (to 694)
            576 STORE_FAST              11 (dat)
for dat in soup.find_all('div',class_='container-fluid'):

183         578 LOAD_FAST               11 (dat)
            580 LOAD_METHOD             20 (get)
            582 LOAD_CONST              30 ('data-code')
            584 CALL_METHOD              1
            586 STORE_FAST              12 (code)
code = dat.get('data-code')

184         588 LOAD_FAST               11 (dat)
            590 LOAD_METHOD             20 (get)
            592 LOAD_CONST              31 ('data-timer')
            594 CALL_METHOD              1
            596 STORE_FAST              13 (timer)
timer = dat.get('data-timer')

185         598 LOAD_FAST               11 (dat)
            600 LOAD_METHOD             20 (get)
            602 LOAD_CONST              32 ('data-token')
            604 CALL_METHOD              1
            606 STORE_FAST              14 (tokena)
tokena = dat.get('data-token')

186         608 LOAD_GLOBAL             26 (tunggu)
            610 LOAD_GLOBAL             27 (int)
            612 LOAD_FAST               13 (timer)
            614 CALL_FUNCTION            1
            616 CALL_FUNCTION            1
            618 POP_TOP
tunggu(int(timer))

187         620 LOAD_FAST                0 (c)
            622 LOAD_ATTR               30 (post)
            624 LOAD_CONST              33 ('https://dogeclick.com/reward')
            626 LOAD_FAST               12 (code)
            628 LOAD_FAST               14 (tokena)
            630 LOAD_CONST              34 (('code', 'token'))
            632 BUILD_CONST_KEY_MAP      2
            634 LOAD_GLOBAL             21 (ua)
            636 LOAD_CONST              14 (15)
            638 LOAD_CONST              15 (True)
            640 LOAD_CONST              35 (('data', 'headers', 'timeout', 'allow_redirects'))
            642 CALL_FUNCTION_KW         5
            644 STORE_FAST               5 (r)
r = c.post('https://dogeclick.com/reward', data={'code':code,  'token':tokena}, headers=ua, timeout=15, allow_redirects=True)

188         646 LOAD_GLOBAL             31 (json)
            648 LOAD_METHOD             32 (loads)
            650 LOAD_FAST                5 (r)
            652 LOAD_ATTR               33 (text)
            654 CALL_METHOD              1
            656 STORE_FAST              15 (js)
js = json.loads(r.text)

189         658 LOAD_GLOBAL              3 (sys)
            660 LOAD_ATTR                4 (stdout)
            662 LOAD_METHOD              5 (write)
            664 LOAD_CONST              26 ('\r\x1b[1;35mSTATUS VISIT    : \x1b[1;36mYou earned ')
            666 LOAD_FAST               15 (js)
            668 LOAD_CONST              36 ('reward')
            670 BINARY_SUBSCR
            672 BINARY_ADD
            674 LOAD_CONST              27 (' ')
            676 LOAD_GLOBAL             28 (cr)
            678 FORMAT_VALUE             0
            680 LOAD_CONST              28 ('\n')
            682 BUILD_STRING             3
            684 BINARY_ADD
            686 CALL_METHOD              1
            688 POP_TOP
            690 EXTENDED_ARG             2
            692 JUMP_ABSOLUTE          574
        >>  694 JUMP_FORWARD           126 (to 822)
sys.stdout.write('\r\x1b[1;35mSTATUS VISIT    : \x1b[1;36mYou earned ' + js['reward'] + f" {cr}\n")

191     >>  696 LOAD_GLOBAL              3 (sys)
            698 LOAD_ATTR                4 (stdout)
            700 LOAD_METHOD              5 (write)
            702 LOAD_CONST               2 ('\r')
            704 CALL_METHOD              1
            706 POP_TOP
sys.stdout.write('\r')

192         708 LOAD_GLOBAL              3 (sys)
            710 LOAD_ATTR                4 (stdout)
            712 LOAD_METHOD              5 (write)
            714 LOAD_CONST              37 ('                                                                ')
            716 CALL_METHOD              1
            718 POP_TOP
sys.stdout.write('                                                                ')

193         720 LOAD_GLOBAL              3 (sys)
            722 LOAD_ATTR                4 (stdout)
            724 LOAD_METHOD              5 (write)
            726 LOAD_CONST               2 ('\r')
            728 CALL_METHOD              1
            730 POP_TOP
sys.stdout.write('\r')

194         732 LOAD_GLOBAL              3 (sys)
            734 LOAD_ATTR                4 (stdout)
            736 LOAD_METHOD              5 (write)
            738 LOAD_CONST              38 ('\x1b[1;35mSTATUS VISIT    : \x1b[1;36mCaptcha Detected')
            740 CALL_METHOD              1
            742 POP_TOP
sys.stdout.write('\x1b[1;35mSTATUS VISIT    : \x1b[1;36mCaptcha Detected')

195         744 LOAD_GLOBAL              3 (sys)
            746 LOAD_ATTR                4 (stdout)
            748 LOAD_METHOD              6 (flush)
            750 CALL_METHOD              0
            752 POP_TOP
sys.stdout.flush()

196         754 LOAD_GLOBAL             10 (sleep)
            756 LOAD_CONST               7 (2)
            758 CALL_FUNCTION            1
            760 POP_TOP
sleep(2)

197         762 LOAD_GLOBAL              7 (client)
            764 LOAD_GLOBAL             34 (GetBotCallbackAnswerRequest)

198         766 LOAD_GLOBAL             35 (channel_username)

199         768 LOAD_FAST                4 (id)
client(GetBotCallbackAnswerRequest(channel_username,id

200         770 LOAD_FAST                2 (posts)
            772 LOAD_ATTR               12 (messages)
            774 LOAD_CONST               9 (0)
            776 BINARY_SUBSCR
            778 LOAD_ATTR               15 (reply_markup)
            780 LOAD_ATTR               16 (rows)
            782 LOAD_CONST               8 (1)
            784 BINARY_SUBSCR
            786 LOAD_ATTR               17 (buttons)
            788 LOAD_CONST               8 (1)
            790 BINARY_SUBSCR
            792 LOAD_ATTR               36 (data)

197         794 LOAD_CONST              39 (('data',))
            796 CALL_FUNCTION_KW         3
            798 CALL_FUNCTION            1
            800 POP_TOP
data=(posts.messages[0].reply_markup.rows[1].buttons[1].data)))

202         802 LOAD_GLOBAL              3 (sys)
            804 LOAD_ATTR                4 (stdout)
            806 LOAD_METHOD              5 (write)
            808 LOAD_CONST              40 ('\r\x1b[1;35mSTATUS VISIT    : \x1b[1;36mSkip captcha ... !\n')
            810 CALL_METHOD              1
            812 POP_TOP
sys.stdout.write('\r\x1b[1;35mSTATUS VISIT    : \x1b[1;36mSkip captcha ... !\n')

203         814 LOAD_GLOBAL             10 (sleep)
            816 LOAD_CONST               7 (2)
            818 CALL_FUNCTION            1
            820 POP_TOP
        >>  822 POP_BLOCK
            824 JUMP_ABSOLUTE           16
sleep(2)

204     >>  826 POP_TOP
            828 POP_TOP
            830 POP_TOP
except:

205         832 LOAD_GLOBAL             10 (sleep)
            834 LOAD_CONST              41 (3)
            836 CALL_FUNCTION            1
            838 POP_TOP
sleep(3)

206         840 LOAD_GLOBAL              7 (client)
            842 LOAD_GLOBAL             11 (GetHistoryRequest)
            844 LOAD_GLOBAL              9 (channel_entity)
            846 LOAD_CONST               8 (1)
            848 LOAD_CONST               0 (None)
            850 LOAD_CONST               9 (0)
            852 LOAD_CONST               9 (0)
            854 LOAD_CONST               9 (0)
            856 LOAD_CONST               9 (0)
            858 LOAD_CONST               9 (0)
            860 LOAD_CONST              10 (('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash'))
            862 CALL_FUNCTION_KW         8
            864 CALL_FUNCTION            1
            866 STORE_FAST               2 (posts)
posts = client(GetHistoryRequest(
peer=channel_entity, 
limit=1, 
offset_date=None, 
offset_id=0, 
max_id=0, 
min_id=0, 
add_offset=0, 
hash=0))

207         868 LOAD_FAST                2 (posts)
            870 LOAD_ATTR               12 (messages)
            872 LOAD_CONST               9 (0)
            874 BINARY_SUBSCR
            876 LOAD_ATTR               13 (message)
            878 STORE_FAST               7 (message)
message = posts.messages[0].message

208         880 LOAD_FAST                2 (posts)
            882 LOAD_ATTR               12 (messages)
            884 LOAD_CONST               9 (0)
            886 BINARY_SUBSCR
            888 LOAD_ATTR               13 (message)
            890 LOAD_METHOD             14 (find)
            892 LOAD_CONST              23 ('You must stay')
            894 CALL_METHOD              1
            896 LOAD_CONST              12 (-1)
            898 COMPARE_OP               3 (!=)
            900 EXTENDED_ARG             3
            902 POP_JUMP_IF_TRUE       928
            904 LOAD_FAST                2 (posts)
            906 LOAD_ATTR               12 (messages)
            908 LOAD_CONST               9 (0)
            910 BINARY_SUBSCR
            912 LOAD_ATTR               13 (message)
            914 LOAD_METHOD             14 (find)
            916 LOAD_CONST              24 ('Please stay on')
            918 CALL_METHOD              1
            920 LOAD_CONST              12 (-1)
            922 COMPARE_OP               3 (!=)
            924 EXTENDED_ARG             4
            926 POP_JUMP_IF_FALSE     1056
if posts.messages[0].message.find('You must stay') != -1 or posts.messages[0].message.find('Please stay on') != -1:

209     >>  928 LOAD_GLOBAL             24 (re)
            930 LOAD_METHOD             25 (findall)
            932 LOAD_CONST              25 ('([\\d.]*\\d+)')
            934 LOAD_FAST                7 (message)
            936 CALL_METHOD              2
            938 STORE_FAST               8 (sec)
sec = re.findall('([\\d.]*\\d+)', message)

210         940 LOAD_GLOBAL             26 (tunggu)
            942 LOAD_GLOBAL             27 (int)
            944 LOAD_FAST                8 (sec)
            946 LOAD_CONST               9 (0)
            948 BINARY_SUBSCR
            950 CALL_FUNCTION            1
            952 CALL_FUNCTION            1
            954 POP_TOP
tunggu(int(sec[0]))

211         956 LOAD_GLOBAL             10 (sleep)
            958 LOAD_CONST               8 (1)
            960 CALL_FUNCTION            1
            962 POP_TOP
sleep(1)

212         964 LOAD_GLOBAL              7 (client)
            966 LOAD_GLOBAL             11 (GetHistoryRequest)
            968 LOAD_GLOBAL              9 (channel_entity)
            970 LOAD_CONST               7 (2)
            972 LOAD_CONST               0 (None)
            974 LOAD_CONST               9 (0)
            976 LOAD_CONST               9 (0)
            978 LOAD_CONST               9 (0)
            980 LOAD_CONST               9 (0)
            982 LOAD_CONST               9 (0)
            984 LOAD_CONST              10 (('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash'))
            986 CALL_FUNCTION_KW         8
            988 CALL_FUNCTION            1
            990 STORE_FAST               2 (posts)
posts = client(GetHistoryRequest(
peer=channel_entity, 
limit=2, 
offset_date=None, 
offset_id=0, 
max_id=0, 
min_id=0, 
add_offset=0, 
hash=0))

213         992 LOAD_FAST                2 (posts)
            994 LOAD_ATTR               12 (messages)
            996 LOAD_CONST               8 (1)
            998 BINARY_SUBSCR
           1000 LOAD_ATTR               13 (message)
           1002 STORE_FAST               9 (messageres)
messageres = posts.messages[1].message

214        1004 LOAD_GLOBAL             24 (re)
           1006 LOAD_METHOD             25 (findall)
           1008 LOAD_CONST              25 ('([\\d.]*\\d+)')
           1010 LOAD_FAST                9 (messageres)
           1012 CALL_METHOD              2
           1014 LOAD_CONST               9 (0)
           1016 BINARY_SUBSCR
           1018 STORE_FAST              10 (reward)
reward = re.findall('([\\d.]*\\d+)', messageres)[0]

215        1020 LOAD_GLOBAL             10 (sleep)
           1022 LOAD_CONST               7 (2)
           1024 CALL_FUNCTION            1
           1026 POP_TOP
sleep(2)

216        1028 LOAD_GLOBAL              3 (sys)
           1030 LOAD_ATTR                4 (stdout)
           1032 LOAD_METHOD              5 (write)
           1034 LOAD_CONST              26 ('\r\x1b[1;35mSTATUS VISIT    : \x1b[1;36mYou earned ')
           1036 LOAD_FAST               10 (reward)
           1038 FORMAT_VALUE             0
           1040 LOAD_CONST              27 (' ')
           1042 LOAD_GLOBAL             28 (cr)
           1044 FORMAT_VALUE             0
           1046 LOAD_CONST              28 ('\n')
           1048 BUILD_STRING             5
           1050 CALL_METHOD              1
           1052 POP_TOP
           1054 JUMP_FORWARD             0 (to 1056)
sys.stdout.write(f"\r\x1b[1;35mSTATUS VISIT    : \x1b[1;36mYou earned {reward} {cr}\n")

218     >> 1056 POP_EXCEPT
           1058 JUMP_ABSOLUTE           16
           1060 END_FINALLY # <- pass
           1062 JUMP_ABSOLUTE           16
        >> 1064 LOAD_CONST               0 (None)
           1066 RETURN_VALUE
else:
	pass
