from django.contrib import admin
from .models import User
from .models import Flight
from .models import Travel
from .models import Travelers

admin.site.register([User, Flight, Travel, Travelers])
