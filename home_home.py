class Home_Category:
    _slots_ = ["name", "code", "price"]

    def _init_(self, name, code):
        self.name = name
        self.code = code
        self.price = 0

    def garden_search(self, name, code):
        GARDEN = {"3 pack garden flower (p)": "$5.0", "Hanging light wire (l)": "$10.0", "Garden bench (b)": "$35:0"}

        for i in GARDEN.keys():
            if i == name:
                return GARDEN[i].strip("$")
            else:
                for j in range(len(i)):
                    if i[j] == "(":
                        if i[j + 1:-1] == code:
                            self.name = name
                            self.code = code
                            self.price = float(GARDEN[i].strip("$"))

    def indoor_search(self, name, code):
        INDOOR = {"Small table lamp (t)": "$5.0", "City picture frame (f1)": "$7.0", "carpet (c)": "$35.0",
                  "flower vase (f2)": "$14.0"}

        for i in INDOOR.keys():
            if i == name:
                return INDOOR[i].strip("$")
            else:
                for j in range(len(i)):
                    if i[j] == "(":
                        if i[j + 1:-1] == code:
                            self.name = name
                            self.code = code
                            self.price = float(INDOOR[i].strip("$"))

    def bathroom_search(self, name, code):
        BATHROOM = {"soap holder (s)": "$5.0", "shower curtain (sc)": "$5.0", "anti-skid mat (m)": "$30.0"}

        for i in BATHROOM.keys():
            if i == name:
                return BATHROOM[i].strip("$")
            else:
                for j in range(len(i)):
                    if i[j] == "(":
                        if i[j + 1:-1] == code:
                            self.name = name
                            self.code = code
                            self.price = float(BATHROOM[i].strip("$"))


class Home_Avatar:
    _slots_ = ["item", "price"]

    def _init_(self, item):
        self.item = item
        self.price = 0

    def order_price(self, price):
        self.price += price


# test data
        x = Home_Category("", "")
        x.garden_search("3 pack garden flower", "l")
        print(x.name)
        y = Home_Avatar(x.name)
        print(y.price)
        y.order_price(x.price)
        print(y.price)
        x.indoor_search("blah blah", "f1")
        print(x.name)
        y.order_price(x.price)
        print(y.price)
        x.bathroom_search("blah", "r")
        print(x.name)
        y.order_price(x.price)
        print(y.price)

