from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializers import *
from myappunv.calc_location import calculate_location 


@api_view(['GET'])
def get_fingerprint(request):
    fingerprint=WiFiFingerprint.objects.all()
    serializer=WiFiFingerprintSerializer(fingerprint,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_fingerprint(request):
    received_data=request.data
        
    fingerprints=WiFiFingerprint.objects.all()
    fingerprints_list=[{
        'ssid':fp.ssid,
        'bssid':fp.bssid,
        'rssi_min':fp.rssi_min,
        'rssi_max':fp.rssi_max,
        'location_name':fp.location_name
    }for fp in fingerprints]
    
    location_scores=calculate_location(received_data,fingerprints_list)
    
    if not location_scores:
        return Response({"message": "لم يتم تحديد الموقع بدقة"},status=400)
    
    estimated_location =max(location_scores,key=location_scores.get)
    
    return Response({"estimated_location":estimated_location})        
    


# class get_fingerprint(APIView):
#     def get(self,request):
#         fingerprint=WiFiFingerprint.objects.all()
#         serializer=WiFiFingerprintSerializer(fingerprint,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         received_data=request.data
        
#         fingerprints=WiFiFingerprint.objects.all()
#         fingerprints_list=[{
#             'ssid':fp.ssid,
#             'bssid':fp.bssid,
#             'rssi_min':fp.rssi_min,
#             'rssi_max':fp.rssi_max,
#             'location_name':fp.location_name
#         }for fp in fingerprints]
        
#         location_scores=calculate_location(received_data,fingerprints_list)
        
#         if not location_scores:
#             return Response({"message": "لم يتم تحديد الموقع بدقة"},status=400)
        
#         estimated_location =max(location_scores,key=location_scores.get)
        
#         return Response({"estimated_location":estimated_location})        
        