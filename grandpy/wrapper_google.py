import requests

from .config import Config


class WrapperGoogle:
    """ I'm the Google Wrapper. """

    def __init__(self):
        """ """
        config = Config()
        self.URL = config.GURL
        self.HEADERS = {"User-Agent": config.UAGENT}
        self.GKEY = config.GKEY_B
        self.PARAMS = {"key": config.GKEY_B}

    def request(self, query="thiais"):
        """ I make the request to Google place.
        In: the parsed question (str)
        Act: I request the Google Place API
        Out: the result (list)
        """
        try:
            request = requests.get(
                url=self.URL,
                params={
                    "key": self.GKEY,
                    "query": query
                },
                headers=self.HEADERS
            )
            results = request.json()

            if results.get('status') != 'OK':
                results = None
                return results
            else:
                return results["results"]

        except requests.RequestException as exception:
            print(exception)

    def number_of_results(self, results):
        """ I check the number of results. """
        return len(results)

    def coordinates(self, results):
        """ I retrieve the coordinates of the place.
        In: the results of Google request (dict)
        Act: I create a dict with latitude and longitude
        Out: latitute and longitude from the viewport northeast
        Out Ex: {
            'location': {
                'lat': 48.760344,
                'lng': 2.387405
                    }
                }
        """
        result = {
            "location": results[0].get('geometry').get('location')
        }
        return result

    def informations(self, results):
        """ I retrieve the informations of the place.
        In: the results of Google request (dict)
        Act: I create a dict with name, formatted_address and types
        Out: the informations of the place (dict)
        Out Ex:
        {
            'name': 'Thiais',
            'formatted_address': '94320 Thiais, France',
            'types': ['locality', 'political']
        }
        """
        result = {
            "name": results[0].get('name'),
            "formatted_address": results[0].get('formatted_address'),
            "types": results[0].get('types')
        }
        return result


if __name__ == "__main__":
    wgoogle = WrapperGoogle()

    # === Tests of methods ===
    # print(wgoogle.request("mairie thiais wiki"), type(wgoogle.request()))
    # print(wgoogle.request("moutarde dijon paris wiki"), type(wgoogle.request()))
    # print(wgoogle.request("chaussures tombouktou besoin marcher aller himalaya"), type(wgoogle.request()))
    # print(wgoogle.number_of_results(wgoogle.request()))
    # print(wgoogle.coordinates(wgoogle.request()))
    # print(wgoogle.informations(wgoogle.request()))
    # print(wgoogle.result_name(wgoogle.request()))
