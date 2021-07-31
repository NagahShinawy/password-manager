"""
created by Nagaj at 31/07/2021
"""
from ui import PwdUI


if __name__ == '__main__':
    ui = PwdUI()
    ui.config(title="Password Manager", is_center=True, width=500, height=300, image="./static/logo.ico")
    ui.run()
