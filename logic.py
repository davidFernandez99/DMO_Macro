from click_listener import ClickListener
from dmo import DMO
from model import ModelDMO

if __name__ == "__main__":
    end = True
    d = DMO()
    model = ModelDMO(d)
    click_mouse = ClickListener()
    while end:
        print("""
        1. Set Digimon -> Click with mouse at the color of the digimon in the screen.
        2. Start script -> Bot start (previously set the digimon), use ESC to end it.
        3. Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            print("\n Click over the pixel of the digimon")
            click_mouse.start_listener()
            state = click_mouse.state
            while state:
                state = click_mouse.state
            d.set_color(click_mouse.coordinates)
            print("\n Digimon set")
        elif ans == "2":
            print("\n Bot started")
            model.dmo_macro()
        elif ans == "3":
            print("\n Goodbye")
            end = False
        else:
            print("\n Not Valid Choice, Try again")
