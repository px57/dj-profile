from django.contrib import admin
from profiles.models import Profile, ForgetPassword, BreakTimeModels, ResetPasswordModels

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'group',
    ]

        

@admin.register(ForgetPassword)
class ForgetPasswordAdmin(admin.ModelAdmin):
    list_display = [
        'token'
    ]

@admin.register(ResetPasswordModels)
class ResetPasswordModelsAdmin(admin.ModelAdmin):
    list_display = [
        'token'
    ]