#!/usr/bin/env python
'''
File:   config.py
Author: Gabriel Ryan
Email:  gryan@gdssecurity.com
Source: http://github.com/s0lst1c3/sentrygun_server

Description: Flask configuration file

'''

# namespace for web interface
SOCKETIO_NS='/watchdog'

# namespace for sensor clients
LISTENER_NS='/punisher'

# identity file for ssh connections
IDENTITY_FILE='/root/.ssh/id_rsa'
