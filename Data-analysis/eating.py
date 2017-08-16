import re
INPUT_PAT = re.compile(r'(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)')
t=int(input())
out=[]

if t>=1 and t<=100000:
     while t >= 1:
        try:
            x11,y11,x12,y12 = (int(i) for i in INPUT_PAT.match(input()).groups())
            x21, y21, x22, y22 = (int(i) for i in INPUT_PAT.match(input()).groups())
            # print(x11,x12,y11,y12)

            h1=0
            v1=0
            h2=0
            v2=0
            if x11 == x12:
                v1 = 1
            elif y11 == y12:
                 h1 = 1
            if x21 == x22:
                v2 = 1
            elif y21 == y22:
                h2 = 1
            #print(h1,v1,h2,v2)
            if(h1==v2 or h2==v1 ):
                if x11 == x21 and y11 == y21 :
                    out.append(1)
                elif x11 == x22 and y11 == y22 :
                    out.append(1)
                elif x12 == x21 and y12 == y21 :
                    out.append(1)
                elif x12 == x22 and y12 == y22 :
                    out.append(1)
                else :
                    out.append(0)
            elif(v2==v1 and v1!=0):
                #print("v1==v2")
                if  y22<y21:
                    temp=y21
                    y21=y22
                    y22=temp
                if y12 < y11:
                    temp = y12
                    y12= x11
                    y11 =temp
                s2 = set([(x21, x) for x in range(y21,y22+1)])
                s1 = set([(x11, x) for x in range(y11,y12 + 1)])
                if(len(s1.intersection(s2))>=1):
                    out.append(1)
                else:
                    out.append(0)
            elif (h1==h2 and h1!=0):
                # print("h1==h2")
                if x12 < x11:
                    temp = x11
                    x11 = x12
                    x12 = temp
                if x22 < x21:
                    temp = x22
                    x22 = x21
                    x21 = temp
                s2 = set([(x,y21) for x in range(x21, x22 + 1)])
                s1 = set([(x,y11) for x in range(x11, x12 + 1)])

                if (len(s1.intersection(s2)) >= 1):
                    out.append(1)
                else:
                    out.append(0)
            else:
                out.append(0)
        except Exception :
            out.append(0)

        t-=1
     for i in out:
        if(i==1):
            print("yes")
        else:
            print("no")





