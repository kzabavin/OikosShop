from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Наименование'))
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_list_by_category',
                        args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, verbose_name=_('Категория'))
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Наименование'))
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name=_('Изображение'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Цена'))
    stock = models.PositiveIntegerField(verbose_name=_('Остаток'))
    available = models.BooleanField(default=True, verbose_name=_('Доступность'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Создан'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Изменен'))
    usedin = models.ManyToManyField("shop.Product", verbose_name=_("Используется в"))
    
    class Meta:
        ordering = ('name',)
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail',
                        args=[self.id, self.slug])