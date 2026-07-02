from django.urls import path
from . import views


urlpatterns = [
    path('report/', views.report_animal_view, name='report_animal'),
    path('my-reports/', views.my_reports_view, name='my_reports'),
    path('my-reports/<int:report_id>/', views.my_report_detail_view, name='my_report_detail'),
    path('my-adoption-requests/', views.my_adoption_requests_view, name='my_adoption_requests'),
    path('my-adoption-requests/<int:request_id>/', views.my_adoption_request_detail_view, name='my_adoption_request_detail'),

    path('rescuer/cases/', views.rescuer_assigned_cases_view, name='rescuer_assigned_cases'),
    path('rescuer/completed-cases/', views.rescuer_completed_cases_view, name='rescuer_completed_cases'),
    path('rescuer/cases/<int:report_id>/', views.rescuer_case_detail_view, name='rescuer_case_detail'),

    path('adoption/', views.adoption_home_view, name='adoption_home'),
    path('adoption/available/', views.available_animals_view, name='available_animals'),
    path('adoption/<int:animal_id>/', views.animal_adoption_detail_view, name='animal_adoption_detail'),

    path('shelter/reports/', views.shelter_report_list_view, name='shelter_report_list'),
    path('shelter/reports/<int:report_id>/', views.shelter_report_detail_view, name='shelter_report_detail'),
    path('shelter/reports/<int:report_id>/assign/', views.assign_rescuer_view, name='assign_rescuer'),
    path('shelter/treatment/', views.shelter_treatment_list_view, name='shelter_treatment_list'),
    path('shelter/treatment/<int:report_id>/', views.animal_treatment_detail_view, name='animal_treatment_detail'),
    path('shelter/adoption-requests/', views.shelter_adoption_requests_view, name='shelter_adoption_requests'),
    path('shelter/adoption-requests/<int:request_id>/', views.shelter_adoption_request_detail_view, name='shelter_adoption_request_detail'),
    path('shelter/reports/reviewed/', views.shelter_reviewed_reports_view, name='shelter_reviewed_reports'),
    path('shelter/reports/assigned/', views.shelter_assigned_reports_view, name='shelter_assigned_reports'),
    path('shelter/reports/handover/', views.shelter_handover_reports_view, name='shelter_handover_reports'),
    path('shelter/completed-cases/', views.shelter_completed_cases_view, name='shelter_completed_cases'),
]