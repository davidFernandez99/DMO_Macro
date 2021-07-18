from pynput import mouse


class ClickListener:
    def __init__(self):
        self.listener = mouse.Listener(
            on_click=self.on_click)
        self.state = False
        self.coordinates = []

    def on_click(self, x, y, button, pressed):
        """
        Method to get the click over the screen with the mouse
        :param x: Coordinate x
        :param y: Coordinate y
        :param button: Button
        :param pressed: If is pressed or realeased
        """
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            self.coordinates = [x, y]
            self.stop_listener()
            self.state = False

    def start_listener(self):
        """
        Start the mouse listener
        """
        try:
            self.listener.start()
        except Exception as ex:
            self.listener = mouse.Listener(
                on_click=self.on_click)
            self.listener.start()

        self.state = True

    def stop_listener(self):
        """
        Stop the mouse listener
        """
        self.listener.stop()

    def get_state(self):
        """
        Get if the listener is started or finished
        :return True if state is startes and False if is finished
        """
        return self.listener.s
