"""
created by Nagaj at 31/07/2021
"""
from constants import TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_LOGO_PATH
from ui import PwdUI

if __name__ == "__main__":
    ui = PwdUI()
    ui.config(
        title=TITLE,
        is_center=True,
        width=WINDOW_WIDTH,
        height=WINDOW_HEIGHT,
        image=WINDOW_LOGO_PATH,
        padx=50,
        pady=50,
    )
    ui.create_canvas()
    ui.run()
