from django.contrib.admin import widgets, ModelAdmin, TabularInline
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext, gettext_lazy as _

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from nested_admin.nested import NestedTabularInline

from farmster_server.admin.user_admin_model import UserAdmin
from farmster_server.models.deal import Deal
from farmster_server.models.deal_part import DealPart

user_model = get_user_model()


class BaseModelAdmin(TranslationAdmin):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        vertical = False  # change to True if you prefer boxes to be stacked vertically
        kwargs['widget'] = widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            vertical,
        )
        return super(BaseModelAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


class BaseTabularInline(TranslationTabularInline):
    extra = 0
    readonly_fields = ('admin_link',)
    sortable_field_name = 'order'

    def admin_link(self, instance):
        url = reverse('admin:%s_%s_change' % (instance._meta.app_label,
                                              instance._meta.model_name),
                      args=(instance.id,))
        return format_html(u'<a href="{}" target="_blank">Go To Edit Page</a>', url)


class UserCropInline(TabularInline):
    model = user_model.crops.through


class UserPlacesInline(TabularInline):
    model = user_model.places.through


class UserFarmersInline(TabularInline):
    model = user_model.farmers.through


class UserCropListingsInline(TabularInline):
    model = user_model.favorite_crop_listings.through


class DealPartsInline(NestedTabularInline):
    model = DealPart


class DealsInline(NestedTabularInline):
    model = Deal
    inlines = [DealPartsInline]


class FarmsterUserAdmin(UserAdmin):
    list_display = ('id', 'phone_number', 'first_name', 'last_name', 'is_admin')
    list_editable = ('first_name', 'last_name', 'is_admin')
    ordering = ('phone_number',)
    search_fields = ('id', 'phone_number', 'first_name', 'last_name', 'email')
    inlines = [
        UserCropInline,
        UserPlacesInline,
        UserFarmersInline,
        UserCropListingsInline,
        DealsInline
    ]
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )


class CropAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'type', 'image_url')
    list_editable = ('name', 'type', 'image_url')
    inlines = [
        UserCropInline
    ]


class PlaceAdmin(ModelAdmin):
    list_display = ('id', 'name', 'district', 'type', 'country')
    list_editable = ('name', 'district', 'type', 'country')
    inlines = [
        UserPlacesInline
    ]


class AgentAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number')
    list_editable = ('first_name', 'last_name', 'phone_number')


class FarmerAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number')
    list_editable = ('first_name', 'last_name', 'phone_number')
    inlines = [
        UserFarmersInline
    ]


class CropListingAdmin(ModelAdmin):
    list_display = ('id', 'crop', 'harvest_date', 'amount', 'amount_unit', 'status')
    list_editable = ('harvest_date', 'amount', 'amount_unit', 'status')
    inlines = [
        UserCropListingsInline
    ]


class DealAdmin(ModelAdmin):
    list_display = ('id', 'farmer')
    list_editable = ('farmer',)
    inlines = [
        DealPartsInline
    ]


class ContactAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'location')
    list_editable = ('first_name', 'last_name', 'phone_number', 'location')


class DealPartsAdmin(ModelAdmin):
    list_display = ['id', 'date', 'currency', 'price', 'amount', 'crop_size', 'crop']
    list_editable = ['date', 'currency', 'price', 'amount', 'crop_size', 'crop']
