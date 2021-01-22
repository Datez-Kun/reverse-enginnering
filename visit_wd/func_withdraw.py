# FileName : <zen_ezz>
# Python Bytecode : 3.8
# Time Succses Decompiled : Mon Aug 24 02:51:10 2020
# Timestamp In Code: 2020-06-25 21:39:46

sys.stdout.write('\r')
sys.stdout.write('                                                              ')
sys.stdout.write('\r')
sys.stdout.write('\x1b[1;35mSTATUS WD       : \x1b[1;36mGathering info ... !')
sys.stdout.flush()
client.send_message(entity=channel_entity, message='/Balance')
sleep(1)
posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
message = posts.messages[0].message
bal = re.findall('([\\d.]*\\d+)', message)[0]
client.send_message(entity=channel_entity, message='/Withdraw')
sleep(1)
posts_ = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
if posts_.messages[0].message.find('Your balance is too small to') != -1:
    sys.stdout.write(f"\r\x1b[1;35mSTATUS WD       : \x1b[1;36mAvailable balance {bal} {cr}\n\n")
    sleep(1)
else:
    client.send_message(entity=channel_entity, message=wallet)
    sleep(1)
    client.send_message(entity=channel_entity, message=bal)
    sleep(1)
    client.send_message(entity=channel_entity, message='/Confirm')
    sys.stdout.write(f"\r\x1b[1;35mSTATUS WD       : \x1b[1;36mSuccess withdraw {bal} {cr}\n\n")
    sleep(1)


