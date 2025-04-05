import reflex as rx
from typing import List, Dict, Any

class Tasks(rx.State):
    # List of tasks
    tasks: List[Dict[str, Any]] = []
    new_task: str = ""

    def add_task(self):
        if self.new_task.strip() != "":
            # create a new unique id based on time
            
            import time
            id_task = int(time.time() * 1000) 

            self.tasks.append({

            })