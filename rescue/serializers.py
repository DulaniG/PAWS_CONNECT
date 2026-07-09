from rest_framework import serializers
from .models import Report, RescueUpdate, Animal, AdoptionRequest


def get_user_display_name(user):
    if user:
        return getattr(user, 'full_name', '') or user.username
    return None


def build_file_url(request, file_field):
    if file_field:
        url = file_field.url
        if request:
            return request.build_absolute_uri(url)
        return url
    return None


class RescueUpdateSerializer(serializers.ModelSerializer):
    report_id = serializers.IntegerField(source='report.id', read_only=True)
    rescuer_name = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = RescueUpdate
        fields = [
            'id',
            'report_id',
            'rescuer_name',
            'status',
            'status_display',
            'update_text',
            'photo_url',
            'created_at',
        ]

    def get_rescuer_name(self, obj):
        return get_user_display_name(obj.rescuer)

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_photo_url(self, obj):
        request = self.context.get('request')
        return build_file_url(request, obj.photo)


class AnimalSummarySerializer(serializers.ModelSerializer):
    treatment_status_display = serializers.SerializerMethodField()
    gender_display = serializers.SerializerMethodField()
    animal_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = [
            'id',
            'name',
            'age',
            'gender',
            'gender_display',
            'health_status',
            'treatment_status',
            'treatment_status_display',
            'animal_image_url',
            'adoption_ready_date',
            'outcome_date',
        ]

    def get_treatment_status_display(self, obj):
        return obj.get_treatment_status_display()

    def get_gender_display(self, obj):
        return obj.get_gender_display()

    def get_animal_image_url(self, obj):
        request = self.context.get('request')
        return build_file_url(request, obj.animal_image)


class ReportListSerializer(serializers.ModelSerializer):
    report_id = serializers.IntegerField(source='id', read_only=True)
    reporter_name = serializers.SerializerMethodField()
    animal_type_display = serializers.SerializerMethodField()
    condition_display = serializers.SerializerMethodField()
    suggested_priority_display = serializers.SerializerMethodField()
    priority_display = serializers.SerializerMethodField()
    verification_status_display = serializers.SerializerMethodField()
    report_status_display = serializers.SerializerMethodField()
    current_rescue_status_display = serializers.SerializerMethodField()
    assigned_shelter_name = serializers.SerializerMethodField()
    assigned_rescuer_name = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = [
            'id',
            'report_id',
            'reporter_name',
            'animal_type',
            'animal_type_display',
            'other_animal_type',
            'condition',
            'condition_display',
            'description',
            'image_url',
            'latitude',
            'longitude',
            'location_description',
            'map_link',
            'suggested_priority',
            'suggested_priority_display',
            'priority',
            'priority_display',
            'verification_status',
            'verification_status_display',
            'report_status',
            'report_status_display',
            'current_rescue_status',
            'current_rescue_status_display',
            'assigned_shelter_name',
            'assigned_rescuer_name',
            'reported_at',
            'updated_at',
        ]

    def get_reporter_name(self, obj):
        return get_user_display_name(obj.reporter)

    def get_animal_type_display(self, obj):
        return obj.get_animal_type_display()

    def get_condition_display(self, obj):
        return obj.get_condition_display()

    def get_suggested_priority_display(self, obj):
        return obj.get_suggested_priority_display()

    def get_priority_display(self, obj):
        if obj.priority:
            return obj.get_priority_display()
        return None

    def get_verification_status_display(self, obj):
        return obj.get_verification_status_display()

    def get_report_status_display(self, obj):
        return obj.get_report_status_display()

    def get_current_rescue_status_display(self, obj):
        return obj.get_current_rescue_status_display()

    def get_assigned_shelter_name(self, obj):
        return get_user_display_name(obj.assigned_shelter)

    def get_assigned_rescuer_name(self, obj):
        return get_user_display_name(obj.assigned_rescuer)

    def get_image_url(self, obj):
        request = self.context.get('request')
        return build_file_url(request, obj.image)


class ReportDetailSerializer(ReportListSerializer):
    rescue_updates = RescueUpdateSerializer(many=True, read_only=True)
    animal = serializers.SerializerMethodField()

    class Meta(ReportListSerializer.Meta):
        fields = ReportListSerializer.Meta.fields + [
            'rescue_updates',
            'animal',
        ]

    def get_animal(self, obj):
        try:
            animal = obj.animal
        except Animal.DoesNotExist:
            return None

        return AnimalSummarySerializer(animal, context=self.context).data


class AnimalSerializer(serializers.ModelSerializer):
    report_id = serializers.IntegerField(source='report.id', read_only=True)
    report_animal_type = serializers.SerializerMethodField()
    shelter_name = serializers.SerializerMethodField()
    assigned_rescuer_name = serializers.SerializerMethodField()
    gender_display = serializers.SerializerMethodField()
    treatment_status_display = serializers.SerializerMethodField()
    animal_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = [
            'id',
            'report_id',
            'report_animal_type',
            'shelter_name',
            'assigned_rescuer_name',
            'name',
            'age',
            'gender',
            'gender_display',
            'animal_image_url',
            'health_status',
            'treatment_status',
            'treatment_status_display',
            'treatment_notes',
            'vet_info',
            'arrival_date',
            'adoption_ready_date',
            'outcome_date',
            'outcome_notes',
            'created_at',
            'updated_at',
        ]

    def get_report_animal_type(self, obj):
        return obj.report.get_animal_type_display()

    def get_shelter_name(self, obj):
        return get_user_display_name(obj.shelter)

    def get_assigned_rescuer_name(self, obj):
        return get_user_display_name(obj.assigned_rescuer)

    def get_gender_display(self, obj):
        return obj.get_gender_display()

    def get_treatment_status_display(self, obj):
        return obj.get_treatment_status_display()

    def get_animal_image_url(self, obj):
        request = self.context.get('request')
        return build_file_url(request, obj.animal_image)


class AdoptionRequestSerializer(serializers.ModelSerializer):
    adoption_request_id = serializers.IntegerField(source='id', read_only=True)
    animal_id = serializers.IntegerField(source='animal.id', read_only=True)
    report_id = serializers.IntegerField(source='animal.report.id', read_only=True)
    animal_name = serializers.SerializerMethodField()
    requester_name = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()
    processed_by_name = serializers.SerializerMethodField()

    class Meta:
        model = AdoptionRequest
        fields = [
            'id',
            'adoption_request_id',
            'animal_id',
            'report_id',
            'animal_name',
            'requester_name',
            'message',
            'status',
            'status_display',
            'processed_by_name',
            'decision_notes',
            'created_at',
            'processed_at',
            'updated_at',
        ]

    def get_animal_name(self, obj):
        return obj.animal.name or obj.animal.report.get_animal_type_display()

    def get_requester_name(self, obj):
        return get_user_display_name(obj.requester)

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_processed_by_name(self, obj):
        return get_user_display_name(obj.processed_by)