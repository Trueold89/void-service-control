# -*- coding: utf-8 -*-
import importlib.resources
import json
from enum import Enum
from os import listdir as ls
from subprocess import run as execute
from subprocess import PIPE
from sys import argv


from VoidServiceControl.env import *


class Help(Exception):
    def __str__(self) -> str:
        """
        Returns the program usage help
        :return: Program usage help
        """
        return lang.messages["help"]


def Su() -> None:
    """
    Checks if the user has administrator rights
    """
    user = execute('whoami', shell=True, text=True, stdout=PIPE).stdout[:-1]
    if user != 'root':
        raise PermissionError(lang.errors["su"])


# Types of service actions
class Action(Enum):
    ENABLE = ["enable", "e", "on", "up"]
    DISABLE = ["disable", "d", "off", "down"]


# Types of run arguments
class Arg(Enum):
    HELP = ["--help", "-h", "help"]

    @classmethod
    def all(cls) -> list[str]:
        """
        Returns all types of run arguments
        :return: All types of run arguments list
        """
        return cls.HELP.value + cls.__action()

    @classmethod
    def __action(cls) -> list[str]:
        """
        Returns all types of service actions
        :return: All types of service actions list
        """
        actions = list(map(lambda action: action.value, Action))
        out = []
        for lst in actions:
            out.extend(lst)
        return out


class Args(object):

    def __init__(self) -> None:
        self.__arguments = argv[1:]
        self.__check()

    def __check(self) -> None:
        """
        Checks the arguments
        """
        if len(self.__arguments) == 0:
            raise TypeError(lang.errors["usage"])
        if len(self.__arguments) != 2 and self.__arguments[0] not in Arg.HELP.value:
            raise TypeError(lang.errors["usage"])
        if self.__arguments[0] in Arg.HELP.value:
            raise Help()
        if self.__arguments[0] not in Arg.all():
            raise TypeError(lang.errors["args"])

    def __action(self) -> Action:
        """
        Returns the action to the service
        :return: Service action
        """
        actions = list(Action)
        for action in actions:
            if self.__arguments[0] in action.value:
                return action

    def __iter__(self):
        yield self.__action()
        yield self.__arguments[1]


class Service(object):
    __enabled = False

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__check()

    def __check(self) -> None:
        """
        Checks if the service exists and is enabled
        """
        all_services = ls(SV_PATH)
        enabled_services = ls(ENABLED_PATH)
        if self.__name not in all_services:
            raise ValueError(lang.errors["ne"].format(self.getname()))
        if self.__name in enabled_services:
            self.__enabled = True

    def getname(self) -> str:
        """
        Returns the service name
        :return: Service name
        """
        return self.__name

    def enable(self) -> None:
        """
        Enable the service
        """
        if self.__enabled:
            raise ValueError(lang.errors["enabled"].format(self.getname()))
        execute(f'ln -s {SV_PATH}/{self.__name} {ENABLED_PATH}/', shell=True)

    def disable(self):
        """
        Disable the service
        """
        if not self.__enabled:
            raise ValueError(lang.errors["disabled"].format(self.getname()))
        execute(f'rm {ENABLED_PATH}/{self.__name}', shell=True)


class Interface(object):

    def __init__(self, service: str) -> None:
        self.service = Service(service)

    def action(self, action: Action) -> None:
        """
        Performs an action on the service
        :param action: Action on the service
        """
        match action:
            case Action.ENABLE:
                self.service.enable()
                print(lang.messages["enabled"].format(self.service.getname()))
            case Action.DISABLE:
                self.service.disable()
                print(lang.messages["disabled"].format(self.service.getname()))


class Translate(object):

    def __init__(self, language: str):
        """
        :param language: Language (ex. en_US)
        """
        self.lang = language
        self.errors = self.__translation["errors"]
        self.messages = self.__translation["messages"]

    @property
    def __translation(self):
        try:
            with importlib.resources.open_text(__package__, f"{self.lang}.json", "utf-8") as json_file:
                return json.loads(json_file.read())
        except FileNotFoundError:
            with importlib.resources.open_text(__package__, f"en_US.json", "utf-8") as json_file:
                return json.loads(json_file.read())


lang = Translate(LANG)
