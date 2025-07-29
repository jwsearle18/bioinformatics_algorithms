import os
import sys
import importlib.util
from typing import List, Tuple

def run_test(lesson: int, problem: int, function_name: str, args: List):
    """
    Runs a test for a given lesson and problem.

    Args:
        lesson: The lesson number.
        problem: The problem number.
        function_name: The name of the function to test.
        args: The arguments to pass to the function.
    """
    # Construct the path to the input and output files
    input_file = f"tests/lesson_{lesson}_{problem}_inputs/sample.txt"
    output_file = f"tests/lesson_{lesson}_{problem}_outputs/sample.txt"

    # Read the expected output
    with open(output_file, "r") as f:
        expected_output = f.read().strip()

    # Construct the path to the module
    module_path = f"src/lesson_{lesson}/{function_name}.py"

    # Load the module
    spec = importlib.util.spec_from_file_location(function_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get the function from the module
    function = getattr(module, function_name)

    # Run the function
    output = function(*args)

    # Compare the output to the expected output
    if str(output) == expected_output:
        print(f"Test for lesson {lesson}, problem {problem} passed!")
    else:
        print(f"Test for lesson {lesson}, problem {problem} failed!")
        print(f"Expected output: {expected_output}")
        print(f"Actual output: {output}")

def main():
    """
    Runs all the tests.
    """
    # Lesson 3, Problem 1
    with open("tests/lesson_3_1_inputs/sample.txt", "r") as f:
        lines = f.read().strip().splitlines()
        k = int(lines[0])
        d = int(lines[1])
        paired_reads = [tuple(line.split("|")) for line in lines[2:]]
    run_test(3, 1, "string_reconstruction_from_read_pairs", [paired_reads, k, d])

    # Lesson 4, Problem 1
    with open("tests/lesson_4_1_inputs/sample.txt", "r") as f:
        lines = f.read().strip().splitlines()
        s = lines[0]
        t = lines[1]
    run_test(4, 1, "local_alignment", [1, 1, 1, s, t])

    # Lesson 7, Problem 1
    with open("tests/lesson_7_1_inputs/sample.txt", "r") as f:
        lines = f.read().strip().splitlines()
        pi = lines[0]
        states = lines[2].split()
        trans_df = pd.read_csv(io.StringIO("\n".join(lines[4:])), sep="\t")
    run_test(7, 1, "prob_hidden_path", [pi, states, trans_df])

    # Lesson 7, Problem 2
    with open("tests/lesson_7_2_inputs/sample.txt", "r") as f:
        lines = f.read().strip().splitlines()
        x = lines[0]
        alphabet = lines[2].split()
        pi = lines[4]
        states = lines[6].split()
        emissions_df = pd.read_csv(io.StringIO("\n".join(lines[8:])), sep="\t")
    run_test(7, 2, "prob_outcome_given_hidden_path", [x, alphabet, pi, states, emissions_df])

    # Lesson 7, Problem 3
    with open("tests/lesson_7_3_inputs/sample.txt", "r") as f:
        lines = f.read().strip().splitlines()
        x = lines[0]
        alphabet = lines[2].split()
        states = lines[4].split()
        trans_df = pd.read_csv(io.StringIO("\n".join(lines[6:6+len(states)]-1)), sep="\t")
        emissions_df = pd.read_csv(io.StringIO("\n".join(lines[6+len(states):])), sep="\t")
    run_test(7, 3, "viterbi_algorithm", [x, alphabet, states, trans_df, emissions_df])

    # Lesson 7, Problem 4
    with open("tests/lesson_7_4_inputs/sample.txt", "r") as f:
        lines = f.read().strip().splitlines()
        x = lines[0]
        alphabet = lines[2].split()
        states = lines[4].split()
        trans_df = pd.read_csv(io.StringIO("\n".join(lines[6:6+len(states)]-1)), sep="\t")
        emissions_df = pd.read_csv(io.StringIO("\n".join(lines[6+len(states):])), sep="\t")
    run_test(7, 4, "outcome_likelihood", [x, alphabet, states, trans_df, emissions_df])

    # Lesson 7, Problem 5
    with open("tests/lesson_7_5_inputs/sample.txt", "r") as f:
        lines = f.read().strip().splitlines()
        threshold = float(lines[0])
        alphabet = lines[2].split()
        alignment = lines[4:]
    run_test(7, 5, "profile_hmm", [threshold, alphabet, alignment])

    # Lesson 7, Problem 6
    with open("tests/lesson_7_6_inputs/sample.txt", "r") as f:
        lines = f.read().strip().splitlines()
        threshold = float(lines[0])
        alphabet = lines[2].split()
        alignment = lines[4:]
    run_test(7, 6, "profile_hmm_with_pseudocounts", [threshold, alphabet, alignment])

if __name__ == "__main__":
    main()
