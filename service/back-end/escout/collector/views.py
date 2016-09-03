from django.http import HttpResponse


# TODO Create track request example for testing
# TODO Needs to be made async
# Main request tracking method
def track(request, file_name):
    # Collect request data
    client_id = request.GET['ci']
    client_host = request.GET['ch']
    client_session_id = request.GET['csi']

    # Prepare record
    record = file_name + " " + client_id + " " + client_host + " " + client_session_id + "\n"

    try:
        # TODO Replace for the database recording
        log_file = open('log.txt', 'a', encoding="utf-8")
        log_file.write(record)
        log_file.close()

    except IOError as error:
        print(error.message)

    # Prepare and return fake image
    gif_file = open("escout/static/file/__tf.gif", "rb")
    file_data = gif_file.read()

    response = HttpResponse(file_data, content_type="image/gif")
    return response
