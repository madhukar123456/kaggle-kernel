import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask API is running!'

def run_terminal_commands(commands):
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True)
            print(f'Successfully ran command: {command}')
        except subprocess.CalledProcessError as e:
            print(f'Error running command {command}: {e}')
            

if __name__ == "__main__":
    # List of terminal commands to run
    commands_to_run = [
        'mkdir ~/.kaggle',
        'cp kaggle.json ~/.kaggle/',
        'chmod 600 ~/.kaggle/kaggle.json',
        'kaggle kernels push -p python-code/',
        # Add more commands as needed
    ]

    # Start running the terminal commands
    run_terminal_commands(commands_to_run)

    # Start the Flask API
    app.run(debug=True)