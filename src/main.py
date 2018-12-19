from simulation import *
import tkinter as tk
from gui import View


def start():
    root = tk.Tk()
    view = View(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()


def main():
    """    
    Entry point.
    """
    
    game = Simulation()
    start()
    
if __name__ == "__main__":
    main() 
    
