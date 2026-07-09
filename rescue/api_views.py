from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Report, RescueUpdate, Animal, AdoptionRequest
from .serializers import (
    ReportListSerializer,
    ReportDetailSerializer,
    RescueUpdateSerializer,
    AnimalSerializer,
    AdoptionRequestSerializer,
)


class ReportListAPIView(generics.ListAPIView):
    serializer_class = ReportListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Report.objects.select_related(
            'reporter',
            'assigned_shelter',
            'assigned_rescuer',
        ).order_by('-reported_at')


class ReportDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ReportDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Report.objects.select_related(
            'reporter',
            'assigned_shelter',
            'assigned_rescuer',
        ).prefetch_related('rescue_updates')


class RescueUpdateListAPIView(generics.ListAPIView):
    serializer_class = RescueUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RescueUpdate.objects.select_related(
            'report',
            'rescuer',
        ).order_by('-created_at')


class AnimalListAPIView(generics.ListAPIView):
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Animal.objects.select_related(
            'report',
            'shelter',
            'assigned_rescuer',
        ).order_by('-updated_at')


class AnimalDetailAPIView(generics.RetrieveAPIView):
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Animal.objects.select_related(
            'report',
            'shelter',
            'assigned_rescuer',
        )


class AdoptionRequestListAPIView(generics.ListAPIView):
    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AdoptionRequest.objects.select_related(
            'animal',
            'animal__report',
            'requester',
            'processed_by',
        ).order_by('-created_at')


class AdoptionRequestDetailAPIView(generics.RetrieveAPIView):
    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return AdoptionRequest.objects.select_related(
            'animal',
            'animal__report',
            'requester',
            'processed_by',
        )