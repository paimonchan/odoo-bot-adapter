from ..helpers import consts
from .bot_handler_abstract import BotHandlerAbstract
from .bot_slack import BotSlack

class BotHandlerFactory(BotHandlerAbstract):
    """
    factory for all bot handler.
    """
    handlers = dict()
    
    def __init__(self):
        self.handlers = {
            # TODO add type bot (ie slack, telegrams, discord etc)
            consts.BOT_SLACK: BotSlack()
        }
    
    def response_handler(self, bot_event, message):
        bot_type = False  # TODO: add field bot type in command
        handler = self.handlersl.get(bot_type)
        if not handler:
            message = 'Not found handler for bot type: {}'.format(bot_type)
            raise Exception(message)
        handler.response_handler(bot_event, message)