from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Record, RecordReview

class RecordSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(read_only=True)
    # _id = serializers.SerializerMethodField(read_only=True)
    # isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Record
        fields = '__all__'