import tkinter as tk
from tkinter import ttk
import widgets as wg

class AddGoal(wg.NormalFrame):
    '''GUI frame to add goals'''
    def __init__(self, parent, *args, **kwargs):
       
        importance = tk.StringVar()
        completion = tk.StringVar()
        
        wg.NormalFrame.__init__(self, parent, *args, **kwargs)

        # Goals
        wg.TextLabel(self, text="Goal Parent").grid(column=1, row=1)
        wg.TextLabel(self, text="Goal"       ).grid(column=1, row=2)
        wg.TextLabel(self, text="Outcome"    ).grid(column=1, row=3)
        goal_parent   = wg.ShortResponse(self)
        goal_main     = wg.ShortResponse(self)
        goal_outcome  = wg.LongResponse (self)
        goal_parent  .grid(column=2, row=1)
        goal_main    .grid(column=2, row=2)
        goal_outcome .grid(column=2, row=3)
        
        
        # Importance
        wg.HLine(self).grid(column=1, row=10)
        
        wg.TextLabel(self, text="Importance").grid(column=1, row=11, pady=(5,2))
        impt_high   = wg.CircleButton(self)
        impt_medium = wg.CircleButton(self)
        impt_low    = wg.CircleButton(self)
        impt_high  .configure(text="High", variable=importance, value="high")
        impt_medium.configure(text="Medium", variable=importance, value="medium")
        impt_low   .configure(text="Low", variable=importance, value="low")
        impt_high  .grid(column=2, row=11)
        impt_medium.grid(column=2, row=12) 
        impt_low   .grid(column=2, row=13) 


        # Completion
        wg.HLine(self).grid(column=1, row=20)

        wg.TextLabel(self, text="Completion").grid(column=1, row=21, pady=(5,2))
        compl_high   = wg.CircleButton(self)
        compl_medium = wg.CircleButton(self)
        compl_low    = wg.CircleButton(self)
        compl_high  .configure(text="Not started", variable=completion, value="none")
        compl_medium.configure(text="In progress", variable=completion, value="some")
        compl_low   .configure(text="Completed"  , variable=completion, value="all")
        compl_high  .grid(column=2, row=21)
        compl_medium.grid(column=2, row=22) 
        compl_low   .grid(column=2, row=23) 
  
        # Dates

        wg.HLine(self).grid(column=1, row=30)

        wg.TextLabel(self, text="Start by date").grid(column=1, row=31)
        wg.TextLabel(self, text="End by date").grid(column=1, row=32)
        start_date = wg.ShortResponse(self)
        end_date   = wg.ShortResponse(self)
        start_date.grid(column=2, row=31)
        end_date  .grid(column=2, row=32)
        
        SaveButton(main_frame, text="Save", command=self.save).grid(column=1, row=100, sticky ="ns", columnspan=2)
        
        
        
        
def main():
    root = tk.Tk()
    goal_frame = AddGoal(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()