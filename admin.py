from django.contrib import admin
from profiles.models import Profile, ForgetPassword, BreakTimeModels, ResetPasswordModels
from chatroom.models import ChatRoom, Message

class ChildModelInline(admin.TabularInline):
    model = Message
    extra = 1 


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'enterprise_name',
        'enterprise_role',
        'email',
        'user',
        'group',
    ]
    exclude = [
        'settings',
        
    ]
    inlines = [
        ChildModelInline,

    ]

@admin.register(ForgetPassword)
class ForgetPasswordAdmin(admin.ModelAdmin):
    list_display = ['token']

@admin.register(ResetPasswordModels)
class ResetPasswordModelsAdmin(admin.ModelAdmin):
    list_display = [
        'token'
    ]