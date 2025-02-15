import subprocess
import sys
import os 
import shutil

CATALINA_HOME = "/Users/waseem/Developer/servers/tomcat"
CATALINA_SCRIPT = f"{CATALINA_HOME}/bin/catalina.sh" 
LOGS_DIR = f"{CATALINA_HOME}/logs"
WORK_DIR = f"{CATALINA_HOME}/work"
TEMP_DIR = f"{CATALINA_HOME}/temp"

# For Windows system replace with 'catlina.bat' in CATLINA_SCRIPT path

def start_tomcat():
    try:
        # Calling delete_logs,delete_temp & delete_work function to perform deletion.
        delete_logs()
        delete_temp()
        delete_work()
        subprocess.run([CATALINA_SCRIPT, "start"], check=True)
        print("Tomcat started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Tomcat: {e}")

def stop_tomcat():
    """Stop the Tomcat server."""
    try:
        subprocess.run([CATALINA_SCRIPT, "stop"], check=True)
        print("Tomcat stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop Tomcat: {e}")

def restart_tomcat():
    # Calling delete_logs,delete_temp & delete_work function to perform deletion.
    delete_logs()
    delete_temp()
    delete_work()
    stop_tomcat()
    start_tomcat()

# 1. Working on 'logs' folder
def delete_logs():
    try:
        # Check if the logs directory exists or not
        if os.path.exists(LOGS_DIR):
            # Loop over the files in the logs directory and remove them
            for filename in os.listdir(LOGS_DIR):
                file_path = os.path.join(LOGS_DIR, filename)
                try:
                    # Remove files or directories
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  # Delete the file or symbolic link
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Delete the directory
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
            print("Logs directory cleared successfully.")
        else:
            print(f"Logs directory does not exist: {LOGS_DIR}")
    except Exception as e:
        print(f"Failed to clear logs directory: {e}")
# End of work on logs dir

# 2. Working on 'Work' folder
def delete_work():
    try:
        # Check if the logs directory exists or not
        if os.path.exists(WORK_DIR):
            # Loop over the files in the logs directory and remove them
            for filename in os.listdir(WORK_DIR):
                file_path = os.path.join(WORK_DIR, filename)
                try:
                    # Remove files or directories
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  # Delete the file or symbolic link
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Delete the directory
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
            print("work directory cleared successfully.")
        else:
            print(f"work directory does not exist: {WORK_DIR}")
    except Exception as e:
        print(f"Failed to clear work directory: {e}")
# End of work on work dir


# 3. Working on 'temp' folder
def delete_temp():
    try:
        # Check if the logs directory exists or not
        if os.path.exists(TEMP_DIR):
            # Loop over the files in the logs directory and remove them
            for filename in os.listdir(TEMP_DIR):
                file_path = os.path.join(TEMP_DIR, filename)
                try:
                    # Remove files or directories
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  # Delete the file or symbolic link
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Delete the directory
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
            print("temp directory cleared successfully.")
        else:
            print(f"temp directory does not exist: {TEMP_DIR}")
    except Exception as e:
        print(f"Failed to clear temp directory: {e}")
# End of work on 'temp' dir

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