from django.contrib import admin
from api.models import User
from api.models import Flight
from api.models import Travel
from api.models import Travelers

admin.site.register([User, Flight, Travel, Travelers])
