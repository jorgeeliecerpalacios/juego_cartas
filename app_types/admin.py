from django.contrib import admin

# Register your models here.

from app_types.models import Type, Challange


@admin.register(Challange)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'dificult', 'types')
    list_display_links = ('pk', 'name',)
    list_editable = ('description', 'dificult')

    search_fields = (
        'name',
        'pk',
        'dificult',
        'description',
        'types__name',
    )

    list_filter = (
        'created',
        'modified',
        'types'
    )
    fieldsets = (
        ('Challenge', {
            'fields': [
                ('name'),
                ('description'),
                ('types')
            ]
            }),
        ('Extra info', {
            'fields': [
                ('dificult')
                ]
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)
    save_on_top = True


class ChallengeInline(admin.TabularInline):
    model = Challange
    extra = 1
    can_delete = False
    verbose_name_plural = 'challanges'
    save_on_top = True


@admin.register(Type)
class TypesAdmin(admin.ModelAdmin):
    # Type admin.

    inlines = [ChallengeInline]

    list_display = ('pk', 'name', 'quantity', 'photo')
    list_display_links = ('pk', 'name',)
    list_editable = [('quantity')]

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
            'fields': [
                ('name'), ('photo')
                ]
        }),
        ('Extra info', {
            'fields': [('quantity')]
                
        }),
        ('Metadata', {
            'fields': (('created', 'modified')),
        })
    )

    readonly_fields = ('created', 'modified',)
    save_on_top = True


# admin.site.register(Challange)

# admin.site.register(Type)
