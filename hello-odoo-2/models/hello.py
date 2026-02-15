from odoo import models, fields

class HelloOdoo(models.Model):
    _name = 'hello.odoo'
    _description = 'Hello Odoo from Mazen'

    name = fields.Char(string='Name', required=True)
    message = fields.Text(string='Message', default='Hello Mazen')
