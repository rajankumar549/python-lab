from statistics import mean
import matplotlib.pyplot as plt
import numpy  as num

def get_slope(xs,ys):
    m=(mean(xs)*mean(ys)-mean(xs*ys))/(mean(xs)**2-mean(xs**2))
    b=mean(ys)-m*mean(xs)
    return m,b


if __name__=='__main__':
    xs=[1,2,3,4,5,6]
    ys=[5,4,6,5,6,7]
    plt.style.use('fivethirtyeight')
    xs= num.array(xs,dtype=num.float64)
    ys = num.array(ys, dtype=num.float64)
    m,b=get_slope(xs,ys)
    reg_line=[m*x+b for x in xs]
    plt.scatter(xs, ys,color='black')
    plt.plot(xs,reg_line,color='blue')
    predicat_x=8
    predicat_y=(m*predicat_x)+b
    plt.scatter(predicat_x,predicat_y,color='red')
   # plt.show()
    print(m)
    print(b)
    #plt.scatter(xs, ys)
    #plt.show()
