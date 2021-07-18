from pynput.keyboard import Key, Listener, Controller
import time


class ModelDMO:
    def __init__(self, dmo):
        self.listener = Listener(
            on_release=self.on_release)
        self.state = False
        self.dmo = dmo

    def on_release(self, key):
        """
        Method to get the release key in the keyboard
        :param key: Key released
        """
        print('{0} release'.format(
            key))
        if key == Key.esc:
            self.state = False
            self.stop_listener()

    def start_listener(self):
        """
        Start the keyboard listener
        """
        self.listener.start()
        self.state = True

    def stop_listener(self):
        """
        Stop the keyboard listener
        """
        self.listener.stop()

    def dmo_macro(self):
        """
        Init the macro until the user uses ESC
        """
        self.start_listener()
        keyboard = Controller()
        state = self.state
        while state:
            keyboard.press(Key.tab)
            is_color = self.dmo.compare_color()
            while is_color:
                keyboard.press('1')
                keyboard.release('1')
                time.sleep(0.5)
                keyboard.press('4')
                keyboard.release('4')
                time.sleep(0.5)

                is_color = self.dmo.compare_color()

            state = self.state
        self.stop_listener()
