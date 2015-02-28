from __future__ import absolute_import

from celery import Celery
import sys
sys.path.append("/home/zhangbohan/PycharmProjects/k8s-excutor")

app = Celery('task')

# Optional configuration, see the application user guide.
app.config_from_object('pkg.application.celeryconfig')

if __name__ == '__main__':
    app.start()