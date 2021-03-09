from django.db import models
from mapbox_location_field.models import LocationField, AddressAutoHiddenField
# from mapbox_location_field.spatial.models import SpatialLocationField


# Create your models here.
class UserLocationModel(models.Model):
    location = LocationField(map_attrs={"center": [0, 0], "marker_color": "blue"})
    # address = AddressAutoHiddenField()
