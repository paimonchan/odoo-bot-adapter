from odoo import models, fields
from ..helpers import consts

class BotEvent(models.Model):
    _name = 'paimon.bot.event'

    bot_type = fields.Selection(consts.BOT_TYPES)
    command_id = fields.Many2one(
        'fore.bot.command', readonly=True)
    channel_id = fields.Char(
        states=STATES_READONLY,
        help='store id from channel message 3rd party')
    channel_name = fields.Char(
        states=STATES_READONLY,
        help='store name from channel message 3rd party')
    user_id = fields.Char(
        states=STATES_READONLY,
        help='user id from 3rd party')
    user_name = fields.Char(
        states=STATES_READONLY,
        help='user name from 3rd party')
    command = fields.Char(
        states=STATES_READONLY,
        help='command text that send from channel message')
    text = fields.Char(
        states=STATES_READONLY,
        help='text after command text')