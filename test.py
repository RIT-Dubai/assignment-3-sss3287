import home_home as hh

def test_indoor_search():
    '''This function tests if the function searches indoor items'''
    x=hh.Home_Category("", "", 0)
    assert(x.search_indoor("f1") == True)

def test_bathroom_search():
    '''This function tests if the function searches bathroom items'''
    x=hh.Home_Category("", "", 0)
    assert(x.search_bathroom("b") == True)

def test_garden_search():
    '''This function tests if the function searches garden items'''
    x=hh.Home_Category("", "", 0)
    assert(x.search_garden("p") == True)


def test_garden_order():
    '''This function tests if the function searches garden items'''
    x=hh.garden_order([])
    assert(x == True)

def test_indoor_order():
    '''This function tests if the function searches garden items'''
    x=hh.garden_order([])
    assert(x == True)

def test_bathroom_order():
    '''This function tests if the function searches garden items'''
    x=hh.bathroom_order([])
    assert(x == True)


'''NOTE : In order for these tests to pass you may have comment out only the main function
           that is def main() and call main in the plots_cli module
           to do that just put # in front of them #def main(): and #main()'''
