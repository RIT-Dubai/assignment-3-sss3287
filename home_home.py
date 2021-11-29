class Home_Category:
    '''This class searches for that particular item in each category'''
    __slots__ = ["name", "code", "price"]

    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price

    def search_garden(self, code):
        '''This searches for garden items'''
        g={"p": ("3 pack garden flower", 5.0), "l": ("Hanging light wire", 10.0), "b": ("Garden bench", 35.0)}
        for item_code in g.keys():
            count=0
            if item_code==code:
                self.code=code
                for i in g[item_code]:
                    if count==0:
                        self.name=i
                        count+=1
                    elif count==1:
                        self.price=i
                return True

    def search_indoor(self, code):
        '''This searches for indoor items'''
        i={"t": ("Small table lamp", 5.0), "f1": ("City picture frame", 7.0), "r": ("4x5 entry rug", 35.0),"f2": ("flower vase", 14.0)}

        for item_code in i.keys():
            count=0
            if item_code==code:
                self.code=code
                for i in i[item_code]:
                    if count==0:
                        self.name=i
                        count+=1
                    elif count==1:
                        self.price=i
                return True

    def search_bathroom(self, code):
        '''This searches for bathroom items'''
        b={"s": ("Soap holder", 5.0), "c": ("Shower Curtain", 10.0), "m": ("Anti-skid mat", 30.0)}

        for item_code in b.keys():
            count=0
            if item_code==code:
                self.code=code
                for i in b[item_code]:
                    if count==0:
                        self.name=i
                        count+=1
                    elif count==1:
                        self.price=i
                return True

class Home_Avatar:
    '''This class stores a particular item of each category'''
    __slots__ = ["garden", "indoor", "bathroom", "total_price"]

    def __init__(self, garden, indoor, bathroom, price):
        self.garden=garden
        self.indoor=indoor
        self.bathroom=bathroom
        self.total_price=price

    def set_order_price(self, price):
        self.total_price+=price

def garden_options():
    '''This provides the options of garden items'''
    g_items={"3 pack garden flower (p)": "$5.0", "Hanging light wire (l)": "$10.0", "Garden bench (b)": "$35.0", "None and next (n)": "$0.0"}

    for i in g_items.keys():
        print(i, end=": ")
        print(g_items[i], end="  ")

def indoor_options():
    '''This provides the options of indoor items'''
    i_items={"Small table lamp (t)": "$5.0", "City picture frame (f1)": "$7.0", "4x5 entry rug (r)": "$35.0","flower vase (f2)": "$14.0", "None and next (n)": "$0.0"}

    for i in i_items.keys():
        print(i, end=": ")
        print(i_items[i], end="  ")

def bathroom_options():
    '''This provides the options of bathroom items'''
    b_items={"Soap holder (s)": "$5.0", "Shower Curtain (c)": "$10.0", "Anti-skid doormat (m)": "$30.0", "None and next (n)": "$0.0"}

    for i in b_items.keys():
        print(i, end=": ")
        print(b_items[i], end="  ")

def garden_order(y, garden_code_list):
    '''This creates an order for garden items'''
    a=Home_Category("", "", 0)
    print("Your order for a new home experience:")
    for i in garden_code_list:
        a.search_garden(i)
        if a.search_garden(i)==True:
            print(a.name, end=" - ")
            print("$"+str(a.price))

def indoor_order(y, indoor_code_list):
    '''This creates an order for indoor items'''
    b=Home_Category("", "", 0)
    for i in indoor_code_list:
        b.search_indoor(i)
        if b.search_indoor(i)==True:
            print(b.name, end=" - ")
            print("$"+str(b.price))

def bathroom_order(y, bathroom_code_list):
    '''This creates an order for bathroom items'''
    c=Home_Category("", "", 0)
    for i in bathroom_code_list:
        c.search_bathroom(i)
        if c.search_bathroom(i)==True:
            print(c.name, end=" - ")
            print("$"+str(c.price))


    print("Total due: $"+str(y.total_price))

def order_item(ch, category, x, y, gcl=[], icl=[], bcl=[]):
    '''This creates an order for all items of respective categories'''
    if category=="g":
        for i in ch:
            x.search_garden(i)
            y.garden.append(x.name)
            y.set_order_price(x.price)
            print("one", x.name, "is added to your home for", x.price)
            gcl.append(i)
        return

    elif category=="i":
        for i in ch:
            x.search_indoor(i)
            y.indoor.append(x.name)
            y.set_order_price(x.price)
            print("one", x.name, "is added to your home for", x.price)
            icl.append(i)
        return

    elif category=="b":
        for i in ch:
            x.search_bathroom(i)
            y.bathroom.append(x.name)
            y.set_order_price(x.price)
            print("one", x.name, "is added to your home for", x.price)
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
    c1=input("Choose one type of garden idea (O for options, n for next category):")
    if c1!="n":
        print("Garden options:")
    while c1!="n":
        garden_options()
        c1=input(":")
        c1_split=c1.split()
        if c1!="n":
            order_item(c1_split, "g", x, y, garden_code_list)

    c2=input("Choose your indoor living space ideas (O for options, n for next category):")
    if c2!="n":
        print("Indoor options:")
    while c2!="n":
        indoor_options()
        c2=input(":")
        c2_split=c2.split()
        if c2!="n":
            order_item(c2_split, "i", x, y, [], indoor_code_list)

    c3=input("Choose your bathroom ideas (O for options, n for exit):")
    if c3!="n":
        print("Bathroom options:")
    while c3!="n":
        bathroom_options()
        c3=input(":")
        c3_split=c3.split()
        if c3!="n":
            order_item(c3_split, "b", x, y, [], [], bathroom_code_list)

    garden_order(y, garden_code_list)
    indoor_order(y, indoor_code_list)
    bathroom_order(y, bathroom_code_list)


main()
