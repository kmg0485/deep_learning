from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
import mimetypes
import os
from django.http import HttpResponse, Http404
import urllib
from .models import Painting
from users.models import User
from painters.models import Painting, Painter
from painters.serializers import ImageCreateSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from painters.serializers import ImageCreateSerializer

"""
def Download_view(request, pk):
    painting = get_object_or_404(Painting, pk=pk)
    url = painting.image.url[1:]
    file_url = urllib.parse.unquote(url)
    
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            # quote_file_url = urllib.parse.quote(painting.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            # response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404
"""    
    
class ImageView(APIView) :
    permission_classes = [IsAuthenticated]
    
    def post(self, request) :
        serializer = ImageCreateSerializer(data = request.data)
        painter = Painter.objects.get(id=request.data["painter"])
        print(f"페인터의 id : {request.data['painter']}")
        print(f"화풍 스타일 : {painter.style}")
        if serializer.is_valid() :
            serializer.save(user=request.user)
            print(f"콘텐트, 넣은 사진 : {serializer.data['picture']}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            