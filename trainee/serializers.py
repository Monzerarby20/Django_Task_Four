from rest_framework import serializers
from .models import Trainee ,Track

class TraineeSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Trainee.objects.all())

    class Meta:
        model = Trainee
        fields = '__all__'
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track  # Ensure Track model exists in models.py
        fields = '__all__'