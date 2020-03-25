import os
import shutil

file=open("train_test_split.txt",'r')

l=[]
for i in file:
	l.append(i)

#storing all the names of folders(classes) in the list x
x=os.listdir('images')

#creating two folders 'train' and 'val'
os.mkdir('train')
os.mkdir('val')

for i in x:
	os.mkdir('train/'+i)

for i in x:
	os.mkdir('val/'+i)


z=[]
for i in x:
	am=os.listdir('images/'+i)
	
	z.append(am)

c=0
for i in z:
	size=len(i)
	train=0.8*size
	val=0.2*size
	train=int(train)
	val=int(val)
	#print(train+1,size)
	
	for y in range(train):
		shutil.copyfile('images/'+x[c]+'/'+z[c][y],'train/'+x[c]+'/'+z[c][y])

	for o in range(train+1,size):
		shutil.copyfile('images/'+x[c]+'/'+z[c][o],'val/'+x[c]+'/'+z[c][o])
	c=c+1
	