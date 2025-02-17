import subprocess
import sys
import os 
import shutil
import logging
from datetime import datetime
import platform as pf

# Vairaable Configurations
CATALINA_HOME = "/Users/waseem/Developer/servers/tomcat"
CATALINA_SCRIPT = f"{CATALINA_HOME}/bin/catalina.sh" if pf!="Windows" else f"{CATALINA_HOME}/bin/catalina.bat"
LOGS_DIR = f"{CATALINA_HOME}/logs"
WORK_DIR = f"{CATALINA_HOME}/work"
TEMP_DIR = f"{CATALINA_HOME}/temp"
APP_LOG_DIR = "logs"
CURR_DATE = datetime.now().strftime("%Y-%m-%d")
LOG_FILENAME = f"{APP_LOG_DIR}/TMS-{CURR_DATE}.LOG"

logging.basicConfig(
    level=logging.DEBUG,
    filemode="a",
    filename=LOG_FILENAME,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"

)
logging.info("---------------*****----------------")

if os.path.exists(APP_LOG_DIR):
    logging.info(f"{APP_LOG_DIR} Directory already Exists . . .")
else:
    os.mkdir(APP_LOG_DIR)
    logging.info(f"{APP_LOG_DIR} Directory has been Created . . .")

def start_tomcat():
    try:
        housekeepingBoat(LOGS_DIR)
        housekeepingBoat(TEMP_DIR)
        housekeepingBoat(WORK_DIR)
        subprocess.run([CATALINA_SCRIPT, "start"], check=True)
        print("Tomcat started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Tomcat: {e}")

def stop_tomcat():
  
    try:
        subprocess.run([CATALINA_SCRIPT, "stop"], check=True)
        print("Tomcat stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop Tomcat: {e}")

def restart_tomcat():
    housekeepingBoat(LOGS_DIR)
    housekeepingBoat(TEMP_DIR)
    housekeepingBoat(WORK_DIR)
    stop_tomcat()
    start_tomcat()

# Function to delete all contents including folders & sub folders. 
def housekeepingBoat(folder):
    try:
        # Check if the logs directory exists or not
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    # Remove files or directories
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  # Delete the file or symbolic link
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Delete the directory
                except Exception as e:
                    logging.error(f"{folder} Failed to delete {file_path}. Reason: {e}")
            print(f"{folder} directory cleared successfully.")
        else:
            print(f"{folder} directory does not exist: {LOGS_DIR}")
            print(f"It's okay!! Apache Tomact will create {folder} directroy")
    except Exception as e:
        print(f"Failed to clear {folder} directory: {e}")
# End of work on logs dir

def usage():
    """Print usage information."""
    print("Usage: python tomcat-master-script.py [start|stop|restart]")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    action = sys.argv[1].lower()

    if action == "start":
        start_tomcat()
    elif action == "stop":
        stop_tomcat()
    elif action == "restart":
        restart_tomcat()
    else:
        print(f"Unknown action: {action}")
        usage()
        sys.exit(1)