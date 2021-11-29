class Home_Category:
    _slots_ = ["_name", "code", "_price"]

    def _init_(self, name, code, price):
        self.__name = name
        self.__code = code
        self.__price = price

    def garden_search(self, name, code):
        GARDEN={"p": ("3 pack garden flower", 5.0), "l": ("Hanging light wire", 10.0), "b": ("Garden bench", 35.0)}

        for i in GARDEN.keys():
            if i==code or GARDEN[i][0]==name:
                self.__name=name
                self.__code=code
                self.__price=GARDEN[i][1]

    def indoor_search(self, name, code):
        INDOOR={"t": ("Small table lamp", 5.0), "f1": ("City picture frame", 7.0), "r": ("4x5 entry rug", 35.0),"f2": ("flower vase", 14.0)}

        for i in INDOOR.keys():
            if i==code or INDOOR[i][0]==name:
                self.__name=name
                self.__code=code
                self.__price=INDOOR[i][1]

    def bathroom_search(self, name, code):
        BATHROOM={"s": ("Soap holder", 5.0), "c": ("Shower Curtain", 5.0), "m": ("anti-skid doormat", 30.0)}

        for i in BATHROOM.keys():
            if i==code or BATHROOM[i][0]==name:
                self.__name=name
                self.__code=code
                self.__price=BATHROOM[i][1]

class Home_Avatar:
    _slots_ = ["_garden", "indoor", "bathroom", "_total_price"]

    def _init_(self, garden, indoor, bathroom, price):
        self.__garden=garden
        self.__indoor=indoor
        self.__bathroom=bathroom
        self.__total_price=price

    def order_price(self, price):
        self.__total_price+=price

    def get_price(self):
        return self.__total_price



