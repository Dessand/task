# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

class QuickCreateProductWizard(models.TransientModel):

    _name = 'quick.create.product.wizard'
    #_inherit = 'product.template'
    _description = 'Quick Create Product Wizard'

    @tools.ormcache()
    def _get_default_category_id(self):
        # Deletion forbidden (at least through unlink)
        return self.env.ref('product.product_category_all')

    def _read_group_categ_id(self, categories, domain, order):
        category_ids = self.env.context.get('default_categ_id')
        if not category_ids and self.env.context.get('group_expand'):
            category_ids = categories._search([], order=order, access_rights_uid=SUPERUSER_ID)
        return categories.browse(category_ids)


    name = fields.Char(string='Name', required=True)

    type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service')], string='Product Type', default='consu', required=True,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')
    categ_id = fields.Many2one(
        'product.category', 'Product Category',change_default=True,
        default=_get_default_category_id, group_expand='_read_group_categ_id',required=True
        )
    
    sale_ok = fields.Boolean('Can be Sold', default=True)
    purchase_ok = fields.Boolean('Can be Purchased', default=True)

    # default_code = fields.Char(
    #     'Internal Reference', compute='_compute_default_code',
    #     inverse='_set_default_code', store=True)

    manufactur_id = fields.Many2one('phone.manufacturer', required = True, string='Manufacturer')
    phone_model_id = fields.Many2one('phone.model',string='Model', required = True, domain="[('manuf_id', '=', manufactur_id)]")
    image = fields.Binary(string="Image")

    def action_quick_create_product(self):

        vals = {

            'type': self.type,
            'categ_id': self.categ_id.id,
            #'default_code': self.default_code,
            'manufactur_id': self.manufactur_id.id,
            'phone_model_id': self.phone_model_id.id,
            'sale_ok': self.sale_ok,
            'purchase_ok': self.purchase_ok,
            'image_1920':self.image,
            'name':self.name
        }
        self.env['product.template'].create(vals)

        return {"type": "action", "name": "action_quick_create_product"}

    @api.onchange("manufactur_id")
    def onchange_model_manufact(self):
        
        self.phone_model_id = 0

        if self.manufactur_id:

            self.phone_model_id = fields.Many2one('phone.model', string='Model', domain="[('manuf_id', '=', self.manufactur_id)]")
            self.name = self.manufactur_id.name

        else:
            self.phone_model_id = 0

    @api.onchange("phone_model_id")
    def onchange_phone_model(self):

        if self.phone_model_id.name:
            self.name = str(self.manufactur_id.name) + ' '+ str(self.phone_model_id.name)





    # def _set_default_code(self):
    #     for template in self:
    #         if len(template.product_variant_ids) == 1:
    #             template.product_variant_ids.default_code = template.default_code
