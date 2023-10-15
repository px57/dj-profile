from django.db import models
import imp
from lib2to3.pytree import Base
from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from kernel.models.base_metadata_model import BaseMetadataModel
from kernel.http.serialize.media import serialize_file_fields, serialize_phone_number, serialize_size_video
from django.conf import settings
from kernel.models.decorators import serializer_object
from mediacenter.models import FilesModel

class ForgetPassword(BaseMetadataModel):
    """_summary_

    Args:
        BaseMetadataModel (_type_): _description_
    """
    
    token = models.CharField(max_length=32)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    
    def serialize(self, request):
        """_summary_

        Args:
            request (_type_): _description_
        """
        serialize = model_to_dict(self)
        return serialize

class BreakTimeModels(BaseMetadataModel):
    """_summary_

    Args:
        models (_type_): _description_
    """
    last_use = models.DateTimeField()
    key = models.CharField(max_length=255)

class Profile(BaseMetadataModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    
    language = models.CharField(
        max_length=10,
        default='en',
        choices=(
            ('fr', 'Français'),
            ('en', 'English'),
            ('es', 'Español'),
            ('de', 'Deutsch'),
            ('it', 'Italiano'),
            ('pt', 'Português'),
            ('ru', 'Русский'),
            ('zh', '中文'),
            ('ja', '日本語'),
            ('ar', 'العربية'),
            ('ko', '한국어'),
            ('hi', 'हिन्दी'),
        )
    )

    avatar = models.ForeignKey(
        'mediacenter.FilesModel',
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='avatar'
    )
    
    group = models.CharField(
        max_length=20,
        choices=(
            ('root', 'Admin'),
            ('player', 'Player'),
        ),
        default='player',
    )
    
    settings = models.JSONField(
        default={}, 
        null=False,
    )

    email_verified = models.BooleanField(
        default=False,
    )

    is_anonymous = models.BooleanField(
        default=False,
    )

    def __unicode__(self):
        return u"%s" % (self.user)
    
    @property
    def username(self):
        """_summary_
        """
        return self.user.username
    
    @property
    def first_name(self):
        """_summary_
        """
        return self.user.first_name

    @property
    def last_name(self):
        """_summary_
        """
        return self.user.last_name
    
    @property
    def email(self):
        """_summary_
        """
        if self.user is None:
            return ''
        return self.user.email
    
    default_params = {
        'send_email__tocomment': True,
    }

    def get_serialized_avatar(self, request):
        """
            @description: Récupérer l'avatar de l'utilisateur.
        """
        if self.avatar is None:
            # TODO: moove the default avatar into the settings
            # FilesModel(
            #     scr
            # )
            return None
        return self.avatar.serialize(request)
    
    def get_settings_key(self, get_key):
        """_summary_

        Args:
            key (_type_): _description_
        """

        saving = False

        for key in self.default_params:
            if key not in self.settings.keys():
                saving = True
                self.settings[key] = self.default_params[key]
                continue
        
        if saving:
            self.save()
            
        if get_key not in self.settings.keys():
            raise Exception('This key "' + get_key + '" doesn\'t exists into the settings')
        return self.settings[get_key]
    
    def set_settings_key(self, key, value):
        """_summary_
        """
        if key not in self.default_params:
            return False

        self.settings[key] = value
        return True

    def serialize__exclude(self, *args, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            'little': [
                'settings', 
                'user', 
                'email_verified', 
                'is_staff', 
                'activated', 
                'email',
            ],
        }.get(kwargs.get('serializer_type', None), ['settings', 'user', 'email_verified', 'is_staff', 'activated'])

    @serializer_object
    def serialize(self, request, *args, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            '_object': self,
            '_update': {
                'id': self.user.id,
                'avatar': self.get_serialized_avatar(request),
                'username': self.user.username,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
                'email': self.user.email,
                'is_staff': self.user.is_staff,
            },
            '_exclude': self.serialize__exclude(*args, **kwargs),
            '_include': [],
        }

class ResetPasswordModels(BaseMetadataModel):
    """
        Il s'agit ici de
    """
    profile = models.ForeignKey(
        Profile,
        verbose_name='UID',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    token = models.CharField(
        max_length=32,
        unique=True,
    )
    status = models.CharField(
        max_length=30,
        default='NEW',
        choices=(
            ('NEW', 'Nouveaux ticket de récupérations'),
            ('USED', 'Ticket utilisée'),
        ))

    def use_ticket(self, new_password):
        """
            @description: Modifier le jeton juste ici.
        """
        # -> Modifications du mote de passe
        self.profile.user.set_password(new_password)
        self.profile.user.save()

        # -> Modification du type de jeton
        self.status = 'USED';
        self.save()

    def serialize(self, request):
        """
            @description:
        """
        return model_to_dict(self)
    
class NetWorkModels(BaseMetadataModel):
    """
        @description: La liste des éléments de networks.
    """
    profile = models.ForeignKey(
        Profile,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    url = models.CharField(
        max_length=250,
        default=''
    )
    key = models.CharField(
        max_length=50,
        default='',
        choices=(
            ('instagram', 'Instagram'),
            ('tiktok', 'Tiktok'),
            ('youtube', 'Youtube'),
            ('linkedin', 'Linkedin'),
            ('facebook', 'Facebook'),
            ('twitter', 'Twitter'),
        )
    )

    def serialize(self, request):
        """
            @description:
        """
        icone_list = {
            'instagram': 'icon-INSTAGRAM',
            'tiktok': 'icon-TIKTOK',
            'youtube': 'icon-YOUTUBE1',
            'linkedin': 'icon-LINKEDIN',
            'facebook': 'icon-FACEBOOK1',
            'twitter': 'icon-TWITTER1',
        }
        serialized = model_to_dict(self)
        serialized['icon'] = icone_list.get(self.key, '')
        return serialized
    
class VerifyIdentifier(BaseMetadataModel):
    profile = models.ForeignKey(
        Profile,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    token = models.CharField(
        max_length=32,
        unique=True,
    )
    status = models.CharField(
        max_length=30,
        default='NEW',
        choices=(
            ('NEW', 'Nouveaux ticket de vérification'),
            ('USED', 'Ticket utilisée'),
        )
    )
    