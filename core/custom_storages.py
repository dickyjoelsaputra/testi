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
        Override _save to ensure file stays open during upload
        """
        if hasattr(content, 'seekable') and content.seekable():
            content.seek(0)
        return super()._save(name, content)

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
