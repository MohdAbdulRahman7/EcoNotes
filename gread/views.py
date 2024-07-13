from django.http import HttpResponse
from django.shortcuts import render  # this is used to render templates when view function is invoked
from datetime import datetime, timedelta
from django.contrib.auth import get_user


# def homepage(request):
#     #return HttpResponse('My Home Page!') -- instead of this, render a template (home.html)
#     return render(request, 'homepage.html')

# def about(request):
#     return render(request, 'about.html')

# def homepage(request):
#     # Track visits for the homepage
#     visits = int(request.COOKIES.get('visits', '0'))
#     last_visit = request.COOKIES.get('last_visit', None)
#
#     response = render(request, 'homepage.html')
#
#     if last_visit:
#         last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
#         if (datetime.now() - last_visit_time).days > 0:
#             response.set_cookie('visits', visits + 1)
#             response.set_cookie('last_visit', datetime.now())
#     else:
#         response.set_cookie('last_visit', datetime.now())
#         response.set_cookie('visits', visits + 1)
#
#     return response


# def homepage(request):
#     user = get_user(request)
#     response = render(request, 'homepage.html')  # Default response
#
#     if user.is_authenticated:
#         user_id = user.id
#         visits_cookie_name = f'visits_{user_id}'
#         last_visit_cookie_name = f'last_visit_{user_id}'
#
#         visits = int(request.COOKIES.get(visits_cookie_name, '0'))
#         last_visit = request.COOKIES.get(last_visit_cookie_name, None)
#
#         try:
#             if last_visit:
#                 last_visit_time = datetime.strptime(last_visit, "%Y-%m-%d %H:%M:%S")
#                 if (datetime.now() - last_visit_time) > timedelta(seconds=30):
#                     visits += 1
#                     response.set_cookie(visits_cookie_name, visits)
#                     response.set_cookie(last_visit_cookie_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#             else:
#                 response.set_cookie(last_visit_cookie_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#                 response.set_cookie(visits_cookie_name, visits + 1)
#         except ValueError:
#             # If there is an issue with the datetime format, reset the cookies
#             response.set_cookie(last_visit_cookie_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#             response.set_cookie(visits_cookie_name, 1)
#
#     return response
#
#
# def about(request):
#     user = get_user(request)
#     if user.is_authenticated:
#         user_id = user.id
#         visits_cookie_name = f'visits_{user_id}'
#         visits = int(request.COOKIES.get(visits_cookie_name, '0'))
#         context = {'visits': visits}
#     else:
#         context = {'visits': None}
#
#     return render(request, 'about.html', context)


def homepage(request):
    user = get_user(request)
    cookie_consent = request.COOKIES.get('cookie_consent')

    response = render(request, 'homepage.html')

    if user.is_authenticated and cookie_consent == 'accepted':
        user_id = user.id
        visits_cookie_name = f'visits_{user_id}'
        last_visit_cookie_name = f'last_visit_{user_id}'

        visits = int(request.COOKIES.get(visits_cookie_name, '0'))
        last_visit = request.COOKIES.get(last_visit_cookie_name, None)

        try:
            if last_visit:
                last_visit_time = datetime.strptime(last_visit, "%Y-%m-%d %H:%M:%S")
                if (datetime.now() - last_visit_time) > timedelta(seconds=30):
                    visits += 1
                    response.set_cookie(visits_cookie_name, visits)
                    response.set_cookie(last_visit_cookie_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            else:
                response.set_cookie(last_visit_cookie_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                response.set_cookie(visits_cookie_name, visits + 1)
        except ValueError:
            # If there is an issue with the datetime format, reset the cookies
            response.set_cookie(last_visit_cookie_name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            response.set_cookie(visits_cookie_name, 1)

    return response


def about(request):
    user = get_user(request)
    cookie_consent = request.COOKIES.get('cookie_consent')

    if user.is_authenticated and cookie_consent == 'accepted':
        user_id = user.id
        visits_cookie_name = f'visits_{user_id}'
        visits = int(request.COOKIES.get(visits_cookie_name, '0'))
        context = {'visits': visits}
    else:
        context = {'visits': None}

    return render(request, 'about.html', context)