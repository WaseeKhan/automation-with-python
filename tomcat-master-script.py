# Required module imports
import subprocess
import sys
import os 
import shutil
import logging
from datetime import datetime
import platform as pf

# Gloable Vairable Configurations
CATALINA_HOME = "/Users/waseem/Developer/servers/tomcat"
CATALINA_SCRIPT = f"{CATALINA_HOME}/bin/catalina.sh" if pf!="Windows" else f"{CATALINA_HOME}/bin/catalina.bat"
LOGS_DIR = f"{CATALINA_HOME}/logs"
WORK_DIR = f"{CATALINA_HOME}/work"
TEMP_DIR = f"{CATALINA_HOME}/temp"
SCRIPT_LOG_DIR = "logs"
CURR_DATE = datetime.now().strftime("%d%m%Y")
SCRIPT_LOG_FILENAME = f"{SCRIPT_LOG_DIR}/TMS{CURR_DATE}.LOG"


# create script logs folder if not exists
if not os.path.exists(SCRIPT_LOG_DIR):
    os.mkdir(SCRIPT_LOG_DIR)
    logging.info(f"{SCRIPT_LOG_DIR} dir has been created successfully!")

# Logger config
logging.basicConfig(
    level=logging.DEBUG,
    filemode="a",  #append
    filename=SCRIPT_LOG_FILENAME,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)
logging.info(">>>>>>>>>> Master Script Started <<<<<<<<<<")


def start_tomcat():
    try:
        # Called delete method here
        housekeepingBoat(LOGS_DIR) 
        housekeepingBoat(TEMP_DIR)
        housekeepingBoat(WORK_DIR)

        subprocess.run([CATALINA_SCRIPT, "start"], check=True)
        print("Tomcat started successfully.")
        logging.info("Tomcat started successfully. . . ")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Tomcat: {e}")
        logging.error(f"Failed to start Tomcat: {e}")

def stop_tomcat():
    try:
        subprocess.run([CATALINA_SCRIPT, "stop"], check=True)
        print("Tomcat stopped successfully.")
        logging.info("Tomcat stopped successfully. . .")
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop Tomcat: {e}")
        logging.error(f"Failed to stop Tomcat: {e}")

def restart_tomcat():
    housekeepingBoat(LOGS_DIR)
    housekeepingBoat(TEMP_DIR)
    housekeepingBoat(WORK_DIR)
    stop_tomcat()
    start_tomcat()

def status_tomcat():
    try:
        result = subprocess.run(["pgrep", "-f", "catalina"], stdout=subprocess.PIPE)
        if result.returncode == 0:
            print("Tomcat is running.")
            logging.info("Tomcat Status : RUNNING")
        else:
            print("Tomcat is not running.")
            logging.info("Tomcat Status : NOT RUNNING")
    except Exception as e:
        logging.error(f"Error checking Tomcat status: {e}")
        print(f"Error checking Tomcat status: {e}")

# Function to delete all contents including folders & sub folders. 
def housekeepingBoat(folder):
    try:
        # Check if the logs directory exists or not
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                logging.info(f"Housekeeping inside: {folder}")
                try:
                    # Remove files or directories
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  # Delete the file or symbolic link
                        logging.info(f"Deleted : {file_path}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Delete the directory
                        logging.info(f"Deleted : {file_path}")
                except Exception as e:
                    logging.error(f"Failed to delete {file_path}. Reason: {e}")
            logging.info(f"Housekeeping Activity Completed Inside Directroy: {folder}")
        else:
            logging.warning(f"Directory does not exist: {folder} ")
            logging.info(f"It's okay!! Apache Tomact will create {folder} directroy automatically")
    except Exception as e:
        print(f"Failed to clear directory : {folder} : {e}")
        logging.warning(f"Failed to clear directory: {folder} : {e}")
# End of work on logs dir

def usage():
    # How to use script
    print("Usage: python3 tomcat-master-script.py [start|stop|restart|status]")
    logging.info("Usage: python3 tomcat-master-script.py [start|stop|restart|status]")

# logging.info(">>>>>>>>>> Master Script End <<<<<<<<<<")

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
    elif action =="status":
        status_tomcat()
    else:
        print(f"Unknown Action: {action}")
        usage()
        sys.exit(1)