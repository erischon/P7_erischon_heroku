from grandpy.wrapper_wiki import WrapperWiki
from tests.results_wiki import wiki_pageid_result, wiki_text_result, location, coord, pageid

wwiki = WrapperWiki()

def test_location_to_coord():
    """ I test the formatting of location coordonates. """
    result_a = wwiki.location_to_coord(location)
    result_b = wwiki.location_to_coord(location)
    
    assert isinstance(result_a, str)
    assert result_b == "48.76569917989272|2.392394129892722"

def test_coord_to_pageid(monkeypatch):
    """ I test if there is a pageid. """
    class MockRequestGetPageID:
        def __init__(self, url, params=None, headers=None):
            pass 
        def json(self):
            return wiki_pageid_result

    monkeypatch.setattr('requests.get', MockRequestGetPageID)
    result_a = wwiki.coord_to_pageid(coord)

    assert isinstance(wwiki.coord_to_pageid(coord), int)
    assert result_a == 1509079

def test_wiki_text(monkeypatch):
    """ I test if there is a text. """
    class MockRequestGetText:
        def __init__(self, url, params=None, headers=None):
            pass 
        def json(self):
            return wiki_text_result

    monkeypatch.setattr('requests.get', MockRequestGetText)

    assert isinstance(wwiki.wiki_text(pageid), dict)