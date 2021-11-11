from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class SecurityTokenWorkaroundS3Boto3Storage(S3Boto3Storage):
    def _get_security_token(self):
        return None


class StaticStorage(SecurityTokenWorkaroundS3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(SecurityTokenWorkaroundS3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
