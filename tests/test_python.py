"""
Tests for this week's exercises.
"""

import os
import sys
import io


def test_EnvironmentVariables():
    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "EnvironmentVariables"))
    sys.path.append(exercise_dir)
    
    from main import set_my_var
    
    # Ensure the environment variable is not set before testing
    if 'my_var' in os.environ:
        del os.environ['my_var']
    
    # Call the function to set the environment variable
    result = set_my_var()
    
    # Check that the environment variable is correctly set
    assert 'my_var' in os.environ, "'my_var' was not set in the environment"
    assert os.environ['my_var'] == 'value', "Environment variable 'my_var' has the wrong value"
    assert result == 'value', "Function did not return the correct value"


def test_Subprocess():
    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Subprocess"))
    sys.path.append(exercise_dir)
    
    from main import run_subprocess
    
    # Create a sample file for testing
    sample_file = os.path.join(exercise_dir, "sample.txt")
    with open(sample_file, "w") as f:
        f.write("This is a test file.\nIt has multiple lines.\n")
    
    # Run the subprocess function
    result = run_subprocess()
    
    # Verify the output of the subprocess
    expected_output = "This is a test file.\nIt has multiple lines.\n"
    assert result == expected_output, "Subprocess did not return the correct output"
    
    # Clean up the sample file
    os.remove(sample_file)


def test_CommandLineScript():
    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "CommandLineScript"))
    sys.path.append(exercise_dir)
    
    from main import num_words
    
    # Test the num_words function with a sample string
    test_string = "This is a test string with six words"
    result = num_words(test_string)
    assert result == 6, "num_words did not return the correct word count"
    
    # Create a sample file for testing
    sample_file = os.path.join(exercise_dir, "sample.txt")
    with open(sample_file, "w") as f:
        f.write("This is a test file.\nIt has multiple lines.\n")
    
    # Simulate running the script with sys.argv
    sys.argv = ["main.py", sample_file]
    from main import __main__ as main_script
    
    # Redirect stdout to capture the script's output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        main_script()
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Verify the output
    assert "The file has 8 words." in output, "Script output is incorrect"
    
    # Clean up the sample file
    os.remove(sample_file)


def test_ArgparseScript():
    # Add the exercise directory to the Python path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ArgparseScript"))
    sys.path.append(exercise_dir)
    
    from main import num_words  # Reuse the num_words function for simplicity
    
    # Test the num_words function with a sample string
    test_string = "Another test string with five words"
    result = num_words(test_string)
    assert result == 5, "num_words did not return the correct word count"
    
    # Create a sample file for testing
    sample_file = os.path.join(exercise_dir, "sample.txt")
    with open(sample_file, "w") as f:
        f.write("Test file for argparse.\nAnother line.\nLine items here.\n")
    
    # Simulate running the script with argparse
    sys.argv = ["main.py", sample_file, "line"]
    from main import __main__ as main_script
    
    # Redirect stdout to capture the script's output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        main_script()
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Verify the output (case-sensitive partial match for "line")
    assert "The word line occurred 3 times" in output, "Script output is incorrect"
    
    # Clean up the sample file
    os.remove(sample_file)
