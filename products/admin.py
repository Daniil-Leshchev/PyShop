from django.contrib import admin
from .models import Product, Offer

#кастомизируем отображение объекта в админке джанго. Чтобы не было так: ProductObject(1...)
#list_display - какие колонки будут отображаться
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Product, ProductAdmin)#при кастомном отображении необходимо при регистрации модели указать и кастомный класс
admin.site.register(Offer, OfferAdmin)