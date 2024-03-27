#!/usr/bin/python3
# -*- coding: utf-8 -*-
from VoidServiceControl.classes import Su, Interface, Args, Help


def main() -> None:
    try:
        Su()
        action, services = tuple(Args())
        for service_name in services:
            service = Interface(service_name)
            service.action(action)
            del service
    except TypeError as e:
        print(f"{e}\n\n{Help()}")
    except (ValueError, PermissionError, Help) as e:
        print(e)


if __name__ == '__main__':
    main()
