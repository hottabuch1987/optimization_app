# from django.http import JsonResponse
# from django.shortcuts import render
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.views import APIView
#
# from .models import User
# from .serializers import UserSerializer
# from rest_framework.response import Response
# from . forms import SignupForm
#
#
# # мой аккаунт
# @api_view(['GET'])
# def me(request):
#     return JsonResponse({
#         'id': request.user.id,
#         'name': request.user.name,
#         'email': request.user.email,
#
#     })
#
#
# # регистрация
# @api_view(['POST'])
# @authentication_classes([])
# @permission_classes([])
# def signup(request):
#     data = request.data
#     message = 'success'
#
#     form = SignupForm({
#         'email': data.get('email'),
#         'password1': data.get('password1'),
#         'password2': data.get('password2'),
#     })
#
#     if form.is_valid():
#         form.save()
#
#     else:
#
#         message = form.errors.as_json()
#     print(message)
#
#     return JsonResponse({'message': message}, safe=False)

#
# class SignInUser(APIView):
#     def post(self, request):
#         forms = SignupForm()
#         if request.forms.is_valid():
#             forms.save()
#             return Response(forms.data)
#
# class UserView(APIView):
#     def get(self, request, format=None):
#
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#

