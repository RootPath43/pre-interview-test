
from django.urls import path, include
from .views import (
    CategoryTypePerformanceView,
    StatusBasedView,
    FilterAndAggregateView,
    ConversionRateView
    )


app_name = 'endpoint'

urlpatterns = [
 
    path('conversion-rate/', ConversionRateView.as_view(), name='conversion-rate/'),

    path('status-distribution/', StatusBasedView.as_view(), name='status-distribution'),

    path('category-type-performance/', CategoryTypePerformanceView.as_view(), name='category-type-performance'),

    path('filtered-aggregation/', FilterAndAggregateView.as_view(), name='filtered-aggregation'),

]
