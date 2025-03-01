# -*- coding: utf-8 -*-
# Copyright 2019-2022 Artem Shurshilov
# Odoo Proprietary License v1.0

# This software and associated files (the "Software") may only be used (executed,
# modified, executed after modifications) if you have purchased a valid license
# from the authors, typically via Odoo Apps, or if you have received a written
# agreement from the authors of the Software (see the COPYRIGHT file).

# You may develop Odoo modules that use the Software as a library (typically
# by depending on it, importing it and using its resources), but without copying
# any source code or material from the Software. You may distribute those
# modules under the license of your choice, provided that this license is
# compatible with the terms of the Odoo Proprietary License (For example:
# LGPL, MIT, or proprietary licenses similar to this one).

# It is forbidden to publish, distribute, sublicense, or sell copies of the Software
# or modified copies of the Software.

# The above copyright notice and this permission notice must be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from odoo import fields, models, api
import json


class ResConfigSettingsIapFirebase(models.TransientModel):
    _inherit = 'res.config.settings'

    # Wizard default data
    res_users_firebase_title_web = fields.Char(
        string='Firebase title web', help="Secret firebase title web-app")
    res_users_firebase_body_web = fields.Char(
        string='Firebase body web', help="Secret firebase body web-app")
    res_users_firebase_icon_web = fields.Char(
        string='Firebase icon web', help="Secret firebase icon web-app")
    res_users_firebase_image_web = fields.Char(
        string='Firebase image web', help="Secret firebase image web-app")
    res_users_firebase_action_web = fields.Char(
        string='Firebase action web', help="Secret firebase action web-app")

    # Key for all notifications
    mail_firebase_key = fields.Char(string='Mail Firebase key', default="AAAAmsbwHC4:APA91bHOpTMKFkbZ5qhAVFsb0Qgk2Hsgh3H_oYh_8xxYleJzGm0LHcljtcUYBP-KWmB5hITRrLFEHLJOphWSwLUr9Qtr4md3VdTKu8_tHl7k69RmfIaAiCj88fJisRmWVJACyChGKJYf",
                                    help="Secret firebase key")
    firebase_channel_notify = fields.Boolean(string='Channels(discuss) notify', default=True,
    help="Enable notify from discuss channels messages")
    firebase_message_post_notify = fields.Boolean(string='Chatter(record) notify', default=False,
    help="Enable notify from discuss channels messages")
    # firebase_white_list_models = fields.Many2many('ir.model', domain=[('transient', '=', False)],
    # help="White lists models to use in message post")

    def set_values(self):
        res = super(ResConfigSettingsIapFirebase, self).set_values()
        config_parameters = self.env['ir.config_parameter']
        config_parameters.set_param(
            "mail_firebase_key", self.mail_firebase_key)
        config_parameters.set_param(
            "res_users_firebase_title_web", self.res_users_firebase_title_web)
        config_parameters.set_param(
            "res_users_firebase_body_web", self.res_users_firebase_body_web)
        config_parameters.set_param(
            "res_users_firebase_icon_web", self.res_users_firebase_icon_web)
        config_parameters.set_param(
            "res_users_firebase_image_web", self.res_users_firebase_image_web)
        config_parameters.set_param(
            "res_users_firebase_action_web", self.res_users_firebase_action_web)
        config_parameters.set_param(
            "firebase_channel_notify", self.firebase_channel_notify)
        config_parameters.set_param(
            "firebase_message_post_notify", self.firebase_message_post_notify)
        # config_parameters.set_param(
        #     "firebase_white_list_models", self.firebase_white_list_models.ids)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettingsIapFirebase, self).get_values()
        mail_firebase_key = self.env['ir.config_parameter'].get_param(
            'mail_firebase_key')
        if not mail_firebase_key:
            mail_firebase_key = "AAAAmsbwHC4:APA91bHOpTMKFkbZ5qhAVFsb0Qgk2Hsgh3H_oYh_8xxYleJzGm0LHcljtcUYBP-KWmB5hITRrLFEHLJOphWSwLUr9Qtr4md3VdTKu8_tHl7k69RmfIaAiCj88fJisRmWVJACyChGKJYf"
        res.update(mail_firebase_key=mail_firebase_key)
        res.update(res_users_firebase_title_web=self.env['ir.config_parameter'].get_param(
            'res_users_firebase_title_web'))
        res.update(res_users_firebase_body_web=self.env['ir.config_parameter'].get_param(
            'res_users_firebase_body_web'))
        res.update(res_users_firebase_icon_web=self.env['ir.config_parameter'].get_param(
            'res_users_firebase_icon_web'))
        res.update(res_users_firebase_image_web=self.env['ir.config_parameter'].get_param(
            'res_users_firebase_image_web'))
        res.update(res_users_firebase_action_web=self.env['ir.config_parameter'].get_param(
            'res_users_firebase_action_web'))
        res.update(firebase_channel_notify=self.env['ir.config_parameter'].get_param(
            'firebase_channel_notify'))
        res.update(firebase_message_post_notify=self.env['ir.config_parameter'].get_param(
            'firebase_message_post_notify'))
        # if self.env['ir.config_parameter'].get_param('firebase_white_list_models'):
        #     names_list =self.env['ir.model'].browse(json.loads(self.env['ir.config_parameter'].get_param(
        #         'firebase_white_list_models'))).mapped('name')
        #     res.update(firebase_white_list_models=names_list)
        # else:
        #     res.update(firebase_white_list_models=self.env['ir.config_parameter'].get_param(
        #     'firebase_white_list_models'))
        return res
