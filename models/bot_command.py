import code
from unicodedata import name
from odoo import models, fields, api
from ..helpers import consts

PREFIX_NAME = 'COMMAND/'
class BotCommand(models.Model):
    _name = 'paimon.bot.command'

    name = fields.Char(copy=False, readonly=True)
    bot_type = fields.Selection(consts.BOT_TYPES)
    # not using relation from ir.model
    # because for easy create entry from xml (hard to connect existing entry relation into xml)
    # its more easy to use string instead
    model = fields.Char(
        string='Model Name', track_visibility='onchange',
        help='Model on which the server command need to trigger.')
    method = fields.Char(
        string='Method Name', track_visibility='onchange',
        help='Function which will be call when command is passing')
    channel_id = fields.Char(
        string='Channel ID', required=True, index=True, copy=False,
        track_visibility='onchange',
        help="""
        only from this channel that allowed to triggered command.
        please note, fill channel id, not channel name, because some 3rd party,
        not return channel name (some return but not real name).
        for slack:
            https://app.slack.com/client/TMXFTDKPG/GV2D1HHNH
            the channel id is GV2D1HHNH (on URI[3])
        """)
    command = fields.Char(
        string='Command', required=True, index=True, copy=False, track_visibility='onchange',
        help='trigger mesasge for selected method or default message')
    default_message = fields.Text(
        string='Default Message',
        help="""
            when no model_name is filled, then default message will be 
            used as return message that will post to 3rd party platform.
        """)

    def _get_sequence(self):
        sequence_model = self.env['ir.sequence'].sudo()
        sequence = sequence_model.search([('code', '=', self._name)], limit=1)
        if not sequence:
            sequence = sequence_model.create(dict(
                prefix      = PREFIX_NAME,
                name        = self._name,
                code        = self._name,
                paddings    = 3
            ))
        return sequence._next()
    
    @api.model
    def create(self, vals):
        if not vals.get('name'):
            vals['name'] = self._get_sequence()
        return super().create(vals)