from concurrent.futures import ThreadPoolExecutor
import threading
import time

def process_student(student):
    """Calculate a student's total, average, and result."""
    name, marks = student

    # Simulate a task that takes some time.
    time.sleep(1)

    total = sum(marks)
    average = total / len(marks)
    status = "Pass" if average >= 50 else "Fail"

    print(f"Processed {name} using {threading.current_thread().name}")

    return {
        "name": name,
        "total": total,
        "average": average,
        "status": status,
    }

def main():
    students = [
        ("Ali", [75, 80, 68]),
        ("Sara", [90, 85, 92]),
        ("Ahmed", [40, 55, 48]),
        ("Ayesha", [65, 70, 72]),
        ("Usman", [35, 42, 38]),
    ]

    print("Starting parallel student result processing...\n")

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(process_student, students))

    print("\nStudent Results")
    print("-" * 55)

    for result in results:
        print(
            f"Name: {result['name']:<8} "
            f"Total: {result['total']:<4} "
            f"Average: {result['average']:.2f} "
            f"Result: {result['status']}"
        )

    print("\nAll student records processed successfully.")


if __name__ == "__main__":
    main()
