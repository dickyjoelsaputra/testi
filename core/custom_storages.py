from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.base import File

class KeepOpenFile(File):
    """File wrapper that keeps the underlying file open"""
    def __init__(self, file, name=None):
        super().__init__(file, name)
        self._file = file
        self._is_opened = True

    def open(self, mode=None):
        if not self._is_opened:
            self._file.open(mode or self.mode)
            self._is_opened = True
        return self

    def close(self):
        if self._is_opened:
            self._file.close()
            self._is_opened = False

    def __del__(self):
        self.close()

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'

    def url(self, name, parameters=None, expire=None):
        url = super().url(name, parameters, expire)
        custom_domain = self.connection.meta.client.meta.endpoint_url
        if not custom_domain.startswith('https://'):
            custom_domain = f'https://{custom_domain}'
        return url.replace(
            f"{custom_domain}/",
            f"{custom_domain}/{self.bucket_name}/"
        )

class MediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False

    def _save(self, name, content):
        """
        Simplified _save method that avoids temporary files
        """
        from django.core.files.base import ContentFile
        
        if hasattr(content, 'temporary_file_path'):
            # Handle temporary files directly
            with open(content.temporary_file_path(), 'rb') as f:
                return super()._save(name, f)
        
        # Handle in-memory content
        if hasattr(content, 'seek'):
            content.seek(0)
        
        if not hasattr(content, 'read'):
            content = ContentFile(content)
        
        return super()._save(name, content)

    def get_available_name(self, name, max_length=None):
        if self.file_overwrite:
            return name
        return super().get_available_name(name, max_length)

    def url(self, name, parameters=None, expire=None):
        url = super().url(name, parameters, expire)
        custom_domain = self.connection.meta.client.meta.endpoint_url
        if not custom_domain.startswith('https://'):
            custom_domain = f'https://{custom_domain}'
        return url.replace(
            f"{custom_domain}/",
            f"{custom_domain}/{self.bucket_name}/"
        )
