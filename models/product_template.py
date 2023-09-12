from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        print('vals', vals)
        if vals:

           product = self.env['product.update'].create({'product_update': vals,
                                               'user_id': self.create_uid.id,
                                               'date': self.create_date,
                                               })
           print('product', product.product_update)
        return res

