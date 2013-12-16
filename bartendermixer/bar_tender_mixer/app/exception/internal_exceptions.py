# -*- coding: utf-8 -*-
from exceptions import Exception

class ResultadoConsultaNuloError(Exception):
	"""docstring for ResultadoConsultaNuloError"""
	def __init__(self, message):
		Exception.__init__(self)
		self.message = message
	def __str__(self):
		return self.message
