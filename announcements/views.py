from rest_framework.views import APIView
from .models import Announcement
from .serializers import AnnouncementSerializer, AnnouncementDetailSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound, NotAuthenticated

class Announcements(APIView):

    def get(self, request):
        all_Announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(all_Announcements, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if request.user.is_authenticated:
            serializer = AnnouncementSerializer(data=request.data)
            if serializer.is_valid():
                new_announcement = serializer.save()
                return Response(AnnouncementSerializer(new_announcement))
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated

class AnnouncementDetail(APIView):

    def get_object(self, pk):
        try:
            return Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            raise NotFound
        
    def get(self, request, pk):
        serializer = AnnouncementDetailSerializer(self.get_object(pk))
        return Response(serializer.data)
    
    def put(self, request, pk):
        serializer = AnnouncementDetailSerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
            )
        if serializer.is_valid():
            updated_review = serializer.save()
            return Response(AnnouncementDetailSerializer(updated_review).data)
        else:
            return Response(serializer.errors)