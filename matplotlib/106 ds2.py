

import matplotlib.pyplot as plt

x1 = [1,2,3]
y1 = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,8]

plt.plot(x1, y1, label='First Line')
plt.plot(x2, y2, label='Second Line')
plt.xlabel('Plot Number')  #x-axis label
plt.ylabel('Important var') #y-axis label
plt.title('Interesting Graph\nCheck it out')  #title for the graph
plt.legend() #for line indicator i.e 1st line which colour ,2nd line which colour
plt.show()



