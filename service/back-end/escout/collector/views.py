import logging

from django.db import DatabaseError
from django.http import HttpResponse
from escout.dashboard.models import Application, Event

logger = logging.getLogger(__name__)


# NOTE Tracking URL 127.0.0.1:8081/collector/__tf.gif?pid=bf1f2920-7773-11e6-9395-0800279eb82c&usi=5938498940&utz=-180&nm=click&tp=action&p=2&stt=1473527002230&spt=1473527027805&dsc=click on a button
# TODO Needs to be made async
# Main request tracking method
def track(request, file_name):
    application_personal_id = request.GET.get('pid', False)
    if application_personal_id:
        try:

            application_model = Application.objects.get(personal_id=application_personal_id)

            event = Event()
            event.application = application_model

            event.user_session_id = request.GET.get('usi', None)
            event.user_timezone = request.GET.get('utz', None)
            event.name = request.GET.get('nm', None)
            event.type = request.GET.get('tp', None)
            event.priority = request.GET.get('p', None)
            event.start_time = request.GET.get('stt', None)
            event.stop_time = request.GET.get('spt', None)
            event.description = request.GET.get('dsc', None)
            event.save()

        except (Application.DoesNotExist, DatabaseError) as error:
            logger.error(error)
        finally:
            return _respond()


# Prepare and return fake image
def _respond():
    gif_file = open("escout/static/file/__tf.gif", "rb")
    file_data = gif_file.read()

    response = HttpResponse(file_data, content_type="image/gif")

    return response
