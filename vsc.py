#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import
import os, subprocess, sys

# Const
SV_PATH = '/etc/sv'
ENABLED_PATH = '/var/service'

# Access
def su():
    out = subprocess.run('whoami', shell=True, text=True, stdout=subprocess.PIPE)
    user = out.stdout[:-1]
    if user == 'root':
        return True
    else:
        return False

# Print help message 
def helpmsg():
    print('''
Usage:
---
vsc {e/enable/on/up} <service_name> - Run service and add it to autostart
vsc {d/disable/off/down <service_name> - Stop service and remove it from autostart
---
''')
    sys.exit(1)

# Check exec args
def args_check():
    args = sys.orig_argv[2:]
    if len(args) == 2:
        return args
    elif len(args) == 1 and args[0] in ['--h','--help']:
        helpmsg()
    else:
        return False

# Check availability
def availability(service, action):
    all = os.listdir(SV_PATH)
    enabled = os.listdir(ENABLED_PATH)
    all = service in all
    if all == False:
        raise Exception(f"Service '{service}' doesn't exist")
    if service in enabled:
        if action == 'on':
            raise Exception(f"Service '{service}' already enabled")
        elif action == 'off':
            return True
    else:
        if action == 'off':
            raise Exception(f"Service '{service}' already disabled")
        elif action == 'on':
            return True

# Main
def main():
    try:
        args = args_check()
        if args == False:
            raise Exception('Bad usage. See --help')
        if su() == False:
            raise Exception('Access denied')
        action, service = args
        if action in ['enable','e','on','up']:
            if availability(service,'on'):
                subprocess.run(f'ln -s {SV_PATH}/{service} {ENABLED_PATH}/', shell=True)
                print(f"Service '{service}' successfully enabled")
        if action in ['disable','d','off','down']:
            if availability(service,'off'):
                subprocess.run(f'rm {ENABLED_PATH}/{service}', shell=True)
                print(f"Service '{service}' successfully disabled")
    except Exception as ex:
        print(ex)
        sys.exit(0)

if __name__ == '__main__':
    main()
