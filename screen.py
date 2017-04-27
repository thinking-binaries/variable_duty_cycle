# screeny.py  02/03/2017  D.J.Whale
#
# A simple plottable canvas.
# Written using Tkinter, but without any background looping requirements.
# works a bit like a BBC micro screen!
# Great for using in programs where you don't want Tkinter to take over top loop.

try:
    import Tkinter as tk # python2
except ImportError:
    import tkinter as tk # python3


class Screen():
    OFF            = "#FFFFFF" # black
    ON             = "#000000" # white
    DEFAULT_WIDTH  = 640
    DEFAULT_HEIGHT = 480

    @staticmethod
    def create_canvas(width=None, height=None, left=None, top=None):
        root = tk.Tk()
        root.attributes('-alpha', 0.0) #For icon
        root.iconify()

        window = tk.Toplevel(root)
        if left is not None and top is not None:
            window.geometry("%dx%d+%d+%d" % (width, height, left, top))
        else:
            window.geometry("%dx%d" % (width, height))
        window.overrideredirect(1)

        canvas = tk.Canvas(window, width=width, height=height, bg='white')
        canvas.pack()
        canvas.my_window = window
        canvas.my_window.my_root = root
        canvas.my_window.update() # cause canvas to draw
        return canvas

    def __init__(self, width=None, height=None, left=None, top=None):
        if width  is None: width  = Screen.DEFAULT_WIDTH
        if height is None: height = Screen.DEFAULT_HEIGHT
        self.canvas = self.create_canvas(width, height, left, top)
        self.width  = width
        self.height = height
        self.x = None
        self.y = None

    def start(self):
        self.canvas.my_window.update() # cause canvas to draw
        self.draw_backdrop()

    def update(self):
        self.canvas.my_window.my_root.update_idletasks()

    #TODO: enable/disable auto updates (for flicker-free operation)
    #TODO: def clear() just create_rect(width, height)
    #TODO: set_pen_colour()
    #TODO: line()
    #TODO: circle()
    #TODO: arc()
    #TODO: text()
    #TODO: rect(with fill)
    #TODO: def stop()

    def draw_backdrop(self):
        pass # nothing to do?
        #TODO could draw x and y axies here
        # horizontal line
        #self.canvas.create_line(left, midx, right, midy)
        # vertical line
        #self.canvas.create_line(midx, top, midx, bottom)
        #self.update()

    def goto(self, x, y):
        self.x = x
        self.y = y

    def plot(self, x, y, fill=None):
        if fill is None: fill = self.ON
        self.canvas.create_rectangle(x, y, x, y, fill=fill)
        self.update()

    def line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, fill=self.ON)
        self.x = x2
        self.y = y2

    def line_to(self, x, y):
        if self.x is None or self.y is None:
            self.goto(x, y)
        else:
            self.line(self.x, self.y, x, y)
            self.x = x
            self.y = y

#----- TEST HARNESS -----------------------------------------------------------

if __name__ == "__main__":
    s = Screen()
    for i in range(0, 100):
        s.plot(i, i)

    raw_input("finished?")

# END

