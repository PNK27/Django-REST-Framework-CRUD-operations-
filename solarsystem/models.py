from django.db import models

class Planet(models.Model):
    claimID = models.IntegerField()
    claimantName = models.CharField(max_length = 15)
    expDate = models.DateField()
    claimedBodyId = models.IntegerField()
    createTime = models.DateTimeField()
    modTime = models.DateTimeField()


'''
Claim ID (string)
Claimant Name (string)
Expiration Date (Date field)
Claimed Body (valid ID from the OpenData API)
Creation Time (datetime in ISO-8601 representation)
Modification Time (datetime in ISO-8601 representation)
'''
