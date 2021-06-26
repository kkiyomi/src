from rest_framework import serializers
from account.models import *
from tvshow.models import TVShow, ReleaseV2


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Account
        fields = ["email", "username", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def save(self):

        account = Account(
            email=self.validated_data["email"], username=self.validated_data["username"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        account.set_password(password)
        account.save()
        return account


class ReadingListAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingList
        fields = ["account"]


class AccountDetailSerializer(serializers.ModelSerializer):
    readinglist = ReadingListAddSerializer()

    class Meta:
        model = Account
        fields = ["id", "username", "email", "date_joined", "last_login", "readinglist"]


class SerieAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ["current_release_id", "tvshow", "readinglist"]


class SerieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ["current_release_id"]


class ReleaseV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseV2
        fields = ["id", "number", "link", "date_added"]


class TVShowSerializer(serializers.ModelSerializer):
    latest = ReleaseV2Serializer(read_only=True, source="latest_release")

    class Meta:
        model = TVShow
        fields = ["id", "title", "slug", "latest"]


class ReadingListSerieSerializer(serializers.ModelSerializer):
    tvshow = TVShowSerializer()
    release = ReleaseV2Serializer(read_only=True)

    class Meta:
        model = Serie
        fields = ["id", "current_release_id", "tvshow", "readinglist", "release"]
