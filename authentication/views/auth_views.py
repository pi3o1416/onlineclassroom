

from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ..serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer


def _set_cookie(response, cookie_name:str, cookie_value:str, max_age=3600*24*15):
    """
    Set httponly cookie in response.
    Get response, cookie_name, cookie value as parameter
    retrun response.
    """
    response.set_cookie(cookie_name, cookie_value, max_age,
                        httponly=True, samesite=None, secure=True)
    return response


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Obtain token using username & password.
    Refresh Token will be set on cookie with httponly flag.
    ClientSide will be responsible to store and maintain Access Token.
    """
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            refresh_token = response.data.get('refresh')
            response = _set_cookie(
                response=response,
                cookie_name='refresh_token',
                cookie_value=refresh_token
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    """
    Refresh access and refresh token.
    This view will search refresh token in cookie.
    If found return new access and refresh token.
    """
    serializer_class = CustomTokenRefreshSerializer
    permission_classes = [AllowAny]

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            refresh_token = response.data.get('refresh')
            response = _set_cookie(
                response=response,
                cookie_name='refresh_token',
                cookie_value=refresh_token
            )
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)


