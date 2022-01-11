from odoo import models, fields
from datetime import datetime
from ..helpers import consts

STATES_READONLY = {
    consts.EVENT_STATE_DONE: [('readonly', True)]
}

class BotEvent(models.Model):
    _name = 'paimon.bot.event'

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
        help='command that send from channel message')
    payload = fields.Char(
        states=STATES_READONLY,
        help='text/payload after command')
    date = fields.Datetime(
        copy=False, readonly=True,
        default=datetime.today())
    state = fields.Selection(
        consts.EVENT_STATE_SELECTION, required=True)
    error = fields.Char(
        copy=False, readonly=True,
        help='store error message when bot event failed to run')