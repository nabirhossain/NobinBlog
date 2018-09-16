from django.contrib import admin
from .models import author, category, post
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["auth_name"]

    class Meta:
        Model = author
admin.site.register(author, AuthorAdmin)

@admin.register(category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    pass


@admin.register(post)
class PostAdmin(ImportExportModelAdmin):
    list_display = ["__str__",'post_category','posted_on']
    list_filter = ['posted_on','post_author']
    search_fields = ["__str__"]
    list_per_page = 10
    pass
