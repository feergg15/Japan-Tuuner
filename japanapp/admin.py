from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Coche
admin.site.register(Coche)

from .models import Escape
admin.site.register(Escape)

from .models import Llanta
admin.site.register(Llanta)

from .models import Volante
admin.site.register(Volante)

from .models import Body_Kit
admin.site.register(Body_Kit)

from .models import Proyecto
admin.site.register(Proyecto)

from .models import Suspension
admin.site.register(Suspension)

from .models import Filtro
admin.site.register(Filtro)

from .models import User
admin.site.register(User)