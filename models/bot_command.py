from odoo import models, fields
from ..helpers import consts

class BotCommand(models.Model):
    _name = 'paimon.bot.command'

    bot_type = fields.Selection(consts.BOT_TYPES)