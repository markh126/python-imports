from appliances.appliance import Appliance

class Stove(Appliance):

    def __init__(self, color, heat_method="electric"):
        super().__init__(color)

    def heat_soup(self):
        print("This soup is piping hot!")
