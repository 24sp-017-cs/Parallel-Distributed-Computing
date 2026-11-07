# Task 3: Process-Based Parallelism in Python

## Objective

The objective of this task is to demonstrate process-based parallelism using Python's `multiprocessing` module.

## Topic

**Process-Based Parallelism — Multiprocessing Pool**

This assignment demonstrates the use of multiple worker processes to perform independent calculations concurrently.

## Description

The program processes six sales records. Each record contains a product name, quantity sold, and unit price.

For each record, the program:

- Calculates the product's total revenue.
- Identifies the worker process that handled the record.
- Returns the calculated result to the main process.
- Displays a sales revenue report.
- Calculates the total revenue for all products.

A pool of three worker processes is used to distribute the tasks.

## Python Concepts Used

### 1. multiprocessing.Pool

`Pool(processes=3)` creates a pool of three worker processes.

### 2. pool.map()

`pool.map()` distributes the sales records to the worker processes and collects the results in the original input order.

### 3. Functions

The `calculate_revenue()` function calculates the revenue for each product.

### 4. Process Identification

`current_process().name` identifies the worker process handling each task.

### 5. Multiprocessing Entry-Point Guard

The condition `if __name__ == "__main__":` ensures that the main program starts only when the file is executed directly. This is important for safe multiprocessing behavior across platforms.

## Requirements

- Python 3.7 or later
- No external Python packages required

## How to Run

Open a terminal inside the Task 3 folder and run:

```bash
python3 multiprocessing_example.py
```

## Expected Results

The program calculates the following revenues:

| Product | Quantity | Unit Price (PKR) | Revenue (PKR) |
|---|---:|---:|---:|
| Laptop | 5 | 150,000 | 750,000 |
| Mouse | 20 | 1,500 | 30,000 |
| Keyboard | 10 | 3,500 | 35,000 |
| Monitor | 4 | 45,000 | 180,000 |
| Headphones | 8 | 5,000 | 40,000 |
| Printer | 3 | 25,000 | 75,000 |

**Total Revenue: PKR 1,110,000**

Worker process names and the order of processing messages may vary between runs. The final sales results remain in the original input order.

## Conclusion

This task demonstrates how Python's multiprocessing module can distribute independent calculations among multiple processes. Process-based parallelism can be beneficial for CPU-bound workloads because separate processes can execute Python code on multiple CPU cores, subject to available hardware and workload characteristics.
