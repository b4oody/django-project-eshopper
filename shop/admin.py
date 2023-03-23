from django.contrib import admin

from mptt.admin import  DraggableMPTTAdmin
from shop.models import Product, Category, Size, Color, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'amount', 'img_preview')
    list_display_links = ('id', 'name')
    list_filter = ('price',)
    ordering = ('price',)





class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Кількість товарів в підкатегорії'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Кількість підкатегорій в категорії'




class ColorAdmin(admin.ModelAdmin):
    list_display=('name', 'color_bg')
admin.site.register(Color, ColorAdmin)




admin.site.register(Product,ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)


class OrderAdmin(admin.ModelAdmin):
    list_display=('customer','complete')
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display=('product', 'order', 'quantity')
admin.site.register(OrderItem, OrderItemAdmin)

