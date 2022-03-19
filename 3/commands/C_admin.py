import sys
sys.path.append(".")
from imports import *


@setM(0)
async def f_에블핑(Ms, message, client):
    await message.channel.send("@everyone")
    
@setM(0)
async def f_히어핑(Ms, message, client):
    await message.channel.send("@here")
    
@setM(1)
async def f_청소(Ms, message, client):
    await message.channel.purge(limit=int(Ms[0])+1)
    msg = await message.channel.send(f"{Ms[0]}개의 메시지를 지움")
    await asyncio.sleep(2.0)
    await msg.delete()

@setM(1)
async def f_역할생성(Ms, message, client):
    await message.guild.create_role(name=Ms[0])
    await message.add_reaction(체크)

@setM(1)
async def f_역할제거(Ms, message, client):
    role = discord.utils.get(message.guild.roles, name=Ms[0])
    await role.delete()
    await message.add_reaction(체크)

@setM(2)
async def f_채널생성(Ms, message, client):
    category = discord.utils.get(message.guild.categories, name=' '.join(Ms[1]))
    await message.guild.create_text_channel(Ms[0], category=category)
    await message.add_reaction(체크)

@setM(1)
async def f_채널제거(Ms, message, client):
    channel = discord.utils.get(message.guild.channels, name=Ms[0])
    await channel.delete()
    await message.add_reaction(체크)

@setM(1)
async def f_코드(Ms, message, client):
    if '\n' in Ms[0]:
        exec('global 출력\n' + '\n'.join(Ms[0].split('\n')[:-1]) + '\n출력=' + Ms[0].split('\n')[-1])
        outputmsg = str(출력)
    else:
        outputmsg = str(eval(Ms[0]))

    # 2000글자씩 나누어보내기
    if not len(outputmsg): await message.channel.send('*말을 할수 없는*')
    while len(outputmsg):
        await message.channel.send(outputmsg[:2000])
        outputmsg = outputmsg[2000:]

@setM(1)
async def f_await코드(Ms, message, client):
    exec('global awaitFunction\nasync def awaitFunction(message, client):\n' + '\n'.join(list(map(lambda x: '    '+x, Ms[0].split('\n')[:-1]))) + '\n    return ' + Ms[0].split('\n')[-1])
    outputmsg = str(await awaitFunction(message, client))

    # 2000글자씩 나누어보내기
    while len(outputmsg):
        await message.channel.send(outputmsg[:2000])
        outputmsg = outputmsg[2000:]
