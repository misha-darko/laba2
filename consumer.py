import time
import queue
from producer import task_queue, results, results_lock, stop_event
def consumer(name):
    while not stop_event.is_set():
        try:
            task = task_queue.get(timeout=1)
            if task is None:
                task_queue.put(None)
                break
            with open(task, 'r', encoding='utf-8') as f:
                text = f.read()
                words = text.split()
                avg_length = sum(len(w) for w in words) / len(words) if words else 0
                text_lower = text.lower()
                vowels = sum(1 for _ in text_lower if _ in 'aeiouyаеёиоуыэюя')
                consonants = sum(1 for _ in text_lower if _.isalpha() and _ not in 'aeiouyаеёиоуыэюя')
            with results_lock:
                results.append((task, round(avg_length, 2), vowels, consonants))
            print(f"{name} processed: {task}")
            time.sleep(0.5)
        except queue.Empty:
            continue
