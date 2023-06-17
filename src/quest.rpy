init python:

## This class lets the dev create some events for his game. By default, all the events have the 
## pending state and are hidden.
    class Quest:
        def __init__(self, id, title, category,  state= "pending"):
            self.id = id
            self.title = title
            self.category = category
            self.state = state

        def __repr__(self):
            return "<{}>".format(self.title)