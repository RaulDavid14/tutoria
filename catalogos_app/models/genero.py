from catalogos_app.models.catalogo import CatalogoModel


class CatGeneroModel(CatalogoModel):
    class Meta:
        db_table = 'catalogo_generos'
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
