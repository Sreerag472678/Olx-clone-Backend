from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from .models import Login,Product_view
from .serializers import ProductSerializer,UserRegister,ProductViewSerializer,ProfileSerializer
from rest_framework.views  import APIView
from rest_framework.authtoken.models import Token 
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.decorators import api_view, permission_classes
import logging
import json

logger = logging.getLogger(__name__)
@api_view(['GET'])
@permission_classes([AllowAny])
def product_list(request):
    logger.debug('Product list view accessed')
    if request.method == 'GET':
        products = Product_view.objects.all()
        serializer = ProductSerializer(products, many=True)
        response = Response(serializer.data)    
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate' 
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
        
class ProductViewListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    # def get(self, request, *args, **kwargs):
    #     queryset = Product_view.objects.all()
    #     serializer = ProductViewSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # instance=form.save(commit=False)  
            # instance.Product_view =request.Addtitle
            # instance.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure only authenticated users can upload
def upload_product(request):
    if request.method == 'POST':
        image_file = request.FILES.get('Image')
        product = Product(
            Brand=request.POST.get('Brand'),
            Description=request.POST.get('Description'),
            Addtitle=request.POST.get('Addtitle'),
            Year=request.POST.get('Year'),
            Price=request.POST.get('Price'),
            Phone=request.POST.get('Phone'),
            Location=request.POST.get('Location'),
            State=request.POST.get('State'),
            District=request.POST.get('District'),
            Image=image_file
        )
        product.save()
        return Response({'message': 'Product added successfully'})
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    data = {
        'username': user.username,
        'email': user.email,
       
    }
    return Response(data)


def search_products(request):
    query = request.GET.get('q', '')  
    if query:       
        products = Product_view.objects.filter(Addtitle__icontains=query).values()  
        products_list = list(products)  
        return JsonResponse(products_list, safe=False)  
    else:
        return JsonResponse({'error': 'No search query provided'}, status=400)  

class Register(APIView):
    permission_classes = [AllowAny] 

    def post(self, request, format=None):
        serializer = UserRegister(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                'response': 'User registered successfully',
                'username': user.username,
                'email': user.email
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegister
    permission_classes = (AllowAny,)
    

@api_view(['POST'])
def Logout_user(request):
    """Handle user logout by blacklisting the refresh token."""
    try:
        
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'detail': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_205_RESET_CONTENT)

    except TokenError as e:
        return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserRegister(user)
        return Response(serializer.data)
        

