# -*- coding: utf-8 -*-
# from odoo import http


# class Hardsail(http.Controller):
#     @http.route('/hardsail/hardsail', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hardsail/hardsail/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hardsail.listing', {
#             'root': '/hardsail/hardsail',
#             'objects': http.request.env['hardsail.hardsail'].search([]),
#         })

#     @http.route('/hardsail/hardsail/objects/<model("hardsail.hardsail"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hardsail.object', {
#             'object': obj
#         })

