from .catalogo import CatalogoModel

class CatMotivoSesionModel(CatalogoModel):
    class Meta:
        db_table = 'cat_motivos_sesiones'
        verbose_name = 'Motivo Sesión'
        verbose_name_plural = 'Motivos Sesiones'
    
    def __str__(self):
        return f'{self.abreviacion} {self.nombre}'