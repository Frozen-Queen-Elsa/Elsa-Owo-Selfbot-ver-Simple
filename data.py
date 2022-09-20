from version import Version
from requests import get
from color import color
from menu import UI
from time import sleep
from re import findall
from inputimeout import TimeoutOccurred, inputimeout
import json
ui = UI()
class data:
	def __init__(self):
		self.commands=[
			"hunt",
			"hunt",
			"battle"
			]
		self.wbm = [13,18]
		self.OwOID = '408785106942164992'
		self.totalcmd = 0
		self.totaltext = 0
		self.username=""
		self.userid = ""
		self.checknogem=False
		self.stopped = False
		self.version = int(''.join(map(str, Version)))
		self.wait_time_daily = 60
		self.channel2 = []

		#OCF
		self.checknocash=False
		self.totalwon=0
		self.totallost=0
		self.checknocash=False
		self.countcfmaxlost=0
		self.countosmaxlost=0
		#Gems
		self.checkgemtime=0
		self.checkusegem = 0
		self.skipcheckgem=0
		#link captcha
		self.captchalink='https://discord.com/oauth2/authorize?response_type=code&redirect_uri=https%3A%2F%2Fowobot.com%2Fapi%2Fauth%2Fdiscord%2Fredirect&scope=identify%20guilds&client_id=408785106942164992'
		self.votelink='https://discord.com/login?redirect_to=%2Foauth2%2Fauthorize%3Fscope%3Didentify%2520guilds%2520email%26redirect_uri%3Dhttps%253A%252F%252Ftop.gg%252Flogin%252Fcallback%26response_type%3Dcode%26client_id%3D422087909634736160%26state%3DL2JvdC80MDg3ODUxMDY5NDIxNjQ5OTIvdm90ZQ%3D%3D'
		self.js='function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
  
		with open('settings.json', "r") as file:
			data = json.load(file)
			self.token = data["token"]
			self.channel = data["channel"]
			self.channelspam=data['channelspam']
			self.gm = data["gm"]
			self.wcrate = data["wcrate"]
			self.lbox = data["lbox"]
			self.usegem = data["usegem"]
			self.sm = data["sm"]
			self.pm = data["pm"]
			self.prayid = data["prayid"]
			self.em = data["em"]
			self.prefix = data["prefix"]
			self.allowedid = data["allowedid"]
			self.webhook = data["webhook"]
			self.webhookping = data["webhookping"]
			self.daily = data["daily"]
			self.stop = data["stop"]
			self.change = data['change']			
			self.sell = data['sell']
			self.solve = data['solve']
			#self.sound = data['sound']
			self.rhunt = data['rhunt']
			self.rbattle = data['rbattle']
			self.rowo = data['rowo']
			self.rbuyring = data['rbuyring']
			#OCF
			self.casinom =data['casinom']
			self.cfm =data['cfm']
			self.cfbet = int(data["cfbet"])
			self.current_cfbet = self.cfbet
			self.cfrate = int(data["cfrate"])
			self.osm =data['osm']
			self.osbet = int(data["osbet"])
			self.current_osbet = self.osbet
			self.osrate = int(data["osrate"])
			self.maxbet = data["maxbet"]
			self.channelocf =data["channelocf"]
			self.api=data['api']
		self.tokenbackup=self.token
		




a = data()
#a.check()
