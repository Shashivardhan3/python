

# pie chart:
import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,        #starting from 90 angle
        shadow= True,
        explode=(0,0,0.6,0),  # for highlighting particular activity
        autopct='%1.2f%%'     # for showing the percentages
        )

plt.title('Interesting Graph\nCheck it out')
plt.show()
