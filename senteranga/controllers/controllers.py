# -*- coding: utf-8 -*-
# from odoo import http


# class Senteranga(http.Controller):
#     @http.route('/senteranga/senteranga/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/senteranga/senteranga/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('senteranga.listing', {
#             'root': '/senteranga/senteranga',
#             'objects': http.request.env['senteranga.senteranga'].search([]),
#         })

#     @http.route('/senteranga/senteranga/objects/<model("senteranga.senteranga"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('senteranga.object', {
#             'object': obj
#         })
