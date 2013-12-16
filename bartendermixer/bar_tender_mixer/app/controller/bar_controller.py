# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import sys 
import re
import MySQLdb
from django.utils.datastructures import MultiValueDictKeyError
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
import logging
import serial
logging.basicConfig()
logger = logging.getLogger(__name__)

def index(request):
	return render_to_response("index.html", context_instance=RequestContext(request))
	
def opcao1(request):
	ser = serial.Serial('/dev/ttyACM1',9600,timeout=1)
	ser.write('R')
	return render_to_response("index.html", context_instance=RequestContext(request))

def opcao2(request):
	ser = serial.Serial('/dev/ttyACM1',9600,timeout=1)
	ser.write('r')
	return render_to_response("index.html", context_instance=RequestContext(request))


