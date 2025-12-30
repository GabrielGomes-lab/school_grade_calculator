import ttkbootstrap as tb
from view.gui import AppGUI

if __name__ == "__main__":
    root = tb.Window(themename="superhero")  # dark moderno
    app = AppGUI(root)
    root.mainloop()
