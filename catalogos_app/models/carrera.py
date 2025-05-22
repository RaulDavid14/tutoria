from catalogos_app.models.catalogo import CatalogoModel

class CatCarreraModel(CatalogoModel):
    class Meta:
        db_table = 'carreras'
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'