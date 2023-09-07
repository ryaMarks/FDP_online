from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone
from .models import UserProfile


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')


def user_activity(request):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile
        user_profile.last_activity = datetime.now()
        user_profile.save()

def online_users(request):
    # Consulta para obter todos os usuários online nos últimos 5 minutos
    online_users = UserProfile.objects.filter(last_activity__gte=timezone.now() - timezone.timedelta(minutes=3))
    online_users_count = online_users.count()
    return render(request, 'online_users_count.html', {'online_users_count': online_users_count})
