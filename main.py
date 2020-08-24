# Learning Object Orientated Programming (version 0.2)
from tkinter import *

# Window Defaults
app_title = 'Learning OOP!'
win_size = '500x500'
bg_color = '#fff'
fg_color = '#269269'

# main function
def main():
    
    app = Tk()
    gui = Main(app)
    gui.app.mainloop()


# Main class
class Main():

    # Initialize
    def __init__(self, win):

        # App Window Defaults
        self.app = win
        self.app.title(app_title)
        self.app.geometry(win_size)
        self.app.config(bg=bg_color)

        # Header Frame
        self.header_frame = Frame(self.app, bg=bg_color)
        self.header_frame.pack(ipady=20)

        # Header Label
        self.title_label = Label(self.header_frame, text='Hello', bg=bg_color, fg=fg_color)
        self.title_label.pack(side='left', padx=(0,20), pady=20)

        # Button to change color of header_frame, title_label and change text, also..
        # Button (invokes "change" method)
        self.change_btn = Button(self.header_frame, text='Change Color', \
                                 bg=fg_color, fg=bg_color, relief='flat', command=self.change)
        self.change_btn.pack(side='left', pady=20)

    # Change Method
    def change(self):
        """
            We are creating a loop here..
            When we clicked the (Change Color) button, we invoked this (change) method here,
            the last line of this method is the button invoking the (change_back) method,
            "just below", which in turn changes colors back to default settings.
            The last line in the (change_back) method, invokes this (change) method.
            (we are looping).
        """

        # Change Back Method
        def change_back():

            # Change settings back to default
            self.app.config(bg=bg_color)
            self.header_frame.config(bg=bg_color)
            self.title_label.config(text='Hello', bg=bg_color, fg=fg_color)
            # Button (invokes "change" method)
            self.change_btn.config(text='Change Color', bg=fg_color, fg=bg_color, \
                                   command=self.change)


        # Change colors and text
        self.app.config(bg=fg_color)
        self.header_frame.config(bg=fg_color)
        self.title_label.config(text='OOP!', bg=fg_color, fg=bg_color)
        # Button (invokes "change_back" method)
        self.change_btn.config(text='Change Back', bg=bg_color, fg=fg_color, \
                               command=change_back)


if __name__ == '__main__':
    # Invoke "main" function
    main()
