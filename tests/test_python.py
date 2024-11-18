"""
Tests for this week's exercises.
"""

import os
import sys
import io
import tempfile
import shutil

import subprocess



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


def test_CommandLineScript():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Add the exercise directory to the Python path
        exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "CommandLineScript"))
        sys.path.append(exercise_dir)
        
        from main import num_words
        
        # Test the num_words function with a sample string
        test_string = "This is a test string with eight words"
        result = num_words(test_string)
        assert result == 8, "num_words did not return the correct word count"
        
        # Create a temporary sample file for testing
        sample_file = os.path.join(temp_dir, "sample.txt")
        with open(sample_file, "w") as f:
            f.write("This is a test file.\nIt has multiple lines.\n")
        
        # Copy the main script to the temporary directory
        main_script_src = os.path.join(exercise_dir, "main.py")
        main_script_dst = os.path.join(temp_dir, "main.py")
        shutil.copy(main_script_src, main_script_dst)
        
        # Run the script using subprocess
        result = subprocess.run(
            ["python", "main.py", "sample.txt"],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        
        # Check that the script ran successfully
        assert result.returncode == 0, f"Script exited with an error: {result.stderr}"
        
        # Verify the output
        assert "The file has 9 words." in result.stdout, "Script output is incorrect"


def test_ArgparseScript():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Add the exercise directory to the Python path
        exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ArgparseScript"))
        sys.path.append(exercise_dir)
        
        # Create a temporary sample file for testing
        sample_file = os.path.join(temp_dir, "file1.txt")
        with open(sample_file, "w") as f:
            f.write("This is a test file.\nIt has multiple lines with the word test.\nTest this file.\n")

        # Copy the main script to the temporary directory
        main_script_src = os.path.join(exercise_dir, "main.py")
        main_script_dst = os.path.join(temp_dir, "main.py")
        shutil.copy(main_script_src, main_script_dst)
        
        # Run the script using subprocess with 'test' as the word
        result = subprocess.run(
            ["python", "main.py", "file1.txt", "test"],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        
        # Check that the script ran successfully
        assert result.returncode == 0, f"Script exited with an error: {result.stderr}"
        
        # Verify the output
        assert "The word test occurred 2 times" in result.stdout, "Script output is incorrect"

        # Run the script again with 'this' as the word
        result = subprocess.run(
            ["python", "main.py", "file1.txt", "this"],
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Check that the script ran successfully
        assert result.returncode == 0, f"Script exited with an error: {result.stderr}"

        # Verify the output
        assert "The word this occurred 1 times" in result.stdout, "Script output is incorrect"

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
    result = run_subprocess(sample_file)
    
    # Verify the output of the subprocess
    expected_output = "This is a test file.\nIt has multiple lines.\n"
    assert result == expected_output, "Subprocess did not return the correct output"
    
    # Clean up the sample file
    os.remove(sample_file)
