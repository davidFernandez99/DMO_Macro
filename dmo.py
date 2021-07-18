import pyautogui
import numpy


class DMO:
    def __init__(self):
        self.coordinates = [0, 0]
        self.color = numpy.zeros(shape=(1, 1, 3))

    def set_color(self, coordinates):
        """
        Method to set the color of a point in the screen in RGB
        :param coordinates: Coordinates to obtain the color
        """
        try:
            self.coordinates = coordinates
            x = coordinates[0]
            y = coordinates[1]
            screenshot = pyautogui.screenshot(region=(x, y, 1, 1))
            image = numpy.asarray(screenshot)
            if image.shape == (1, 1, 3):
                self.color = image
            else:
                print("Error with image format")
        except Exception as ex:
            print(ex)

    def get_color(self):
        """
        Method to obtain the color set in DMO
        :return: Color set at this moment
        """
        return self.color

    def compare_color(self):
        """
        Method to obtain if the color of self.coordinates is equal right now to self.color
        :return: True if is equal, False otherwise
        """
        try:
            x = self.coordinates[0]
            y = self.coordinates[1]
            screenshot = pyautogui.screenshot(region=(x, y, 1, 1))
            image = numpy.asarray(screenshot)
            if image.shape == (1, 1, 3):
                return True if numpy.array_equal(image, self.color) else False

            else:
                print("Error with image format")
        except Exception as ex:
            print(ex)
