class Button:
    def __init__(self, name: str):
        self._name = name

    def __str__(self):
        return f"<Button {self._name}>"


class Window:

    def __init__(self, buttons: list[Button]):
        self._buttons = buttons

    def show(self):
        print(f"Window; buttons: {', '.join([str(button) for button in self._buttons])}")
