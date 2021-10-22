import matplotlib.pyplot as plt
import numpy as np

num_on_point=100
x=np.random.randint(0,50, num_on_point)
y=x+50*np.random.randn(num_on_point)
sizes=np.random.randint(0,200,num_on_point)
colors=np.random.randint(0,10,num_on_point)
plt.scatter(x,y,s=sizes,c=colors)
plt.show()