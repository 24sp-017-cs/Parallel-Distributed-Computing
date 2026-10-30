
# Task 2: Thread-Based Parallelism in Python

## Objective

The objective of this task is to demonstrate thread-based parallelism in Python by processing multiple student records concurrently using `ThreadPoolExecutor`.

## Topic

**Thread-Based Parallelism — Thread Pool**

This example is based on the thread-based parallelism concepts covered in Chapter 2 of the Python Parallel Programming Cookbook, Second Edition.

## Description

The program processes the marks of five students. Each student has three subject marks.

For every student, the program calculates:

- Total marks
- Average marks
- Pass or fail status

A student passes if their average is 50 or higher.

The program uses a thread pool with three workers. Each worker processes a student's record, and the results are displayed after all tasks have completed.

## Python Concepts Used

### 1. ThreadPoolExecutor

`ThreadPoolExecutor(max_workers=3)` creates a pool that can run up to three tasks concurrently.

### 2. executor.map()

`executor.map()` submits the student records for processing and collects the results in the same order as the input records.

### 3. Functions

The `process_student()` function calculates the total, average, and result for each student.

### 4. Threading

The `threading.current_thread().name` expression displays which worker thread processed each student.

### 5. Conditional Statements

The program uses a conditional expression to determine whether a student passes or fails.

## Requirements

- Python 3.7 or later
- No external Python packages required

## How to Run

Open a terminal in the Task 2 folder and execute:

```bash
python3 thread_pool_example.py
```

## Example Output

```text
Starting parallel student result processing...

Processed Ali using ThreadPoolExecutor-0_0
Processed Sara using ThreadPoolExecutor-0_1
Processed Ahmed using ThreadPoolExecutor-0_2
Processed Ayesha using ThreadPoolExecutor-0_0
Processed Usman using ThreadPoolExecutor-0_1

Student Results
-------------------------------------------------------
Name: Ali      Total: 223  Average: 74.33 Result: Pass
Name: Sara     Total: 267  Average: 89.00 Result: Pass
Name: Ahmed    Total: 143  Average: 47.67 Result: Fail
Name: Ayesha   Total: 207  Average: 69.00 Result: Pass
Name: Usman    Total: 115  Average: 38.33 Result: Fail

All student records processed successfully.
```

**Note:** Worker thread names and the order of the processing messages may vary between runs. The student results remain in the original input order.

## Conclusion

This task demonstrates how Python's `ThreadPoolExecutor` can manage multiple independent tasks concurrently. Thread pools are particularly useful for I/O-bound workloads, where tasks spend time waiting for operations to complete. The example also demonstrates task submission, result collection, and worker thread identification.
