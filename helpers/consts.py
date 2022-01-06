BOT_SLACK = 'slack'
BOT_TELEGRAM = 'telegram'

BOT_TYPES = [
    (BOT_SLACK, 'slack'),
    (BOT_TELEGRAM, 'telegram'),
]

EVENT_STATE_DRAFT = 'draft'
EVENT_STATE_FAIL = 'fail'
EVENT_STATE_DONE = 'done'

EVENT_STATE_SELECTION = [
    (EVENT_STATE_DRAFT, 'Draft'),
    (EVENT_STATE_FAIL, 'Failure'),
    (EVENT_STATE_DONE, 'Done'),
]