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


