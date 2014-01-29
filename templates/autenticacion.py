from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("Si se logueo.")
            # Redirect to a success page.
        else:
        	return HttpResponse("No se logueo.")
            # Return a 'disabled account' error message
    else:
    	return HttpResponse("No se logueo2.")
        # Return an 'invalid login' error message.
