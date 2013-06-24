from django.contrib import admin
from models import PageModel, Categories, PageViewCount, HomePageModels

admin.site.register(PageModel)
admin.site.register(Categories)
admin.site.register(PageViewCount)
admin.site.register(HomePageModels)