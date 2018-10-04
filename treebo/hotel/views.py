from django.shortcuts import render
from django.db.models import Avg
from django.db.models import Max
from django.db.models import Min
from django.http import JsonResponse

from hotel.models import deals, stats
from hotel.serializers import DealsSerializer, StatsSerializer
from rest_framework import viewsets
from django.db.models import F
from django.db.models import Count

from rest_framework.views import APIView

# Create your views here.

class DealsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = deals.objects.all().order_by('id')
    serializer_class = DealsSerializer
    count=stats.objects.get(id = 1)
    count.api_hits=F('api_hits')+1
    count.save()


class StatsViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request):
        count=stats.objects.get(id = 1)
        count.api_hits=F('api_hits')+1
        count.save()
        
        average_rating=deals.objects.all().aggregate(Avg('rating'))['rating__avg']
        price={}
        price['Minimum']=deals.objects.all().aggregate(Min('actual_price'))['actual_price__min']
        price['Maximum']=deals.objects.all().aggregate(Max('actual_price'))['actual_price__max']
        
        hotel_distribution={}
        hotel_distribution['BLR']=deals.objects.all().filter(location__contains="Chennai").values('location').annotate(total=Count('location')).count()
        hotel_distribution['CHE']=deals.objects.all().filter(location__contains="Bengaluru").values('location').annotate(total=Count('location')).count()
        hotel_distribution['MUM']=deals.objects.all().filter(location__contains="Mumbai").values('location').annotate(total=Count('location')).count()
        hotel_distribution['HYD']=deals.objects.all().filter(location__contains="Hyderabad").values('location').annotate(total=Count('location')).count()
        hotel_distribution['DEL']=deals.objects.all().filter(location__contains="Delhi").values('location').annotate(total=Count('location')).count()
        
        result={}
        result['average-rating']=average_rating
        result['api-hits']=str(stats.objects.get(id = 1))
        result['price']=price
        result['area-wise-hotel-distribution']=hotel_distribution
        
        return JsonResponse(result)