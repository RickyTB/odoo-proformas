# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Proforma(models.Model):
    _name = "proformas.proforma"  # nombre de la base de datos: todo_app
    _description = "Proformas"

    name = fields.Char(string="Nombre")
    year = fields.Char(string=u"Año")
    institution_id = fields.Many2one(
        comodel_name='proformas.institution', string=u'Institución')
    area_org_id = fields.Many2one(
        comodel_name='proformas.area.org', string=u"Area Orgánica")
    area_geo_id = fields.Many2one(
        comodel_name='proformas.area.geo', string=u"Area Geográfica")
    # aselection = fields.Selection([('a', 'A'), ('b', 'B')])
    partida_ids = fields.One2many(
        comodel_name="proformas.partida", string="Partida", inverse_name='proforma_id')


# campos como atributos
# primero escribir todo
#

class Institution(models.Model):
    _name = "proformas.institution"  # nombre de la base de datos: todo_app
    _description = ""

    name = fields.Char(string=u"Nombre de la institución")


class AreaOrg(models.Model):
    _name = "proformas.area.org"  # nombre de la base de datos: todo_app
    _description = ""

    name = fields.Char(string=u"Nombre")


class AreaGeo(models.Model):
    _name = "proformas.area.geo"  # nombre de la base de datos: todo_app
    _description = ""

    name = fields.Char(string=u"Nombre")


class Partida(models.Model):
    _name = "proformas.partida"

    name = fields.Char(string="Nombre")
    month1 = fields.Float(string="Enero", default=0)
    month2 = fields.Float(string="Febrero", default=0)
    month3 = fields.Float(string="Marzo", default=0)
    month4 = fields.Float(string="Abril", default=0)
    month5 = fields.Float(string="Mayo", default=0)
    month6 = fields.Float(string="Junio", default=0)
    month7 = fields.Float(string="Julio", default=0)
    month8 = fields.Float(string="Agosto", default=0)
    month9 = fields.Float(string="Septiembre", default=0)
    month10 = fields.Float(string="Octubre", default=0)
    month11 = fields.Float(string="Noviembre", default=0)
    month12 = fields.Float(string="Diciembre", default=0)
    total = fields.Float(compute="compute_total", string="Total")
    proforma_id = fields.Many2one(
        comodel_name='proformas.proforma', string=u"Proforma")

    @api.onchange("month1", "month2", "month3", "month4", "month5", "month6", "month7", "month8", "month9", "month10", "month11", "month12")
    def compute_total(self):
        for record in self:
            record.total = record.month1 + record.month2 + record.month3 + record.month4 + record.month5 + record.month6 + \
                record.month7 + record.month8 + record.month9 + \
                record.month10 + record.month11 + record.month12
