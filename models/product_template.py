from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    product_update_ids = fields.One2many('product.update', 'product_update_id', string='Product Update')

    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        print('vals', vals)
        if vals:
            product = self.env['product.update'].create({'product_update': vals,
                                                         'user_id': self.create_uid.id,
                                                         'date': self.create_date,
                                                         'product_update_id': self.id,
                                                         })
            print('product', product.product_update_id)
        return res

