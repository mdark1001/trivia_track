"""
@author miguelCabrera1001 | 
@date 20/12/18
@project 
@name main
"""
import json
import logging
import werkzeug
from datetime import datetime
from math import ceil
from odoo import fields, http, SUPERUSER_ID
from odoo.http import request
from odoo.tools import ustr

_logger = logging.getLogger(__name__)

headers_response = [
    ("Access-Control-Allow-Origin", "*"),
    ('Content-Type', 'application/json'),
    ('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
]


class triviaControllers(http.Controller):

    @http.route('/home/trivias', auth='public', method=['GET'], type='http', website=True)
    def trivia(self):
        return request.render('trivia_track.page_trivia', {})

    @http.route('/page/trivia', auth='user', method=['GET'], type='http', website=True)
    def trivias(self):
        return request.render('trivia_track.page_trivia', {})

    @http.route('/page/rifa', auth='user', type='http', website=True)
    def trivia(self, **kw):
        return request.render('trivia_track.page_rifa', {})

    @http.route('/page/folioAleatorio', auth='user', type='http', website=True)
    def folioAleatorio(self):

        request.env.cr.execute(""" select t.name as folio from oohel_trivia_track as  t
                              INNER JOIN res_users as u on u.id =t.user_id
                                order by RANDOM() LIMIT 1;  """)
        folio = request.env.cr.fetchone()

        return request.make_response(json.dumps({'state': 200,
                                                 'message': 'Se registro correctamente la trivia',
                                                 'folio': folio
                                                 }),
                                     headers=headers_response)

    @http.route('/page/save_trivia/', auth="user", type="http", website=True)
    def saveTrivia(self, **kw):
        try:
            tatal_correctas = int(kw.get('total_correct', 0))
            user_id = request.env.user.id
            if not self.validaUsuarioTrivia(user_id):
                self.registraUsuarioTrivia(user_id, tatal_correctas)
                self.registraFolios(user_id, tatal_correctas)
                return request.make_response(json.dumps({'state': 200,
                                                         'message': 'Se registro correctamente la trivia'}),
                                             headers=headers_response)
            else:
                return request.make_response(json.dumps({'state': 500,
                                                         'message': 'Error al pracesar la solicitud'}),
                                             headers=headers_response)

        except Exception as e:
            print(e)
            print("Ocurrio un error....")
            return request.make_response(json.dumps({'state': 500,
                                                     'message': 'Error al pracesar la solicitud'}),
                                         headers=headers_response)

    def validaUsuarioTrivia(self, id_usuario):
        return request.env['oohel.usuario_trivia'].sudo().search_count([('user_id', '=', id_usuario)])

    def registraUsuarioTrivia(self, id_usuario, total):
        request.env['oohel.usuario_trivia'].sudo().create({
            'user_id': id_usuario,
            'total': total
        })
        return True

    def registraFolios(self, id_usuario, total):
        print(range(0, total))
        for i in range(0, total):
            print("AAAAAA---------------->>>>")
            folio = request.env['core_generador_folio'].sudo().getFolio("SSL-")
            print(folio)
            request.env['oohel.trivia_track'].sudo().create({
                'user_id': id_usuario,
                'name': folio
            })
            # return True
