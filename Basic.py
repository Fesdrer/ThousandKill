import os

RESET="\033[0m"  
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"

ENCODING='utf-8'

def clear():
	os.system('cls')
def context():
	print('1-learn')
	print('2-turn')
	print('3-exit')
def examumget()->tuple[str,int,int,int]:
	"""
	the first int: 0->basictest,1->shanbei

	the second int: if random
	
	the third int: 1->5
	"""
	infilepath=input('Input infilepaths: ')
	int1=int(input('Do you want to use Shanbei(0 no 1 yes): '))
	int2=int(input('Do you want to rand(0 no 1 yes): '))
	print(YELLOW+'1-ask Q answer A')
	print('2-ask A answer Q')
	print('3-ask Q answer A and ask A answer Q')
	print('4-ask A spell Q')
	print('5-ask Q answer A'+RESET)
	int3=int(input('Which one do you chose: '))
	return infilepath,int1,int2,int3
def turnfilenumget()->tuple[str,int,int,int,str]:
	"""
	the first int: if t

	the second int: if tr

	the third int: 0->txt,1->md
	"""
	str1=input('Input infilepath: ')
	int1=int(input('Do you want to "t": '))
	int2=int(input('Do you want to "tr": '))
	int3=int(input('Export in "txt" or "md"(0 "txt" or 1 "md"): '))
	str2=input('Input outfilepath: ')
	return str1,int1,int2,int3,str2