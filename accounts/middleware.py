from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages


class AccountCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user  # Who is the current user ?
        if user.is_authenticated:
            if user.user_type == '1':  # Admin
                if modulename == 'epoll.views':
                    error = True
                    if request.path == reverse('epoll:fetch_ballot'):
                        pass
                    else:
                        messages.error(
                            request, "You do not have access to this resource")
                        return redirect(reverse('administrator:adminDashboard'))
            elif user.user_type == '2':  # Voter
                if modulename == 'administrator.views':
                    messages.error(
                        request, "You do not have access to this resource")
                    return redirect(reverse('epoll:voterDashboard'))
            else:  # None of the aforementioned ? Please take the user to login page
                return redirect(reverse('accounts:accounts_login'))
        else:
            # If the path is login or has anything to do with authentication, pass
            if request.path == reverse('accounts:accounts_login') or request.path == reverse('accounts:accounts_register') or modulename == 'django.contrib.auth.views' or request.path == reverse('home:index'):
                pass
            elif modulename == 'administrator.views' or modulename == 'epoll.views':
                # If visitor tries to access administrator or voters functions
                messages.error(
                    request, "You need to be logged in to perform this operation")
                return redirect(reverse('accounts:accounts_login'))
            else:
                return redirect(reverse('accounts:accounts_login'))
