import os
import time
import queue
import threading
task_queue = queue.Queue()
results = []
results_lock = threading.Lock()
stop_event = threading.Event()
def create_sample_files():
    files = {
        "file1.txt": "съешь же ещё этих мягких французских булок, да выпей чаю",
        "file2.txt": "The quick brown fox jumps over the lazy dog",
        "file3.txt": "Jackdaws love my big sphinx of quartz",
        "file4.txt": "omg lol nvm lol omg omg",
        "file5.txt": "A pangram or holoalphabetic sentence is a sentence using every letter of a given alphabet at least once"
    }
    for name, content in files.items():
        with open(name, 'w', encoding='utf-8') as f:
            f.write(content)
def producer():
    create_sample_files()
    files = [f for f in os.listdir() if f.endswith('.txt')]
    for file in files:
        if stop_event.is_set():
            break
        task_queue.put(file)
        print(f"Produced: {file}")
        time.sleep(0.5)
    task_queue.put(None)
