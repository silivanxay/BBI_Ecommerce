
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ImageSerializer


class ImageUploadView(APIView):

    def post(self, request, *args, **kwargs):

      image_serializer = ImageSerializer(data=request.data)

      if image_serializer.is_valid():
          image_serializer.save()
          return Response(image_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)