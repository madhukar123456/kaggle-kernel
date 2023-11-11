import subprocess
from multiprocessing import Process
import time

def run_terminal_commands(commands):
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True)
            print(f'Successfully ran command: {command}')
        except subprocess.CalledProcessError as e:
            print(f'Error running command {command}: {e}')

def run_flask_app():
    from your_flask_app_module import app

    app.run(debug=True)

if __name__ == "__main__":
    # List of terminal commands to run
    commands_to_run = [
        'mkdir ~/.kaggle',
        'cp kaggle.json ~/.kaggle/',
        'chmod 600 ~/.kaggle/kaggle.json',
        'kaggle kernels push -p python-code/',
        # Add more commands as needed
    ]

     # Start the Flask API in a separate process
    flask_process = Process(target=run_flask_app)

    try:
        # Start running the terminal commands
        run_terminal_commands(commands_to_run)

        # Start the Flask API
        flask_process.start()

        # Allow some time for the Flask API to start (adjust as needed)
        time.sleep(2)

    except KeyboardInterrupt:
        pass
    finally:
        # Stop the Flask API process when done
        flask_process.terminate()