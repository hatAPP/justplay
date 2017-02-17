__author__ = 'lkl'
# -*- coding:utf-8 -*-
import re
class Tool:
	removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
	removeAddr = re.compile('<a.*?>|</a>')
	replaceLine = re.compile('<tr>|<div>|</div>|</p>')
	replaceTD= re.compile('<td>')
	#将换行符或双换行符替换为n
	replaceBR = re.compile('<br><br>|<br>')
	#将其余标签剔除
	removeExtraTag = re.compile('<.*?>')
	#将多行空行删除
	removeNoneLine = re.compile('n+')
	def replace(self,x):
		x = re.sub(self.removeImg,"",x)
		x = re.sub(self.removeAddr,"",x)
		x = re.sub(self.replaceLine,"n",x)
		x = re.sub(self.replaceTD,"t",x)
		x = re.sub(self.replaceBR,"n",x)
		x = re.sub(self.removeExtraTag,"",x)
		x = re.sub(self.removeNoneLine,"n",x)
		#strip()将前后多余内容删除
		return x.strip()
