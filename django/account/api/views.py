from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import *
from account.models import *


class RegistrationCreateAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            account = Account.objects.get(username=serializer.data["username"])
            token = Token.objects.get(user=account.pk).key
            resp = {
                "data": serializer.data,
                "msg": "Success",
                "token": token,
            }
            return Response(resp, status=status.HTTP_201_CREATED)
        resp = {
            "data": serializer.errors,
            "msg": "Error",
        }
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class AccountRetrieveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token = request.META.get("HTTP_AUTHORIZATION").split(" ")[-1]
        user = Account.objects.filter(id=Token.objects.get(key=token).user.id)
        serializer = AccountDetailSerializer(user, many=True)
        return Response(serializer.data)


class SerieCreateAPIView(generics.CreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieAddSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION").split(" ")[-1]
        token_user = Token.objects.get(key=token).user.id
        serie_user = request.data.get("readinglist")
        if serie_user != token_user:
            resp = {
                "msg": "Error",
            }
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)


class SerieRetrieveDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION").split(" ")[-1]
        token_user = Token.objects.get(key=token).user.id
        serie_user = Serie.objects.get(pk=self.kwargs["pk"]).readinglist.pk
        if serie_user != token_user:
            resp = {
                "msg": "Error",
            }
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION").split(" ")[-1]
        token_user = Token.objects.get(key=token).user.id
        serie_user = Serie.objects.get(pk=self.kwargs["pk"]).readinglist.pk
        if serie_user != token_user:
            resp = {
                "msg": "Error",
            }
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        return super().delete(request, *args, **kwargs)


class ReadingListAPIView(generics.ListAPIView):
    serializer_class = ReadingListSerieSerializer

    def get_queryset(self):
        readinglist_id = self.kwargs["readinglist"]
        return Serie.objects.filter(readinglist=readinglist_id)

    def get(self, request, readinglist, format=None):
        follows = self.get_queryset()
        serializer = ReadingListSerieSerializer(follows, many=True)
        return Response(serializer.data)


class ReadingList2CreateAPIView(generics.CreateAPIView):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListAddSerializer


class ReadingListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token = request.META.get("HTTP_AUTHORIZATION").split(" ")[-1]
        try:
            user = ReadingList(account=Token.objects.get(key=token).user)
            user.save()
        except Exception:
            resp = {
                "msg": "Error",
            }
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        resp = {
            "msg": "Success",
        }
        return Response(resp, status=status.HTTP_201_CREATED)
