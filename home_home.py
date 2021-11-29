class Home_Category:
    __slots__ = ["__name", "__code", "__price"]

    def __init__(self, name, code, price):
        self.__name = name
        self.__code = code
        self.__price = price

    def garden_search(self, code):
        GARDEN={"p": ("3 pack garden flower", 5.0), "l": ("Hanging light wire", 10.0), "b": ("Garden bench", 35.0)}
        for item_code in GARDEN.keys():
            count=0
            if item_code==code:
                self.__code=code
                for i in GARDEN[item_code]:
                    if count==0:
                        self.__name=i
                        count+=1
                    elif count==1:
                        self.__price=i
                return True

    def indoor_search(self, code):
        INDOOR={"t": ("Small table lamp", 5.0), "f1": ("City picture frame", 7.0), "r": ("4x5 entry rug", 35.0),"f2": ("flower vase", 14.0)}

        for item_code in INDOOR.keys():
            count=0
            if item_code==code:
                self.__code=code
                for i in INDOOR[item_code]:
                    if count==0:
                        self.__name=i
                        count+=1
                    elif count==1:
                        self.__price=i
                return True

    def bathroom_search(self, code):
        BATHROOM={"s": ("Soap holder", 5.0), "c": ("Shower Curtain", 5.0), "m": ("Anti-skid doormat", 30.0)}

        for item_code in BATHROOM.keys():
            count=0
            if item_code==code:
                self.__code=code
                for i in BATHROOM[item_code]:
                    if count==0:
                        self.__name=i
                        count+=1
                    elif count==1:
                        self.__price=i
                return True

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    def get_code(self):
        return self.__code

class Home_Avatar:
    __slots__ = ["__garden", "__indoor", "__bathroom", "__total_price"]

    def __init__(self, garden, indoor, bathroom, price):
        self.__garden=garden
        self.__indoor=indoor
        self.__bathroom=bathroom
        self.__total_price=price

    def set_order_price(self, price):
        self.__total_price+=price

    def set_garden(self, garden_item):
        self.__garden.append(garden_item)

    def set_indoor(self, indoor_item):
        self.__indoor.append(indoor_item)

    def set_bathroom(self, bathroom_item):
        self.__bathroom.append(bathroom_item)

    def get_price(self):
        return self.__total_price
    def get_garden(self):
        return self.__garden
    def get_indoor(self):
        return self.__indoor
    def get_bathroom(self):
        return self.__bathroom

def garden_options():
    Garden_items={"3 pack garden flower (p)": "$5.0", "Hanging light wire (l)": "$10.0", "Garden bench (b)": "$35.0", "None and next (n)": "$0.0"}

    for i in Garden_items.keys():
        print(i, end=": ")
        print(Garden_items[i], end="  ")

def indoor_options():
    Indoor_items={"Small table lamp (t)": "$5.0", "City picture frame (f1)": "$7.0", "4x5 entry rug (r)": "$35.0","flower vase (f2)": "$14.0", "None and next (n)": "$0.0"}

    for i in Indoor_items.keys():
        print(i, end=": ")
        print(Indoor_items[i], end="  ")

def bathroom_options():
    Bathroom_items={"Soap holder (s)": "$5.0", "Shower Curtain (c)": "$5.0", "Anti-skid doormat (m)": "$30.0", "None and next (n)": "$0.0"}

    for i in Bathroom_items.keys():
        print(i, end=": ")
        print(Bathroom_items[i], end="  ")

def garden_order(y, garden_code_list):
    z1=Home_Category("", "", 0)
    print("Your order for a new home experience:")
    for i in garden_code_list:
        z1.garden_search(i)
        if z1.garden_search(i)==True:
            print(z1.get_name(), end=" - ")
            print("$"+str(z1.get_price()))

def indoor_order(y, indoor_code_list):
    z2=Home_Category("", "", 0)
    for i in indoor_code_list:
        z2.indoor_search(i)
        if z2.indoor_search(i)==True:
            print(z2.get_name(), end=" - ")
            print("$"+str(z2.get_price()))

def bathroom_order(y, bathroom_code_list):
    z3=Home_Category("", "", 0)
    for i in bathroom_code_list:
        z3.bathroom_search(i)
        if z3.bathroom_search(i)==True:
            print(z3.get_name(), end=" - ")
            print("$"+str(z3.get_price()))


    print("Total due: $"+str(y.get_price()))

def order_item(ch, category, x, y, gcl=[], icl=[], bcl=[]):
    if category=="g":
        for i in ch:
            x.garden_search(i)
            y.set_garden(x.get_name())
            y.set_order_price(x.get_price())
            print("one", x.get_name(), "is added to your home for", x.get_price())
            gcl.append(i)
        return

    elif category=="i":
        for i in ch:
            x.indoor_search(i)
            y.set_indoor(x.get_name())
            y.set_order_price(x.get_price())
            print("one", x.get_name(), "is added to your home for", x.get_price())
            icl.append(i)
        return

    elif category=="b":
        for i in ch:
            x.bathroom_search(i)
            y.set_bathroom(x.get_name())
            y.set_order_price(x.get_price())
            print("one", x.get_name(), "is added to your home for", x.get_price())
            bcl.append(i)
        return

def main():
    print("""
Welcome to Home Ideas Center, where all orders include a new home feeling!\n
For your new Home space...
    """)
    x=Home_Category("", "", 0)
    y=Home_Avatar([], [], [], 50)
    garden_code_list=[]
    indoor_code_list=[]
    bathroom_code_list=[]
    ch1=input("Choose one type of garden idea (O for options, n for next category):")
    if ch1!="n":
        print("Garden options:")
    while ch1!="n":
        garden_options()
        ch1=input(":")
        ch1_split=ch1.split()
        order_item(ch1_split, "g", x, y, garden_code_list)

    ch2=input("Choose your indoor living space ideas (O for options, n for next category):")
    if ch2!="n":
        print("Indoor options:")
    while ch2!="n":
        indoor_options()
        ch2=input(":")
        ch2_split=ch2.split()
        order_item(ch2_split, "i", x, y, [], indoor_code_list)

    ch3=input("Choose your bathroom ideas (O for options, n for exit):")
    if ch3!="n":
        print("Bathroom options:")
    while ch3!="n":
        bathroom_options()
        ch3=input(":")
        ch3_split=ch3.split()
        order_item(ch3_split, "b", x, y, [], [], bathroom_code_list)

    garden_order(y, garden_code_list)
    indoor_order(y, indoor_code_list)
    bathroom_order(y, bathroom_code_list)

main()

