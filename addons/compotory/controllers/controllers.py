# -*- coding: utf-8 -*-
# from odoo import http


# class Compotory(http.Controller):
#     @http.route('/compotory/compotory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/compotory/compotory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('compotory.listing', {
#             'root': '/compotory/compotory',
#             'objects': http.request.env['compotory.compotory'].search([]),
#         })

#     @http.route('/compotory/compotory/objects/<model("compotory.compotory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('compotory.object', {
#             'object': obj
#         })

