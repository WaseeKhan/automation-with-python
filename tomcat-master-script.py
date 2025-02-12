import os
import platform
import time

tomcat_bin = "/Users/waseem/Developer/servers/tomcat/bin"
# tomcat_start_script_filename = "startup.sh"

def tomcatMasterScript(tomcat_start_script_filename):
    print(f"We're here: ",os.getcwd())
    time.sleep(2)
    os.chdir(tomcat_bin)
    print(f"We've moved to tomcat bin: ",os.getcwd())
    time.sleep(2)
    os.system(tomcat_start_script_filename)

if platform.system()=="Windows":
    tomcatMasterScript("./startup.bat")
else:
    tomcatMasterScript("./startup.sh")