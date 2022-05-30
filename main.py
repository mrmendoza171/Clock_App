from configuration import *
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from datetime import datetime
import pytz
from frames.dashboard import Dashboard
from frames.settings import Settings


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.root_startup()
        self.create_menus()
        self.interface = Interface(self)
        self.interface.grid(row=0, column=0)


    def root_startup(self):
        self.title("Digital Clock")
        self.config(bg=BACKGROUND)

        aspect_ratio = 16/9
        height = 600
        width = int(height * aspect_ratio)

        # Centers root window
        positionRight = int(self.winfo_screenwidth() / 2 - width / 2)
        positionDown = int(self.winfo_screenheight() / 2 - height / 2)
        self.geometry(f"+{positionRight}+{positionDown}")
        size = f"{width}x{height}"
        self.geometry(size)

        # Allows frame to be centered
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Set icon for window
        # im = ImageTk.PhotoImage(file=os.path.join(BASE_URL,'assets','images','clock_icon.png'))
        # self.iconphoto(False, im)




    def create_menus(self):
        header_menu = Menu(self)
        self.config(menu=header_menu)

        edit_menu = Menu(header_menu, tearoff=False)
        header_menu.add_cascade(label='Settings', menu=edit_menu)
        edit_menu.add_command(label='Customize Theme', command='')

        def right_click_popup(e):
            click_menu.tk_popup(e.x_root, e.y_root)

        click_menu = Menu(self, tearoff=False)
        click_menu.add_command(label='Customize Theme', command='')
        click_menu.add_separator()
        click_menu.add_command(label='Exit', command=lambda: Interface.exit_script(self))
        self.bind('<Button-3>', right_click_popup)





class Interface(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Clock App started, launching startup_script...\n")

        main_frame = Frame(self, bg=TERTIARY)
        main_frame.grid(row=0, column=0)

        center_column = Frame(main_frame, bg=TERTIARY)
        center_column.grid(row=0, column=1)
        header_frame = Frame(center_column, bg=TERTIARY)
        header_frame.grid(row=0, column=0)


        self.home_frame = ttk.Notebook(center_column)
        self.home_frame.grid(row=1, column=0)
        dashboard_tab = Frame(self.home_frame, bg=TERTIARY)
        dashboard_tab.grid(row=0, column=0)
        settings_tab = Frame(self.home_frame, bg=TERTIARY)
        settings_tab.grid(row=0, column=0)


        self.home_frame.add(dashboard_tab, text="Dashboard")
        self.home_frame.add(settings_tab, text="Settings")
        self.navigate_tab(1)

        dashboard_app = Dashboard(dashboard_tab)
        dashboard_app.grid(row=0, column=0)
        settings_app = Settings(settings_tab)
        settings_app.grid(row=0, column=0)

    def navigate_tab(self, tab_num):
        self.home_frame.select(tab_num)

    def exit_script(self):
        print("Shutting down...")
        self.quit()





if __name__ == '__main__':
    now = datetime.now(tz=pytz.UTC)
    timenow = datetime.strftime(now, date_format_print)
    print(f"Current time: {timenow}")

    root = Root()
    root.mainloop()















