# teachers/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import Teacher
from .forms import TeacherForm
from django.shortcuts import redirect
from django.http import HttpResponse

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher_success')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.request.session['teacher_id'] = self.object.id
            self.request.session['teacher_name'] = self.object.name
            response = redirect(self.get_success_url())
            response.set_cookie('teacher_subject', self.object.subject)
            return response
        else:
            print(form.errors)
            return self.form_invalid(form)


    def form_invalid(self, form):
        return super().form_invalid(form)

class TeacherSuccessView(TemplateView):
    template_name = 'teachers/success.html'