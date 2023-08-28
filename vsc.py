#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Modules
import os
import subprocess
import sys

# Vars
allsv_path = '/etc/sv/'
enabledsv_path = '/var/service/'
allsv = os.listdir(allsv_path) 
enabledsv = os.listdir(enabledsv_path)

# Functions

## Help
def helpmsg():
    msg = '''
Usage:
---
vsc {e/enable/on/up} <service_name> - Run service and add it to autostart
vsc {d/disable/off/down <service_name> - Stop service and remove it from autostart
---'''
    return msg

## Access
def su():
        user = subprocess.run('whoami', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if user.stdout[:-1] == 'root':
            return args()
        else:
            return 'Access denied'

## Service
def exec(option, service):
    if option == 'on':
        if service in enabledsv:
            return 'Service alredy enabled'
        if service in allsv:
            subprocess.run(f'ln -s {allsv_path}{service} {enabledsv_path}', shell=True)
            return f'Service {service} successfully enabled'
        if not(service in allsv):
            return f"Service {service} doesn't exist"
    if option == 'off':
        if not(service in allsv):
            return f"Service {service} doesn't exist"
        if not(service in enabledsv):
            return f'Service {service} has already been disabled'
        if service in enabledsv:
            subprocess.run(f'rm {enabledsv_path}{service}', shell=True)
            return f'Service {service} successfully disabled'

# Get argv
def getargs():
    global service
    global option
    option = sys.argv[1]
    service = sys.argv[2]
    return options(option)
    
# Args
def args():
    if len(sys.orig_argv[1:]) == 2:
        if sys.orig_argv[2] == '--help':
            return helpmsg()
    elif len(sys.orig_argv[1:]) == 3:
        return getargs()
    else:
        return 'Invalid usage, see --help'

def options(option):
    options = {
            'on': ['enable','e','on','up'],
            'off': ['disable','d','off','down']
            }
    for i in options.keys():
        if option in options.get(i):
            return exec(i,service)
    return f'Invalid option: {option}, see --help'

print(su())
