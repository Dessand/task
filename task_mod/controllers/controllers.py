# -*- coding: utf-8 -*-
# from odoo import http


# class TaskMod(http.Controller):
#     @http.route('/task_mod/task_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_mod/task_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_mod.listing', {
#             'root': '/task_mod/task_mod',
#             'objects': http.request.env['task_mod.task_mod'].search([]),
#         })

#     @http.route('/task_mod/task_mod/objects/<model("task_mod.task_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_mod.object', {
#             'object': obj
#         })
