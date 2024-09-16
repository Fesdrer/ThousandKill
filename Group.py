from Basic import *
from Element import *
import random
import copy

class Group:
	def __init__(self,op:int):
		self.op=op
		self.elements:list[Element]=[]
	def change_t(self):
		self.op=5-self.op
		for i in self.elements:
			i.change_t()
	def change_tr(self):
		for i in self.elements:
			i.change_tr()
	def random(self):
		random.shuffle(self.elements)
	def change_ori_and_tr(self):
		lens=len(self.elements)
		for i in range(0,lens):
			tmp=copy.deepcopy(self.elements[i])
			tmp.change_tr()
			self.elements.append(tmp)
	def output_md(self)->str:
		ret=''
		if self.op==2:
			ret='|Q|A|\n|:-:|:-:|\n'
		else:
			ret='|Q|A|e.g.|\n|:-:|:-:|:-:|\n'
		for i in self.elements:
			ret+=i.output_md()
		return ret
	def output_txt(self)->str:
		ret=str(self.op)+'\n'
		for i in self.elements:
			ret+=i.output_txt()
		return ret