

# Create your models here.
from django.db import models
from datetime import datetime, date
from authapi.models import User
from utility.models import (
    UniqueNamedBaseModel,
    NamedBaseModel,
    VerboseNamedBaseModel,
    BaseModel,
    AGE_GROUPS,
    SPROUTLINGS,
    DEFAULT_CHAR_FIELD_MAX,
    DEFAULT_MAX_CHAR,
)
# from tms.models import Fundamental, LearningMoment, Checkpoint
from user_profile.options import (
    DEFAULT_CHAR_FIELD_MAX,
    # MILESTONES,
    ROLE_LIST,
    GENDER_LIST,
    # EDUCATION_LIST,
)
# from cms.models import Activity, Lesson, Module, Project
# from pre_discovery_questionnaire.models import Answer, Language
from django.core.validators import RegexValidator, MinValueValidator


class UserProfile(models.Model):
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    # ----
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="profile")
   
    email = models.EmailField(max_length=255)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    role = models.CharField(choices=ROLE_LIST, max_length=255, default="NONE")

    preferred_name = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    # default as an empty string
    gender = models.CharField(choices=GENDER_LIST, max_length=255, blank=True)

    country = models.CharField(max_length=DEFAULT_CHAR_FIELD_MAX, blank=True, null=True)
    dob = models.DateField(null=True)
    image = models.ImageField(blank=True, null=True, max_length=DEFAULT_MAX_CHAR)
   
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=DEFAULT_CHAR_FIELD_MAX, null=True, blank=True)

    def __str__(self):
        if self.email:
            return self.email
        if self.preferred_name:
            return self.preferred_name
        return "UserProfile {}".format(self.id)