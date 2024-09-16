import Basic
import File
import Exam
import os

if __name__=='__main__':
	while True:
		Basic.clear()
		Basic.context()
		tmp=input().strip()
		if tmp=='1':
			Basic.clear()
			infilepath,ifShanbei,ifRand,examops=Basic.examumget()
			now=File.Imports(infilepath)
			examop=0
			if examops==1:
				examop=0
			if examops==2:
				examop=0
				now.change_tr()
			elif examops==3:
				examop=0
				now.change_ori_and_tr()
			elif examops==4:
				examop=1
			elif examops==5:
				examop=1
				now.change_tr()
			if ifRand==1:
				now.random()
			if ifShanbei==0:
				now=Exam.CommonExam(now,examop)
			else:
				now=Exam.ShanbeiExam(now,examop)
			Basic.clear()
			if len(now.elements)==0:
				print(Basic.GREEN+'Excellent!'+Basic.RESET)
			else:
				print('Wrong '+Basic.RED+str(len(now.elements))+Basic.RESET)
			outfilepath=input('Input outfilepath: ')
			if outfilepath!='':
				File.Export_txt(outfilepath,now)
		elif tmp=='2':
			Basic.clear()
			infilepath,ift,iftr,ifmd,outfilepath=Basic.turnfilenumget()
			now=File.Imports(infilepath)
			if ift==1:
				now.change_t()
			if iftr==1:
				now.change_tr()
			if ifmd==1:
				File.Export_md(outfilepath,now)
			else:
				File.Export_txt(outfilepath,now)
		else:
			break