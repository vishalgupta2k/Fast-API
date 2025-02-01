import subprocess
import os

def run_scripts():
    # Activate virtual environment
    activate_script = os.path.join("env", "Scripts", "activate")
    activate_command = f'cmd /k "{activate_script} & fastapi dev src/"'
    
    # Run the command
    subprocess.run(activate_command, shell=True)

if __name__ == "__main__":
    run_scripts()