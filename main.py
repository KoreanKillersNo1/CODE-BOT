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
from ydl import *
from game import *
from user import *
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
  print(client.user.name)
  print('성공적으로 봇이 시작되었습니다.')
  print('코드 봇 이제 사용 하셔도 좋습니다')
  print('현재 온라인 멤버 수 : {online}명')
  game = discord.Game('코드 봇ㅣ!도움말ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
  await client.change_presence(status=discord.Status.online, activity=game)

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
    , '뙨놈', '뚜쟁', '띠바', '띠발', '띠불', ' 띠팔', '메친넘', '메친놈', '미췬', '미췬', '미친넘', '미친년'
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

def bool(message:str):
  for i in data:
    if i in message.lower():
        return True
    return False

@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕")

@bot.command()
async def 주사위(ctx):
    result, _color, bot1, bot2, user1, user2, a, b = dice()

    embed = discord.Embed(title = "주사위 게임 결과", description = None, color = _color)
    embed.add_field(name = "Super Bot의 숫자 " + bot1 + "+" + bot2, value = ":game_die: " + a, inline = False)
    embed.add_field(name = ctx.author.name+"의 숫자 " + user1 + "+" + user2, value = ":game_die: " + b, inline = False)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)

@bot.command()
async def 도박(ctx, money):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    win = gamble()
    result = ""
    betting = 0
    _color = 0x000000
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        cur_money = getMoney(ctx.author.name, userRow)

        if money == "올인":
            betting = cur_money
            if win:
                result = "성공"
                _color = 0x00ff56
                print(result)

                modifyMoney(ctx.author.name, userRow, int(0.5*betting))

            else:
                result = "실패"
                _color = 0xFF0000
                print(result)

                modifyMoney(ctx.author.name, userRow, -int(betting))
                addLoss(ctx.author.name, userRow, int(betting))

            embed = discord.Embed(title = "도박 결과", description = result, color = _color)
            embed.add_field(name = "배팅금액", value = betting, inline = False)
            embed.add_field(name = "현재 자산", value = getMoney(ctx.author.name, userRow), inline = False)

            await ctx.send(embed=embed)
            
        elif int(money) >= 10:
            if cur_money >= int(money):
                betting = int(money)
                print("배팅금액: ", betting)
                print("")

                if win:
                    result = "성공"
                    _color = 0x00ff56
                    print(result)

                    modifyMoney(ctx.author.name, userRow, int(0.5*betting))

                else:
                    result = "실패"
                    _color = 0xFF0000
                    print(result)

                    modifyMoney(ctx.author.name, userRow, -int(betting))
                    addLoss(ctx.author.name, userRow, int(betting))

                embed = discord.Embed(title = "도박 결과", description = result, color = _color)
                embed.add_field(name = "배팅금액", value = betting, inline = False)
                embed.add_field(name = "현재 자산", value = getMoney(ctx.author.name, userRow), inline = False)

                await ctx.send(embed=embed)

            else:
                print("돈이 부족합니다.")
                print("배팅금액: ", money, " | 현재자산: ", cur_money)
                await ctx.send("돈이 부족합니다. 현재자산: " + str(cur_money))
        else:
            print("배팅금액", money, "가 10보다 작습니다.")
            await ctx.send("10원 이상만 배팅 가능합니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        await ctx.send("도박은 회원가입 후 이용 가능합니다.")

    print("------------------------------\n")

@bot.command()
async def 랭킹(ctx):
    rank = ranking()
    embed = discord.Embed(title = "레벨 랭킹", description = None, color = 0x4A44FF)

    for i in range(0,len(rank)):
        if i%2 == 0:
            name = rank[i]
            lvl = rank[i+1]
            embed.add_field(name = str(int(i/2+1))+"위 "+name, value ="레벨: "+str(lvl), inline=False)

    await ctx.send(embed=embed) 

@bot.command()
async def 회원가입(ctx):
    print("회원가입이 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if userExistance:
        print("DB에서 ", ctx.author.name, "을 찾았습니다.")
        print("------------------------------\n")
        await ctx.send("이미 가입하셨습니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("")

        Signup(ctx.author.name, ctx.author.id)

        print("회원가입이 완료되었습니다.")
        print("------------------------------\n")
        await ctx.send("회원가입이 완료되었습니다.")

@bot.command()
async def 탈퇴(ctx):
    print("탈퇴가 가능한지 확인합니다.")
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
    if userExistance:
        DeleteAccount(userRow)
        print("탈퇴가 완료되었습니다.")
        print("------------------------------\n")

        await ctx.send("탈퇴가 완료되었습니다.")
    else:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")

        await ctx.send("등록되지 않은 사용자입니다.")

@bot.command()
async def 내정보(ctx):
    userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)

    if not userExistance:
        print("DB에서 ", ctx.author.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 자신의 정보를 확인할 수 있습니다.")
    else:
        userExistance, userRow = checkUser(ctx.author.name, ctx.author.id)
        level, exp, money, loss = userInfo(userRow)
        rank = getRank(userRow)
        data = datetime.datetime.utcfromtimestamp(((int(ctx.author.id) >> 22) + 1420070400000) / 1000)
        userNum = checkUserNum()
        expToUP = level * level + 6 * level
        boxes = int(exp / expToUP * 20)
        print("------------------------------\n")
        embed = discord.Embed(title="!유저 정보", description=ctx.author.name, color=0x62D0F6)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=ctx.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=ctx.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(data.year) + "년" + str(data.month) + "월" + str(data.day) + "일",inline=True)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="레벨", value=level)
        embed.add_field(name="순위", value=str(rank) + "/" + str(userNum))
        embed.add_field(name="XP: " + str(exp) + "/" + str(expToUP),value=boxes * ":blue_square:" + (20 - boxes) * ":white_large_square:", inline=False)
        embed.add_field(name="보유 자산", value=money, inline=False)

        await ctx.send(embed=embed)


@bot.command()
async def 정보(ctx, user: discord.User):
  userExistance, userRow = checkUser(user.name, user.id)

  if not userExistance:
    print("DB에서 ", user.name, "을 찾을 수 없습니다")
    print("------------------------------\n")
    await ctx.send(user.name  + " 은(는) 등록되지 않은 사용자입니다.")
  else:
    level, exp, money, loss = userInfo(userRow)
    rank = getRank(userRow)
    userNum = chekcUserNum()
    print("------------------------------\n")
    embed = discord.Embed(title="유저 정보", description = user.name, color = 0x62D0F6)
    embed.add_field(name = "레벨", value = level)
    embed.add_field(name = "경험치", value = str(exp) + "/" + str(level*level + 6*level))
    embed.add_field(name = "순위", value = str(rank) + "/" + str(userNum))
    embed.add_field(name = "보유 자산", value = money, inline = False)
    embed.add_field(name = "도박으로 날린 돈", value = loss, inline = False)

    await ctx.send(embed=embed)


@bot.command()
async def 송금(ctx, user: discord.User, money):
    print("송금이 가능한지 확인합니다.")
    senderExistance, senderRow = checkUser(ctx.author.name, ctx.author.id)
    receiverExistance, receiverRow = checkUser(user.name, user.id)

    if not senderExistance:
        print("DB에서", ctx.author.name, "을 찾을수 없습니다")
        print("------------------------------\n")
        await ctx.send("회원가입 후 송금이 가능합니다.")
    elif not receiverExistance:
        print("DB에서 ", user.name, "을 찾을 수 없습니다")
        print("------------------------------\n")
        await ctx.send(user.name  + " 은(는) 등록되지 않은 사용자입니다.")
    else:
        print("송금하려는 돈: ", money)

        s_money = getMoney(ctx.author.name, senderRow)
        r_money = getMoney(user.name, receiverRow)

        if s_money >= int(money) and int(money) != 0:
            print("돈이 충분하므로 송금을 진행합니다.")
            print("")

            remit(ctx.author.name, senderRow, user.name, receiverRow, money)

            print("송금이 완료되었습니다. 결과를 전송합니다.")

            embed = discord.Embed(title="송금 완료", description = "송금된 돈: " + money, color = 0x77ff00)
            embed.add_field(name = "보낸 사람: " + ctx.author.name, value = "현재 자산: " + str(getMoney(ctx.author.name, senderRow)))
            embed.add_field(name = "→", value = ":moneybag:")
            embed.add_field(name="받은 사람: " + user.name, value="현재 자산: " + str(getMoney(user.name, receiverRow)))
                    
            await ctx.send(embed=embed)
        elif int(money) == 0:
            await ctx.send("0원을 보낼 필요는 없죠")
        else:
            print("돈이 충분하지 않습니다.")
            print("송금하려는 돈: ", money)
            print("현재 자산: ", s_money)
            await ctx.send("돈이 충분하지 않습니다. 현재 자산: " + str(s_money))

        print("------------------------------\n")


@bot.command()
async def reset(ctx):
    resetData()

@bot.command()
async def add(ctx, money):
    user, row = checkUser(ctx.author.name, ctx.author.id)
    addMoney(row, int(money))
    print("money")

@bot.command()
async def exp(ctx, exp):
    user, row = checkUser(ctx.author.name, ctx.author.id)
    addExp(row, int(exp))
    print("exp")

@bot.command()
async def lvl(ctx, lvl):
    user, row = checkUser(ctx.author.name, ctx.author.id)
    adjustlvl(row, int(lvl))
    print("lvl")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "!reset":
        await bot.process_commands(message)
        return
    else:
        userExistance, userRow = checkUser(message.author.name, message.author.id)
        channel = message.channel
        if userExistance:
            levelUp, lvl = levelupCheck(userRow)
            if levelUp:
                print(message.author, "가 레벨업 했습니다")
                print("")
                embed = discord.Embed(title = "레벨업", description = None, color = 0x00A260)
                embed.set_footer(text = message.author.name + "이 " + str(lvl) + "레벨 달성!")
                await channel.send(embed=embed)
            else:
                modifyExp(userRow, 1)
                print("------------------------------\n")

        await bot.process_commands(message)
    
    if message.content.startswith("!도움말"):
        embed = discord.Embed(title="Code Bot", description="개발중", color=0x6E17E3)
        embed.add_field(name="─────────기능─────────", value="ㅤ", inline=False)
        embed.add_field(name=bot.command_prefix + "도움말", value="도움말을 봅니다", inline=False)
        embed.add_field(name="─────────놀이─────────", value="ㅤ", inline=False)
        embed.add_field(name=bot.command_prefix + "주사위", value="주사위를 굴려 봇과 대결합니다", inline=False)
        embed.add_field(name=bot.command_prefix + "도박 [돈]", value="(오류)도박 게임입니다", inline=False)
        embed.add_field(name="─────────정보─────────", value="ㅤ", inline=False)
        embed.add_field(name=bot.command_prefix + "내정보", value="자신의 정보를 확인합니다", inline=False)
        embed.add_field(name=bot.command_prefix + "정보 [대상]", value="멘션한 [대상]의 정보를 확인합니다", inline=False)
        embed.add_field(name=bot.command_prefix + "송금 [대상] [돈]", value="멘션한 [대상]에게 [돈]을 보냅니다", inline=False)
        embed.add_field(name=bot.command_prefix + "랭킹", value="랭킹을 봅니다", inline=False)
        embed.add_field(name="─────────관리자 권한─────────", value="ㅤ", inline=False)
        embed.add_field(name="─────────테스트─────────", value="ㅤ", inline=False)
        await message.channel.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다. !도움을 입력하여 명령어를 확인하세요.")

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
