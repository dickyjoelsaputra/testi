from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'

    def url(self, name, parameters=None, expire=None):
        url = super().url(name, parameters, expire)
        # Replace the domain-only URL with bucket-included URL
        return url.replace(
            f"{self.connection.meta.client.meta.endpoint_url}/",
            f"{self.connection.meta.client.meta.endpoint_url}/{self.bucket_name}/"
        )

class MediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
