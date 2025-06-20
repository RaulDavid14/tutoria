from catalogos_app.models.catalogo import CatalogoModel

class CatProgramaEducativoModel(CatalogoModel):
    class Meta:
        db_table = 'programa_educativo'
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'