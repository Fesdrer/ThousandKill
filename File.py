from Basic import *
from Group import *

def Imports(filepaths:str)->Group:
	filepaths=filepaths.split()
	ret=Group(3)
	allop=2
	for filepath in filepaths:
		with open(filepath,encoding=ENCODING) as file:
			files=file.readlines()
			for i in range(0,len(files)):
				files[i]=files[i].strip()
			op=int(files[0])
			while (len(files)-1)%op!=0:
				files.append('')
			i=1
			while i<=len(files)-1:
				if op==2:
					ret.elements.append(Element(op,files[i],files[i+1]))
				else:
					ret.elements.append(Element(op,files[i],files[i+1],files[i+2]))
				i+=op
			allop=max(allop,op)
	if allop==2:
		ret.op=2
	else:
		for i in ret.elements:
			if i.op==2:
				i.change_t()
	return ret
def Export_md(filepath:str,group:Group):
	with open(filepath,'w',encoding=ENCODING) as file:
		file.write(group.output_md())
def Export_txt(filepath:str,group:Group):
	with open(filepath,'w',encoding=ENCODING) as file:
		file.write(group.output_txt())