# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Manufacturer(models.Model):

	_name = 'phone.manufacturer'
	_description = 'Phone Manufacturer'

	name = fields.Char(string='Manufacturer', required=True)



