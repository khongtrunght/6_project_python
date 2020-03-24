# Generating asine vs cosine curve
import  numpy as np
import matplotlib

x = np.arange(-2*np.pi,2*np.pi,np.pi)
y = np.sin(x)
z = np.cos(x)

mpl.plot(x,y)
mpl.show()

matplotlib.plot()