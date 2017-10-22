from rest_framework.response import Response
from rest_framework.views import APIView

from .models import employee
from .serializers import employeeSerializer


class employeeList(APIView):
    def get(self, request):
        emp = employee.objects.all()
        serial = employeeSerializer(emp, many=True)
        return Response(serial.data)

    def post(self, request):
        pass
