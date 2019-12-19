"""
@author miguelCabrera1001 | 
@date 20/12/18
@project 
@name trivia_track
"""

from odoo import fields, api, models


class TriviaTrack(models.Model):
    _name = 'oohel.trivia_track'
    name = fields.Char(string='Folio',
                       required=True)
    user_id = fields.Many2one('res.users',
                              'Propietario',
                              required=True, default=lambda self: self.env.user)
    fecha = fields.Datetime(string='Fecha', default=lambda self: fields.Datetime.now())
    active = fields.Boolean(
        string='Activo',
        default=True
    )


class usuarioTrivia(models.Model):
    _name = 'oohel.usuario_trivia'

    user_id = fields.Many2one('res.users',
                              'Propietario',
                              required=True, default=lambda self: self.env.user)
    fecha = fields.Datetime(string='Fecha', default=lambda self: fields.Datetime.now())

    total = fields.Integer(string='Total de preguntas correctas')
