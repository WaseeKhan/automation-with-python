import subprocess
import sys

CATALINA_HOME = "/Users/waseem/Developer/servers/tomcat"
CATALINA_SCRIPT = f"{CATALINA_HOME}/bin/catalina.sh" 

# For Windows system replace with 'catlina.bat' in CATLINA_SCRIPT path

def start_tomcat():
    """Start the Tomcat server."""
    try:
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
    """Restart the Tomcat server."""
    stop_tomcat()
    start_tomcat()

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