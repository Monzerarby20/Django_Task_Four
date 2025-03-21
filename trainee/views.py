from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.generic import ListView
from .models import Trainee, Track
from .serializers import TraineeSerializer, TrackSerializer

class ListTraineeView(ListView):
    model = Trainee
    template_name = "trainee_list.html"

class TraineeListCreateView(APIView):
    def get(self, request):
        trainees = Trainee.objects.all()
        serializer = TraineeSerializer(trainees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateTraineeView(generics.UpdateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

class DeleteTraineeView(generics.DestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

class AddTraineeView(generics.CreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

@api_view(['PUT'])
def track_update(request, pk):
    try:
        track = Track.objects.get(pk=pk)
    except Track.DoesNotExist:
        return Response({"error": "Track not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TrackSerializer(track, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
