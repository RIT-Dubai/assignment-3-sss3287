class Home_Category:
    __slots__=["garden", "indoor", "bathroom"]

    def _init_(self, garden, indoor, bathroom):
        GARDEN = {"3 pack garden flower (p)": "$5.0", "Hanging light wire (l)": "$10.0"}
        INDOOR = {"Small table lamp (t): $5.0 City picture frame(f1): $7.0 4x5 entry rug (r): $35.0 flower vase (f2): $14.0"}
        BATHROOM = {}

        def search_garden():
            for i in GARDEN.keys():
                if i[-2] == garden or i == garden:
                    self.garden = GARDEN[i].strip("$")

        def search_indoor():
            for i in INDOOR.keys():
                if i[-2] == indoor or i == indoor:
                    self.indoor = indoor

        def search_bathroom():
            for i in BATHROOM.keys():
                if i[-2] == bathroom or i == bathroom:
                    self.bathroom = bathroom
