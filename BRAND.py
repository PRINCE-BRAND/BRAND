import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from BRAND import make
 
        make()
 
 
 
elif bit == "32bit":
 
        from BRAND32 import make
 
 
        make()
