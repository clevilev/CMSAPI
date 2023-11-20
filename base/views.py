from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from .models import *


@api_view(['POST'])
def create_camp(request):
    try:
        tenant = Camp(schema_name=request.data['camp_domain'], name=request.data['camp_name'])
        tenant.save()
        domain = request.data['camp_domain'] + '.localhost'
        domain = Domain(domain=domain, tenant=tenant, is_primary=True)
        domain.save()
        User.objects.create(first_name='Camp',
                            last_name='Admin',
                            username=request.data['camp_domain'],
                            email=request.data['camp_admin_email'],
                            password=make_password(request.data['password']),
                            is_superuser=False,
                            is_staff=True,
                            is_active=True
                            )
        connection.set_schema(request.data['camp_domain'], True)
        User.objects.create(first_name='Camp',
                            last_name='Admin',
                            username=request.data['camp_domain'],
                            email=request.data['camp_admin_email'],
                            password=make_password(request.data['password']),
                            is_superuser=True,
                            is_active=True
                            )
        connection.set_schema_to_public()
        return Response({'status': 'Camp Created'})
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return HttpResponse("<h1>Public Index</h1>")
