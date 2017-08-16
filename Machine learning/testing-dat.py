from statistics import mean
import matplotlib.pyplot as plt
import numpy  as num
import random

def get_slope(xs,ys):
    m=(mean(xs)*mean(ys)-mean(xs*ys))/(mean(xs)**2-mean(xs**2))
    b=mean(ys)-m*mean(xs)
    return m,b

def suare_error(y_org,y_line):
    return sum((y_line-y_org)**2)

def r_ca(y_org,y_line):
    y_mean=[mean(y_org) for y in y_org]
    sqr_error_reg=suare_error(y_org,y_line)
    sqr_error_mean = suare_error(y_org, y_mean)
    return (1-(sqr_error_reg/sqr_error_mean)),y_mean
#data set create karne ke liya
def create_data_set(hm,variance,step=2,corelation=False):
    ys=[]
    val=1
    for i in range(hm):
        y=val+random.randrange(-variance,variance)
        ys.append(y)
        if corelation and corelation=='pos':
            val+=step
        elif corelation and corelation=='neg':
            val-=step
    xs=[x for x in range(len(ys))]
    return num.array(xs,dtype=num.float64),num.array(ys,dtype=num.float64)




if __name__=='__main__':
    xs,ys=create_data_set(40,20,2,"pos")
    m,b=get_slope(xs,ys)
    reg_line=[m*x+b for x in xs]
    plt.scatter(xs, ys,color='red')#,label='Data-point')
    plt.plot(xs,reg_line,color='blue')#,label='Best-fit-line')
    predicat_x=8
    predicat_y=(m*predicat_x)+b
    plt.scatter(predicat_x,predicat_y,s=100,color='black')#,label='Predicate-point')
    r,y_mean=r_ca(y_org=ys,y_line=reg_line)
    plt.plot(xs,y_mean,color='green')#,label='mean-line')
    print(r)
    #print(y_mean)
    #print(m)
    #print(b)
    #plt.legend()
    plt.show()
    #plt.scatter(xs, ys)
    #plt.show()

