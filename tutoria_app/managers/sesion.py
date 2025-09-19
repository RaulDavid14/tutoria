from django.db.models import Manager
from django.db.models import Q

class SesionManager(Manager):
    def sesionesFind(self, filter, usuario):
        queryset = self.get_queryset()

        if usuario.rol == 'estudiante':
            queryset = queryset.filter(alumno=usuario.alumno.id)
        elif usuario.rol == 'tutor' :
            queryset = queryset.filter(docente=usuario.docente.id)
      
        if filter.get('startDate') is not None and filter.get('endDate') is not None:
            queryset = queryset.filter(
                fecha_registro__range=[filter['startDate'], filter['endDate']]
            )
        if filter.get('estado') is not None:
            queryset = queryset.filter(estado = filter.get('estado'))
        
        if filter.get('buscar') is not None and usuario.rol == 'tutor':
            pass
        
        queryset = queryset.order_by(filter['order'])
        return queryset
    