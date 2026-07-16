from django.db import models



class Brand(models.Model):
    name = models.CharField(max_lengh=100,verbose_name='Nome')
    id_active = models.BooleanField(default=True,verbose_name='Ativo')
    description = models.TextField(null=True,verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='criado em')
    update_at = models.DateTimeField(auto_now_add=True,verbose_name='atualizado em')