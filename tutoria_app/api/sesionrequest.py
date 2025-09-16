from rest_framework import serializers


class SesionRequestSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=True)
    size = serializers.IntegerField(required=True)
    order = serializers.CharField(required=False, allow_blank=True)
    startDate = serializers.DateTimeField(required=False, allow_null=True)
    endDate = serializers.DateTimeField(required=False, allow_null=True)
    estado = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        start_date = data.get("startDate")
        end_date = data.get("endDate")

        if (start_date and not end_date) or (end_date and not start_date):
            raise serializers.ValidationError(
                "Debes proporcionar tanto startDate como endDate para filtrar por rango de fechas."
            )

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError(
                "El campo startDate no puede ser mayor que endDate."
            )

        return data