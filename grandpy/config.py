import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """ """

    def __init__(self):
        """ """
        self.GURL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        self.GKEY_B = os.getenv("GKEY_B")
        self.GKEY_F = os.getenv("GKEY_F")
        self.UAGENT = "OC-P7 - GNU/Windows - Version 0.1"

        #
        self.WURL = "https://fr.wikipedia.org/w/api.php"