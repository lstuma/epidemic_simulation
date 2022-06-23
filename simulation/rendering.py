import pyglet


class Window(pyglet.window.Window):

    def __init__(self, width, height, caption='Window', resizable=False):
        # Instantiate window
        super().__init__(width=width, height=height, caption=caption, resizable=resizable)
        # Batch of objects that will be drawn in the window
        self.batch = pyglet.graphics.Batch()

    def on_draw(self):
        # Clear window before drawing
        self.clear()
        # Draw the batch
        self.batch.draw()


def getLayer(layer):
    return pyglet.graphics.OrderedGroup(layer)

def run_app():
    # Run app
    pyglet.app.run()

class Circle(object):
    def __init__(self, **kwargs):
        # All properties of the circle
        self.properties = dict()
        """
        position    : center position of circle\n
        radius      : radius of circle\n
        batch       : batch with which the circle will be rendered\n
        layer       : layer (group) on which the circle will be rendered\n
        color       : color of circle\n
        """

        # Configure the circle
        self.configure(**kwargs)

    def configure(self, **kwargs):
        # Update all properties passed by the arguments
        for arg_key, arg_value in kwargs.items():
            self.properties[arg_key] = arg_value

        try:
            # Create new shape object
            self.shape = pyglet.shapes.Circle(self.properties['position'][0], self.properties['position'][1], radius=self.properties['radius'], batch=self.properties['batch'], group=getLayer(self.properties['layer']), color=self.properties['color'])
        except Exception as e:
            # Error message
            print(f'ERROR: Could not create circle shape: {e}')

        # Set opacity
        if self.properties['opacity']:
            try:
                self.shape.opacity = self.properties['opacity']
            except Exception as e:
                # Error message
                print(f'ERROR: Could not set opacity of circle: {e}')
