#Wykres funkcji y=f(x)
#import matplotlib.pyplot as plt
#x = [1, 2, 3]
#y = [4, 6, 5]
#plt.plot(x,y)
#plt.show()


#Funkcja trygonometryczna
#import numpy as np
#import matplotlib.pyplot as plt
#x = np.arange(0.0, 2.0, 0.01)
#y = np.sin(2.0*np.pi*x)
#plt.plot(x,y,'r:',linewidth=6)
#plt.xlabel('Czas')
#plt.ylabel('Pozycja')
#plt.title('Nasz pierwszy wykres')
#plt.grid(True)
#plt.plot(x,y)
#plt.show()

#Kilka wykresów we wspólnych osiach
#import numpy as np
#import matplotlib.pyplot as plt
#x = np.arange(0.0, 2.0, 0.01)
#y1 = np.sin(2.0*np.pi*x)
#y2 = np.cos(2.0*np.pi*x)
#plt.plot(x, y1,'r:',x,y2,'g')
#plt.legend('dane y1', 'dane y2')
#plt.xlabel('Czas')
#plt.ylabel('Pozycja')
#plt.title('Wykres')
#plt.grid(True)
#plt.show()

#Kilka wykresów we wspólnych osiach v2
#import numpy as np
#import matplotlib.pyplot as plt
#x = np.arange(0.0, 2.0, 0.01)
#y1 = np.sin(2.0*np.pi*x)
#y2 = np.cos(2.0*np.pi*x)
#y = y1*y2
#l1, = plt.plot(x,y,'b')
#l2,l3 = plt.plot(x,y1,'r:',x,y2,'g')
#plt.legend((l2,l3,l1),('dane y1','dane y2','y1*y2'))
#plt.xlabel('Czas')
#plt.ylabel('Pozycja')
#plt.title('Wykres')
#plt.grid(True)
#plt.show()

#Subplot - tablica wykresów
#from pylab import *
#figure(figsize=(8,6), dpi=100)
#x = linspace(-2*pi,2*pi,100)
#subplot(2, 2, 1)
#plot(x, sin(x))
#subplot(2,2,2)
#plot(x, sin(x)/x)
#subplot(2,2,3)
#plot(x,exp(-x**2))
#subplot(2,2,4)
#plot(x, sqrt(1-x**2))
#show()

#Różne tablice wykresów
#from pylab import *
#figure(figsize=(8,6), dpi=100)
#x = linspace(-2*pi,2*pi,100)
#subplot(2,1,1)
#plot(x,sin(x))
#subplot(2,3,4)
#plot(x, sin(x)/x)
#subplot(2,3,5)
#plot(x,exp(-x**2))
#subplot(2,3,6)
#plot(x,sqrt(1-x**2))
#show()

#Różne kombinacje subplotów
#from pylab import *
#figure(figsize=(8,6), dpi=100)
#x = linspace(-2*pi,2*pi,100)
#subplot(2,2,1)
#plot(x, sin(x))
#subplot(4,2,2)
#plot(x, sin(x)/x)
#subplot(4,2,4)
#plot(x, exp(-x**2))
#subplot(4,1,3)
#plot(x, sqrt(1-x**2))
#subplot(4,3,10)
#plot(x,x**2)
#subplot(4,3,11)
#plot(x,1/x)
#subplot(4,3,12)
#plot(x, cos(x*5))
#show()

#Kolory w matplotlib
#from pylab import *
#fig=figure(figsize=(8,6), dpi=100)
#marginesy
#fig.subplots_adjust(left = 0.2, bottom = 0.1, right = 0.8, top= 0.85, wspace = 0.5, hspace = 0.2)
#matplotlib.rc('axes', linewidth = 3) #grubość ramki
#matplotlib.rc('font', family = 'serif', size = 10) #fonty
#matplotlib.rc('axes', titlesize = 18) #font tytułu
#matplotlib.rc('axes', labelsize = 14) #font opisu osi
#matplotlib.rc('axes', edgecolor = (0.62, 0.3, 0.0)) #kolor ramki
#matplotlib.rc('axes', facecolor = (1.0, 0.9, 0.75)) #kolor tła
#matplotlib.rc('xtick.major', size = 10) #kreska podziałki oś x
#matplotlib.rc('ytick.major', size = 5) #kreska podziałki oś y
#x = linspace(-2*pi, 2*pi, 100)
#subplot(2, 2, 1)
#plot(x, sin(x), c = "red")
#title(u"Tytuł")
#xlabel(u"oś x")
#ylabel(u"oś y")
#subplot(2, 2, 2)
#plot(x, sin(x)/x, lw = 3, ls = "--")
#title("$y(x) = \\frac {\\sin x}{x}$")
#grid() #siatka
#subplot(2, 2, 3)
#plot(x, exp(-x**2), label = "$y(x) = e^{-x^2}$")
#legend(loc = 3, prop={'size':16}) #zmiana rozmiaru legendy
#subplot(2, 2, 4)
#plot(x, x**2, c="green",ls="",marker="*")
#text(-3,30,"dodatkowy opis")
#text(-6.3,20,u"dodatkowy duży opis",fontsize=16)
#savefig("..pics/mpl_08.png") #zapis do pliku
#show()

#Mapa konturowa
#from pylab import *
#def f(x,y):
	#return exp(-x**2-y**2/4)+\
	#exp(-(x+2)**2-y**2/2)+\
	#exp(-(x-2)**2-2*y**2)
#n=256
#z=3.5
#x=linspace(-z,z,n)
#y=linspace(-z,z,n)
#X,Y=meshgrid(x,y)
#contourf(X,Y,f(X,Y),8)
#C=contour(X,Y,f(X,Y),8,colors='b',linewidths=1)
#clabel(C,inline=1,fontsize=10)
#savefig("kontur.jpg")
#show()

#Dane w postaci obrazka
#from pylab import *
#def f(x,y):
	#return exp(-x**2-y**2/4)+\
	#exp(-(x+2)**2-y**2/2)+\
	#exp(-(x-2)**2-2*y**2)
#n=256
#z=3.5
#x=linspace(-z,z,n)
#y=linspace(-z,z,n)
#X,Y=meshgrid(x,y)
#imshow(f(X,Y),cmap="hot")
#savefig("obrazek.jpg")
#show()

#Wykres 3D
#from pylab import *
#from mpl_toolkits.mplot3d\
#import Axes3D
#fig=figure()
#axe=Axes3D(fig)
#n=40
#z=10
#x=linspace(-z,z,n)
#y=linspace(-z,z,n)
#X,Y=meshgrid(x,y)
#R=sqrt(X**2+Y**2)
#Z=sin(R)/R
#axe.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='hot')
#savefig("3d.jpg")
#show()

#Histogram
#import matplotlib.pyplot as plt
#zliczenia=[0,1,2,2,3,3,3,3,3,3,4,4,4,5,7]
#plt.hist(zliczenia)
#plt.show()

#Histogram 2
#from pylab import *
#import matplotlib.pyplot as plt
#f=figure(figsize=(3,5),dpi=100)
#f.subplots_adjust(hspace=0.4,bottom=0.02)
#subplot(2,1,1)
#x=randn(1000)
#hist(x,50)
#title("histogram")
#subplot(2,1,2)
#x=[1,2,3,4]
#l=map(str,x)
#e=[0,0,0.05,0]
#labels='Python','C++','Ruby','Java'
#sizes=[250,140,210,200]
#colors=['gold','yellowgreen','lightcoral','lightskyblue']
#explode=(0.1,0,0,0)
#plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
#plt.axis('equal')
#title("wykres kołowy")
##savefig("hist.jpg")
#show()

#Rozkład Gaussa
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.mlab as mlab
#mi,sigma=100,15
#x=mi+sigma*np.random.randn(10000)
#sigma**2
#n,bins,patches=plt.hist(x,50,density=True,facecolor='green',alpha=0.75)
#bincenters=0.5*(bins[1:]+bins[:-1])
#y=mlab.normpdf(bincenters,mi,sigma)
#l=plt.plot(bincenters,y,'r--',linewidth=1)
#plt.show()

#Wizualizacja zawartości tablicy dwuwymiarowej
#import numpy as np
#import matplotlib.pyplot as plt
#A=np.arange(20)
#X,Y=np.meshgrid(A,A)
#Z=X+Y
#plt.imshow(Z,cmap='hot',interpolation='none')
#plt.colorbar()
#plt.show()

#Zadanie 1A
#import matplotlib.pyplot as plt
#import numpy as np
#x=np.arange(-10,10,2)
#a=int(input("Podaj liczbę a: "))
#b=int(input("Podaj liczbę b: "))
#y=a*x+b
#plt.title("Wykres funkcji f(x)=a*x+b")
#plt.plot(x,y)
#plt.show()

#Zadanie 1B
#import matplotlib.pyplot as plt
#import numpy as np
#x=np.arange(-10,10,1)
#a=1
#b=2
#y=a*x+b
#plt.title("Wykres funkcji f(x)=a*x+b")
#plt.plot(x,y)
#plt.show()

#Zadanie 2
#import matplotlib.pyplot as plt
#import numpy as np
#x1=np.arange(-10,0,0.5)
#x2=np.arange(0,10,0.5)
#a=int(input("Podaj liczbę a: "))
#y1=x1/(-3)+a
#y2=x2*x2/3
#plt.plot(x1,y1,'g',x2,y2,'r')
#plt.title("Wykres f(x)")
#plt.show()

#Ruchy Browna
#import matplotlib.pyplot as plt
#import numpy as np
#import random
#a=int(input("Podaj ilość ruchów: "))
#x=[]
#y=[]
#while a > 0:
	#x.append(random.randint(0,10))
	#y.append(random.randint(0,10))
	#a=a-1
#plt.plot(x,y,'ro',x,y,'r:')
#plt.title("Ruchy Browna")
#plt.show()

#Poprawione Ruchy Browna
import matplotlib.pyplot as plt
import numpy as np
import random as r
from pylab import *
a=int(input("Podaj ilość ruchów: "))
x=[0]
y=[0]
j=0
while a > 0:
	x.append(x[j]+1*cos(degrees(r.uniform(0,2))))
	y.append(y[j]+1*sin(degrees(r.uniform(0,2))))
	j=j+1
	a=a-1
x_end=x[a-1]
y_end=y[a-1]
x_linia=[0,x_end]
y_linia=[0,y_end]
przesuniecie=sqrt((x[a-1]*x[a-1])+(y[a-1]*y[a-1]))
ruch_czastki=plt.plot(x,y,'ro',x,y,'r:')
koncowa_droga=plt.plot(x_linia,y_linia,'g')
plt.legend(koncowa_droga,'Przesuniecie')
plt.title("Ruchy Browna")
plt.show()
