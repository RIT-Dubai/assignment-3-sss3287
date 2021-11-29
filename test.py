import home_home

def test_indoor_search():
    '''This function tests if the function searches indoor items'''
    x=home_home.Home_Category("", "", 0)
    assert(x.search_indoor("f1") == True)

def test_bathroom_search():
    '''This function tests if the function searches bathroom items'''
    x=home_home.Home_Category("", "", 0)
    assert(x.search_bathroom("c") == True)

def test_garden_search():
    '''This function tests if the function searches garden items'''
    x=home_home.Home_Category("", "", 0)
    assert(x.search_garden("p") == True)


def test_garden_order():
    '''This function tests if the function searches garden items'''
    x=home_home.garden_order(0, [1])
    assert(x == None)

def test_indoor_order():
    '''This function tests if the function searches garden items'''
    x=home_home.garden_order([])
    assert(x == True)

def test_bathroom_order():
    '''This function tests if the function searches garden items'''
    x=home_home.bathroom_order([])
    assert(x == True)


'''NOTE : In order for these tests to pass you may have comment out only the main function
           that is def main() and call main in the home_home module
           to do that just put # in front of them #def main(): and #main()'''
