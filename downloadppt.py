# -*- coding: utf-8 -*-
# @Author: wangfpp
# @Date:   2018-06-07 14:22:41
# @Last Modified by:   wangfpp
# @Last Modified time: 2018-06-07 15:35:56
import os
import requests
import json
import re
#html = requests.get('https://wkretype.bdimg.com/retype/zoom/52545804fc4ffe473368ab5e?pn=58&o=jpg_6&md5sum=09d31e16d339c65ad1162099716e3216&sign=71aeffdf24&png=3845995-3877303&jpg=7833121-7959729')
class saveImg(object):
	def __init__(self,baseUrl,path):
		self.baseUrl = baseUrl
		self.path = path
	def get_jsonp(self):
		req = requests.get(self.baseUrl)
		if req.status_code == 200:
			data = (req.content)
			json = self.loads_jsonp(data)
			for i in range(len(json['list'])):
				self.save_file(i,self.path,json['list'][i]['zoom'])
	def loads_jsonp(self,jsonp):#解析JSONP 这样的方式有风险
	    try:
	        return json.loads(re.match(".*?({.*}).*",jsonp,re.S).group(1))
	    except:
			raise ValueError('Invalid Input')
	def save_file(self,name,path,url):
		html = requests.get(url)
		print name
		if html.status_code == 200:
			full_name = '{}/{}.png'.format(path,name)
			with open(full_name,'wb') as file:
				file.write(html.content)
if __name__ == '__main__':
	baseUrl = 'https://wenku.baidu.com/browse/getbcsurl?doc_id=27e3183917fc700abb68a98271fe910ef02dae44&pn=1&rn=99999&type=ppt&callback=jQuery110108123878709385568_1528356058022&_=1528356058027'
	a = saveImg(baseUrl,'./img')
	a.get_jsonp()