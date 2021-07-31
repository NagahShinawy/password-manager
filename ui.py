"""
created by Nagaj at 31/07/2021
"""
from tkinter import Tk, Canvas


class PwdUI(Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def config(self, title, image=None, is_center=False, **kwargs):
        self.title(title)
        canvas = Canvas(self, width=200, height=224)
        canvas.grid(column=1, row=1)
        super().config(**kwargs)
        if is_center:
            self.__center()
        if image:
            self.iconbitmap(image)

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