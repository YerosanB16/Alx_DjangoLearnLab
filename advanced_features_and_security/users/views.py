from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import get_user_model

User = get_user_model()

# View to list users (requires can_view permission)
@permission_required('users.can_view', raise_exception=True)
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# View to create a new user (requires can_create permission)
@permission_required('users.can_create', raise_exception=True)
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('user_list')
    return render(request, 'users/user_form.html')
