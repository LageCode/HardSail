# -*- coding: utf-8 -*-
# from odoo import http


# class Compomatic(http.Controller):
#     @http.route('/compomatic/compomatic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/compomatic/compomatic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('compomatic.listing', {
#             'root': '/compomatic/compomatic',
#             'objects': http.request.env['compomatic.compomatic'].search([]),
#         })

#     @http.route('/compomatic/compomatic/objects/<model("compomatic.compomatic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('compomatic.object', {
#             'object': obj
#         })

