
import reflex as rx
from myfirstreflex_app.state import Tasks

def tarea_item(task):
    return rx.hstack(
        rx.checkbox(
            is_checked = task["completed"],
            on_change=lambda:Tasks.change_task_status(task["id"]),
        ),
        rx.text(
            task["text"],
            text_decoration="line-through" if task["completed"] else "none",
            font_size="20px",
            color="white",
        ),
        rx.spacer(),
        rx.button(
            "Delete",
            on_click=lambda: Tasks.delete_task(task["id"]),
            color_scheme="red",
            color="white",
            background_color="red.500",
            width="100px",
            height="40px",
            border_buttom="1px solid white",
        ),
    )

def index():
    return rx.center(
        rx.vstack(
            rx.heading("Todo List"),
            rx.hstack(
                rx.input(
                    placeholder="Add a new task",
                    value=Tasks.new_task,
                    on_change=Tasks.set_new_task,
                ),
                rx.button(
                    "add",
                    on_click = Tasks.add_task,
                    color_scheme="teal",
                    color="white",
                    background_color="teal.500",
                ),
            ),
            rx.divider(),
            rx.vstack(
                rx.foreach(
                    Tasks.tasks,
                    tarea_item, 
                )
            ),
            rx.text(
                f"Total: {Tasks.tasks.id_task} tasks."
            )
        )
    )
app = rx.App()
app.add_page(index)
