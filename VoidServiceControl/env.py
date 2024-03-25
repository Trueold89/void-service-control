# -*- coding: utf-8 -*-
from os import environ

# Edit these lines if you are using custom paths to Runit services

SV_PATH = '/etc/sv'
ENABLED_PATH = '/var/service'


# Lang settings
def lang() -> str:
    """
    Get system lang
    :return: system lang
    """
    try:
        return environ["LANG"][:5]
    except KeyError:
        return "en_US"


LANG = lang()
