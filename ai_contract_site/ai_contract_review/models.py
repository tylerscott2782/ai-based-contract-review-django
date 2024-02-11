from django.db import models

# Create your models here.
class Contract(models.Model):
    filename = models.CharField(max_length=200)
    upload_date = models.DateTimeField("date uploaded")
    status = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.filename
    
    def get_data_status(self):
        status_dict = {
            1: "not-scanned",
            2: "scanning",
            3: "scanned",
        }
        return status_dict[self.status]
    
    def get_status_text(self):
        status_dict = {
            1: "Not Scanned",
            2: "Scanning ...",
            3: "Scanned",
        }
        return status_dict[self.status]

    def get_button_text(self):
        status_dict = {
            1: "Begin Scanning",
            2: "Pause",
            3: "View Scan",
        }
        return status_dict[self.status]