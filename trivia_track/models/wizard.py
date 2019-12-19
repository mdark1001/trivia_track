"""
@author miguelCabrera1001 | 
@date 21/12/18
@project 
@name wizard
"""
from datetime import datetime

from odoo import fields, api, models


class foliosBaseRifa(models.TransientModel):
    _name = 'trivia_rifa'
    user_id = fields.Many2one('res.users',
                              'Propietario',
                              required=True,
                              default=lambda self: self.env.user)
    total = fields.Integer(string='Total',
                           default=1
                           )

    def asignar_folios(self):
        for i in range(self.total):
            folio = self.env['oohel.core_generador_folio'].sudo().getFolio("SSL-")
            # print(folio)
            self.env['oohel.trivia_track'].sudo().create({
                'user_id': self.user_id.id,
                'name': folio
            })
