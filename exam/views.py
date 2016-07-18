from django.shortcuts import render, redirect
from .models import examType, subject, chapter, problem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm

def index(request):
	exams = examType.objects.all()
	return render(request, 'public/index.html',{
		"exams": exams
		})


def subject_list(request, exam_id):
	Exam = examType.objects.get(pk=exam_id)
	subjects = Exam.subject_set.all()
	title =  Exam.examName
	exams = examType.objects.all()
	return render(request, 'public/exam.html', {
		"subjects": subjects,
		"title": title,
		"exams": exams
		})

def chapter_list(request, subject_id):
	Subject = subject.objects.get(pk=subject_id)
	chapters = Subject.chapter_set.all()
	title =  Subject.subjectName
	exams = examType.objects.all()
	return render(request, 'public/chapter.html', {
		"chapters": chapters,
		"title": title,
		"exams": exams
		})

def problem_list(request, chapter_id):
	Chapter = chapter.objects.get(pk=chapter_id)
	#problems = Chapter.problem_set.all()
	title =  Chapter.chapterName
	exams = examType.objects.all()
	pr_list = Chapter.problem_set.all()
	paginator = Paginator(pr_list, 15)
	page = request.GET.get('page')
	try:			
		problems = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		problems = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		problems = paginator.page(paginator.num_pages)

	return render(request, 'public/problem.html', {
		"problems": problems,
		"title": title,
		"exams": exams
		})

class UserFormView(View):
	form_class = UserForm
	template_name = 'registration/register.html'

	# получаем форму
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form	})

		#посылаем данные
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			

			user.set_password(password)
			user.save()

			###
			user = authenticate(username=username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('exam:index')

		return render(request, self.template_name, {'form': form})






