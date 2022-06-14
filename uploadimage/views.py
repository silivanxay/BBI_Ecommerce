from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ImageSerializer
from .models import Image


class ImageUploadView(APIView):

    def get(self, request, *args, **kwargs):

        queryset = Image.objects.all()
        image_serializer = ImageSerializer(queryset, many=True)

        return Response(image_serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):

        image_serializer = ImageSerializer(data=request.data)

        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            queryset = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return JsonResponse({'message': 'Image was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
