from django.http import JsonResponse
from rest_framework_simplejwt import exceptions
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomLoginSerializer, LogoutSerializer, RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = []

    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(
                request,
                "signup_success.html",
                {"email": serializer.validated_data["email"]},
            )
        else:
            return render(request, "signup.html", {"errors": serializer.errors})


class LoginView(TokenObtainPairView):
    serializer_class = CustomLoginSerializer
    template_name = "login.html"
    login_success_template = "login_success.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print("Exception caught:", e)
            # return render(request, "login.html", {"errors": str(e)})
            return JsonResponse({"error": "Invalid credentials"}, status=400)

        user = serializer.user
        refresh, access = self.get_tokens_for_user(user)

        return render(
            request,
            self.login_success_template,
            {
                "refresh_token_from_django_view": str(refresh),
                "access_token_from_django_view": str(access),
            },
        )

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        return refresh, access


class LoginRefreshView(TokenRefreshView):
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "You have logged out successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
