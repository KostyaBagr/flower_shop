from django.contrib import admin
from .models import *
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# Register your models here.
from django.utils.safestring import mark_safe
import admin_thumbnails
# admin.site.register(Plant)

# admin.site.register(PlantPhotos)


#plant model
@admin_thumbnails.thumbnail('images')
class PlantsPhotosInline(admin.TabularInline):
    model = PlantPhotos
    extra = 1
    readonly_fields = ('id',)

class PlantAdmin(admin.ModelAdmin):
    list_display = ['id', 'plant_name', 'old_price', 'price', 'category', 'preview']
    list_filter = ['plant_name', 'price', 'old_price', 'category']
    list_display_links = ['id', 'plant_name']
    list_editable = ['price', 'old_price']
    inlines = [PlantsPhotosInline]

    def preview(self, obj):
        return mark_safe(f"<img src='{obj.main_img.url}'style='max-height: 80px; max-width:50px;'>")
#----------------------------------------------------


#order model
class OrderForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone_number': PhoneNumberPrefixWidget(attrs={'class': 'phone-number'}),
        }

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('id',)



class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_display = ['id', 'first_name', 'last_name', 'email', 'city','telegram_name', 'created']
    date_hierarchy = 'created'
    list_editable = ['telegram_name']
    inlines = [OrderItemInline]
    list_filter = ['id', 'first_name', 'last_name', 'city']


#orderitem model
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'plant', 'price', 'quantity', 'time_created']
    date_hierarchy = 'time_created'
    list_editable = ['price', 'quantity']
    list_filter = ['price', 'quantity', 'order']
#-----------------------------------


admin.site.register(Plant, PlantAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
admin.site.register(OrderItem, OrderItemAdmin)