from rest_framework.views import APIView
from .models import Announcement
from .serializers import AnnouncementSerializer, AnnouncementDetailSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound, NotAuthenticated, PermissionDenied

class Announcements(APIView):

    def get(self, request, pk):
        try:
            page = request.query_params.get('page', 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = 10
        start = (page-1) * page_size
        end = start + page_size
        all_Announcements = Announcement.objects.all()[start:end]
        serializer = AnnouncementSerializer(all_Announcements, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if request.user.is_staff or request.user.is_superuser:
            serializer = AnnouncementSerializer(data=request.data)
            if serializer.is_valid():
                new_announcement = serializer.save(writer=request.user)
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
        
    def delete(self, request, pk):
        announcement = self.get_object(pk)
        # 1. 유저가 아니면 삭제할 수 없다.
        if not request.user.is_authenticated:
            raise NotAuthenticated
        # 2. 작성자가 아니면 삭제할 수 없다.
        if not request.user.is_staff or not request.user.is_superuser:
            raise PermissionDenied
        announcement.delete()
        return Response(status=HTTP_204_NO_CONTENT)    