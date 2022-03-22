from django.contrib import admin
from .models import Items, Laptop, Shoes, Book, MobilePhone, Clothes, Electronics
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'desc', 'price', 'amount',
                    'author', 'publishingCompany')  # thêm tên cho cột
    # thêm ô tìm kiếm (đặt trong dấu ngoặc vuông)
    search_fields = ['name']
    list_filter = ('name', 'author')        # thêm filter


admin.site.register(Book, BookAdmin)


class ShoesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'desc', 'price',
                    'amount', 'size', 'manufacturer')
    search_fields = ['name']
    list_filter = ('name', 'manufacturer')


admin.site.register(Shoes, ShoesAdmin)


class MobilePhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'desc', 'price',
                    'amount', 'insurance', 'manufacturer')
    search_fields = ['name']
    list_filter = ('name', 'manufacturer')


admin.site.register(MobilePhone, MobilePhoneAdmin)


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'desc', 'price',
                    'amount', 'size', 'material', 'manufacturer')
    search_fields = ['name']
    list_filter = ('name', 'manufacturer')


admin.site.register(Clothes, ClothesAdmin)


class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'desc', 'price',
                    'amount', 'insurance', 'manufacturer')
    search_fields = ['name']
    list_filter = ('name', 'manufacturer')


admin.site.register(Electronics, ElectronicsAdmin)


class LaptopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'desc', 'price',
                    'amount', 'insurance', 'manufacturer')
    search_fields = ['name']
    list_filter = ('name', 'manufacturer')


admin.site.register(Laptop, LaptopAdmin)
