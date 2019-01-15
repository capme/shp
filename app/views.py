from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.response import Response
from .services import TaxProductClass


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def calculate(request):
    svc = TaxProductClass()
    ret = svc.calculate(payload=request.data)
    return Response(
        ret, 200
    )
