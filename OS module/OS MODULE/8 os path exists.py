#os.path.exists

import os

if(os.path.exists("C:/python7am/int2.py")):
   os.remove("C:/python7am/int2.py")
else:
    print("File Doesnt Exist!!!")
