from odoo import models, fields, api

class ProductTemplate(models.Model):

	_inherit = 'product.template'

	manufactur_id = fields.Many2one('phone.manufacturer', string='Manufacturer', required=True)
	phone_model_id = fields.Many2one('phone.model',string='Model', required=True, domain="[('manuf_id', '=', manufactur_id)]")

	
	@api.onchange("manufactur_id")
	def onchange_model_manufact(self):
		
		self.phone_model_id = 0

		if self.manufactur_id:

			self.phone_model_id = fields.Many2one('phone.model', string='Model', required=True, domain="[('manuf_id', '=', self.manufactur_id)]")

		else:
			self.phone_model_id = 0








		

