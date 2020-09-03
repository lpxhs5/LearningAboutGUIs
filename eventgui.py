# Import the GUI widgets that you'll be using, and create the 'app' for your program.
from guizero import App, TextBox, PushButton, Text, info
app = App()

# Function definitions for your events go here.
def btn_go_clicked():
    info("Greetings","Hello, " + txt_name.value + " - I hope you're having a nice day")

def highlight():
    txt_name.bg = 'light blue'

def lowlight():
    txt_name.bg = None

# Your GUI widgets go here
lbl_name = Text(app, text="Hello. What's your name?")
txt_name = TextBox(app)

# makes it so that the textbox is highlighted blue when mouse hovers over it.
txt_name.when_mouse_enters = highlight
txt_name.when_mouse_leaves = lowlight

# command tells the push button which function to run when it is clicked.
btn_go = PushButton(app, command=btn_go_clicked, text="Done")

# Show the GUI on the screen
app.display()