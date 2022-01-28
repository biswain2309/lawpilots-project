from django.shortcuts import render
from django.http import HttpResponse

import socket
import datetime
from uptime import uptime

import logging


db_logger = logging.getLogger('db')


def status(request):

    '''Log data in the Logging database'''
    
    db_logger.info('Info!!', extra={'hostname' : socket.gethostname()})

    '''Plain text as response to the request'''

    data = f'Hostname is {socket.gethostname()} Current date and time is {datetime.datetime.now()} and System Uptime is {uptime()}'

    return HttpResponse(data, content_type='text/plain')



