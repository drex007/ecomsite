from django.contrib import admin

# Register your models here.
from .models import Product,Cart,Order


admin.site.site_header = "My Ecommerce Store"
admin.site.site_title = "Ecom store "
admin.site.index_title = "Ecomsite"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request, queryset):
        queryset.update(category ="default")

    list_display = ('title','price','discount_price', 'category','image')
    search_fields = ('title',)
    actions = ('change_category_to_default',)
    list_editable = ('price', 'category',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','email','total_price', 'date_of_order','city','state')


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Order,OrderAdmin)
