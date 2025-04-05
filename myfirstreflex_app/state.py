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
                "id": id_task,
                "task": self.new_task,
                "completed": False
            })

            # clear the input field
            self.new_task = ""
    def change_task_status(self, id_task: int):
        for i, task in enumerate(self.tasks):
            if task["id"] == id_task:
                self.tasks[i]["completed"] = not self.task[i]["completed"]
                break
    def delete_task(self, id_task: int):
        self.tasks = [task for task in self.tasks if task["id"] != id_task]

    
