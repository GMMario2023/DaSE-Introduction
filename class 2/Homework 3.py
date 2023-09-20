#本题稍微有些困难，难点在于将方案表示出来
#下面展示用二叉数方法来求解所有可能的方案
#我们考虑用四位二进制来表示人羊狼菜的状态，在“原岸”用1表示，在“对岸”用0表示。再转化为十进制
#易知开始时农夫必须带羊过河然后自己返回，此时状态从15变成3再变成11
#尝试寻找可能成功操作，发现三次可以到达4的状态，然后农夫返回后带羊过河，此时状态从4变成12再变成0

#下面构造函数，该函数输入目前的状态，输出可能的状态，由图可知可能的状态有1或2种，若有一种，仍用两数表示，且第二个数为-1
def possible_operations(start):
    if start==11:
        end1=2
        end2=1
    elif start==2:
        end1=14
        end2=-1
    elif start==14:
        end1=4
        end2=-1
    elif start==1:
        end1=13
        end2=-1
    elif start==13:
        end1=4
        end2=-1
    else:
        end1=-1
        end2=-1
    return [end1,end2]
operation={8:"农夫返回",9:"农夫带菜返回",10:"农夫带狼返回",12:"农夫带羊返回",-8:"农夫过河",-9:"农夫带菜过河",-10:"农夫带狼过河",-12:"农夫带羊过河"}
op1=[0,0]
op2=[0,0,0,0]
op3=[0,0,0,0,0,0,0,0]
op1[0]=possible_operations(11)[0]
op1[1]=possible_operations(11)[1]
for i in range(0,2):
    op2[2*i]=possible_operations(op1[i])[0]
    op2[2*i+1]=possible_operations(op1[i])[1]
for i in range(0,4):
    op3[2*i]=possible_operations(op2[i])[0]
    op3[2*i+1]=possible_operations(op2[i])[1]
t=0
strings=["","","",""]
for i in range(0,8):
    if op3[i]==4:
        j=i//2
        strings[t]=operation[4-op2[j]]+','+strings[t]
        strings[t]=operation[op2[j]-op1[j//2]]+','+strings[t]
        strings[t]=operation[op1[j//2]-11]+','+strings[t]
        t=t+1
for i in range(0,4):
    if strings[i]!="":
        strings[i]="方案"+str(i+1)+":农夫带羊过河,农夫返回,"+strings[i]+"农夫返回,农夫带羊过河,<结束>"
        print(strings[i])
        
        
        
        
