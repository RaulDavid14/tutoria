from catalogos_app.models.catalogo import CatalogoModel

class CatEstadoCivilModel(CatalogoModel):
    class Meta:
        db_table = 'estado_civil'
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civiles'
        