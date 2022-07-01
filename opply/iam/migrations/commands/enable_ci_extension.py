from django.contrib.postgres.operations import CITextExtension


def enable_citext_extention():
    return CITextExtension()
