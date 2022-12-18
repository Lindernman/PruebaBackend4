from django.shortcuts import redirect, render
import requests
import requests


def inicio(request):

    if request.session.test_cookie_worked():
        return redirect('detalle')
    return render(request, 'index.html')


def login(request):
    if request.POST:
        data = requests.post(
            'http://127.0.0.1:8000/api/persona/login/', data=request.POST, cookies=request.COOKIES).json()
        if "user_id" in data:

            response = redirect('detalle')
            request.session.set_test_cookie()
            response.set_cookie('user_id', data['user_id'])
            return response
    return render(request, 'login.html')


def register(request):
    if request.POST:
        data = requests.post(
            'http://127.0.0.1:8000/api/persona/register/', data=request.POST, ).json()
        if "user_id" in data:
            return redirect('login')
    return render(request, 'registro.html')


def logout(request):
    if request.session.test_cookie_worked():

        request.session.delete_test_cookie()
    return render(request, 'login.html')


def detalle(request):
    if request.session.test_cookie_worked():
        user_id = request.COOKIES.get('user_id')

        data = requests.get(
            'http://127.0.0.1:8000/api/persona/' + user_id).json()

        return render(request, 'detalle.html', {'auth': True, 'data': data})
    else:
        return redirect('login')


def transaction(request):
    if request.session.test_cookie_worked():
        if request.POST:
            data = requests.post(
                'http://127.0.0.1:8000/api/persona/transaction/', data=request.POST, cookies=request.COOKIES).json()
            print(data)

    return redirect('detalle')
