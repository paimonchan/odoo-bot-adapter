from odoo import models, fields
from ..helpers import consts

class BotEvent(models.Model):
    _name = 'paimon.bot.event'

    bot_type = fields.Selection(consts.BOT_TYPES)