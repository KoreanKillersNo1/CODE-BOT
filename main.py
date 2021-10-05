import discord
import asyncio
import datetime
import os
import random
import json
import requests
import time
import keep_alive
import pytz
import openpyxl
import ranking as ranking
from ydl import *
from game import *
from discord import user
from pypresence import Presence
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions
from discord.utils import get

bot = commands.Bot(command_prefix="!")
client = discord.Client()

cid = 869516899229253693
tid = 869516899229253693
gid = 795723865094881290
dii = 828017942565617674
aid = 571699200664797185
gtid = 869577097994194995

@client.event
async def on_member_join(member):
  role = discord.utils.get(message.guild.roles, name = '[일반 유저]')
  await user.add_roles(role)

@client.event
async def on_member_join(member):
  role = discord.utils.get(message.guild.roles, name = '유저')
  await user.add_roles(role)

@client.event
async def on_ready():
  print(client.user.name)
  print('성공적으로 봇이 시작되었습니다.')
  print('코드 봇 이제 사용 하셔도 좋습니다')
  print('현재 온라인 멤버 수 : {online}명')
  game = discord.Game('코드 봇ㅣ!도움말ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
  await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    f = open("메세지저장.txt", "a")
    f.write(f"서버이름: {message.guild.name}\n전송자: ID {message.author.id} / 닉네임: {message.author}\n시간: {y}년 {m}월 {d}일 {h}시 {min}분\n메세지 내용: {message.content}\n\n\n")
    f.close()



@client.event
async def on_message(message, checkUser=None, levelupCheck=None, modifyExp=None):
  if message.author == client.user:
    return
  if message.content == "!reset":
    await client.process_commands(message)
    return
  else:
    userExistance = checkUser(message.author.name)
    userRow = checkUser(message.author.id)
    channel = message.channel
    if userExistance:
      levelUp, lvl = levelupCheck(userRow)
      if levelUp:
        print(message.author, "가 레벨업 했습니다")
        print("")
        embed = discord.Embed(title="레벨업", description=None, color=0x00A260)
        embed.set_footer(text=message.author.name + "이 " + str(lvl) + "레벨 달성!")
        await message.channel.send(embed=embed)
      else:
        modifyExp(userRow, 1)
        print("------------------------------\n")

        await client.process_commands(message)


@client.event
async def on_message(message, checkUser=None, DeleteAccount=None, Signup=None, checkUserNum=None, userInfo=None,getRank=None, chekcUserNum=None, getMoney=None, remit=None, modifyMoney=None, addLoss=None,cur_money=None):
  if message.guild is None:
    if message.author.bot:
      return
    else:
      embed = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
      embed.add_field(name='전송자', value=message.author, inline=False)
      embed.add_field(name='내용', value=message.content, inline=False)
      embed.set_footer(text=f'!디엠 <@{message.author.id}> [할말] 을 통해 답장을 보내주세요!')
      await client.get_channel(874419000401096754).send(f"`{message.author.name}({message.author.id})`", embed=embed)


  if message.content.startswith('!디엠'):
    if message.author.guild_permissions.manage_messages:
      msg = message.content[26:]
      await message.mentions[0].send(f"**개발자** 님의 답장: {msg}")
      await message.channel.send(f'`{message.mentions[0]}`에게 DM을 보냈습니다')
    else:
      return

  if message.content == "임베드":
      embed = discord.Embed(title="임", description="베", color=0x00ff00)
      embed.set_footer(text="드")
      await message.channel.send(embed=embed)

  if message.content == "!테스트":
      embed = discord.Embed(title="테스트",description="[테스트](https://support.discord.com/hc/ko)", color=0x00ff00)
      embed.set_thumbnail(url="http://theviewers.co.kr/Files/30/Images/201907/38704_35293_1517.jpg")

      await message.channel.send(embed=embed)

  if message.content.startswith("!보상"):
      embed = discord.Embed(title="*{오늘의 보상}*", description=" 보상 : 세븐일레븐 무료 입장권!", color=0x00ff00)
      embed.set_footer(text="보상은 주기적으로 바뀝니다.")
      await message.channel.send(embed=embed)

  if "시발" in message.content or "시부랄" in message.content or "병신" in message.content or "개새끼" in message.content or "시불" in message.content or "수발" in message.content or "새끼" in message.content or "tlqkf" in message.content or "qudtls" in message.content or "roTOrl" in message.content or "시,발" in message.content or "미친년" in message.content or "븅신" in message.content or "등신" in message.content or "니 애미" in message.content or "미국 갔어" in message.content or "tlqk" in message.content or "시1발" in message.content or "시qkf" in message.content or "시이발" in message.content or "tl1qkf" in message.content or "싯1팔" in message.content or "시바" in message.content:
    embed = discord.Embed(title="욕설이 감지되었습니다", description=f"{message.author.mention}님 메세지가 삭제되었습니다. *[사유 : 부적절한 언어 사용]*", color=0xf5d400)
    await message.channel.send(embed=embed)
    await message.delete()
    return

  if message.content.startswith("!리소스팩"):
    embed = discord.Embed(title="겉날개 스킨 리소스팩", description="[겉날개 스킨](https://www.weebly.com/editor/uploads/1/0/5/1/105176727/custom_themes/365187814667513194/files/MoreElytrasbyJohnPaulInsoV1.5.zip)", color=0x00ff00)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/f7/Mojang_employees_2015_Elytra.png/revision/latest/scale-to-width-down/250?cb=20191029123353")

  if message.content.startswith("!투표"):
    if message.author.guild_permissions.administrator:
      vote = message.content[4:].split("/")
      await message.channel.send(" < " + vote[0] + " > ")
      for i in range(1, len(vote)):
        choose = await message.channel.send("```" + vote[i] + "```")
        await choose.add_reaction('👍')
      await message.delete()
      return
    
    else:
      await message.delete()
      await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

  if message.content.startswith("!청소"):
    if message.author.guild_permissions.administrator:
      amount = message.content[4:]
      await message.delete()
      await message.channel.purge(limit=int(amount))

      embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
      embed.set_footer(text="Bot Made by. 『킬쟁이』#3333",icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
      await message.channel.send(embed=embed)
        
    else:
      await message.delete()
      await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

  if message.content.startswith("!마크"):
    embed = discord.Embed(title="ㅤ", description="마크 무료로 설치하는법 어떤사람이 나 3만원 주고 마크 설치함 라고 하길래 알려줬다 1. 마크 사이트를 들어간다 2. 다운로드를 누른다 3. 런처 다운받는다 4. 설치한다 5. 로그인을 한다 6. 재밌게플레이를 한다 3만원에 설치한 사람은 호구다", color=0x000000)
    await message.channel.send(embed=embed)

  if message.content.startswith("!마크"):
    await message.channel.send("@everyone ")

  if message.content.startswith ("!인증 "):
    if message.author.guild_permissions.administrator:
      await message.delete()
      user = message.mentions[0]

      embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
      embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
      embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
      embed.set_footer(text="Bot Made by. 『킬쟁이』#3333")
      await message.channel.send(embed=embed)
      role = discord.utils.get(message.guild.roles, name = '────[일반 유저]────')
      await user.add_roles(role)

    else:
      await message.delete()
      await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))

  if message.content == "!테스트2": # 메세지 감지
    await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
    await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))

  if message.content.startswith ("!공지"):
    await message.delete()
    if message.author.guild_permissions.administrator:
      notice = message.content[4:]
      channel = client.get_channel(795723865094881290)
      embed = discord.Embed(title="**공지사항 제목 (볼드)*", description="\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
      embed.set_footer(text="Bot Made by. 『킬쟁이』#3333 | 담당 관리자 : {}".format(message.author), icon_url="https://cdn.codingworldnews.com/news/photo/202106/4358_6139_4837.jpg")
      embed.set_thumbnail(url="https://cdn.codingworldnews.com/news/photo/202106/4358_6139_4837.jpg")
      await channel.send ("@everyone", embed=embed)
      await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
    else:
      await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

  if message.content == "!특정입력":
    ch = client.get_channel(836974954243162162)
    await ch.send ("{} | {}, 현재 봇은 점검중입니다".format(message.author, message.author.mention))


  if message.content.startswith("!시간"):
    a = datetime.datetime.today().year
    b = datetime.datetime.today().month
    c = datetime.datetime.today().day
    d = datetime.datetime.today().hour
    e = datetime.datetime.today().minute
    await message.channel.send(str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 (3시간 차이남) " + str(e) + "분 입니다")   

  if message.content.startswith("!출근"):
    embed = discord.Embed(title=f"{message.author.name}님이 출근하셨습니다.", color=0x00ff00)
    await client.get_channel(int(cid)).send (embed=embed)

  if message.content.startswith("!퇴근"):
    embed = discord.Embed(title=f"{message.author.name}님이 퇴근하셨습니다.", color=0x00ff00)
    await client.get_channel(int(tid)).send (embed=embed)



  if message.content.startswith("!주사위"):
    result, _color, bot1, bot2, user1, user2, a, b = dice()

    embed = discord.Embed(title="주사위 게임 결과", description=None, color=_color)
    embed.add_field(name="Code Bot의 숫자 " + bot1 + "+" + bot2, value=":game_die: " + a, inline=False)
    embed.add_field(name=message.author.name + "의 숫자 " + user1 + "+" + user2, value=":game_die: " + b, inline=False)
    embed.set_footer(text="결과: " + result)

    await message.channel.send(embed=embed)

  if message.content.startswith("!내정보"):
    userExistance, userRow = checkUser(message.author.name, message.author.id)
    level, exp, money, loss = userInfo(userRow)
    rank = getRank(userRow)
    data = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
    userNum = checkUserNum()
    expToUP = level * level + 6 * level
    boxes = int(exp / expToUP * 20)
    print("------------------------------\n")
    embed = discord.Embed(title="!유저 정보", description=message.author.name, color=0x62D0F6)
    embed = discord.Embed(color=0x00ff00)
    embed.add_field(name="이름", value=message.author.name, inline=True)
    embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
    embed.add_field(name="가입일", value=str(data.year) + "년" + str(data.month) + "월" + str(data.day) + "일", inline=True)
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.add_field(name="레벨", value=level)
    embed.add_field(name="순위", value=str(rank) + "/" + str(userNum))
    embed.add_field(name="XP: " + str(exp) + "/" + str(expToUP),value=boxes * ":blue_square:" + (20 - boxes) * ":white_large_square:", inline=False)
    embed.add_field(name="보유 자산", value=money, inline=False)

    await message.channel.send(embed=embed)

  if message.content.startswith("!정보"):
    userExistance, userRow = checkUser(message.author.name, message.author.id)
    level, exp, money, loss = userInfo(userRow)
    rank = getRank(userRow)
    userNum = chekcUserNum()
    print("------------------------------\n")
    embed = discord.Embed(title="유저 정보", description=user.name, color=0x62D0F6)
    embed.add_field(name="레벨", value=level)
    embed.add_field(name="경험치", value=str(exp) + "/" + str(level * level + 6 * level))
    embed.add_field(name="순위", value=str(rank) + "/" + str(userNum))
    embed.add_field(name="보유 자산", value=money, inline=False)

    await message.channel.send(embed=embed)

  if message.content.startswith("!도움말"):
    embed = discord.Embed(title="Code Bot", description="개발중", color=0x6E17E3)
    embed.add_field(name="─────────기능─────────", value="ㅤ", inline=False)
    embed.add_field(name=bot.command_prefix + "도움말", value="도움말을 봅니다", inline=False)
    embed.add_field(name="욕설 필터링", value="감지해서 메세지를 삭제하고 경고 메세지를 보냅니다", inline=False)
    embed.add_field(name="─────────놀이─────────", value="ㅤ", inline=False)
    embed.add_field(name=bot.command_prefix + "주사위", value="주사위를 굴려 봇과 대결합니다", inline=False)
    embed.add_field(name=bot.command_prefix + "보상", value="오늘의 보상입니다", inline=False)
    embed.add_field(name=bot.command_prefix + "도박 [돈]", value="(오류)도박 게임입니다", inline=False)
    embed.add_field(name="─────────정보─────────", value="ㅤ", inline=False)
    embed.add_field(name="오류 생겨서 고치는중", value="ㅤ", inline=False)
    embed.add_field(name=bot.command_prefix + "내정보", value="자신의 정보를 확인합니다", inline=False)
    embed.add_field(name=bot.command_prefix + "정보 [대상]", value="멘션한 [대상]의 정보를 확인합니다", inline=False)
    embed.add_field(name=bot.command_prefix + "송금 [대상] [돈]", value="멘션한 [대상]에게 [돈]을 보냅니다", inline=False)
    embed.add_field(name=bot.command_prefix + "랭킹", value="랭킹을 봅니다", inline=False)
    embed.add_field(name="─────────관리자 권한─────────", value="ㅤ", inline=False)
    embed.add_field(name=bot.command_prefix + "비밀", value="비밀입니다", inline=False)
    embed.add_field(name=bot.command_prefix + "청소 <int>", value="청소를 합니다", inline=False)
    embed.add_field(name=bot.command_prefix + "투표 <제목>/<내용>", value="공지를 합니다", inline=False)
    embed.add_field(name="─────────테스트─────────", value="ㅤ", inline=False)
    embed.add_field(name=bot.command_prefix + "테스트", value="테스트입니다", inline=False)
    embed.add_field(name=bot.command_prefix + "리소스팩", value="마인크래프트 리소스팩을 보여줍니다", inline=False)
    embed.add_field(name=bot.command_prefix + "임베드", value="임베드를 보여줍니다", inline=False)
    embed.add_field(name=bot.command_prefix + "시간", value="시간을 봅니다", inline=False)
    embed.add_field(name=bot.command_prefix + "마크", value="마크 무료로 설치하는법을 보여줍니다", inline=False)
    await message.channel.send(embed=embed)
    
  if message.content.startswith('!블랙리스트'):
    if message.author.guild_permissions.ban_members:
      try:
        target = message.mentions[0]
      except:
        await message.channel.send('유저가 지정되지 않았습니다')
        return

      j = message.content.split(" ")
      try:
        reason = j[2]
      except IndexError:
        reason = 'None'
      embed = discord.Embed(title='블랙리스트', description=f'{target}님이 {message.guild.name} 블랙리스트에 추가되었습니다.\n사유: {reason}', colour=discord.Colour.red())
      try:
        await target.send(embed=embed)
      except:
        pass
      embed = discord.Embed(title="블랙리스트 추가", color=0x000000)
      embed.add_field(name="닉네임", value=str(target), inline=False)
      embed.add_field(name="사유", value=str(reason), inline=False)
      await client.get_channel(int(gtid)).send(embed=embed)
      await target.ban(reason=reason)

data = ['10새', '10새기', '10새리', '10세리', '10쉐이', '10쉑', '10스', '10쌔'
    , '10쌔기', '10쎄', '10알', '10창', '10탱', '18것', '18넘', '18년', '18노', '18놈', '18뇬', '18럼'
    , '18롬', '18새', '18새끼', '18색', '18세끼', '18세리', '18섹', '18 쉑', '18스', '18아'
    , 'ㄱㅐ', 'ㄲㅏ', 'ㄲㅑ', 'ㄲㅣ', 'ㅅㅂㄹㅁ', 'ㅅㅐ', 'ㅆㅂㄹㅁ', 'ㅆㅍ', 'ㅆㅣ', 'ㅆ앙', 'ㅍㅏ'
    , '凸', ' 갈보', '갈보년', '강아지', '같은년', '같은뇬', '개같은', '개구라', '개년', '개놈', '개뇬', '개대중'
    , '개독', '개돼중', '개랄', '개보지', '개뻥', '개뿔', '개새', '개새기', '개새끼', '개새키', '개색기', '개색끼', '개색키', '개색히'
    , '개섀끼', '개세', '개세끼', '개세이', '개소리', '개쑈', '개쇳기', '개수작', '개쉐', '개쉐리', '개쉐이', '개쉑', '개쉽', '개스끼', '개시키', '개십새기'
    , ' 개십새끼', '개쐑', '개씹', '개아들', '개자슥', '개자지', '개접', '개좆', '개좌식', '개허접', '걔새', '걔수작', '걔시끼', '걔시키', '걔썌', '걸레'
    , '게색기', '게색끼', '광뇬', '구녕', '구라', '구멍', ' 그년', '그새끼', '냄비', '놈현', '뇬'
    , '눈깔', '뉘미럴', '니귀미', '니기미', '니미', '니미랄', '니미럴', '니미씹', '니아배', '니아베'
    , '니아비', '니어매', '니어메', '니어미', '닝기리', '닝기미', '대가리', '뎡신', '도라이', '돈놈'
    , '돌아 이', '돌은놈', '되질래', '뒈져', '뒈져라', '뒈진', '뒈진다', '뒈질', '뒤질래', '등신', '디져라'
    , '디진다', '디질래', '딩시', '따식', '때놈', '또라이', '똘아이', '똘아이', '뙈놈', '뙤놈', '뙨넘'
    , '뙨놈', '뚜쟁', '띠바', '띠발', '띠불', ' 띠팔', '메친넘', '메친놈', '미췬', '미췬', '미친', '미친넘', '미친년'
    , '미친놈', '미친새끼', '미친스까이', '미틴', '미틴넘', '미틴년', '미틴놈', '바랄년', '병자', '뱅마', '뱅신', '벼엉신'
    , '병쉰', '병신', '부랄', '부럴', '불알', '불할', '붕가', '붙어먹', '뷰웅', '븅', '븅신', '빌어먹', '빙시', '빙신'
    , '빠가', '빠구리', '빠굴', '빠큐', '뻐큐', '뻑큐', '뽁큐', '상넘이', '상놈을', '상놈의', '상놈이', '새갸', '새꺄'
    , '새끼', '새새끼', '새키', '색끼', '생쑈', '세갸', '세꺄', '세끼', '섹스', '쇼하네', '쉐', '쉐기', '쉐끼', '쉐리'
    , '쉐에기', '쉐키', '쉑', '쉣', '쉨', '쉬발', '쉬밸', '쉬벌', '쉬뻘', '쉬펄', '쉽알', '스패킹', '스팽', '시궁창'
    , '시끼', '시댕', '시뎅', '시랄', '시발', '시벌', '시부랄', '시부럴', '시부리', '시불', '시브랄', '시팍', '시팔'
    , '시펄', '신발끈', '심발끈', '심탱', '십8', '십라', '십새', '십새끼', '십세', '십쉐', '십쉐이', '십스키', '십쌔'
    , '십창', '십탱', '싶알', '싸가지', '싹아지', '쌉년', '쌍넘', '쌍년', '쌍놈', '쌍 뇬', '쌔끼', ' 쌕', '쌩쑈'
    , '쌴년', '썅', '썅년', '썅놈', '썡쇼', '써벌', '썩을년', '썩을놈', '쎄꺄', '쎄엑', '쒸벌', '쒸뻘', '쒸팔'
    , '쒸펄', '쓰바', '쓰박', '쓰발', '쓰벌', '쓰팔', '씁새', '씁얼', '씌파', '씨8', ' 씨끼', '씨댕', '씨뎅', '씨바', '씨바랄', '씨박', '씨발', '씨방', '씨방새'
    , '씨방세', '씨밸', '씨뱅', '씨벌', '씨벨', '씨봉', '씨봉알', '씨부랄', '씨부럴', '씨부렁', '씨부리', '씨불', '씨붕', '씨브랄', '씨빠', '씨빨', '씨뽀랄', '씨앙'
    , '씨파', '씨팍', '씨팔', '씨펄', '씸년', '씸뇬', '씸새끼', '씹같', '씹년', '씹뇬', '씹보지', '씹새', '씹새기', '씹새끼', '씹새리', '씹세', '씹쉐', '씹스키'
    , '씹쌔', '씹이', '씹자지', '씹질', '씹창', '씹탱', '씹퇭', '씹팔', '씹할', '씹헐', '아가리', '아갈', '아갈이', '아갈통', '아구창', '아구통', '아굴', '얌마'
    , '양넘', '양년', '양놈', '엄창', '엠병', '여물통', '염병', '엿같', '옘병', '옘빙', '오입', '왜년', '왜놈', '욤병', '육갑', '은년', '을년', '이년', '이새끼'
    , '이새키', '이스끼', '이스키', '임마', '자슥', '잡것', '잡넘', '잡년', '잡놈', '저년', '저새끼', '접년', '젖밥', '조까', '조까치', '조낸', '조또', '조랭'
    , '조빠', '조쟁이', '조지냐', '조진다', '조찐', '조질래', '존나', '존나게', '존니', '존만', '존만한', '좀물', '좁년', '좆', '좁밥', '좃까', '좃또', '좃만'
    , '좃밥', '좃이', '좃찐', '좆같', '좆까', '좆나', '좆또', '좆만', '좆밥', '좆이', '좆찐', '좇같', '좇이', '좌식', '주글', '주글래', '주데이', '주뎅', '주뎅이'
    , '주둥아리', '주둥이', '주접', '주접떨', '죽고잡', '죽을래', '죽통', '쥐랄', '쥐롤', '쥬디', '지랄', '지럴', '지롤', '지미랄', '짜식', '짜아식', '쪼다', '쫍빱', '찌랄'
    , '창녀', '캐년', '캐놈', '캐스끼', '캐스키', '캐시키', '탱구', '팔럼', '퍽큐', '호로', '호로놈', '호로새끼', '호로색', '호로쉑', '호로스까이'
    , '호로스키', '후라들', '후래자식', '후레', '후뢰', '씨ㅋ발', 'ㅆ1발', '씌발', '띠발', '띄발', '뛰발', '띠ㅋ발', '뉘뮈', 'abbo', 'abo'
    , 'abortion', 'abuse', 'addict', 'addicts', 'adult', 'africa', 'african', 'alla', 'allah', 'alligatorbait', 'amateur', 'american'
    , 'anal', 'analannie', 'analsex', 'angie', 'angry', 'anus', 'arab', 'arabs', 'areola', 'argie', 'aroused', 'arse', 'arsehole', 'asian'
    , 'ass', 'assassin', 'assassinate', 'assassination', 'assault', 'assbagger', 'assblaster', 'assclown', 'asscowboy', 'asses', 'assfuck'
    , 'assfucker', 'asshat', 'asshole', 'assholes', 'asshore', 'assjockey', 'asskiss', 'asskisser', 'assklown', 'asslick', 'asslicker', 'asslover'
    , 'assman', 'assmonkey', 'assmunch', 'assmuncher', 'asspacker', 'asspirate', 'asspuppies', 'assranger', 'asswhore', 'asswipe', 'athletesfoot'
    , 'attack', 'australian', 'backdoor', 'backdoorman', 'backseat', 'badfuck', 'balllicker', 'balls', 'ballsack', 'banging', 'baptist', 'barelylegal'
    , 'barf', 'barface', 'barfface', 'bast', 'bastard', 'bazongas', 'bazooms', 'beaner', 'beast', 'beastality', 'beastial', 'beastiality', 'beatoff'
    , 'beat-off', 'beatyourmeat', 'beaver', 'bestial', 'bestiality', 'bi', 'biatch', 'bicurious', 'bigass', 'bigbastard', 'bigbutt', 'bigger', 'bisexual'
    , 'bi-sexual', 'bitch', 'bitcher', 'bitches', 'bitchez', 'bitchin', 'bitching', 'bitchslap', 'bitchy', 'biteme', 'black', 'blackman', 'blackout'
    , 'blacks', 'blind', 'blow', 'blowjob', 'boang', 'bogan', 'bohunk', 'bollick', 'bollock', 'bomb', 'bombers', 'bombing', 'bombs', 'bomd', 'bondage'
    , 'boner', 'bong', 'boob', 'boobies', 'boobs', 'booby', 'boody', 'boom', 'boong', 'boonga', 'boonie', 'booty', 'bootycall', 'bountybar', 'bra', 'brea5t'
    , 'breast', 'breastjob', 'breastlover', 'breastman', 'brothel', 'bugger', 'buggered', 'buggery', 'bullcrap', 'bulldike', 'bulldyke', 'bullshit'
    , 'bumblefuck', 'bumfuck', 'bunga', 'bunghole', 'buried', 'burn', 'butchbabes', 'butchdike', 'butchdyke', 'butt', 'buttbang', 'butt-bang', 'buttface'
    , 'buttfuck', 'butt-fuck', 'buttfucker', 'butt-fucker', 'buttfuckers', 'butt-fuckers', 'butthead', 'buttman', 'buttmunch', 'buttmuncher', 'buttpirate'
    , 'buttplug', 'buttstain', 'byatch', 'cacker', 'cameljockey', 'cameltoe', 'canadian', 'cancer', 'carpetmuncher', 'carruth', 'catholic', 'catholics'
    , 'cemetery', 'chav', 'cherrypopper', 'chickslick', "children's", 'chin', 'chinaman', 'chinamen', 'chinese', 'chink', 'chinky', 'choad', 'chode'
    , 'christ', 'christian', 'church', 'cigarette', 'cigs', 'clamdigger', 'clamdiver', 'clit', 'clitoris', 'clogwog', 'cocaine', 'cock', 'cockblock'
    , 'cockblocker', 'cockcowboy', 'cockfight', 'cockhead', 'cockknob', 'cocklicker', 'cocklover', 'cocknob', 'cockqueen', 'cockrider', 'cocksman'
    , 'cocksmith', 'cocksmoker', 'cocksucer', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocktail', 'cocktease', 'cocky', 'cohee'
    , 'coitus', 'color', 'colored', 'coloured', 'commie', 'communist', 'condom', 'conservative', 'conspiracy', 'coolie', 'cooly', 'coon', 'coondog'
    , 'copulate', 'cornhole', 'corruption', 'cra5h', 'crabs', 'crack', 'crackpipe', 'crackwhore', 'crack-whore', 'crap', 'crapola', 'crapper'
    , 'crappy', 'crash', 'creamy', 'crime', 'crimes', 'criminal', 'criminals', 'crotch', 'crotchjockey', 'crotchmonkey', 'crotchrot', 'cum'
    , 'cumbubble', 'cumfest', 'cumjockey', 'cumm', 'cummer', 'cumming', 'cumquat', 'cumqueen', 'cumshot', 'cunilingus', 'cunillingus', 'cunn'
    , 'cunnilingus', 'cunntt', 'cunt', 'cunteyed', 'cuntfuck', 'cuntfucker', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cuntsucker', 'cybersex'
    , 'cyberslimer', 'dago', 'dahmer', 'dammit', 'damn', 'damnation', 'damnit', 'darkie', 'darky', 'datnigga', 'dead', 'deapthroat', 'death'
    , 'deepthroat', 'defecate', 'dego', 'demon', 'deposit', 'desire', 'destroy', 'deth', 'devil', 'devilworshipper', 'dick', 'dickbrain'
    , 'dickforbrains', 'dickhead', 'dickless', 'dicklick', 'dicklicker', 'dickman', 'dickwad', 'dickweed', 'diddle', 'die', 'died', 'dies', 'dike'
    , 'dildo', 'dingleberry', 'dink', 'dipshit', 'dipstick', 'dirty', 'disease', 'diseases', 'disturbed', 'dive', 'dix', 'dixiedike'
    , 'dixiedyke', 'doggiestyle', 'doggystyle', 'dong', 'doodoo', 'doo-doo', 'doom', 'dope', 'dragqueen', 'dragqween', 'dripdick', 'drug'
    , 'drunk', 'drunken', 'dumb', 'dumbass', 'dumbbitch', 'dumbfuck', 'dyefly', 'dyke', 'easyslut', 'eatballs', 'eatme', 'eatpussy'
    , 'ecstacy', 'ejaculate', 'ejaculated', 'ejaculating', 'ejaculation', 'enema', 'enemy', 'erect', 'erection', 'ero', 'escort', 'ethiopian'
    , 'ethnic', 'european', 'evl', 'excrement', 'execute', 'executed', 'execution', 'executioner', 'explosion', 'facefucker', 'faeces'
    , 'fag', 'fagging', 'faggot', 'fagot', 'failed', 'failure', 'fairies', 'fairy', 'faith', 'fannyfucker', 'fart', 'farted', 'farting', 'farty'
    , 'fastfuck', 'fat', 'fatah', 'fatass', 'fatfuck', 'fatfucker', 'fatso', 'fckcum', 'fear', 'feces', 'felatio', 'felch', 'felcher', 'felching'
    , 'fellatio', 'feltch', 'feltcher', 'feltching', 'fetish', 'fight', 'filipina', 'filipino', 'fingerfood', 'fingerfuck', 'fingerfucked'
    , 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fire', 'firing', 'fister', 'fistfuck', 'fistfucked', 'fistfucker'
    , 'fistfucking', 'fisting', 'flange', 'flasher', 'flatulence', 'floo', 'flydie', 'flydye', 'fok', 'fondle', 'footaction'
    , 'footfuck', 'footfucker', 'footlicker', 'footstar', 'fore', 'foreskin', 'forni', 'fornicate', 'foursome', 'fourtwenty'
    , 'fraud', 'freakfuck', 'freakyfucker', 'freefuck', 'fu', 'fubar', 'fuc', 'fucck', 'fuck', 'fucka', 'fuckable', 'fuckbag'
    , 'fuckbuddy', 'fucked', 'fuckedup', 'fucker', 'fuckers', 'fuckface', 'fuckfest', 'fuckfreak', 'fuckfriend', 'fuckhead'
    , 'fuckher', 'fuckin', 'fuckina', 'fucking', 'fuckingbitch', 'fuckinnuts', 'fuckinright', 'fuckit', 'fuckknob', 'fuckme'
    , 'fuckmehard', 'fuckmonkey', 'fuckoff', 'fuckpig', 'fucks', 'fucktard', 'fuckwhore', 'fuckyou', 'fudgepacker', 'fugly'
    , 'fuk', 'fuks', 'funeral', 'funfuck', 'fungus', 'fuuck', 'gangbang', 'gangbanged', 'gangbanger', 'gangsta', 'gatorbait'
    , 'gay', 'gaymuthafuckinwhore', 'gaysex', 'geez', 'geezer', 'geni', 'genital', 'german', 'getiton', 'gin', 'ginzo', 'gipp'
    , 'girls', 'givehead', 'glazeddonut', 'gob', 'god', 'godammit', 'goddamit', 'goddammit', 'goddamn', 'goddamned', 'goddamnes', 'goddamnit'
    , 'goddamnmuthafucker', 'goldenshower', 'gonorrehea', 'gonzagas', 'gook', 'gotohell', 'goy', 'goyim', 'greaseball', 'gringo'
    , 'groe', 'gross', 'grostulation', 'gubba', 'gummer', 'gun', 'gyp', 'gypo', 'gypp', 'gyppie', 'gyppo', 'gyppy', 'hamas', 'handjob', 'hapa', 'harder', 'hardon', 'harem', 'headfuck', 'headlights', 'hebe', 'heeb', 'hell', 'henhouse', 'heroin', 'herpes', 'heterosexual', 'hijack', 'hijacker', 'hijacking'
    , 'hillbillies', 'hindoo', 'hiscock', 'hitler', 'hitlerism', 'hitlerist', 'hiv', 'ho', 'hobo', 'hodgie', 'hoes', 'hole', 'holestuffer', 'homicide', 'homo', 'homobangers', 'homosexual', 'honger', 'honk', 'honkers', 'honkey', 'honky', 'hook', 'hooker', 'hookers', 'hooters', 'hore'
    , 'hork', 'horn', 'horney', 'horniest', 'horny', 'horseshit', 'hosejob', 'hoser', 'hostage', 'hotdamn', 'hotpussy', 'hottotrot', 'hummer', 'husky', 'hussy', 'hustler', 'hymen', 'hymie', 'iblowu', 'idiot', 'ikey', 'illegal', 'incest', 'insest', 'intercourse', 'interracial', 'intheass', 'inthebuff', 'israel', 'israeli', "israel's", 'italiano', 'itch', 'jackass', 'jackoff', 'jackshit', 'jacktheripper', 'jade', 'jap', 'japanese', 'japcrap', 'jebus', 'jeez', 'jerkoff', 'jesus', 'jesuschrist', 'jew', 'jewish', 'jiga', 'jigaboo', 'jigg', 'jigga', 'jiggabo', 'jigger', 'jiggy', 'jihad', 'jijjiboo', 'jimfish', 'jism', 'jiz', 'jizim', 'jizjuice', 'jizm', 'jizz', 'jizzim', 'jizzum', 'joint', 'juggalo', 'jugs', 'junglebunny', 'kaffer', 'kaffir', 'kaffre', 'kafir', 'kanake', 'kid', 'kigger', 'kike', 'kill', 'killed', 'killer', 'killing', 'kills', 'kink', 'kinky', 'kissass', 'kkk', 'knife', 'knockers', 'kock', 'kondum', 'koon', 'kotex', 'krap', 'krappy', 'kraut', 'kum', 'kumbubble', 'kumbullbe', 'kummer', 'kumming', 'kumquat', 'kums', 'kunilingus', 'kunnilingus', 'kunt', 'ky', 'kyke', 'lactate', 'laid', 'lapdance', 'latin', 'lesbain', 'lesbayn', 'lesbian', 'lesbin', 'lesbo', 'lez', 'lezbe', 'lezbefriends', 'lezbo', 'lezz', 'lezzo', 'liberal', 'libido', 'licker', 'lickme', 'lies', 'limey', 'limpdick', 'limy', 'lingerie', 'liquor', 'livesex', 'loadedgun', 'lolita', 'looser', 'loser', 'lotion', 'lovebone', 'lovegoo', 'lovegun', 'lovejuice', 'lovemuscle', 'lovepistol', 'loverocket', 'lowlife', 'lsd', 'lubejob', 'lucifer', 'luckycammeltoe', 'lugan', 'lynch', 'macaca', 'mad', 'mafia', 'magicwand', 'mams', 'manhater', 'manpaste', 'marijuana', 'mastabate', 'mastabater', 'masterbate', 'masterblaster', 'mastrabator', 'masturbate', 'masturbating', 'mattressprincess', 'meatbeatter', 'meatrack', 'meth', 'mexican', 'mgger', 'mggor', 'mickeyfinn', 'mideast', 'milf', 'minority', 'mockey', 'mockie', 'mocky', 'mofo', 'moky', 'moles', 'molest', 'molestation', 'molester', 'molestor', 'moneyshot', 'mooncricket', 'mormon', 'moron', 'moslem', 'mosshead', 'mothafuck', 'mothafucka', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckin', 'mothafucking', 'mothafuckings', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherlovebone', 'muff', 'muffdive', 'muffdiver', 'muffindiver', 'mufflikcer', 'mulatto', 'muncher', 'munt', 'murder', 'murderer', 'muslim', 'naked', 'narcotic', 'nasty', 'nastybitch', 'nastyho', 'nastyslut', 'nastywhore', 'nazi', 'necro', 'negro', 'negroes', 'negroid', "negro's", 'nig', 'niger', 'nigerian', 'nigerians', 'nigg', 'nigga', 'niggah', 'niggaracci', 'niggard', 'niggarded', 'niggarding', 'niggardliness', "niggardliness's", 'niggardly', 'niggards', "niggard's", 'niggaz', 'nigger', 'niggerhead', 'niggerhole', 'niggers', "nigger's", 'niggle', 'niggled', 'niggles', 'niggling', 'nigglings', 'niggor', 'niggur', 'niglet', 'nignog', 'nigr', 'nigra', 'nigre', 'nip', 'nipple', 'nipplering', 'nittit', 'nlgger', 'nlggor', 'nofuckingway', 'nook', 'nookey', 'nookie', 'noonan', 'nooner', 'nude', 'nudger', 'nuke', 'nutfucker', 'nymph', 'ontherag', 'oral', 'orga', 'orgasim', 'orgasm', 'orgies', 'orgy', 'osama', 'paki', 'palesimian', 'palestinian', 'pansies', 'pansy', 'panti', 'panties', 'payo', 'pearlnecklace', 'peck', 'pecker', 'peckerwood', 'pee', 'peehole', 'pee-pee', 'peepshow', 'peepshpw', 'pendy', 'penetration', 'peni5', 'penile', 'penis', 'penises', 'penthouse', 'period', 'perv', 'phonesex', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phungky', 'phuq', 'pi55', 'picaninny', 'piccaninny', 'pickaninny', 'piker', 'pikey', 'piky', 'pimp', 'pimped', 'pimper', 'pimpjuic', 'pimpjuice', 'pimpsimp', 'pindick', 'piss', 'pissed', 'pisser', 'pisses', 'pisshead', 'pissin', 'pissing', 'pissoff', 'pistol', 'pixie', 'pixy', 'playboy', 'playgirl', 'pocha', 'pocho', 'pocketpool', 'pohm', 'polack', 'pom', 'pommie', 'pommy', 'poo', 'poon', 'poontang', 'poop', 'pooper', 'pooperscooper', 'pooping', 'poorwhitetrash', 'popimp', 'porchmonkey', 'porn', 'pornflick', 'pornking', 'porno', 'pornography', 'pornprincess', 'pot', 'poverty', 'premature', 'pric', 'prick', 'prickhead', 'primetime', 'propaganda', 'pros', 'prostitute', 'protestant', 'pu55i', 'pu55y', 'pube', 'pubic', 'pubiclice', 'pud', 'pudboy', 'pudd', 'puddboy', 'puke', 'puntang', 'purinapricness', 'puss', 'pussie', 'pussies', 'pussy', 'pussycat', 'pussyeater', 'pussyfucker', 'pussylicker', 'pussylips', 'pussylover', 'pussypounder', 'pusy', 'quashie', 'queef', 'queer', 'quickie', 'quim', 'ra8s', 'rabbi', 'racial', 'racist', 'radical', 'radicals', 'raghead', 'randy', 'rape', 'raped', 'raper', 'rapist', 'rearend', 'rearentry', 'rectum', 'redlight', 'redneck', 'reefer', 'reestie', 'refugee', 'reject', 'remains', 'rentafuck', 'republican', 'rere', 'retard', 'retarded', 'ribbed', 'rigger', 'rimjob', 'rimming', 'roach', 'robber', 'roundeye', 'rump', 'russki', 'russkie', 'sadis', 'sadom', 'samckdaddy', 'sandm', 'sandnigger', 'satan', 'scag', 'scallywag', 'scat', 'schlong', 'screw', 'screwyou', 'scrotum', 'scum', 'semen', 'seppo', 'servant', 'sex', 'sexed', 'sexfarm', 'sexhound', 'sexhouse', 'sexing', 'sexkitten', 'sexpot', 'sexslave', 'sextogo', 'sextoy', 'sextoys', 'sexual', 'sexually', 'sexwhore', 'sexy', 'sexymoma', 'sexy-slim', 'shag', 'shaggin', 'shagging', 'shat', 'shav', 'shawtypimp', 'sheeney', 'shhit', 'shinola', 'shit', 'shitcan', 'shitdick', 'shite', 'shiteater', 'shited', 'shitface', 'shitfaced', 'shitfit', 'shitforbrains', 'shitfuck', 'shitfucker', 'shitfull', 'shithapens', 'shithappens', 'shithead', 'shithouse', 'shiting', 'shitlist', 'shitola', 'shitoutofluck', 'shits', 'shitstain', 'shitted', 'shitter', 'shitting', 'shitty', 'shortfuck', 'sissy', 'sixtyniner', 'skank', 'skankbitch', 'skankfuck', 'skankwhore', 'skanky', 'skankybitch', 'skankywhore', 'skinflute', 'skum', 'skumbag', 'slant', 'slanteye', 'slapper', 'slav', 'slave', 'slavedriver', 'sleezebag', 'sleezeball', 'slideitin', 'slime', 'slimeball', 'slimebucket', 'slopehead', 'slopey', 'slopy', 'slut', 'sluts', 'slutt', 'slutting', 'slutty', 'slutwear', 'slutwhore', 'smack', 'smackthemonkey', 'smut', 'snatch', 'snatchpatch', 'snigger', 'sniggered', 'sniggering', 'sniggers', "snigger's", 'sniper', 'snot', 'snowback', 'snownigger', 'sob', 'sodom', 'sodomise', 'sodomite', 'sodomize', 'sodomy', 'sonofabitch', 'sonofbitch', 'sooty', 'soviet', 'spaghettibender', 'spaghettinigger', 'spank', 'spankthemonkey', 'sperm', 'spermacide', 'spermbag', 'spermhearder', 'spermherder', 'spic', 'spick', 'spig', 'spigotty', 'spik', 'spit', 'spitter', 'splittail', 'spooge', 'spreadeagle', 'spunk', 'spunky', 'squaw', 'stagg', 'stiffy', 'strapon', 'stringer', 'stripclub', 'stroke', 'stroking', 'stupid', 'stupidfuck', 'stupidfucker', 'suck', 'suckdick', 'sucker', 'suckme', 'suckmyass', 'suckmydick', 'suckmytit', 'suckoff', 'suicide', 'swallow', 'swallower', 'swalow', 'swastika', 'sweetness', 'syphilis', 'taboo', 'taff', 'tampon', 'tang', 'tantra', 'tarbaby', 'tard', 'teat', 'terror', 'terrorist', 'teste', 'testicle', 'testicles', 'thicklips', 'thirdeye', 'thirdleg', 'threesome', 'threeway', 'timbernigger', 'tinkle', 'tit', 'titbitnipply', 'titfuck', 'titfucker', 'titfuckin', 'titjob', 'titlicker', 'titlover', 'tits', 'tittie', 'titties', 'titty', 'tnt', 'tongethruster', 'tongue', 'tonguethrust', 'tonguetramp', 'tortur', 'torture', 'tosser', 'towelhead', 'trailertrash', 'tramp', 'trannie', 'tranny', 'transexual', 'transsexual', 'transvestite', 'triplex', 'trisexual', 'trojan', 'trots'
    , 'tuckahoe', 'tunneloflove', 'turd', 'turnon', 'twat', 'twink', 'twinkie', 'twobitwhore', 'uck', 'uk', 'unfuckable'
    , 'upskirt', 'uptheass', 'upthebutt', 'urinary', 'urinate', 'urine', 'usama', 'uterus', 'vagina', 'vaginal', 'vatican'
    , 'vibr', 'vibrater', 'vibrator', 'vietcong', 'violence', 'virgin', 'virginbreaker', 'vomit', 'vulva', 'wab', 'wank'
    , 'wanker', 'wanking', 'waysted', 'weapon', 'weenie', 'weewee', 'welcher', 'welfare', 'wetb', 'wetback'
    , 'wetspot', 'whacker', 'whash', 'whigger', 'whiskey', 'whiskeydick', 'whiskydick', 'whit', 'whitenigger'
    , 'whites', 'whitetrash', 'whitey', 'whiz', 'whop', 'whore', 'whorefucker', 'whorehouse', 'wigger', 'willie'
    , 'williewanker', 'willy', 'wn', 'wog', 'wop', 'wtf', 'wuss', 'wuzzie', 'xtc', 'xxx', 'yankee', 'yellowman'
    , 'zigabo', 'zipperhead', 'douche', 'lmfao', 'lmao', "니애미", "음식물쓰레기 보다 못한", "지랄마", "ㅄ"]

def messagecheck(message:str):
  for i in data:
    if i in message.lower():
      return True
  return False
