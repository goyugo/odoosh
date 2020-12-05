# -*- coding: utf-8 -*-

from odoo import models, fields, api


class add_field(models.Model):
    _inherit = 'res.partner'

    nama_panggilan = fields.Char('Nama Panggilan')

