import threading
import time
from producer import producer, stop_event, results
from consumer import consumer
def main():
    producer_thread = threading.Thread(target=producer)
    consumers = []
    for i in range(3):
        _ = threading.Thread(target=consumer, args=(f"Consumer-{i + 1}",))
        consumers.append(_)
    producer_thread.start()
    for _ in consumers:
        _.start()
    producer_thread.join()
    time.sleep(2)
    stop_event.set()
    for _ in consumers:
        _.join()
    total_vowels = 0
    total_consonants = 0
    for file, avg_len, vowels, cons in results:
        print(f"\n{file}:")
        print(f"Avg word length: {avg_len}")
        print(f"Vowels: {vowels}")
        print(f"Consonants: {cons}")
        total_vowels += vowels
        total_consonants += cons
    print(f"Total vowels: {total_vowels}")
    print(f"Total consonants: {total_consonants}")
    print(f"Vowels/Consonants ratio: {total_vowels / total_consonants:.2f}")
if __name__ == "__main__":
    main()
