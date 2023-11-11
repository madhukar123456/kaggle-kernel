import subprocess

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
        'pip install kaggle',
        'mkdir ~/.kaggle',
        'cp kaggle.json ~/.kaggle/',
        'chmod 600 ~/.kaggle/kaggle.json',
        'kaggle kernels push -p python-code/',
        # Add more commands as needed
    ]

    # Call the function to run the commands
    run_terminal_commands(commands_to_run)
