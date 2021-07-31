"""
created by Nagaj at 31/07/2021
"""
from tkinter import Tk, Canvas, PhotoImage
from constants import CANVAS_WIDTH, CANVAS_HEIGHT, CANVAS_LOGO_PATH


class PwdUI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.canvas = None

    def config(self, title, image=None, is_center=False, **kwargs):
        self.title(title)
        super().config(**kwargs)
        if image:
            self.iconbitmap(image)

        if is_center:
            self.__center()

    def create_canvas(self):
        self.canvas = Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        pwd_manager_logo = PhotoImage(file=CANVAS_LOGO_PATH)
        self.canvas.create_image(100, 100, image=pwd_manager_logo)
        # self.canvas.grid(row=0, column=1)
        self.canvas.pack()

    def __center(self) -> None:
        """
        add window to the center of screen
        :return:
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (self["width"] / 2))
        y_cordinate = int((screen_height / 2) - (self["height"] / 2))
        self.geometry(f'{self["width"]}x{self["height"]}+{x_cordinate}+{y_cordinate}')

    def run(self):
        self.mainloop()
