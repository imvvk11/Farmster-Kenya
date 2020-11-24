import urllib.parse
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import views, status

from farmster_server.forms.media import UploadFileForm
from farmster_server.models.media import Media


class MediaUpload(views.APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            media = Media(file=request.FILES['file'])
            media.save()
            url = urllib.parse.urljoin(request.build_absolute_uri('/'), media.file.url)
            return Response(status=status.HTTP_201_CREATED, data={
                'url': url
            })


media_upload = MediaUpload.as_view()
