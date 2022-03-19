from imports import *

import commands.C_all as C_all
import commands.C_admin as C_admin

intents = discord.Intents.all()
client = discord.ext.commands.Bot(',', intents=intents)

대충랭던관리자리스트 = [647001590766632966, 646998005643476993, 705339607029645323]

def errormsg():
    return '```\n' + traceback.format_exc() + '\n```'

async def log(*s, channel_id=762916201654386701):
    s = '\n'.join(map(str, s))
    
    print(s)
    if len(s) > 2000:
        await client.get_channel(channel_id).send(s[:2000])
        await log(s[2000:])
    else:
        await client.get_channel(channel_id).send(s)
    
@client.event
async def on_error(event, *args, **kwargs):
    await log('=====', '<@526889025894875158>', 'error!', errormsg(), event, args, kwargs, '=====')
    if str(event) == 'on_message':
        await args[0].add_reaction(엑스)

@client.event
async def on_ready():
    print('시작')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=",도움", type=discord.ActivityType.listening))
    await log(시간(), "<@526889025894875158>", "시작")
    DiscordComponents(client)
    # [무지개] 색
    def RGB2hex(rgb):
        r, g, b = rgb['R'], rgb['G'], rgb['B']

        r = hex(r)[2:]
        g = hex(g)[2:]
        b = hex(b)[2:]

        r = r if len(r)!=1 else '0'+r
        g = g if len(g)!=1 else '0'+g
        b = b if len(b)!=1 else '0'+b

        f = int(f'{r}{g}{b}', 16)
        # await log(hex(f))
        return f

    RGB = {
        'R': 255,
        'G': 0,
        'B': 0
    }
    rgb_spin = {
        'R': 'B',
        'G': 'R',
        'B': 'G'
    }

    nowChange = ['G', +85]

    N_role = client.get_guild(766932314973929522).get_role(855022848224919572)
    N_msg = await client.get_channel(762916201654386701).fetch_message(856802676468875264)

    while not client.is_closed():
        await asyncio.sleep(60)
        try:
            before_color = str(N_role.color)
            await N_role.edit(color=RGB2hex(RGB))
            after_color = str(N_role.color)

            if before_color == after_color:
                pass # await log(f'-----<@526889025894875158> 실패!\n{시간()}\n{before_color} → {after_color}\n-----')
            else:
                await N_msg.edit(content = f'-----성공!\n{시간()}\n{before_color} → {after_color}\n-----')

            RGB[nowChange[0]] += nowChange[1]
            if RGB[nowChange[0]] == (255 if nowChange[1]>0 else 0):
                nowChange[0] = rgb_spin[nowChange[0]]
                nowChange[1] = -nowChange[1]

        except:
            pass
        
@client.event
async def on_button_click(res):
    await res.respond(
        type=InteractionType.ChannelMessageWithSource, content=f"`{res.component.label}`가 눌렸습니다."
    )

@client.event
async def on_message(message):
    if message.guild is None and not message.author.bot: return await message.channel.send('이 봇은 dm에서 사용할수 없습니다.. ***어떤 사람***이 자꾸 dm에서 봇 사용하는데 ***하지 마세요.***')
    if message.guild is None and     message.author.bot: return
    
    m = message.content
    def 시작(s, target=m):
        return k2e(target).startswith(k2e(s))

    if message.guild.id == 826264040740618301:
        note2 = await client.get_channel(833557179821981707).fetch_message(833579939701325854)

        if message.content == ",등록" and not (message.author.id in (647001590766632966, 646998005643476993, 826322347862261760, 725528129648721920)):
            if "<@"+str(message.author.id)+">" in note2.content:
                await message.channel.send("이미 등록되었습니다")
                return
            else:
                await note2.edit(content=f"{note2.content}\n<@{message.author.id}> : 0")
                await message.channel.send("완료")

        if message.content == ",탈퇴" and message.author.id != 647001590766632966:
            if not "<@"+str(message.author.id)+">" in note2.content:
                await message.channel.send("이미 탈퇴되었습니다")
                return
            else:
                noteC = note2.content.split('\n')
                f_noteC = ""
                for i in noteC:
                    if not i.startswith(f"<@{message.author.id}> : "):
                        f_noteC += '\n' + i

                await note2.edit(content=f_noteC)
                await message.channel.send("완료")

        if message.author.id in (647001590766632966, 646998005643476993, 826322347862261760, 725528129648721920):
            if 시작(",+") or 시작(",-"):
                m = message.content
                usermoney = int(m.split()[0][1:])

                userid1 = m.split()[1]
                userid2 = ""
                for i in userid1:
                    if i in "1234567890":
                        userid2 += i
                user = f"<@{userid2}>"

                if not (user in note2.content):
                    await message.channel.send("등록되어있지 않은 유저입니다.")
                    return
                else:
                    notec = note2.content
                    notec = notec.split("\n")[1:]
                    for i in range(len(notec)):
                        if notec[i].startswith(user):
                            noten = i
                    notec[noten] = notec[noten][:24] + str(int(notec[noten][24:])+usermoney)
                    notem = "이름 : 돈\n" + "\n".join(notec)
                    await note2.edit(content = notem)
                    await message.channel.send("완료")
            if 시작(",등록"):
                mm = message.content[4:]
                m = ""
                for i in mm:
                    if i in "1234567890":
                        m += i
                if len(m) != 18:
                    await message.channel.send("잘못된 유저입니다.")
                    return
                if m in note2.content:
                    await message.channel.send("이미 등록되었습니다.")
                    return
                else:
                    await note2.edit(content=f"{note2.content}\n<@{m}> : 0")
                    await message.channel.send("완료")
            if 시작(",탈퇴"):
                mm = message.content[4:]
                m = ""
                for i in mm:
                    if i in "1234567890":
                        m += i
                if len(m) != 18:
                    await message.channel.send("잘못된 유저입니다.")
                    return
                elif not f"<@{m}>" in note2.content:
                    await message.channel.send("이미 탈퇴되었습니다")
                    return
                else:
                    noteC = note2.content.split('\n')
                    f_noteC = ""
                    for i in noteC:
                        if not i.startswith(f"<@{m}> : "):
                            f_noteC += '\n' + i

                    await note2.edit(content=f_noteC)
                    await message.channel.send("완료")


    if message.guild.id == 826264040740618301:
        return

    if message.guild.id == 857545260816138251:
        global 대충랭던관리자리스트
        if message.author.id in 대충랭던관리자리스트:
            if 시작(",권한"):
                user_ = message.content.split()[1]
                user = ""
                for i in user_:
                    if i in "1234567890":
                        user += i
                user = int(user)
                if user in 대충랭던관리자리스트:
                    대충랭던관리자리스트.remove(user) ; await message.channel.send(f"{user} 님은 이제 권한이 없습니다. \n현재 관리자 목록은 {대충랭던관리자리스트}입니다.")
                else:
                    대충랭던관리자리스트.append(user) ; await message.channel.send(f"{user} 님은 이제 권한이 있습니다. \n현재 관리자 목록은 {대충랭던관리자리스트}입니다.")

            elif 시작(",+") or 시작(",-"):
                money = int(message.content.split()[0][1:])

                user = message.content.split()[1]
                userid = ''
                for i in user:
                    if i in '1234567890':
                        userid += i

                user = await message.guild.fetch_member(int(userid))

                level_100 =[863639528505737217, 863639534465581076, 863639536520790078, 863639538537332787, 863639541004501002, 863639543370481664, 863639545807634442, 863639548180299798, 863639550396071986, 863639552136839169]
                level_10 = [857554305065156608, 857554349126844417, 857554366842929164, 857554378516594730, 857554399891030097, 857554413656342538, 857554426847297556, 857554437030412308, 857554446342160384, 857554456745082890]
                level_01 = [857554543206596608, 857554613062205490, 857554647773085696, 857554657751859240, 857554667861311488, 857554676484145152, 857554685689987102, 857554702329839616, 857554715008565260, 857554731320868884]
                exp_100 =  [857555085957922816, 857555101199237121, 857555119193456640, 857555133474406402, 857555150525038643, 857555300885200906, 857555315046350858, 857555325162225665, 857555337242869760, 857555346242928660]
                exp_010 =  [857555356509929513, 857555372083642439, 857555382003302410, 857555390966530048, 857555402122854400, 857555421791125504, 857555431945273354, 857555444846690324, 857555456221380638, 857555466930094100]
                exp_001 =  [857555477574189067, 857555489830862848, 857555519845564416, 857555520822575104, 857555572868775946, 857555585699938324, 857555593437904926, 857555606268280833, 857555616376684554, 857555622954663947]

                temp_list = []
                user_money = [None] * 6
                for i in user.roles:
                    if i.id in level_100:
                        user_money[0] = i.name ; temp_list.append(i)
                    elif i.id in level_10:
                        user_money[1] = i.name ; temp_list.append(i)
                    elif i.id in level_01:
                        user_money[2] = i.name ; temp_list.append(i)
                    elif i.id in exp_100:
                        user_money[3] = i.name ; temp_list.append(i)
                    elif i.id in exp_010:
                        user_money[4] = i.name ; temp_list.append(i)
                    elif i.id in exp_001:
                        user_money[5] = i.name ; temp_list.append(i)

                if None in user_money:
                    await message.channel.send(f'{user}의 역할을 찾을 수 없습니다. 잠시 뒤에 시도해주세요.')
                    return
                await user.remove_roles(*temp_list)
                # await log(시간(), '삭제한거', [(i.id, i.name) for i in temp_list[::-1]], '?!?!?1?1\n', '삭제하고남은거', [(i.id, i.name) for i in user.roles[1:][::-1]])
                await client.get_channel(861552854933045308).send('\n'.join(list(map(str, [시간(), '삭제한거', [(i.id, i.name) for i in temp_list[::-1]], '?!?!?1?1\n', '삭제하고남은거', [(i.id, i.name) for i in user.roles[1:][::-1]]]))))

                usermoney = int(''.join(user_money))
                usermoney += money
                usermoney = str(usermoney).zfill(6)

                if int(usermoney) >= 1000000:
                    await message.channel.send(f"{user}이 1000레벨이 되었습니다.") ; return
                #await log("*"+str(usermoney)+"*")
                logStr = f"{시간()} ; {user} ; lv.`{(int(usermoney)-money)//1000}` exp.`{(int(usermoney)-money)%1000}` 에서 `{money}`exp를 얻어 lv.`{int(usermoney[:3])}` exp.`{int(usermoney[3:])}`이 되었습니다."
                await user.add_roles(message.guild.get_role(level_100[ int( usermoney[0] ) ] ),
                                        message.guild.get_role( level_10[ int( usermoney[1] ) ] ),
                                        message.guild.get_role( level_01[ int( usermoney[2] ) ] ),
                                        message.guild.get_role(  exp_100[ int( usermoney[3] ) ] ),
                                        message.guild.get_role(  exp_010[ int( usermoney[4] ) ] ),
                                        message.guild.get_role(  exp_001[ int( usermoney[5] ) ] ),
                                        reason=logStr)
                await client.get_channel(861552854933045308).send(logStr)

                await message.add_reaction(체크)
            if 시작(",공격력") or 시작(",방어력") or 시작(",공배") or 시작(",방배") or 시작(",곡괭이"):
                note = await client.get_channel(861494824259944499).fetch_message(861495876379213864)

                isAttack = 1 if 시작(",공격력") else 2 if 시작(",방어력") else 3 if 시작(",공배") else 4 if 시작(",방배") else 5 # 공격력: 1, 방어력: 2, 공배: 3, 방배: 4, 곡괭이: 5

                money = message.content.split()[2]

                note_contents = note.content.split('\n')[1:]
                note_content = '\n'.join(note_contents)

                user_ = message.content.split()[1]
                user = ''
                for i in user_:
                    if i in '1234567890':
                        user += i
                user = f"<@{user}>"

                if not (user in note_content):
                    await note.edit(content = f"{note.content}\n{user} : 0 : 0 : 1 : 1 : 없음")
                    note = await client.get_channel(861494824259944499).fetch_message(861495876379213864)
                    note_contents = note.content.split('\n')[1:]
                    note_content = '\n'.join(note_contents)

                for i in range(len(note_contents)):
                    if note_contents[i].startswith(user):
                        P = note_contents[i].split(' : ')
                        P[isAttack] = money
                        P = ' : '.join(P)
                        note_contents[i] = P
                        break
                await note.edit(content = '유저 : 공격력 : 방어력 : 공배 : 방배 : 곡괭이\n' + '\n'.join(note_contents))
                if isAttack == 1:
                    await message.channel.send(f"공격력이 {money}로 설정되었습니다.")
                elif isAttack == 2:
                    await message.channel.send(f"방어력이 {money}로 설정되었습니다.")
                elif isAttack == 3:
                    await message.channel.send(f"공배가 {money}로 설정되었습니다.")
                elif isAttack == 4:
                    await message.channel.send(f"방배가 {money}로 설정되었습니다.")
                else:
                    await message.channel.send(f"곡괭이가 {money}로 설정되었습니다.")
                await note.add_reaction(체크)

        else:
            note = await client.get_channel(861494824259944499).fetch_message(861495876379213864)
            user = f"<@{message.author.id}>"

            rank_dg_mons_dict = {
                857962402438709248: { # channel id # 시작의 초원
                    '스타터 슬라임': [ # message content
                        (1, 1), # need exp
                        5, # exp
                        [
                            (10, '슬라임 발사기')
                        ]
                    ],
                    '스타터 고블린': [
                        (3, 5), 
                        10,
                        [
                            (10, '고블린 검')
                        ]
                    ],
                    '스타터 스켈레톤': [
                        (5, 10),
                        20,
                        [
                            (10, '단단한 뼈')
                        ]
                    ]
                },
                858205689796624395: { # 작은언덕
                    '플라워 슬라임': [
                        (5, 5),
                        15,
                        [
                            (10, '꽃 발사기')
                        ]
                    ],
                    '소일 고블린': [
                        (10, 10), 
                        40,
                        [
                            (5, '소일 소드'),
                            (5, '고블린 가죽 신발')
                        ]
                    ],
                    '그래스 스켈레톤': [
                        (10, 15),
                        25,
                        [
                            (5, '그래스 본')
                        ]
                    ]
                },
                858207335314620426: {#좁은강
                    '워터 슬라임': [
                        (10, 10),
                        20,
                        [
                            (10, '슬라임 물총')
                        ]
                    ],
                    '괴물 물고기': [
                        (15, 20), 
                        50,
                        [
                            (10, '괴어의 이빨')
                        ]
                    ],
                    '늑대거북': [
                        (20, 20),
                        75,
                        [
                            (5, '늑대거북 등껍질 투구'),
                            (2.5, '늑대거북 등껍질 흉갑')
                        ]
                    ]
                },
                858234982890602506: {#아담한숲
                    '리프 슬라임': [
                        (15, 15),
                        30,
                        [
                            (10, '나뭇잎 검')
                        ]
                    ],
                    '트리 고블린': [
                        (25, 20), 
                        100,
                        [
                            (10, '나무 검')
                        ]
                    ],
                    '우드 스켈레톤': [
                        (20, 25),
                        125,
                        [
                            (10, '뾰족한 뼈')
                        ]
                    ]
                },
                858237928629993492: {#높은산
                    '투구 슬라임': [
                        (30, 20),
                        125,
                        [
                            (10, '슬라임 투구')
                        ]
                    ],
                    '아머 고블린': [
                        (40, 25), 
                        150,
                        [
                            (10, '고블린 흉갑')
                        ]
                    ],
                    '재생 해골': [
                        (40, 30),
                        200,
                        [
                            (10, '투척용 뼈')
                        ]
                    ]
                },
                860811683245457418: {#울창한정글
                    '덩굴 골렘': [
                        (75, 50),
                        300,
                        [
                            (50, '덩굴 바위 주먹'),
                            (75, '덩굴 바위 흉갑'),
                        ]
                    ],
                    '정글 슬라임': [
                        (30, 25), 
                        150,
                        []
                    ],
                    '정글 고블린': [
                        (45, 30),
                        225,
                        []
                    ],
                    '정글 스켈레톤': [
                        (45, 35),
                        250,
                        []
                    ]
                },
                860811739753611264: { # 끈죽한늪
                    '거대 늪 슬라임': [
                        (160, 120), 
                        800,
                        [
                            (1, '거대 끈적한 슬라임 발사기')
                        ]
                    ],
                    '늪 슬라임': [
                        (40, 30), 
                        200,
                        [
                            (1, '끈적한 슬라임 발사기')
                        ]
                    ]
                },
                864356805177901056: { # 슬라임마을
                    '이장 슬라임': [
                        (500, 250), 
                        1000,
                        [
                            (35, '슬라임 괭이'),
                            (15, '슬라임 낫'),
                            (50, '슬라임 곡괭이'),
                        ]
                    ],
                    '주민 슬라임': [
                        (100, 50), 
                        500,
                        []
                    ],
                    '농부 슬라임': [
                        (200, 50), 
                        500,
                        [
                            (90, '슬라임 괭이'),
                            (10, '슬라임 낫')
                        ]
                    ],
                    '광부 슬라임': [
                        (300, 100), 
                        500,
                        [
                            (95, '슬라임 곡괭이')
                        ]
                    ]
                },
                864353107361660969: { # 고블린마을
                    '이장 고블린': [
                        (1000, 500), 
                        1500,
                        [
                            (40, '고블린 도끼'),
                            (10, '고블린 톱'),
                            (50, '고블린 곡괭이'),
                        ]
                    ],
                    '주민 고블린': [
                        (250, 150), 
                        1000,
                        []
                    ],
                    '나무꾼 고블린': [
                        (300, 250), 
                        1000,
                        [
                            (95, '고블린 도끼'),
                            (5, '고블린 톱')
                        ]
                    ],
                    '광부 고블린': [
                        (500, 150), 
                        500,
                        [
                            (90, '고블린 곡괭이')
                        ]
                    ]
                },
                864354901655289886: { # 스켈마을
                    '이장 스켈레톤': [
                        (1000, 1000), 
                        2000,
                        [
                            (1, '도축용 뼈'),
                            (50, '뼈 곡괭이'),
                        ]
                    ],
                    '주민 스켈레톤': [
                        (300, 300), 
                        1000,
                        [
                            (95, '투척용 뼈')
                        ]
                    ],
                    '도축업자 스켈레톤': [
                        (500, 1000), 
                        1000,
                        [
                            (3, '도축용 뼈')
                        ]
                    ],
                    '광부 스켈레톤': [
                        (500, 500), 
                        500,
                        [
                            (90, '뼈 곡괭이')
                        ]
                    ]
                },
                873731636980748318: { # 옼으마을
                    '이장 오크': [
                        (1500, 1000), 
                        2750,
                        [
                            (1, '오크의 심장'),
                            (50, '오크 곡괭이'),
                        ]
                    ],
                    '주민 오크': [
                        (750, 500), 
                        1000,
                        [
                            (20, '오크의 팔')
                        ]
                    ],
                    '재봉사 오크': [
                        (1000, 1500), 
                        1000,
                        [
                            (10, '오크의 혼이 깃든 바늘')
                        ]
                    ],
                    '광부 오크': [
                        (1000, 1000), 
                        1000,
                        [
                            (50, '오크 곡괭이')
                        ]
                    ],
                },
                873731663434223656: { # 마녀마을
                    '이장 마녀': [
                        (2000, 3000), 
                        5000,
                        [
                            (10, '중급 마녀의 지팡이'),
                            (1, '고급 마녀의 지팡이'),
                        ]
                    ],
                    '주민 마녀': [
                        (750, 1500), 
                        2000,
                        [
                            (10, '초급 마녀의 지팡이'),
                            (1, '중급 마녀의 지팡이'),
                        ]
                    ],
                    '고위 마녀': [
                        (1000, 2000), 
                        3000,
                        [
                            (5, '중급 마녀의 지팡이'),
                            (0.5, '고급 마녀의 지팡이'),
                        ]
                    ],
                    '광부 마녀': [
                        (1000, 1500), 
                        2000,
                        [
                            (10, '마법 곡괭이'),
                            (5, '특수 마법 곡괭이'),
                        ]
                    ],
                },
                874558759396061184: { # 좀비마을
                    '이장 좀비': [
                        (4500, 3000), 
                        5000,
                        [
                            (5, '좀비 투구'),
                        ]
                    ],
                    '주민 좀비': [
                        (1500, 1500), 
                        2500,
                        [
                            (5, '간이 좀비 투구'),
                        ]
                    ],
                    '의사 좀비': [
                        (4500,1500), 
                        4000,
                        [
                            (1, '좀비 투구'),
                            (10, '간이 좀비 투구'),
                            (1, '좀비 메스(수술용 칼)'),
                        ]
                    ],
                    '간호사 좀비': [
                        (3000, 1000), 
                        3000,
                        [
                            (10, '간이 좀비 투구'),
                            (1, '메첸바움(수술용 가위)'),
                        ]
                    ],
                },
                873731897925201920: { # 골렘마을
                    '주민 골렘': [
                        (3000, 1500), 
                        3500,
                        [
                            (15, '골렘의 주먹'),
                        ]
                    ],
                    '어설트 골렘': [
                        (4500, 3000), 
                        5000,
                        [
                            (25, '골렘의 주먹'),
                            (20, '골렘 흉갑'),
                        ]
                    ],
                    '스로어 골렘': [
                        (3000, 3000), 
                        4000,
                        [
                            (20, '투척용 바위'),
                        ]
                    ],
                    '디펜더 골렘': [
                        (6000, 1500), 
                        5000,
                        [
                            (30, '골렘 흉갑'),
                        ]
                    ],
                },
            }
            for channelid in rank_dg_mons_dict:
                if message.channel.id == channelid:
                    for monster_name in rank_dg_mons_dict[channelid]:
                        short = {'스타터 슬라임': '스슬', '스타터 고블린': '스고', '스타터 스켈레톤': '스스', '플라워 슬라임': '플슬', '소일 고블린': '소고', '그래스 스켈레톤': '그스', '워터 슬라임': '워슬', '괴물 물고기': '괴어', '늑대거북': '늑거', '리프 슬라임': '리슬', '트리 고블린': '트고', '우드 스켈레톤': '우스', '투구 슬라임': '투슬', '아머 고블린': '아고', '재생 해골': '재해', '덩굴 골렘': '덩골', '정글 슬라임': '정슬', '정글 고블린': '정고', '정글 스켈레톤': '정스', '거대 늪 슬라임': '거늪슬', '늪 슬라임': '늪슬', '이장 슬라임':'이슬', '주민 슬라임':'주슬', '농부 슬라임': '농슬', '광부 슬라임': '광슬', '이장 고블린': '이고', '주민 고블린': '주고', '나무꾼 고블린': '나고', '광부 고블린': '광고', '이장 스켈레톤': '이스', '주민 스켈레톤': '주스', '도축업자 스켈레톤': '도스', '광부 스켈레톤': '광스', '이장 오크': '이오', '주민 오크': '주오', '재봉사 오크': '재오', '광부 오크': '광오', '이장 마녀': '이마', '주민 마녀': '주마', '고위 마녀': '고마', '광부 마녀': '광마', '이장 좀비': '이좀', '주민 좀비': '주좀', '의사 좀비': '의좀', '간호사 좀비': '간좀', '주민 골렘': '주골', '어설트 골렘': '어골', '스로어 골렘': '스골', '디펜더 골렘': '디골'}                                   
                        if message.content.startswith(monster_name) or message.content.startswith(short[monster_name]):
                            List = rank_dg_mons_dict[channelid][monster_name]

                            for i in note.content.split('\n')[1:]:
                                if i.startswith(user):
                                    Attack, Defense, MultiAttack, MultiDefense = float(i.split(' : ')[1]), float(i.split(' : ')[2]), float(i.split(' : ')[3]), float(i.split(' : ')[4])
                                    break
                            else:
                                await message.channel.send(f"{message.author}의 공격력, 방어력, 공배, 방배를 찾을수 없습니다.") ; return


                            if List[0][0] <= Attack*MultiAttack and List[0][1] < Defense*MultiDefense:
                                money = List[1]
                                user = message.author

                                level_100 =[863639528505737217, 863639534465581076, 863639536520790078, 863639538537332787, 863639541004501002, 863639543370481664, 863639545807634442, 863639548180299798, 863639550396071986, 863639552136839169]
                                level_10 = [857554305065156608, 857554349126844417, 857554366842929164, 857554378516594730, 857554399891030097, 857554413656342538, 857554426847297556, 857554437030412308, 857554446342160384, 857554456745082890]
                                level_01 = [857554543206596608, 857554613062205490, 857554647773085696, 857554657751859240, 857554667861311488, 857554676484145152, 857554685689987102, 857554702329839616, 857554715008565260, 857554731320868884]
                                exp_100 =  [857555085957922816, 857555101199237121, 857555119193456640, 857555133474406402, 857555150525038643, 857555300885200906, 857555315046350858, 857555325162225665, 857555337242869760, 857555346242928660]
                                exp_010 =  [857555356509929513, 857555372083642439, 857555382003302410, 857555390966530048, 857555402122854400, 857555421791125504, 857555431945273354, 857555444846690324, 857555456221380638, 857555466930094100]
                                exp_001 =  [857555477574189067, 857555489830862848, 857555519845564416, 857555520822575104, 857555572868775946, 857555585699938324, 857555593437904926, 857555606268280833, 857555616376684554, 857555622954663947]

                                temp_list = []
                                user_money = [None] * 6
                                for i in user.roles:
                                    if i.id in level_100:
                                        user_money[0] = i.name ; temp_list.append(i)
                                    elif i.id in level_10:
                                        user_money[1] = i.name ; temp_list.append(i)
                                    elif i.id in level_01:
                                        user_money[2] = i.name ; temp_list.append(i)
                                    elif i.id in exp_100:
                                        user_money[3] = i.name ; temp_list.append(i)
                                    elif i.id in exp_010:
                                        user_money[4] = i.name ; temp_list.append(i)
                                    elif i.id in exp_001:
                                        user_money[5] = i.name ; temp_list.append(i)

                                if None in user_money:
                                    await message.channel.send(f'{user}의 역할을 찾을 수 없습니다. 잠시 뒤에 시도해주세요.')
                                    return
                                await user.remove_roles(*temp_list)
                                # await log(시간(), '삭제한거', [(i.id, i.name) for i in temp_list[::-1]], '?!?!?1?1\n', '삭제하고남은거', [(i.id, i.name) for i in user.roles[1:][::-1]])
                                # await client.get_channel(861552854933045308).send('\n'.join(list(map(str, [시간(), '삭제한거', [(i.id, i.name) for i in temp_list[::-1]], '?!?!?1?1\n', '삭제하고남은거', [(i.id, i.name) for i in user.roles[1:][::-1]]]))))

                                usermoney = int(''.join(user_money))
                                usermoney += money
                                usermoney = str(usermoney).zfill(6)

                                if int(usermoney) >= 1000000:
                                    await message.channel.send(f"{user}이 1000레벨이 되었습니다.") ; return
                                #await log("*"+str(usermoney)+"*")
                                logStr = f"{시간()} ; {user} ; lv.`{(int(usermoney)-money)//1000}` exp.`{(int(usermoney)-money)%1000}` 에서 `{money}`exp를 얻어 lv.`{int(usermoney[:3])}` exp.`{int(usermoney[3:])}`이 되었습니다."
                                await user.add_roles(message.guild.get_role(level_100[ int( usermoney[0] ) ] ),
                                                        message.guild.get_role( level_10[ int( usermoney[1] ) ] ),
                                                        message.guild.get_role( level_01[ int( usermoney[2] ) ] ),
                                                        message.guild.get_role(  exp_100[ int( usermoney[3] ) ] ),
                                                        message.guild.get_role(  exp_010[ int( usermoney[4] ) ] ),
                                                        message.guild.get_role(  exp_001[ int( usermoney[5] ) ] ),
                                                        reason=logStr)
                                await client.get_channel(861552854933045308).send(logStr)
                                
                                await message.channel.send(logStr)
                                await message.add_reaction(체크)
                                for p, q in List[2]:
                                    if random.uniform(0, 100) <= p:
                                        await message.channel.send(f"{q} 을(를) 획득했습니다!")
                                
                            else:
                                await message.channel.send(f"해당 몬스터를 잡을 수 없습니다.\n해당 몬스터는 hp가 {List[0][0]}이고, 공격력이 {List[0][1]}입니다.\n{message.author}은 공격력이 {Attack}\\*{MultiAttack}={Attack*MultiAttack}이고 방어력이 {Defense}\\*{MultiDefense}={Defense*MultiDefense}입니다.")
                    return

            if message.channel.id == 867598299045167144:
                if 시작("채광"):
                    for i in note.content.split('\n')[1:]:
                        if i.startswith(user):
                            Pick = i.split(' : ')[5]
                            #await log('*', Attack, Defense, '*')
                            break
                    else:
                        await message.channel.send(f"{message.author}의 곡괭이를 찾을수 없습니다.") ; return
                    
                    if Pick.startswith("슬라임"):
                        minelist= ["철"]*1 + ["없음"]*99
                    elif Pick.startswith("고블린"):
                        minelist= ["철"]*4 + ["금"]*1 + ["없음"]*95
                    elif Pick.startswith("뼈"):
                        minelist= ["철"]*8 + ["금"]*3 + ["루비"]*1 + ["에메랄드"]*1 + ["사파이어"]*1 + ["다이아몬드"]*1 + ["없음"]*85
                    elif Pick.startswith("오크"):
                        minelist= ["철"]*12 + ["금"]*5 + ["루비"]*2 + ["에메랄드"]*2 + ["사파이어"]*2 + ["다이아몬드"]*2 + ["없음"]*75
                    elif Pick.startswith("마법"):
                        minelist= ["철"]*16 + ["금"]*6 + ["루비"]*2 + ["에메랄드"]*2 + ["사파이어"]*2 + ["다이아몬드"]*2 + ["없음"]*70
                    elif Pick.startswith("특수"):
                        minelist= ["철"]*19 + ["금"]*9 + ["루비"]*3 + ["에메랄드"]*3 + ["사파이어"]*3 + ["다이아몬드"]*3 + ["없음"]*60
                    else:
                        await message.channel.send("곡괭이가 없는 것 같습니다. (오류라고생각되면 언제나 생강을 핑해주세요!)") ; return
                    mine2get = random.choice(minelist)
                    await message.channel.send(f"{mine2get}을 캤습니다!" if mine2get != "없음" else "광물을 캐지 못했습니다...")
            
    # if message.guild.id == 857545260816138251:
    #     return

    # 여기서부터 global 명령어들

    m = message.content
    # print(m)
    
    if message.author.discriminator == '0000': # 웹후크 메시지 무시
        return

    # 관리 = (message.author.id == 526889025894875158 or message.author.guild_permissions.administrator)
    관리 = (message.author.id == 526889025894875158)

    if message.author.id == 405664776954576896 and message.channel.id in (766932314973929527, 783516524685688842, 784228694940057640, 794146499034480661):
        #랭크업, 시간, 도박장, 도박2 에서의 슷칼봇 메시지 삭제
        await message.delete()
        return

    #if message.author.bot: # 봇이 보낸 메시지 무시
    #    return

    if '@everyone' in m or '@here' in m:
        return
    
    cmdlist = [i[2:] for i in dir(C_all) if i.startswith('f_')]
    for cmdName in cmdlist:
        if 시작("," + cmdName):
            C = getattr(C_all, 'f_' + cmdName)
            try:
                await C(message, client)
            except Merror as err:
                e = json.loads(str(err))
                await message.channel.send(f'매개변수가 부족합니다.\n최소 {e[0]}개의 매개변수가 필요하지만, {e[1]}개의 매개변수가 입력되었습니다.\n`,도움 {e[2]}` 로 자세한 도움말을 볼수 있습니다.')
            return

    if 관리:
        cmdlist = [i[2:] for i in dir(C_admin) if i.startswith('f_')]
        for cmdName in cmdlist:
            if 시작("," + cmdName):
                C = getattr(C_admin, 'f_' + cmdName)
                try:
                    await C(message, client)
                except Merror as err:
                    e = json.loads(str(err))
                    # 관리자 명령어라 굳이 추가해야할까 싶지만 그냥 추가함 ㅋㅋ루
                    await message.channel.send(f'매개변수가 부족합니다.\n최소 {e[0]}개의 매개변수가 필요하지만, {e[1]}개의 매개변수가 입력되었습니다.\n`,도움 {e[2]}` 로 자세한 도움말을 볼수 있습니다.')
                return



    if 시작(",날짜") and message.guild.id == 766932314973929522:
        d = datetime.date.today() - datetime.date(2020,10,17)
        await message.channel.send(f"오늘은 {d.days}일입니다.")


    elif 시작(",올려") and message.guild.id == 743101101401964647:
        m = ' '.join(m.split(' ')[1:])
        for i in range(int(m)):
            await message.channel.send("ㅋ올려")

    #elif 시작("섬바삭보") and message.guild.id == 743101101401964647:
    #    await message.channel.send("ㄹㅇㅋㅋ 섬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ밬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ삭ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ봌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

    elif 시작(",우탐") and message.guild.id == 743101101401964647:
        embed = discord.Embed(title=message.author.display_name, color=0x4849c3)
        channelname = message.channel.name.split('-')[0]
        embed.add_field(name=f"{channelname} 탐험 결과", value=f"탐험 레벨: {str(message.author)[-4:]} 로 증가!", inline=False)
        random_result = random.choice(["돈", "경험치", "레벨"])
        embed.add_field(name="획득한 보상", value=f"{random_result} +0.0000000000000000...", inline=False)
        await message.channel.send(embed=embed)

    elif 시작(",잡키") and message.guild.id == 743101101401964647:
        embed = discord.Embed(title="잡초에게 물을 주었다.", color=0x00ff7f)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/3gXDoQqnWaQQKtbS99CR7ViBZY4o7o-epmmsWGgzG4s/https/media.discordapp.net/attachments/783226362856734730/818719628602638387/224_20210125224126.png?width=427&height=427")
        embed.add_field(name="잡초 레벨", value=f"{int(str(message.author)[-4:])-1} -> {str(message.author)[-4:]}", inline=False)
        embed.add_field(name="잡초 성장 진행도", value="ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ", inline=False)
        random_result = random.choice(["돈", "경험치", "레벨"])
        embed.add_field(name="받은 보상", value=f"{random_result} +0.0000000000000000...", inline=False)
        await message.channel.send(embed=embed)

    elif 시작(",커뉴봇") and message.guild.id == 743101101401964647:
        await message.channel.send("ㅋ강화")
        await message.channel.send("ㅋ섭강")
        await message.channel.send("ㅋ잡키") ; await asyncio.sleep(1.0)
        await message.channel.send("ㅋ우탐")
        try:
            mac_msg = await client.wait_for('message', timeout=10.0, check=lambda msg: msg.author.id == 772274871563583499 and msg.channel == message.channel and "매크로" in msg.content)
            await message.channel.send(mac_msg.content[49:54])
        except:
            pass
    elif message.channel.id == 743339107731767366:
      m = m[:5]
      if '69' in m: await message.add_reaction("♋")
      if '74' in m: await message.add_reaction("💦")
      if m[::-1]==m:await message.add_reaction("🪞")



    # 자동 반응
    if message.guild.id == 743101101401964647:
      m = message.content
      try:
        if '피자' in m: await message.add_reaction('🍕')
        if '티비' in m: await message.add_reaction('📺')

      except:
        pass


    if message.guild is None: # dm
        return
    if message.author.bot:
        return





    ##### 여기서부터는 노가다 서버 랭크 관련 코드임. #####

    if message.guild.id == 766932314973929522:
        m = message.content

        mentions = {
            '시인': '<@!647001590766632966>',
            '둔늑': '<@!544076137593176120>',
            '민망': '<@!693386027036835912>',
            '감자': '<@!526889025894875158>',
            }

        for nickname in mentions:
            if m == nickname:
                ping = await message.channel.send(f"{message.author} : {mentions[nickname]}")
                await asyncio.sleep(1.0)
                await ping.delete()
                await message.delete()
                return


        Admins = [647001590766632966, 725528129648721920, 436071996661563402] # 생강, 내려놔, 키기루

        if 시작(",피버") and message.author.id in Admins: # 피버타임
            global 피버
            피버 = not 피버
            if 피버:
                await message.channel.send("피버타임이 *켜*졌습니다")
            else:
                await message.channel.send("피버타임이 *꺼*졌습니다")


        if (시작(",+") or 시작(",-")) and message.author.id in Admins:
            case = 1 # +-
        elif message.channel.id in (766932314973929527, 783516524685688842, 871400280854523905):
            case = 2 # 랭크업
        elif message.channel.id in (784228694940057640, 794146499034480661):
            case = 3 # 도박
        elif 시작(",일급") and message.author.id in Admins:
            case = 4 # 일급
        else:
            return

        if case == 1:
            money = int(m.split()[0][1:])
            users = [ (await message.guild.fetch_member(int(i[-18:] if i[-1] in "1234567890" else i[-19:-1]))) for i in m.split()[1:] ]
        elif case == 2:
            tryRank = None
            if 시작("ㅇ"):
                tryRank = [1,1,0,0,0,0,0,0,0,0]
            if 시작("ㄱ"):
                if 시간()[5:7] == "02" and 시간()[8:10] == "14" or\
                    시간()[5:7] == "03" and 시간()[8:10] == "14" or\
                    시간()[5:7] == "04" and 시간()[8:10] == "12" or\
                    시간()[5:7] == "05" and 시간()[8:10] == "05" or\
                    시간()[5:7] == "05" and 시간()[8:10] == "08" or\
                    시간()[5:7] == "06" and 시간()[8:10] == "06" or\
                    시간()[5:7] == "09" and 시간()[8:10] == "01" or\
                    시간()[5:7] == "11" and 시간()[8:10] == "11" or\
                    시간()[5:7] == "12" and 시간()[8:10] == "01" or\
                    시간()[5:7] == "12" and 시간()[8:10] == "25":
                    tryRank = [1,1,1,0,0,0,0,0,0,0]
                else:
                    await message.channel.send("현재 사용할수 없는 커맨드입니다.") ; return
            if 시작("ㅅ"):
                if 시간()[5:7] == "03" and 시간()[8:10] == "01" or\
                    시간()[5:7] == "07" and 시간()[8:10] == "17" or\
                    시간()[5:7] == "08" and 시간()[8:10] == "15" or\
                    시간()[5:7] == "10" and 시간()[8:10] == "03" or\
                    시간()[5:7] == "10" and 시간()[8:10] == "09":
                    tryRank = [1,1,1,1,0,0,0,0,0,0]
                else:
                    await message.channel.send("현재 사용할수 없는 커맨드입니다.") ; return
            if 시작("ㅌ"):
                if 시간()[5:7] == "01" and 시간()[8:10] == "01" or\
                    시간()[5:7] == "08" and 시간()[8:10] == "30" or\
                    시간()[5:7] == "10" and 시간()[8:10] == "09" or\
                    시간()[5:7] == "12" and 시간()[8:10] == "04" or\
                    시간()[2:4] == "20" and 시간()[5:7] == "01" and 시간()[8:10] == "25" or\
                    시간()[2:4] == "21" and 시간()[5:7] == "02" and 시간()[8:10] == "12" or\
                    시간()[2:4] == "22" and 시간()[5:7] == "02" and 시간()[8:10] == "01" or\
                    시간()[2:4] == "23" and 시간()[5:7] == "01" and 시간()[8:10] == "22" or\
                    시간()[2:4] == "24" and 시간()[5:7] == "02" and 시간()[8:10] == "10" or\
                    시간()[2:4] == "25" and 시간()[5:7] == "01" and 시간()[8:10] == "29" or\
                    시간()[2:4] == "26" and 시간()[5:7] == "02" and 시간()[8:10] == "17" or\
                    시간()[2:4] == "27" and 시간()[5:7] == "02" and 시간()[8:10] == "07" or\
                    시간()[2:4] == "28" and 시간()[5:7] == "01" and 시간()[8:10] == "27" or\
                    시간()[2:4] == "29" and 시간()[5:7] == "02" and 시간()[8:10] == "13" or\
                    시간()[2:4] == "30" and 시간()[5:7] == "02" and 시간()[8:10] == "03" or\
                    시간()[2:4] == "20" and 시간()[5:7] == "10" and 시간()[8:10] == "01" or\
                    시간()[2:4] == "21" and 시간()[5:7] == "09" and 시간()[8:10] == "21" or\
                    시간()[2:4] == "22" and 시간()[5:7] == "09" and 시간()[8:10] == "10" or\
                    시간()[2:4] == "23" and 시간()[5:7] == "09" and 시간()[8:10] == "29" or\
                    시간()[2:4] == "24" and 시간()[5:7] == "09" and 시간()[8:10] == "17" or\
                    시간()[2:4] == "25" and 시간()[5:7] == "10" and 시간()[8:10] == "06" or\
                    시간()[2:4] == "26" and 시간()[5:7] == "09" and 시간()[8:10] == "25" or\
                    시간()[2:4] == "27" and 시간()[5:7] == "09" and 시간()[8:10] == "15" or\
                    시간()[2:4] == "28" and 시간()[5:7] == "10" and 시간()[8:10] == "03" or\
                    시간()[2:4] == "29" and 시간()[5:7] == "09" and 시간()[8:10] == "22" or\
                    시간()[2:4] == "30" and 시간()[5:7] == "09" and 시간()[8:10] == "12":
                    tryRank = [1,1,1,1,1,0,0,0,0,0]
                else:
                    await message.channel.send("현재 사용할수 없는 커맨드입니다.") ; return
            if 시작("ㅊ"):
                if 시간()[5:7] == "01" and 시간()[8:10] == "26":
                    tryRank = [1,1,1,1,1,1,0,0,0,0]
                else:
                    await message.channel.send("현재 사용할수 없는 커맨드입니다.") ; return
            if 시작("ㄹ"):
                if discord.utils.get(message.guild.roles, name="랭커") in message.author.roles:
                    tryRank = [1,1,1,0,0,0,0,0,0,0]
                else:
                    await message.channel.send("랭커만 사용할 수 있는 커맨드입니다.") ; return
            if 시작("ㅍ"):
                if discord.utils.get(message.guild.roles, name="마스터(칭호)") in message.author.roles or\
                    discord.utils.get(message.guild.roles, name="신") in message.author.roles or\
                    discord.utils.get(message.guild.roles, name="챔피언(칭호)") in message.author.roles:
                    tryRank = [1,1,1,1,0,0,0,0,0,0]
                else:
                    await message.channel.send("마스터 이상만 사용할 수 있는 커맨드입니다.") ; return
            if 시작("ㅂ"):
                if 피버:
                    tryRank = [1,1,1,0,0,0,0,0,0,0]
                else:
                    await message.channel.send("현재 사용할수 없는 커맨드입니다.") ; return
            if not tryRank:
                return
            if not random.choice(tryRank):
                await message.channel.send("랭크업에 실패하였습니다...")
                return
            money = 1
            users = [message.author, ]
        elif case == 3:
            #도박 아니면 제거
            if 시작("ㄷ") or 시작("ㄸ"):
                dp = random.choice([2, 2, 1.5, 1.5, 1.5, 1.5, 1, 1, 0.5, 0.5])
            elif 시작("ㅅ") or 시작("ㅆ"):
                dp = random.choice([2, 2, 2, 1.5, 1.5, 1.5, 1.5, 1, 1, 0.5])
            else:
                return
            if dp == 1: # 1배는 계산할 필요가 없음
                await message.channel.send("1배")
                await message.add_reaction(체크)
                return
            money = None # 도박은 지금 money를 계산할수가 없음
            users = [message.author, ]
        elif case == 4:
            m = ' '.join(m.split(' ')[1:])
            try:
                a = int(m)
            except:
                a = 1

            users = {}

            ilGup = {
                '인턴' : 20,
                '과장' : 50,
                '부장' : 150,
                '사장' : 250,
                '부회장' : 500,
                }

            for i in ilGup:
                for o in discord.utils.get(client.get_guild(766932314973929522).roles, name=i).members:
                    users[o] = ilGup[i]

        for user in users:
            if case == 4: # 일급일때
                money = users[user] * a
            # 역할 찾아서 랭크 계산
            userRank = 0

            userGod = ''
            for i in God1:
                if i in [i.name for i in user.roles]:
                    userGod += i

            userGod = God2.index(userGod) if userGod in God2 else 0

            for i in range(len(Ranks_10)):
                if Ranks_10[i] in [i.id for i in user.roles]:
                    userRank += i*10 ; break
            else:
                await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; continue
            for i in range(len(Ranks_01)):
                if Ranks_01[i] in [i.id for i in user.roles]:
                    userRank += i ; break
            else:
                await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; continue

            for i in range(len(Tears)):
                if Tears[i] in [i.name for i in user.roles]:
                    userTear = i ; break
            else:
                await message.channel.send(f"{user}의 역할을 찾을수 없습니다.. 잠시 뒤에 시도해보세요") ; continue

            userAgain = 0
            for i in range(len(Agains_10)):
                if Agains_10[i] in [i.name for i in user.roles]:
                    userAgain += i*10 ; break
            else:
                userAgain += 0*10

            for i in range(len(Agains_01)):
                if Agains_01[i] in [i.name for i in user.roles]:
                    userAgain += i ; break
            else:
                userAgain += 0

            userGodAgain = 0
            for i in range(len(God_Agains_10)):
                if God_Agains_10[i] in [i.id for i in user.roles]:
                    userGodAgain += i*10 ; break
            for i in range(len(God_Agains_01)):
                if God_Agains_01[i] in [i.id for i in user.roles]:
                    userGodAgain += i ; break

            userTotalRank = 0
            userTotalRank += userRank
            userTotalRank += userTear *number_1
            userTotalRank += userAgain *number_2
            userTotalRank += userGod *number_3
            userTotalRank += userGodAgain *number_4

            if case in (1, 2, 4): # (money가 정해져있음)
                userTotalRank += money

            if case == 3: #도박일때
                #얼마나 걸었는지
                try:
                    dmoney = int(message.content.split()[1])
                except:
                    if 시작("ㄷ") or 시작("ㄸ"):
                        dmoney = 100+userAgain*50
                    elif 시작("ㅅ") or 시작("ㅆ"):
                        dmoney = 100+userAgain*100
                    await message.channel.send(f"{dmoney}을 겁니다...")

                #건 돈이 10~(환생횟수+1)*100 아닐경우 제거
                if 시작("ㄷ") or 시작("ㄸ"):
                    if not 10 <= dmoney <= 100+userAgain*50:
                        await message.channel.send(f"`10~100+(환생횟수)*50 (10~{100+userAgain*50})` 만 걸수 있습니다.")
                        return
                elif 시작("ㅅ") or 시작("ㅆ"):
                    if not 10 <= dmoney <= 100+userAgain*100:
                        await message.channel.send(f"`10~100+(환생횟수)*100 (10~{100+userAgain*100})` 만 걸수 있습니다.")
                        return

                #가진돈보다 건돈이 많다면 알림
                if dmoney > userTotalRank:
                    await message.channel.send("랭크가 부족합니다.")
                    return
                if 시작("ㅅ") or 시작("ㅆ"):
                    if userTotalRank < 81000:
                        await message.channel.send("초하-급신부터 사용할수 있습니다.")
                        return

                #도박을 해봄
                await message.channel.send(f"{dp}배")
                if dp == 0.5 and userTotalRank >= 20:
                    mymsg2 = await message.channel.send(f"실드를 구매 및 사용하시겠습니까?\n실드 1개당 20랭크, 20%입니다.\n0️⃣ `100% {round(-dmoney+dmoney*dp)}`\n1️⃣ `20% {round(-20)}, 80% {round(-20-dmoney+dmoney*dp)}`\n2️⃣ `40% {round(-40)}, 60% {round(-40-dmoney+dmoney*dp)}`\n3️⃣ `60% {round(-60)}, 40% {round(-60-dmoney+dmoney*dp)}`\n4️⃣ `80% {round(-80)}, 20% {round(-80-dmoney+dmoney*dp)}`\n5️⃣ `100% {round(-100)}`")
                    await mymsg2.add_reaction("0️⃣");time.sleep(0.5)
                    await mymsg2.add_reaction("1️⃣");time.sleep(0.5)
                    await mymsg2.add_reaction("2️⃣");time.sleep(0.5)
                    await mymsg2.add_reaction("3️⃣");time.sleep(0.5)
                    await mymsg2.add_reaction("4️⃣");time.sleep(0.5)
                    await mymsg2.add_reaction("5️⃣")
                    try:
                        reaction, _ = await client.wait_for('reaction_add', timeout=60.0, check=lambda r, u: str(r.emoji) in "0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣" and u == message.author)
                        reaction = str(reaction.emoji)
                    except:
                        reaction = "0️⃣"
                    if reaction == "0️⃣":
                        money = round(-dmoney+dmoney*dp)
                    elif reaction == "1️⃣":
                        if random.choice([1,0,0,0,0]):
                            money = round(-20)
                            await message.channel.send(f"실드 사용에 성공함 ({money})")
                        else:
                            money = round(-20-dmoney+dmoney*dp)
                            await message.channel.send(f"실드 사용에 실패함 ({money})")

                    elif reaction == "2️⃣":
                        if random.choice([1,1,0,0,0]):
                            money = round(-40)
                            await message.channel.send(f"실드 사용에 성공함 ({money})")
                        else:
                            money = round(-40-dmoney+dmoney*dp)
                            await message.channel.send(f"실드 사용에 실패함 ({money})")

                    elif reaction == "3️⃣":
                        if random.choice([1,1,1,0,0]):
                            money = round(-60)
                            await message.channel.send(f"실드 사용에 성공함 ({money})")
                        else:
                            money = round(-60-dmoney+dmoney*dp)
                            await message.channel.send(f"실드 사용에 실패함 ({money})")

                    elif reaction == "4️⃣":
                        if random.choice([1,1,1,1,0]):
                            money = round(-80)
                            await message.channel.send(f"실드 사용에 성공함 ({money})")
                        else:
                            money = round(-80-dmoney+dmoney*dp)
                            await message.channel.send(f"실드 사용에 실패함 ({money})")

                    elif reaction == "5️⃣":
                        money = round(-100)
                        await message.channel.send(f"실드 사용에 성공함 ({money})")

                else:
                    money = round(-dmoney+dmoney*dp)
                #랭크적용...
                userTotalRank += money
                if userTotalRank < 0:
                    await message.channel.send("랭크가 부족합니다.")
                    return

            # 역할 제거
            for i in user.roles:
                if i.id in Ranks_10 or \
                    i.id in Ranks_01 or \
                    i.name in Tears or \
                    i.name in Agains_10 or \
                    i.name in Agains_01 or \
                    i.name in God1 or \
                    i.name in God_Agains_10 or \
                    i.name in God_Agains_01:
                    await user.remove_roles(i)

            #신급환생적용
            await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_10[(userTotalRank//number_4) // 10]))
            await user.add_roles(discord.utils.get(message.guild.roles, name=God_Agains_01[(userTotalRank//number_4) %  10]))
            userTotalRank %= number_4
            #신급적용
            for i in God2[userTotalRank // number_3]:
                await user.add_roles(discord.utils.get(message.guild.roles, name=i))
            userTotalRank %= number_3
            #환생횟수 적용
            await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_10[(userTotalRank//number_2) // 10]))
            await user.add_roles(discord.utils.get(message.guild.roles, name=Agains_01[(userTotalRank//number_2) %  10]))
            userTotalRank %= number_2
            #티어 적용 (0이어도 0번째(아톰))
            await user.add_roles(discord.utils.get(message.guild.roles, name=Tears[userTotalRank//number_1]))
            userTotalRank %= number_1
            #랭크 적용 (0이어도 0번째(L))
            await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_10[userTotalRank // 10]))
            await user.add_roles(discord.utils.get(message.guild.roles, id=Ranks_01[userTotalRank %  10]))

            if case == 2:
                await message.channel.send("랭크업에 성공하였습니다!")
        await message.add_reaction(체크)

client.run(os.environ["TOKEN3"])
