from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializable import Blogserializer

class BloagListCreate(APIView):
    def get(self, request):
        bloags = Blog.objects.all()
        serializer = Blogserializer(bloags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Blogserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BloagDetail(APIView):
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return None

    def get(self, request, pk):
        bloag = self.get_object(pk)
        if bloag is None:
            return Response({"error": "Not Found"}, status=404)
        serializer = Blogserializer(bloag)
        return Response(serializer.data)

    def put(self, request, pk):
        bloag = self.get_object(pk)
        if bloag is None:
            return Response({"error": "Not Found"}, status=404)

        serializer = Blogserializer(bloag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        bloag = self.get_object(pk)
        if bloag is None:
            return Response({"error": "Not Found"}, status=404)

        bloag.delete()
        return Response(status=204)
