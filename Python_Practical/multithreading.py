import threading
import time

# Function to print numbers
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Simulate a delay

# Function to print alphabets
def print_alphabets():
    for char in 'ABCDE':
        print(f"Alphabet: {char}")
        time.sleep(1)  # Simulate a delay

# Function to print a message repeatedly
def print_message():
    for i in range(1, 6):
        print(f"Message: Hello from thread {i}")
        time.sleep(1)  # Simulate a delay

# Main program
def main():
    # Create threads for different tasks
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_alphabets)
    thread3 = threading.Thread(target=print_message)

    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    print("All threads have completed execution.")

if __name__ == "__main__":
    main()
