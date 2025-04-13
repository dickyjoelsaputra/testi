from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'

    def url(self, name, parameters=None, expire=None):
        url = super().url(name, parameters, expire)
        # Ensure we're using the correct domain and bucket path
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
        Override _save to properly handle file uploads
        """
        if hasattr(content, 'temporary_file_path'):
            # Handle temporary uploaded files
            with open(content.temporary_file_path(), 'rb') as f:
                return super()._save(name, f)
        else:
            # Handle in-memory uploaded files
            if hasattr(content, 'seekable') and content.seekable():
                content.seek(0)
            if hasattr(content, 'read'):
                content = content.read()
            return super()._save(name, content)

    def get_available_name(self, name, max_length=None):
        """
        Get a unique filename if file_overwrite is False
        """
        if self.file_overwrite:
            return name
        return super().get_available_name(name, max_length)

    def url(self, name, parameters=None, expire=None):
        url = super().url(name, parameters, expire)
        # Ensure we're using the correct domain and bucket path
        custom_domain = self.connection.meta.client.meta.endpoint_url
        if not custom_domain.startswith('https://'):
            custom_domain = f'https://{custom_domain}'
        return url.replace(
            f"{custom_domain}/",
            f"{custom_domain}/{self.bucket_name}/"
        )
