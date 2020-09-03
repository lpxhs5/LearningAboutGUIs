from guizero import App, Text

# create an app called 'app' and give it a name.
app = App(title='This is my first GUI')

# make app's background pink.
app.bg = 'pink'

# add a text message to the app named 'app'.
firstmessage = Text(app, text='guis are cool!')
secondmessage = Text(app, text='this is green')
thirdmessage = Text(app, text='I\'m a new message!')

# change the font size of message one
firstmessage.text_size = 40

# change the background colour of message two
secondmessage.bg = 'green'

# change text colour, font and text size on message three.
thirdmessage.text_color = 'purple'
thirdmessage.font = 'Comic Sans MS'
thirdmessage.text_size = 30

# display the app. Without this, the app won't show up.
app.display()