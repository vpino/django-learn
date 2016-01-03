from django.contrib import admin

from apis.models import PackageGeneric, PackageGenericEdu, PackageCinnamon, PackageCinnamonEdu, PackageMate, PackageMateEdu


#class AnswerInLine(admin.StackedInline):
    #model = Answer
    #extra = 3

#class QuestionAdmin(admin.ModelAdmin):
    #inlines = [AnswerInLine]

# Register your models here.
admin.site.register(PackageGeneric)
admin.site.register(PackageGenericEdu)
admin.site.register(PackageCinnamon)
admin.site.register(PackageCinnamonEdu)
admin.site.register(PackageMate)
admin.site.register(PackageMateEdu)

