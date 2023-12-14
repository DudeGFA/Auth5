from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from Account.models import FieldGroup, Field, Authorization
from .forms import GroupForm, FieldForm
from django.shortcuts import  render, redirect
from Account.forms import UrlForm
from django.contrib.auth.models import User

# Create your views here.
class LandingView(View):
    def get(self, request):
        return render(request, "landing.html")

class HomeView(LoginRequiredMixin, View):
    def get(self, request, group='default field group'):
        # Getting all field groups owned by the user
        try:
            if not request.user.profile:
                return redirect('/account/login/')
        except Exception:
            return redirect('/account/login/')

        field_groups_for_owner = FieldGroup.objects.filter(owner=request.user.profile)

        # Extracting names of all field groups for the owner
        field_group_names = field_groups_for_owner.values_list('name', flat=True)
        # print(field_group_names)
        active_field_group = FieldGroup.objects.filter(owner=request.user.profile, name=group).first()
        context = {'active_field_group': active_field_group, 'field_group_names': field_group_names}
        return render(request, 'dashboard.html', context)
    
    def post(self, request, group=None):
        try:
            if not request.user.profile:
                return redirect('/account/login/')
        except Exception:
            return redirect('/account/login/')

        request_type = request.POST.get("type")
        if request_type == 'group':
            new_group_name = request.POST.get("new_group")
            if not new_group_name:
                redirect_group = request.POST.get("groups")
                return redirect ('/dashboard/' + redirect_group)
            group = GroupForm({'name': new_group_name, 'owner': request.user.profile})
            if group.is_valid():
                group.save()
                return redirect('/dashboard/' + new_group_name)
            else:
                print(group.errors)
        elif request_type == 'field':
            new_field_name = request.POST.get("new_field")
            group_id = request.POST.get("group")
            group = FieldGroup.objects.get(id=group_id)
            new_field = FieldForm({'name': new_field_name, 'group': group})
            if new_field.is_valid():
                new_field.save()
            return redirect("/dashboard/"+group.name)
        elif request_type is None:
            field_name = request.POST.get("name")
            group_id = request.POST.get("group")
            authorized_user_id = request.POST.get("auth")
            group = FieldGroup.objects.get(id=group_id)
            field = Field.objects.filter(name=field_name, group=group).first()
            field_form = FieldForm(request.POST or None, instance=field)
            if field_form.is_valid():
                field_form.save()
            else:
                print(field_form.errors)
            if authorized_user_id:
                print(authorized_user_id)
                authorized_user = User.objects.filter(username=authorized_user_id.strip()).first()
                if authorized_user:
                    try:
                        Authorization.objects.create(field=field, user_profile=authorized_user.profile)
                    except Exception:
                        pass
            return redirect("/dashboard/"+group.name)
        return redirect("/dashboard/")

class WebsiteDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            if request.user.website:
                return render(request, 'website/dashboard.html')
        except Exception:
            pass
        return redirect('/account/website/login/')
    
    def post(self, request):
        callback_url = request.POST.get('callback-url')
        url_form = UrlForm({'url': callback_url})
        if url_form.is_valid():
            callback_url = url_form.cleaned_data['url']
            print(callback_url)
            request.user.website.callback_url = callback_url
            request.user.website.save()
        else:
            print(url_form.errors)
        return redirect('/dashboard/website/')