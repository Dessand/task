from odoo import models, fields, api

class PhoneModel(models.Model):

	_name = 'phone.model'
	_description = 'Phone Model'

	name = fields.Char(string='Model', required=True)
	manuf_id = fields.Many2one('phone.manufacturer', string='Manufacturer', required=True)

