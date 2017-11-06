#coding:utf-8
#Author:se55i0n

import re
import os
import sys
import sqlite3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#colour
W = '\033[0m'
G = '\033[1;32m'
R = '\033[1;31m'
O = '\033[1;33m'
B = '\033[1;34m'

#User-Agent
agent = {'UserAgent':'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))'}

#re
rtitle   = re.compile(r'title="(.*)"')
rheader  = re.compile(r'header="(.*)"')
rbody    = re.compile(r'body="(.*)"')
rbracket = re.compile(r'\((.*)\)')

path = os.path.dirname(os.path.abspath(__file__))

#中文乱码及ssl错误
def setting():
	reload(sys)
	sys.setdefaultencoding('utf-8')
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#banner
def banner():
	banner = '''
 _       __     __    _____
| |     / /__  / /_  / __(_)___  ____ ____  _____
| | /| / / _ \/ __ \/ /_/ / __ \/ __ `/ _ \/ ___/
| |/ |/ /  __/ /_/ / __/ / / / / /_/ /  __/ /
|__/|__/\___/_.___/_/ /_/_/ /_/\__, /\___/_/
                              /____/
	'''
	print B + banner + W
	print '-'*54

def check(_id):
	with sqlite3.connect(path +'/web.db') as conn:
		cursor = conn.cursor()
		result = cursor.execute('SELECT name, keys FROM `fofa` WHERE id=\'{}\''.format(_id))
		for row in result:
			return row[0], row[1]

def count():
	with sqlite3.connect(path + '/web.db') as conn:
		cursor = conn.cursor()
		result = cursor.execute('SELECT COUNT(id) FROM `fofa`')
		for row in result:
			return row[0]
