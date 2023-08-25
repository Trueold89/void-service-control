#!/bin/python3

###########
# Modules #
###########

import os
import subprocess
import sys

#############
# Functions #
#############

# Access check
def sucheck():
    user = subprocess.run('whoami', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if user.stdout[:-1] == 'root':
        return True
    else:
        return 'Run script as root user'

#Args check
def argcheck():
    if len(sys.orig_argv[1:]) == 3:
        return True
    else:
        return 'Invalid usage'

#Options check
def optcheck(option):
    path = ''
    allopts_list = []
    allopts = { 'enable': ['enable', 'e', 'on'], 'disable': ['disable','d','off'], 'down': ['down','dt']}
    for i in allopts.keys():
        allopts_list = allopts_list + allopts[i]
    if not(option in allopts_list):
        print(f'Invalid option: {option}')
        sys.exit()
    while path == '':
        if option in allopts['enable']:
            option = 'enable'
            path = '/etc/sv'
        if option in allopts['disable']:
            option = 'disable'
            path = '/var/service'
        if option in allopts['down']:
            option = 'down'
            path = '/etc/sv'
    return path, option

#Service check
def svcheck(service,path):
    list = os.listdir(path)
    if service in list:
        return True
    else:
        return f'Service not found: {service}'

#Control service
def action(option,service):
    if option == 'enable':
        subprocess.run(f'ln -s /etc/sv/{service} /var/service', shell=True)
        return f'{service} enabled'
    if option == 'disable':
        subprocess.run(f'rm /var/service/{service}', shell=True)
        return f'{service} disabled'
    if option == 'down':
        subprocess.run(f'touch /etc/sv/{service}/down', shell=True)
        return f'Down-file created for {service}'

########
# Exec #
########

ac = argcheck()
if ac == True:
    suc = sucheck()
    if suc == True:
        oc = optcheck(sys.argv[1])
        sc = svcheck(sys.argv[2],oc[0])
        if sc == True:
            print(action(oc[1],sys.argv[2]))
        else:
            print(sc)
    else:
        print(suc)
else:
    print(ac)
