import sys
sys.path.append(".")
from imports import *


@setM(0, 1)
async def f_도움(Ms, message, client):
    """
    `,도움`
    전체 도움말을 출력합니다.
    `,도움 <명령어 이름>`
    <명령어 이름>의 도움말을 출력합니다.
    """
    embed = discord.Embed(title="도움말", color=0x825cff)

    cmds = [ i[2:] for i in globals() if i.startswith('f_')]

    if Ms[0] in cmds:
        embed.add_field(name=Ms[0], value=globals()[f"f_{Ms[0]}"].func.__doc__, inline=False)
    else:
        embed.add_field(name="`,도움 <명령어>`로 세부 도움말을 확인할수 있습니다", value=' '.join(map(lambda x: f'`{x}`', cmds)), inline=False)

    embed.set_footer(text= f'{message.author.name} | {시간()}')
    await message.channel.send(embed=embed)
    
@setM(0, 1)
async def f_말(Ms, message, client):
    """
    `,말 <할 말>`
    <할 말>을 출력합니다.
    """
    try:
        await message.channel.send(Ms[0])
    except:
        await message.channel.send('말을 할수 없는')

@setM(0)
async def f_초대(Ms, message, client):
    """
    `,초대`
    이 봇의 초대링크를 출력합니다.
    """
    await message.channel.send("https://discord.com/oauth2/authorize?&client_id=688978156535021599&scope=bot&permissions=8")

@setM(1)
async def f_번역(Ms, message, client):
    """
    `,번역 <한글>`
    <한글>을 영어로 번역합니다.
    `,번역 <영어>`
    <영어>를 한글로 번역합니다.
    """
    await message.channel.send(translate(Ms[0]))

@setM(0)
async def f_시간(Ms, message, client):
    """
    `,시간`
    현재 시간을 출력합니다.
    """
    await message.channel.send(시간())
    
@setM(1)
async def f_썸네일(Ms, message, client):
    """
    `,썸네일 <url>`
    유튜브 <url>의 썸네일을 출력합니다.
    """
    await message.channel.send(get_thumbnail_by_url(Ms[0]))

@setM(1)
async def f_최신영상(Ms, message, client):
    """
    `,최신영상 <채널>`
    유튜브 <채널>의 최신영상의 제목과 썸네일을 출력합니다.
    """
    await message.channel.send(get_last_video_by_search(Ms[0]))
    
@setM(1)
async def f_영한(Ms, message, client):
    """
    `,영한 <영타>`
    <영타>를 한타로 변환합니다.
    """
    await message.channel.send(e2k(Ms[0]))

@setM(1) 
async def f_한영(Ms, message, client):
    """
    `,한영 <한타>`
    <한타>를 영타로 변환합니다.
    """
    await message.channel.send(k2e(Ms[0]))

@setM(0)
async def f_임베드(Ms, message, client):
    """
    `,임베드`
    임베드를 만듭니다.
    """
    inputdict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
    look_dict = {"제목":'', "색":'', "소제목":'', "내용":'', "푸터":''}
    mymsg = await message.channel.send("준비중...")
    for i in range(len(list(inputdict.keys()))):
        await mymsg.delete()
        mymsg = await message.channel.send(str(i) + ". " + list(inputdict.keys())[i] + "을(를) 입력해주세요.\n```yaml\n" + '\n'.join([ key + ' : ' + look_dict[key] for key in look_dict ]) + '\n```')
        inputmsg = await client.wait_for('message', timeout=30.0, check=lambda msg: msg.channel.id == message.channel.id and msg.author == message.author)
        inputmsg = inputmsg.content
        inputdict[list(inputdict.keys())[i]] = inputmsg
        look_dict[list(inputdict.keys())[i]] = inputmsg[:7]+'...' if len(inputmsg) > 10 else inputmsg
    await mymsg.delete()
    try:
        embed = discord.Embed(title=inputdict["제목"], color=int(inputdict["색"], 16))
    except:
        embed = discord.Embed(title=inputdict["제목"], color=0x000000)
    embed.add_field(name=inputdict["소제목"], value=inputdict["내용"], inline=False)
    embed.set_footer(text=inputdict["푸터"])
    await message.channel.send(embed=embed)
    
@setM(0)
async def f_정보(Ms, message, client):
    """
    `,정보`
    만든사람을 핑합니다.
    """
    await message.channel.send(f"만든사람: 감자#9400 ( ||<@526889025894875158>|| )")
    
@setM(1, 3)
async def f_지뢰찾기(Ms, message, client):
    """
    `,지뢰찾기 <랜덤|최대|최소>`
    <랜덤|최대|최소> 크기의 지뢰찾기 판을 만듭니다.
    `,지뢰찾기 <x> <y> <지뢰 수>`
    <x> * <y> 크기의 지뢰찾기 판을 만듭니다.
    """
    #제대로 input 했는지 확인
    if 시작('랜덤', Ms[0]):
        Ms[0] = random.randint(1, 17)
        Ms[1] = random.randint(1, 50)
        Ms[2] = random.randint(1, Ms[0]*Ms[1])
    elif 시작('최대', Ms[0]):
        Ms[0] = 17
        Ms[1] = 50
        Ms[2] = random.randint(1, Ms[0]*Ms[1])
    elif 시작('최소', Ms[0]):
        Ms[0] = Ms[1] = Ms[2] = 1
    else:
        Ms[0] = int(Ms[0])
        Ms[1] = int(Ms[1])
        Ms[2] = int(Ms[2])

    if not (  (1 <= Ms[0] <= 17) and (1 <= Ms[1] <= 50) and (1 <= Ms[2] <= Ms[0]*Ms[1])  ):
        await message.channel.send("```<x> : 1~17\n<y> : 1~50\n<지뢰 수> : 1~<x>*<y>\n또는 ,지뢰찾기 <랜덤|최대|최소>```") ; return
    #확인 끝, 틀 만들기
    mine_map = []
    for i in range(Ms[1]):
        mine_map.append([])
        for j in range(Ms[0]):
            mine_map[i].append(지뢰[0])
    #틀 만들기 끝, 지뢰 넣기
    i=0
    while i < Ms[2]:
        i1 = random.randrange(Ms[1])
        i2 = random.randrange(Ms[0])
        if mine_map[i1][i2] == 지뢰[10]:
            continue
        else:
            mine_map[i1][i2] = 지뢰[10]
            i+=1
    #지뢰 넣기 끝, 숫자 넣기
    for i1 in range(Ms[1]):
        for i2 in range(Ms[0]):
            if mine_map[i1][i2] == 지뢰[10]:
                continue
            else:
                i=0

                i += 1 if i1>0       and i2>0       and mine_map[i1-1][i2-1] == 지뢰[10] else 0
                i += 1 if i1>0       and                mine_map[i1-1][i2  ] == 지뢰[10] else 0
                i += 1 if i1>0       and i2<Ms[0]-1 and mine_map[i1-1][i2+1] == 지뢰[10] else 0
                i += 1 if                i2>0       and mine_map[i1  ][i2-1] == 지뢰[10] else 0
#               i += 1 if                               mine_map[i1  ][i2  ] == 지뢰[10] else 0
                i += 1 if                i2<Ms[0]-1 and mine_map[i1  ][i2+1] == 지뢰[10] else 0
                i += 1 if i1<Ms[1]-1 and i2>0       and mine_map[i1+1][i2-1] == 지뢰[10] else 0
                i += 1 if i1<Ms[1]-1 and                mine_map[i1+1][i2  ] == 지뢰[10] else 0
                i += 1 if i1<Ms[1]-1 and i2<Ms[0]-1 and mine_map[i1+1][i2+1] == 지뢰[10] else 0

                mine_map[i1][i2] = 지뢰[i]
    mine_map_lookver = ''
    for i in mine_map:
        for j in i:
            mine_map_lookver += f"||{j}||"
        mine_map_lookver += '\n'

    for j in mine_map_lookver.split():
        await asyncio.sleep(1.0)
        await message.channel.send(j)
    await message.channel.send(f"{Ms[0]} * {Ms[1]}, 지뢰 수: {Ms[2]}")
    
@setM(2)
async def f_타자(Ms, message, client):
    """
    `,타자 시작 <n>`
    <n>글자의 랜덤한 한글을 타자합니다.
    `,타자 옛한글 <n>`
    <n>글자의 랜덤한 옛한글을 타자합니다.
    `,타자 유니코드 <n>`
    <n>글자의 랜덤한 유니코드를 타자합니다.
    """
    if 시작('옛한글', Ms[0]):
        case = 1 # 옛한글
    elif 시작('유니코드', Ms[0]):
        case = 2 # 유니코드 전체
    else:
        case = 3 # 한글만
        
    try:
      n = int(Ms[1])
    except:
      return await message.channel.send('뭔가 잘못된듯 함. `,도움 타자`를 해보는건 어떨까요?')
    
    A = "ᄀᄁᄂᄃᄄᄅᄆᄇᄈᄉᄊᄋᄌᄍᄎᄏᄐᄑᄒᄓᄔᄕᄖᄘᄙᄚᄜᄝᄞᄟᄠᄡᄢᄣᄤᄥᄦᄧᄩᄪᄫᄬᄭᄮᄯᄱᄲᄳᄴᄵᄶᄷᄸᄹᄺᄻᄼᄾᅀᅁᅂᅄᅅᅇᅈᅉᅋᅌᅍᅎᅏᅓᅕᅘᅙ"
    B = "ᅡᅢᅣᅤᅥᅦᅧᅨᅩᅪᅫᅬᅭᅮᅯᅰᅱᅲᅳᅴᅵᅶᅷᅸᅿᆀᆂᆆᆇᆈᆉᆌᆍᆎᆐᆑᆒᆔᆕᆖᆘᆚᆛᆜᆝᆞᆟᆡᆢ"
    C = "ᆨᆩᆪᆫᆮᆯᆰᆱᆲᆳᆶᆷᆸᆹᆺᆻᆼᆽᆾᆿᇀᇂᇃᇆᇇᇈᇌᇎᇐᇓᇗᇙᇚᇜᇝᇟᇡᇢᇣᇦᇧᇩᇪᇫᇬᇰᇱᇳᇹ"
    
    taja_list = []
    for _ in range(n):
        if case == 2:
            taja_list.append( chr(random.choice(range(0x110000))) )
        elif case == 1 and random.randint(0,1):
            taja_list.append( random.choice(A)+random.choice(B)+random.choice(C) )
        else:
            taja_list.append( chr(random.randint(ord('가'), ord('힣'))) )
            
    real_taja_str = ''.join(taja_list)
    taja_str = ''.join( [f'{빈공 * random.randint(1, 5)}{i}{빈공 * random.randint(1, 5)}' for i in taja_list] )
    
    
    timeout = n*5
    timeout = min(timeout, 60) # 최대 60초
    timeout = max(timeout, 10) # 최소 10초
    
    first_time = time.time()
    await message.channel.send(f'{timeout}초 안에 다음 문장(?)을 입력해주세요.(복붙 금지)\n> {taja_str}')
    
    try:
        user_msg = await client.wait_for('message', timeout=timeout, check=lambda msg: msg.channel.id == message.channel.id and msg.author.id == message.author.id)
    except:
        await message.channel.send('시간 초과!') ; return
    
    last_time = time.time()
    total_time = last_time - first_time
    if user_msg.content == real_taja_str:
        await message.channel.send(f'<@!{user_msg.author.id}>님이 `{total_time}`초동안 `{n/total_time}글자/s`로 타자에 성공했습니다.')
    else:
        await message.channel.send(f'<@!{user_msg.author.id}>님이 타자에 실패하였습니다.')
        
@setM(0)
async def f_프사(Ms, message, client):
    """
    `,프사`
    자신의 프사를 출력합니다.
    """
    await message.channel.send(embed=discord.Embed(title="프사", color=0xffccff).set_image(url=message.author.avatar_url))
    
@setM(0)
async def f_핑(Ms, message, client):
    """
    `,핑`
    핑을 합니다.
    """
    await message.channel.send(f"<@{message.author.id}>")
   
@setM(0, 1, 2)
async def f_기억(Ms, message, client):
    """
    `,기억`
    기억된 목록을 출력합니다.
    `,기억 <키워드>`
    <키워드>에 기억된 <대답>을 출력합니다.
    `,기억 <키워드> <대답>`
    <키워드>에 <대답>을 기억합니다.
    """
    if Ms[0] == None: # 목록
        await message.channel.send(str(기억.keys())[10:-1].replace(', ', ',\n'))
    elif Ms[1] == None: # 찾기
        await message.channel.send(f"{기억[Ms[0]][0]} - `{기억[Ms[0]][1]}`" if Ms[0] in 기억 else "없음")
    else: # 등록
        if Ms[0] in list(기억.keys()):
            기억[Ms[0]] = [Ms[1], str(message.author)]
            await message.channel.send(Ms[0] + " 을(를) 덮음")
        else:
            기억[Ms[0]] = [Ms[1], str(message.author)]
            await message.channel.send(Ms[0] + " 을(를) 기억")
    
@setM(0)
async def f_슬롯(Ms, message, client):
    """
    `,슬롯`
    슬롯머신을 돌립니다.
    """
    ghkrfbf = []
    ghkrfbf += [1]*4930
    ghkrfbf += [2]*8451
    ghkrfbf += [3]*11972
    ghkrfbf += [4]*17606
    ghkrfbf += [5]*22535
    ghkrfbf += [6]*34507
    msg = await message.reply(content=슬롯[0]*3, mention_author=False)
    await asyncio.sleep(1.0)
    a = [random.choice(ghkrfbf), random.choice(ghkrfbf), random.choice(ghkrfbf)]
    await msg.edit(content = 슬롯[a[0]] + 슬롯[a[1]] + 슬롯[a[2]], mention_author=False)

    a.sort()
    a = tuple(a)
    if a in [(1,1,1) , (2,2,2) , (3,3,3)]:
        await msg.edit(content=msg.content+"\n**잭팟!**")
    if a in [(1,1,2) , (1,1,3) , (1,2,2) , (2,2,3) , (1,3,3) , (2,3,3)]:
        await msg.edit(content=msg.content+"\n**빅윈!**")

@setM(0)
async def f_버튼(Ms, message, client):
    """
    `,버튼`
    버튼을 만듭니다.
    """
    await message.channel.send(
        "와!",
        components=[
            Button(style=ButtonStyle.random_color(), label="wa!")
        ]
    )

@setM(1)
async def f_계산(Ms, message, client):
    """
    `,계산 <식>`
    <식>을 계산합니다.
    """
    response = W_client.query(Ms[0])

    f = list(response.results)[-1].text if len(list(response.results)) else '과부하!'
    await message.channel.send(f)
