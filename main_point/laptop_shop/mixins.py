# mixins.py
from django.db import models
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings

class GoogleDriveFileMixin(models.Model):
    class Meta:
        abstract = True

    def delete_google_drive_file(self):
        if self.image:
            credentials = service_account.Credentials.from_service_account_file(
                settings.GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE, scopes=['https://www.googleapis.com/auth/drive']
            )
            drive_service = build('drive', 'v3', credentials=credentials)

            # Get the file ID from the image URL
            file_id = self.image.url.split('id=')[1].split('&')[0]

            # Use the Google Drive API to delete the file
            drive_service.files().delete(fileId=file_id).execute()

    def delete(self, *args, **kwargs):
        self.delete_google_drive_file()
        super().delete(*args, **kwargs)
