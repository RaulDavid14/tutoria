from rest_framework import serializers
from tutoria_app.models.sesion import SesionModel

class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionModel
        exclude = [
            'fecha_respuesta',
            'alumno',
            'docente',
            'comentario'
        ]