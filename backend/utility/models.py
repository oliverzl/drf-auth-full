from django.db import models
from authapi.models import User
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from unidecode import unidecode
from rest_framework.pagination import PageNumberPagination

DEFAULT_CHAR_FIELD_MAX = 10000
DEFAULT_MAX_CHAR = 1023

SPROUTS = "Sprouts"
SPROUTLINGS = "Sproutlings"
BUDS = "Buds"
BLOSSOMS = "Blossoms"
BLOOMS = "Blooms"

AGE_GROUPS = [
    (SPROUTS, "18 months - 2 years"),
    (SPROUTLINGS, "2 years - 3 years"),
    (BUDS, "3 years - 4 years"),
    (BLOSSOMS, "4 years - 5 years"),
    (BLOOMS, "5 years - 6 years"),
]

AGE_GROUPS_RANKING = {
    SPROUTS: 1,
    SPROUTLINGS: 2,
    BUDS: 3,
    BLOSSOMS: 4,
    BLOOMS: 5,
}

AGE_GROUPS_RANKING_REVERSE = {
    1: SPROUTS,
    2: SPROUTLINGS,
    3: BUDS,
    4: BLOSSOMS,
    5: BLOOMS,
}


TEACHER_LEVELS = [("B", "Beginner"), ("I", "Intermediate"), ("A", "Advanced")]

HEART = "heart"
HEAD = "head"
HANDS = "hands"


GOAL_TAGS = [
    (HEART, "Heart"),
    (HEAD, "Head"),
    (HANDS, "Hands"),
]

ACTIVITY_TYPES = [
    ("Video", "Video"),
    ("Text", "Text"),
    ("Mcq", "Mcq"),
    ("FillInTheBlank", "FillInTheBlank"),
    ("Matching", "Matching"),
    ("FlipCard", "FlipCard"),
]


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 10000


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        default=None,
        on_delete=models.SET_NULL,
        null=True,
        related_name="%(class)s_created_by",
    )
    updated_by = models.ForeignKey(
        User,
        default=None,
        on_delete=models.SET_NULL,
        null=True,
        related_name="%(class)s_updated_by",
    )

    class Meta:
        abstract = True


class NamedBaseModel(BaseModel):
    name = models.CharField(max_length=DEFAULT_CHAR_FIELD_MAX)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class UniqueNamedBaseModel(NamedBaseModel):
    name = models.CharField(max_length=DEFAULT_CHAR_FIELD_MAX, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        try:
            self.slug = slugify(unidecode(self.name_en))
        except:
            print("Self.name_en doesn't exist. proceed to use self.name")
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)


class VerboseNamedBaseModel(NamedBaseModel):
    description = models.CharField(max_length=DEFAULT_CHAR_FIELD_MAX, blank=True)

    class Meta:
        abstract = True


# class TeacherTrainingBaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, null=True, related_name='teacher_%(class)s_created_by')
#     updated_by = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, null=True, related_name='teacher_%(class)s_updated_by')

#     class Meta:
#         abstract=True

# class TeacherNamedBaseModel(TeacherTrainingBaseModel):
#     name = models.CharField(max_length=DEFAULT_CHAR_FIELD_MAX)

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return self.name


class TeacherUniqueNamedBaseModel(BaseModel):
    name = models.CharField(max_length=DEFAULT_CHAR_FIELD_MAX, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# class TeacherVerboseNamedBaseModel(TeacherNamedBaseModel):
#     description = models.CharField(max_length=DEFAULT_CHAR_FIELD_MAX, null=True)

#     class Meta:
#         abstract=True
