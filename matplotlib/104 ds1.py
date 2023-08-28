
#Matplotlib: For plottings different types of Graphs

#matplotlib is an external module which is not part of python software

#so we need to download and install these external modules using a component called pip

#pip :Pip is a package manager which quickly downloads and installs any external modules.

#pip is available in the installed folder of python i.e-->C:\Python39\scripts\pip

#first install matplotlib module as follows

#Matplotlib is an external module, we need to download and install by using pip

#Installing External modue-------->matplotlib

#C:\Users\DELL>cd\

#C:\>cd C:\python39\scripts

#C:\python39\scripts>pip install matplotlib
#also install pandas module

#C:\python39\scripts>pip install pandas
#it installs i)python-dateutil ii)numpy iii)pytz etc

#graphs :

import matplotlib.pyplot as plt   #matplotlib--->package, pyplot-->module ,plot()--->function

plt.plot([1,2,3],[5,7,4],".")
plt.show()

'''
Instead of the linear graph, the values can be displayed discretely by adding a format string to the plot() function. Following formatting characters can be used.

Sr.No.	Character & Description
1	
'-'    Solid line style

2	
'--'   Dashed line style

3	
'-.'  Dash-dot line style

4	
':'   Dotted line style

5	
'.'   Point marker

6	
','  Pixel marker

7	
'o'  Circle marker

8	
'v'  Triangle_down marker

9	
'^'  Triangle_up marker

10	
'<'  Triangle_left marker

11	
'>'  Triangle_right marker

12	
'1'  Tri_down marker

13	
'2'  Tri_up marker

14	
'3'  Tri_left marker

15	
'4'  Tri_right marker

16	
's'  Square marker

17	
'p'  Pentagon marker

18	
'*'  Star marker

19	
'h'  Hexagon1 marker

20	
'H'  Hexagon2 marker

21	
'+'  Plus marker

22	
'x'  X marker

23	
'D'  Diamond marker

24	
'd'  Thin_diamond marker

25	
'|'  Vline marker

26	
'_'  Hline marker

The following color abbreviations are also defined.

Character	Color
'b'	Blue
'g'	Green
'r'	Red
'c'	Cyan
'm'	Magenta
'y'	Yellow
'k'	Black
'w'	White '''


 
