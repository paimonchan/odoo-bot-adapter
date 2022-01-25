import logging
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime
from ..helpers import consts

_logger = logging.getLogger(__name__)

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

    def _get_command_id(self):
        self.ensure_one()
        command = self.env['paimon.bot.command'].search([
            ('channel_id', '=', self.channel),
            ('command', '=', self.command)
        ])
        return command.id

    def assign_command(self):
        for record in self:
            if record.command_id: continue
            record.command_id = record._get_command_id()

    def force_assign_command(self):
        for record in self:
            record.command_id = record._get_command_id()

    def run(self):
        for event in self:
            if event.state != consts.EVENT_STATE_DRAFT:
                continue
            event.assign_command()
            event.process_command_function()
    
    def process_command_function(self):
        if not self.command_id:
            return
        command_id = self.command_id
        model_name = command_id.model
        method_name = command_id.method
        default_message = command_id.default_message
        model = self.env['ir.model'].search([('model', '=', model_name)])

        # check if model is exist
        if not model:
            message = 'Model not found: {}'.format(model_name)
            _logger.warning(message)
            raise UserError(message)

        # if not callable function and not default message is defined, mark as error and skip
        if not model_name and not method_name and not default_message:
            message = 'model_id, model_name and default_message is not defined.'
            _logger.warning(message)
            raise UserError(message)
        

    @api.model
    def create(self, vals):
        res = super().create(vals)
        res.assign_command()
        return res