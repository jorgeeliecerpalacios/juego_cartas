from django.contrib import admin

# Register your models here.

from app_types.models import Types


class TypesAdmin(admin.ModelAdmin):
    # Profile admin.

    list_display = ('pk', 'name', 'description', 'quantity', 'photo')
    list_display_links = ('pk', 'name',)
    list_editable = ('description', 'quantity', 'photo')

    search_fields = (
        'name',
        'pk',
        'quantity'
    )

    list_filter = (
        'created',
        'modified'
    )
    fieldsets = (
        ('Type', {
            'fields': (('name', 'photo'),),
        }),
        ('Extra info', {
            'fields': (
                ('name', 'description')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)


admin.site.register(Types)
