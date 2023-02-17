import datetime

from rest_framework import authentication, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from infringement.models import Infringement
from officer.models import Officer
from vehicle.models import Vehicle


class TokenAuthentication(authentication.TokenAuthentication):
    authentication.TokenAuthentication.keyword = 'Bearer'
        

class InfringementCreate(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            officer = Officer.objects.get(user=request.user)
            vehicle = request.data.get('placa_patente')
            comment_infringement = request.data.get('comentarios')
            timestamps = datetime.datetime.strptime(request.data.get('timestamp'),'%Y-%m-%d %H:%M:%S')
            
            vehicle_filtered = Vehicle.objects.filter(plate=vehicle.upper())
            
            if not vehicle_filtered:
                return Response(
                    {
                        "data":{
                            "status": status.HTTP_404_NOT_FOUND,
                            "respuesta" : f'la placa suministrada no se encuetra registrada dentro de la plataforma',
                        }
                    },
                )
            else:
                get_vehicle = Vehicle.objects.get(plate=vehicle.upper())
                infringement = Infringement(
                    vehicle = get_vehicle,
                    assigned_officer = officer,
                    created_at = timestamps,
                    comment = comment_infringement
                )
                infringement.save()
            
            
            return Response(
                {
                    "data":{
                        "status": status.HTTP_201_CREATED,
                        "numero_infraccion" : f'{infringement.infringement_id}',
                        "oficial_asignado": f'{infringement.assigned_officer}'
                    }
                },
            )
        except ValueError:
            return Response(
                {
                    "data":{
                        "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                        "respuesta" : "Ha ocurrido un error inesperado",
                    }
                },
            )
        

class InfringementSearch(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        try:
            
            queryset = Infringement.objects.filter(vehicle__person__email=request.data.get('email'))
            
            if not queryset:
                return Response(
                    {
                        "data":{
                            "status": status.HTTP_404_NOT_FOUND,
                            "respuesta" : f'el email suministrado no se encuetra registrado dentro de la plataforma',
                        }
                    },
                )
            else:
                infringements = []
                for infringement in queryset:
                    infringements.append(
                        {
                            'fecha_multa': infringement.created_at,
                            'numero_multa': infringement.infringement_id,
                            'oficial_asignado': infringement.assigned_officer.officer_name
                        }
                    )
                
                return Response(
                    {
                        "status" : status.HTTP_200_OK,
                        "data" : {
                            "multas" : infringements,
                        }
                    },
                )
        
        except ValueError:
            return Response(
                {
                    "data":{
                        "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                        "respuesta" : "Ha ocurrido un error inesperado",
                    }
                },
            )