# -*- coding: utf-8 -*-
# © 2017 Stefan Becker <s.becker@humanilog.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models, _


class EventEvent(models.Model):
    _inherit = 'event.event'

    team_min = fields.Integer(string=_('Minimum Teams'))
    team_max = fields.Integer(string=_('Maximum Teams'))
    team_attendee_min = fields.Integer(string=_('Minimum Attendees / Teams'))
    team_attendee_max = fields.Integer(string=_('Maximum Attendees / Teams'))


class EventTeam(models.Model):
    _name = 'event.team'

    name = fields.Char(string=_('Name'))
    slogan = fields.Char(string=_('slogan'))
    logo = fields.Binary(string=_('logo'))


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    team_id = fields.Many2one(
        string='Event team',
        comodel_name='event.team')
