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

# y=Home_Avatar([],[],[],50)
# y.order_price(50)
# print(y.get_price())

def garden_options():
    Garden_items={"3 pack garden flower (p)": "$5.0", "Hanging light wire (l)": "$10.0", "Garden bench (b)": "$35.0", "None and next (n)": "$0.0"}
    print("Garden options:")
    for i in Garden_items.keys():
        print(i, end=": ")
        print(Garden_items[i], end="  ")

def indoor_options():
    Indoor_items={"Small table lamp (t)": "$5.0", "City picture frame (f1)": "$7.0", "4x5 entry rug (r)": "$35.0","flower vase (f2)": "$14.0", "None and next (n)": "$0.0"}

    print("Indoor options")
    for i in Indoor_items.keys():
        print(i, end=": ")
        print(Indoor_items[i], end="  ")

def bathroom_options():
    Bathroom_items={"Soap holder (s)": "$5.0", "Shower Curtain (c)": "$5.0", "Anti-skid doormat (m)": "$30.0", "None and next (n)": "$0.0"}

    print("Bathroom options")
    for i in Bathroom_items.keys():
        print(i, end=": ")
        print(Bathroom_items[i], end="  ")

def print_order():
    return

def search_item(ch):
    return

def main():
    print("""
Welcome to Home Ideas Center, where all orders include a new home feeling!\n
For your new Home space...
    """)
    ch1=input("Choose one type of garden idea (O for options, n for next category):")
    while ch1!="n":
        ch1=input(garden_options())
    ch2=input("Choose your indoor living space ideas (O for options, n for next category):")
    while ch2!="n":
        ch2=input(indoor_options())
    ch3=input("Choose your bathroom ideas (O for options, n for exit):")
    while ch3!="n":
        ch3=input(bathroom_options())


