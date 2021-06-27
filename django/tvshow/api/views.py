from rest_framework import generics
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from django.db.models import Max
from .serializers import *

from tvshow.models import TVShow
from math import ceil


class SetPagination(PageNumberPagination):
    page_size = 5

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "length": ceil(self.page.paginator.count / self.page_size),
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "results": data,
            }
        )


class TVShowListAPIView(generics.ListAPIView):
    queryset = (
        TVShow.objects.filter(releasev2__gt=0)
        .annotate(latest_release=Max("releasev2__date_added"))
        .order_by("-latest_release")
    )
    serializer_class = TVShowSerializer
    pagination_class = SetPagination


class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TVShowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = TVShow.objects.all()
    serializer_class = TVShowDetailSerializer
    lookup_field = "id"


class ReleaseRetrieveAPIView(generics.ListAPIView):
    queryset = ReleaseV2.objects.all()
    serializer_class = ReleaseV2Serializer

    def get_queryset(self):
        tvshow_id = self.kwargs["id"]
        return ReleaseV2.objects.filter(tvshow__id=tvshow_id)


class TVShowCreateAPIView(generics.CreateAPIView):
    queryset = TVShow.objects.all()
    serializer_class = TVShowAddSerializer


class ReleaseCreateAPIView(generics.CreateAPIView):
    queryset = ReleaseV2.objects.all()
    serializer_class = ReleaseAddSerializer


class TVShowStateView(generics.UpdateAPIView):
    queryset = TVShow.objects.all()
    serializer_class = TVShowStateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION").split(" ")[-1]
        token_user = Token.objects.get(key=token).user.id
        if True:
            resp = {
                "yaya": token_user,
                "msg": "Error",
            }
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        return super().put(request, *args, **kwargs)
