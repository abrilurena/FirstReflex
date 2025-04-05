
import reflex as rx

class Estado(rx.State):
    x: int = 0

    def increment(self):
        self.x += 1
        return rx.vstack (
           rx.text(f"Contador: {Estado.x}"),
           rx.button("Incrementar", on_click=Estado.x)        
           )

def index() -> rx.Component:
    return rx.text("Hello, Reflex!")

app = rx.App()
app.add_page(index)
