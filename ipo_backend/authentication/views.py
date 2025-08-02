from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError
import logging

logger = logging.getLogger('authentication')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        logger.info(f"Login attempt with username: {attrs.get('username')}")
        
        # Ensure username and password are strings
        username = attrs.get('username')
        password = attrs.get('password')
        
        if not username or not isinstance(username, str):
            logger.warning("Invalid username provided")
            raise serializers.ValidationError({'username': ['Username must be a valid string']})
        
        if not password or not isinstance(password, str):
            logger.warning("Invalid password provided")
            raise serializers.ValidationError({'password': ['Password must be a valid string']})
        
        try:
            data = super().validate(attrs)
            
            # Add user information to the response
            user = self.user
            data.update({
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'is_staff': user.is_staff,
                    'is_superuser': user.is_superuser,
                    'date_joined': user.date_joined
                }
            })
            
            logger.info(f"User {username} logged in successfully")
            return data
        except Exception as e:
            logger.warning(f"Login failed for {username}: {str(e)}")
            raise

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        logger.info(f"Registration attempt with data: {request.data}")
        
        # Get data from request
        username = request.data.get('username')
        email = request.data.get('email', '')
        password = request.data.get('password')
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        
        # Validation
        errors = {}
        
        if not username:
            errors['username'] = ['Username is required']
        elif not isinstance(username, str):
            errors['username'] = ['Username must be a string']
        elif len(username.strip()) == 0:
            errors['username'] = ['Username cannot be empty']
        elif User.objects.filter(username=username).exists():
            errors['username'] = ['Username already exists']
            
        if not password:
            errors['password'] = ['Password is required']
        elif not isinstance(password, str):
            errors['password'] = ['Password must be a string']
        else:
            try:
                validate_password(password)
            except ValidationError as e:
                errors['password'] = list(e.messages)
                
        if email and User.objects.filter(email=email).exists():
            errors['email'] = ['Email already exists']
        
        if errors:
            logger.warning(f"Registration validation failed: {errors}")
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Create user
        logger.info(f"Creating user: {username}")
        user = User.objects.create_user(
            username=username.strip(),
            email=email.strip() if email else '',
            password=password,
            first_name=first_name.strip() if first_name else '',
            last_name=last_name.strip() if last_name else ''
        )
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        
        logger.info(f"User {username} created successfully")
        return Response({
            'message': 'User created successfully',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        }, status=status.HTTP_201_CREATED)
        
    except IntegrityError as e:
        logger.error(f"Database integrity error during registration: {str(e)}")
        return Response({
            'error': 'User with this information already exists'
        }, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        logger.error(f"Unexpected error during registration: {str(e)}", exc_info=True)
        return Response({
            'error': 'An unexpected error occurred during registration'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    try:
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined,
            'is_staff': user.is_staff
        })
    except Exception as e:
        logger.error(f"Error fetching user profile: {str(e)}")
        return Response({
            'error': 'Unable to fetch user profile'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)