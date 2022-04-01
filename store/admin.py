from django.contrib import admin
from store.models import Category, Product, Book,Clother,Mobile,Desktop,Shose

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 24


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'availibility', 'updated', 'created')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)
    list_editable = ('price', 'availibility')
    list_per_page = 24


"""class ItemAdmin(admin.ModelAdmin):
    site_header = 'Quản lí mặt hàng'

item_admin = ItemAdmin(name = 'itemadmin')

"""

class itemAdmiSite(admin.AdminSite):
    site_header = 'Quản lý Item'

item_site = itemAdmiSite(name='ItemAdmin')

item_site.register(Book)
item_site.register(Clother)
item_site.register(Mobile)
item_site.register(Desktop)
item_site.register(Shose)