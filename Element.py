from Basic import *

class Element:
	def __init__(self,op:int,query:str,answer:str,eg:str=''):
		self.op=op
		self.query=query
		self.answer=answer
		self.eg=eg
	def change_t(self):
		self.op,self.eg=5-self.op,''
	def change_tr(self):
		self.query,self.answer=self.answer,self.query
	def output_md(self)->str:
		if self.op==3:
			return '|'+self.query+'|'+self.answer+'|'+self.eg+'|\n'
		else:
			return '|'+self.query+'|'+self.answer+'|\n'
	def output_txt(self)->str:
		if self.op==3:
			return self.query+'\n'+self.answer+'\n'+self.eg+'\n'
		else:
			return self.query+'\n'+self.answer+'\n'
	def check(self,header:str='')->int:
		"""
		return 0 is ok
		
		return 1 is no

		return 2 the last is no
		"""
		clear()
		if header!='':
			print(header)
		print(self.query)
		tmp=input().strip()
		if tmp=='mark the last':
			return 2
		print(self.answer)
		if self.op==3:
			print(GREEN+'e.g.: '+RESET+self.eg)
		tmp=input().strip()
		if tmp=='f':
			return 1
		return 0
	def checkspell(self,header:str='')->int:
		"""
		return 0 is ok

		return 1 is no
		"""
		marknow=0
		while True:
			clear()
			if header!='':
				print(header)
			print(self.answer)
			tmp=input().strip()
			if tmp==self.query:
				break
			else:
				marknow=1
				print(self.query)
				if self.op==3:
					print(GREEN+'e.g.: '+RESET+self.eg)
				tmp=input()
		return marknow
	def exam(self,examop:int,header:str='')->int:
		"""
		examop=0: common exam

		or spell exam
		"""
		if examop==0:
			return self.check(header)
		else:
			return self.checkspell(header)