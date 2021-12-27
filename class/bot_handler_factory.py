from .bot_handler_abstract import BotHandlerAbstract

class BotHandlerFactory(BotHandlerAbstract):
    """
    factory for all bot handler.
    """
    handlers = dict()
    
    def __init__(self):
        self.handlers = {
            # TODO add type bot (ie slack, telegrams, discord etc)
        }
    
    def response_handler(self):
        # TODO call response for each corresponding bot handler type
        pass