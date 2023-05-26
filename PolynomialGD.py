import matplotlib.pyplot as plt
import math

class Sine:
    def __init__(self,period,amplitude):
        self.period=period
        if self.period==0:
            self.period=1
        self.amplitude=amplitude
        if self.amplitude==0:
            self.amplitude=1.

    def calc(self,x):
        return self.amplitude*math.sin(x*self.period)

    def diff(self,x):
        return self.amplitude*math.cos(x*self.period)

    def string(self):
        amplitude_string=""
        period_string=""
        if self.amplitude!=1:
            amplitude_string=str(self.amplitude)+"*"
        if self.period!=1:
            period_string=str(self.period)+"*"
        return amplitude_string+"sine("+period_string+"x)"

class Polynomial:
    def __init__(self,first,*args):
        self.args=[]
        self.args.append(first)
        for i in range(len(args)):
            a=args[i]
            self.args.append(a)

    def calc(self,x):
        y=0
        for i in range(len(self.args)):
            y=y+self.args[i]*x**i
            #print(f"index: {i} this: {self.args[i]*x**i} sum: {y}")
        return y

    def diff(self,x):
        y=0
        for i in range(len(self.args)):
            if i>0:
                y=y+(i)*self.args[i]*x**(i-1)
                #print(f"index: {i} this: {(i)*self.args[i]*x**(i-1)} sum: {y}")
        return y

    def format_float(self,f):
        result=str(f)
        if f%1==0:
            i=int(f)
            result=str(i)
        return result

    def string(self):
        result=""
        for i in range(len(self.args)):
            if self.args[i]!=0:
                if i==0:
                    result=self.format_float(self.args[i])
                    continue
                if result!="" and self.args[i]>0:
                    result+="+"
                argstr=self.format_float(self.args[i])
                # Remove unnecessary +1* and -1* values
                if argstr=="1":
                    argstr="+"
                if argstr=="-1":
                    argstr="-"
                # Add "*" for values other than +1 or -1
                if argstr!="+" and argstr!="-":
                    argstr+="*"
                # Use power of value when greater than 1
                pow=""
                if i>1:
                    pow="^"+str(i)
                result+=argstr+"X"+pow
        return result

def gradient_descent(gradient, start, learn_rate, n_iter):
    vector=start
    for _ in range(n_iter):
        diff=-learn_rate*gradient(vector)
        vector+=diff
        #print(f"diff: {diff} vector: {vector}")
    return vector

#poly=Sine(1,2)
poly=Polynomial(2.0,-1,4.0,-0.5,0.25,0.125)

# Note that not all polynomial functions will have a zero differential value, so this gradient descent can explode
x=2
y=0
xgrad=[]
ygrad=[]
for i in range(5):
    y=poly.calc(x)
    xgrad.append(x)
    ygrad.append(y)
    x=gradient_descent(poly.diff,x,0.1,1)
print(f"xgrad: {xgrad} ygrad: {ygrad}")
#gradient=gradient_descent(poly.diff,2,0.1,10)
#print(f"gradient: {gradient} value: {poly.calc(gradient)}")

# Print graph of polynomial function and derivative of polynomial function
xvals=[]
iterations=100
for i in range(iterations):
    x=i/10.0-iterations/20.0
    xvals.append(x)
yvals=[]
diffvals=[]
minxval=10000
minyval=10000
maxyval=0
for x in xvals:
    d=poly.diff(x)
    y=poly.calc(x)
    yvals.append(y)
    diffvals.append(d)
    if y>maxyval:
        maxyval=y
    if d>maxyval:
        maxyval=d
    if(y<minyval and (d>-1 and d<1)):
        minxval=x
        minyval=y
        print(f"A: x: {x} y: {y} d: {d} minxval: {minxval} minyval: {minyval}")
print(f"xvals: {xvals}")
print(f"yvals: {yvals}")
print(f"diff: {diffvals}")

# b is for "solid blue line"
plt.plot(xvals, yvals, 'blue', label='f(x)')
plt.plot(xvals, diffvals, 'r--', label="f'(x)")
plt.plot(xgrad,ygrad,'ro',label="gradient")
plt.plot([xvals[0],xvals[len(xvals)-1]], [0,0], 'black',linewidth=2.0)
plt.title('Polynomial: '+poly.string())
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
if minxval!=10000:
    plt.annotate(f'local min: [{minxval:.2f},{minyval:.2f}]', xy=(minxval, minyval), xytext=(minxval, minyval+(maxyval/5)),
        arrowprops=dict(facecolor='black', shrink=0.05),ha="center")
plt.show()
