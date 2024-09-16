from Basic import *
from Group import *
import copy

def CommonExam(group:Group,examop:int)->Group:
	havelearnednum=0
	lastElement=None
	ret=Group(group.op)
	def headerget()->str:
		front='have learned '+GREEN+str(havelearnednum)+RESET
		back='    still need to learn '+RED+str(len(group.elements)-havelearnednum)+RESET
		return front+back
	for i in group.elements:
		tmp=i.exam(examop,headerget())
		while tmp==2:
			if lastElement!=None:
				ret.elements.append(lastElement)
				lastElement=None
			tmp=i.exam(examop,headerget())
		if tmp==1:
			ret.elements.append(i)
			lastElement=None
		else:
			lastElement=i
		havelearnednum+=1
	clear()
	return copy.deepcopy(ret)
def ShanbeiExam(group:Group,examop:int)->Group:
	ret=Group(group.op)
	lastElement=None
	havelearnednum=0
	nolearn:list[tuple[Element,int]]=[]
	for i in group.elements:
		nolearn.append((i,0))
	def headerget()->str:
		front='have learned '+GREEN+str(havelearnednum)+RESET
		back='    still need to learn '+RED+str(len(nolearn))+RESET
		return front+back
	def insert_no(x):
		if x!=None:
			if x[1]==0:
				ret.elements.append(x[0])
			nolearn.insert(min(len(nolearn),8),(x[0],1))
	def insert_yes(x):
		if x!=None and x[1]==1:
			nolearn.insert(min(len(nolearn),16),(x[0],2))
	def insert_turn(x):
		if x!=None:
			if x[1]==1:
				nolearn.pop(min(len(nolearn)-1,16))
			if x[1]==0:
				ret.elements.append(x[0])
			nolearn.insert(min(len(nolearn),8),(x[0],1))
	while len(nolearn)!=0:
		tmp=nolearn[0][0].exam(examop,headerget())
		while tmp==2:
			insert_turn(lastElement)
			lastElement=None
			tmp=nolearn[0][0].exam(examop,headerget())
		now=nolearn[0]
		nolearn.pop(0)
		if tmp==1:
			insert_no(now)
			lastElement=None
		else:
			insert_yes(now)
			lastElement=now
		havelearnednum+=1
	return copy.deepcopy(ret)