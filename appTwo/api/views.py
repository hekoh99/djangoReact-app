from django.shortcuts import render
from rest_framework import serializers, generics
from chat.models import Chat
from rest_framework.response import Response

# Create your views here.
class ChatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'name', 'create_dt')


# api/moim 으로 get하면 이 listview로 연결
class chatLV(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

class chatDV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer
