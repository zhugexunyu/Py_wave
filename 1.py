import matplotlib.pyplot as plt
import numpy as np
import sys
from pyecharts import Bar

#D:/FreeTROS/Py_test/1.txt
#C:/Users/zxc/Desktop/1.txt
filename = "" 
fs=[]
fa=[]
data_str=""
err_str = ""
dalen = 0
lena = 1
bar=Bar()


filename = input("请输入文件：")

f = open(filename,'r')
data = f.readlines()
f.close()
print(type(data))
print(len(data))
print(type(fs))

#将列表转换成字符串
data_str = data[0]
#print(data_str)
temp=[float(i) for i in data_str.split(';')] 
#print(temp)
#print(len(temp))

#一路采集数据处理
for i in temp:
    dalen = temp.index(i)
    fa.append(i*3.3/4096)
    dalen+=1
#    fs.append(dalen)

#print(fa)    2019.1.24
falen = len(fa)
while lena <= falen:
    fs.append(lena)
    lena+=1

#print(fs)    2019.1.24

'''
for i in temp:
    dalen = temp.index(i)
    if(dalen%2) == 0:
        fs.append(i)
        dalen+=1

print(len(fs))
falen = len(fs)
while lena <= falen:
    fa.append(lena)
    lena+=1

print()
print(len(fa))
'''

'''
原始程序
for i in temp:
    dalen = temp.index(i)
    if(dalen%2) == 0:
        fs.append(i)
        dalen+=1
    else:
        fa.append(i)
        dalen+=1
'''
#try:
#    len(fs) == len(fa)
#except expression as identifier:
#    pass


if(len(fs) != len(fa)):
    err_str = "x和y的数量不相等"
    print(err_str)
    print(len(fs))
    print(len(fa))
    print(fs)
    print(fa)
    

testfx = len(fa)
testfx = range(testfx)

try:
    bar.add("1",fs,fa,is_more_utils=True)
    plt.plot(testfx,fa,'r')
#    plt.axis([0, testfx, 0, 2.5])
#    plt.figure(figsize=plt.figaspect(2.0), facecolor=(1, 0, 0, .1))
except ValueError as ve:
    print("err:{0}".format(ve))
#    raise
except:
    print("Unexpected error:", sys.exc_info()[0])
#    raise


#bar.add("FFT",fs,fa,is_more_utils=True)
#bar.render()

#plt.plot(fs,fa,'r')
'''    
    描点程序
    plt.plot(testfx,fa,'r', markerfacecolor='blue', marker='o')
    for a, b in zip(testfx, fa):  
        plt.text(a, b, (a,b),ha='center', va='bottom', fontsize=10)  
    plt.legend()
'''
bar.render()
#X坐标显示
#plt.xticks(np.arange(0,len(fa),1))
plt.show()

'''
test
将列表转换成字符串
list2=[str(i) for i in data]
print(len(list2))
'''