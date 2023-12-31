from odoo import models, fields, api


class ProductUpdate(models.Model):
    _name = 'product.update'
    _description = 'Product Update'
    _rec_name= 'date'

    date = fields.Date('Date', tracking=True)
    user_id = fields.Many2one('res.users', 'Users', ondelete='cascade')
    product_update = fields.Char(string='Case Updated')
    product_update_id = fields.Many2one('product.template', 'product update')



