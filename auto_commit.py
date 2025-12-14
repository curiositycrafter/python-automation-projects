import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

LAST = 0
DELAY = 5

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        global LAST
        if event.is_directory:
            return
        if event.src_path.endswith("auto_commit_on_save.py"):
            return
        now = time.time()
        if now - LAST < DELAY:
            return

        LAST = now
        msg = f"auto save {datetime.now().strftime('%H:%M:%S')}"

        os.system("git add .")
        os.system(f'git commit -m "{msg}"')
        os.system("git push")

observer = Observer()
observer.schedule(Handler(), ".", recursive=True)
observer.start()

print("✅ Watching → auto commit → auto push")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
