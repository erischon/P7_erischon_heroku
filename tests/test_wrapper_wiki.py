from grandpy.wrapper_wiki import WrapperWiki

wwiki = WrapperWiki()

location = {'location': {'lat': 48.76569917989272, 'lng': 2.392394129892722}}
coord = "48.76569917989272|2.392394129892722"
pageid = "1509079"

def test_location_to_coord():
    """ I test the formatting of location coordonates. """
    result_a = str(type(wwiki.location_to_coord(location)))
    result_b = wwiki.location_to_coord(location)
    assert result_a == "<class 'str'>"
    assert result_b == "48.76569917989272|2.392394129892722"

def test_coord_to_pageid():
    """ I test if there is a pageid. """
    result_a = str(type(wwiki.coord_to_pageid(coord)))
    assert result_a == "<class 'int'>"

def test_wiki_text():
    """ """
    result_a = str(type(wwiki.wiki_text(pageid)))
    assert result_a == "<class 'dict'>"