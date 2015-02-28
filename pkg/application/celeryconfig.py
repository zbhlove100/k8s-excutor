from kombu import Queue

CELERY_IMPORTS = ('pkg.domain.common.bl.impl.task.tasks', )
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost:5672//'
CELERY_TASK_RESULT_EXPIRES=3600
CELERY_DEFAULT_QUEUE = 'celery'
CELERY_QUEUES = (
    Queue('celery',    routing_key='celery'),
)
CELERY_DEFAULT_EXCHANGE = 'celery'
CELERY_DEFAULT_ROUTING_KEY = 'celery'
CELERY_ROUTES = {
    'pkg.tasks.add': {
        'queue': 'celery',
        'routing_key': 'celery',
    },
}