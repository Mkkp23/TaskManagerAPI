from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "completed", "created_at"]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("The title field cannot be empty.")
        return value

    def validate_description(self, value):
        if value and len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 chars.")
        return value
