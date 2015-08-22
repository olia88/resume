from django.shortcuts import render
from registration.forms import RegistrationForm
from myapp.models import Member
from myapp.forms import MemberForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

def main(request):
    return render(request, 'main.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    member_form=MemberForm(request.POST or None)
    registration_form=RegistrationForm(request.POST or None)

    if request.method == 'POST':
        member_form = MemberForm(request.POST, request.FILES)
        registration_form = RegistrationForm(request.POST)
        if member_form.is_valid() and registration_form.is_valid():
            member_form.save()
            registration_form.save()
            registration_form.new_person_form = member_form
            registration_form.save()
        else:
            member_form = member_form
            registration_form = registration_form
    return render(request, 'registration/registration_form.html', {
        'member_form': member_form,
        'registration_form': registration_form,
        })

class MemberUpdate(UpdateView):
    fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth', 'avatar']
    model = Member
    success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(MemberUpdate, self).form_valid(form)

class UserDelete(DeleteView):
    # form_class = MemberForm
    fields = ['username', 'password']
    model = User
    success_url = reverse_lazy('user-list')

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super(UserDelete, self).form_valid(form)