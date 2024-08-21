from rest_framework.decorators import api_view
from rest_framework.response import Response
from. serializer import *

@api_view(['GET'])
def get_banner(request):
    balance = Banner.objects.last()
    serialized_data = BannerSerializer(balance).data
    return Response(serialized_data)

