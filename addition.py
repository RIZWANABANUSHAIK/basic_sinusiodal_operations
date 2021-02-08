import numpy as np
from matplotlib import pyplot as plt 
n=np.arange(0,500)
F=250; Fs=10000;
s=0.5*np.sin(2*np.pi*F/Fs*n+np.pi/2)
plt.subplot(331)
plt.plot(n,s);

p=0.5*np.sin(3*np.pi*F/Fs*n+np.pi/3)
plt.subplot(332)
plt.plot(n,p);

plt.subplot(333)
plt.plot(n,s+p); 

a=0.5*np.sin(3*np.pi*F/Fs*n+np.pi/3)
plt.subplot(334)
plt.plot(n,a);

b=1.0*np.sin(3*np.pi*F/Fs*n+np.pi/4)
plt.subplot(335)
plt.plot(n,b);
plt.subplot(336)
plt.plot(a+b);

c=0.5*np.sin(3*np.pi*F/Fs*n+np.pi/3)
plt.subplot(337)
plt.plot(n,c);

d=1.0*np.sin(4*np.pi*F/Fs*n+np.pi/3)
plt.subplot(338)
plt.plot(n,d);

plt.subplot(3,3,9)
plt.plot(n,c+d)
plt.show()
