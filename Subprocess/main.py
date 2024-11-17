"""
Subprocess exercise.

Using subprocesses to execute commands.

The `subprocess` module in Python allows you to run shell commands from your Python code.
You can use this module to interact with the command line and capture the output of commands.

You should implement the function `run_subprocess` that uses a subprocess to execute a bash command 
(such as `cat`) to read the contents of `sample.txt` and store the output in the variable `text`. 
The function should return `text`.
"""

# You will need to add an import


def run_subprocess():
    pass


if __name__ == '__main__':
    # Main for demonstration

    # Call the function to execute the subprocess
    result = run_subprocess()

    # Print the contents of the file
    print(f"Contents of sample.txt:\n{result}")
