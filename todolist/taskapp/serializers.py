from rest_framework import serializers
from taskapp.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор по модели Task."""

    class Meta:
        model = Task
        read_only_fields = ["id", "start", "end"]
        fields = read_only_fields + ["title", "status"]

        # fields = "__all__"
