import tkinter
from tkinter import messagebox
class EQOrderGUI:
    def __init__(self):
        # Create Main Window
        self.main_window = tkinter.Tk()

        # Create Frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        # Create labels and entry boxes
        self.report_Label = tkinter.Label(self.top_frame, \
                                          text = 'Report:')
        self.form_Label = tkinter.Label(self.middle_frame, \
                                        text = 'Form:')
        

        self.report_entry = tkinter.Entry(self.top_frame,\
                                          width = 10)
        self.form_entry = tkinter.Entry(self.middle_frame, \
                                        width = 10)

        # Create Buttons
        self.report_button = tkinter.Button(self.top_frame, \
                                        text = 'Browse')
        self.form_button = tkinter.Button(self.middle_frame, \
                                          text = 'Browse')
        self.build_button = tkinter.Button(self.bottom_frame, \
                                           text = 'Build')

        self.report_Label.pack(side = 'left')
        self.form_Label.pack(side = 'left')

        self.report_entry.pack(side = 'left')
        self.form_entry.pack(side = 'left')

        self.report_button.pack(side = 'left')
        self.form_button.pack(side = 'left')
        self.build_button.pack()

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()





        #Enter main loop
        tkinter.mainloop()
        
EqOrderGUI = EQOrderGUI()     
