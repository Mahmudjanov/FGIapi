from rest_framework.decorators import api_view
from rest_framework.response import Response
from. serializer import *


@api_view(['GET'])
def get_banner(request):
    banner = Banner.objects.last()
    serialized_data = BannerSerializer(banner).data
    return Response(serialized_data)



@api_view(['GET'])
def get_service(request):
    service = Service.objects.last()
    serialized_data = ServiceSerializer(service).data
    return Response(serialized_data)




@api_view(['GET'])
def get_product(request):
    product = Product.objects.last()
    serialized_data = ProductSerializer(product).data
    return Response(serialized_data)



@api_view(['POST'])
def create_form(request):
    form = Form.objects.create(
        ism = request.POST.get("ism"),
        familiya = request.POST.get("familiya"),
        email = request.POST.get("email"),
        text = request.POST.get("text")
    )
    serialized_data = FormSerializer(form).data
    return Response(serialized_data)



@api_view(['GET'])
def contact(request):
    contact = Contact.objects.last()
    serialized_data = ContactSerializer(contact).data
    return Response(serialized_data)