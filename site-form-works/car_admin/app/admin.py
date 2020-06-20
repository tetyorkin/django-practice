from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'review_count']
    search_fields = ['brand', 'model']
    list_filter = ['brand', 'model']
    ordering = ['-id']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['car', 'title']
    search_fields = ['car__brand', 'title']
    list_filter = ['car__brand']
    ordering = ['-id']
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
