from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
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
    verbose_name_plural = '1.Categories'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse('categ', args=[self.slug])





class Color(models.Model):
    name=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Colors'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.name

# Size
class Size(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Sizes'

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я Продукта")
    code = models.CharField(max_length=255, verbose_name='Код Продукта')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    discount_price = models.FloatField(blank=True, null=True)
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True,blank=True)
    amount = models.DecimalField(max_digits=50, decimal_places=0, verbose_name='Кількість Продуктів')
    is_published = models.BooleanField(default=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural='2.Product'

    def get_absolute_url(self):
        return reverse('categ', kwargs={'slug': self.slug})

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "75"/>')

    def __str__(self):
        return self.name







class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)


    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum([product.get_total for product in orderitem])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



