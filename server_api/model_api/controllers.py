import base64
from wsgiref.util import FileWrapper

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def audio_to_table(request: WSGIRequest) -> HttpResponse:
    try:
        if request.content_type in ["multipart/form-data", "application/x-www-form-urlencoded"]:
            encoding = request.POST.get("coded", "")
            # get file from request body coded by base64 and convert it to .wav file
            audio_bytes = dict(request.POST).get("wav")
            # read file "test_ouput.csv" and put it to variable "result_table" encoded by base64
            with open("tests_input/test_output.csv", "rb") as file:
                file_str = bytes(file.read())
                result_table_as_bytes = file_str
                if encoding == "base64":
                    result_table_as_bytes = base64.b64encode(file_str)
                result_table = SimpleUploadedFile("result.csv", result_table_as_bytes, content_type="text/csv")
                # return status code 200 and response body .csv file
                return HttpResponse(result_table, content_type="text/csv")
        else:
            return HttpResponse("Bad request", status=400)
    except Exception as _:
        # Return unknown error
        return HttpResponse("Unknown error", status=500)