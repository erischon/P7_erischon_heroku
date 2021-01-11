from grandpy.wrapper_google import WrapperGoogle
from tests.results_google import google_result, wrapper_result

wgoogle = WrapperGoogle()


class MockRequestGet:
    def __init__(self, url, params=None, headers=None):
        pass

    def json(self):
        return google_result


def test_google_request(monkeypatch):
    """ I test if there is a answer to a request. """
    monkeypatch.setattr('requests.get', MockRequestGet)
    assert isinstance(wgoogle.request(), list)


def test_number_of_results():
    """ I test if I have a number. """
    result_a = wgoogle.number_of_results(google_result)
    assert isinstance(result_a, int)


def test_coordinates():
    """ I test if the answer is a dictionary. """
    result_a = wgoogle.coordinates(wrapper_result)
    assert isinstance(result_a, dict)


def test_informations():
    """ I test if the answer is a dictionary. """
    result_a = wgoogle.informations(wrapper_result)
    assert isinstance(result_a, dict)
