__authour__ = 'mkm'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os
import tool
class Spider:
	def __init__(self):
		self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
		self.tool = tool.Tool()
	def getPage(self,pageIndex):
		url = self.siteURL + "?page=" + str(pageIndex)
	#	print url
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		return response.read().decode('gbk')
	def getContents(self,pageIndex):
		page = self.getPage(pageIndex)
		pattern = re.compile('<div.*?class="list-item.*?<a.*?href="(.*?)".*?class="lady-avatar">.*?<img.*?src="(.*?)".*?<a.*?class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
		items = re.findall(pattern,page)
		contents = []
		for item in items:
			contents.append([item[0],item[1],item[2],item[3],item[4]])
			return contents
		#	print item[0],item[1],item[2],item[3],item[4]
	def getDetailPage(self,infoURL):
		response = urllib2.urlopen(infoURL)
		return response.read().decode('gbk')
	def getBrief(self,page):
		pattern = re.compile('<div.*?class="mm-aixiu-content".*?>(.*?)<!--',re.S)
		result = re.search(pattern,page)
		return self.tool.replace(result.group(1))
	def getAllImg(self,page);
		pattern = re.compile('<img.*?src="(.*?)"',re.S)
		images = re.findall(patternImg,content.group(1))
		return images
	def saveImgs(self,images,name)
		number = 1
		print uf"发现",name,u"共有",len(images),u"张照片"
		for imageURL in images:
			splitPath = imageURL.split('.')
			fTail = splitPath.pop()
			if len(fTail)>3:
				fTail = "jpg"
			fileName = name + "/" +str(name) + "." + fTail
			self.saveImg(imageURL,fileName)
			number += 1
	
		
	def saveImg(self,imageURL,fileName):
		u = urllib.urlopen(imageURL)
		data = u.read()
		f = open(fileName, 'wb')
		f.write(data)
		f.close()
	def saveBrief(self,content,name)
		fileName = name +"/"+name + ".txt"
		f = open(fileName, "w+")
		print u"正在偷偷保存她的个人信息为",fileName
		f.write(content.encode('utf-8'))
	def mkdir(self,path):
		path = path.strip()
		isExists = os.path.exists(path)
		if not isExists:
			os.makedirs(path)
			return True
		else:
			return False
spider = Spider()
spider.getContents(1)
		
	
