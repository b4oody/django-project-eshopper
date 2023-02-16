import mptt
from django.db import models

from django.urls import reverse

# CATEGORY_CHOICES = (
#     ('S', 'Shirt'),
#     ('J', 'Jeans'),
#     ('JA', 'Jackets'),
#     ('SH', 'Shoes'),
# )
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='children', db_index=True)
  slug = models.SlugField(null=False, unique=True)

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'categories'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse('categ', args=[self.slug])





class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я Продукта")
    code = models.CharField(max_length=255, verbose_name='Код Продукта')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    discount_price = models.FloatField(blank=True, null=True)

    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True,blank=True)
    amount = models.DecimalField(max_digits=50, decimal_places=0, verbose_name='Кількість Продуктів')
    is_published = models.BooleanField(default=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('categ', kwargs={'slug': self.slug})

    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.name






