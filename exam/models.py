# Create your models here.
from django.db.models import CharField, ImageField, ForeignKey, TextField, PositiveSmallIntegerField, CASCADE, Model


class examType(Model):
	examName = CharField(max_length=20, verbose_name = 'Экзамен')
	examTypeLogo = ImageField(upload_to='exam/images/examTypeLogos', blank=True, null = True, verbose_name = "Логотип")

	class Meta:
		verbose_name = "Экзамен"
		verbose_name_plural = "Экзамены"
	def __str__(self):
		return self.examName

class subject(Model):
	exam = ForeignKey(examType, on_delete=CASCADE,verbose_name = "Экзамен")
	subjectName = CharField(max_length=30,verbose_name = "Предмет")
	subjectLogo = ImageField(upload_to='exam/images/subjectLogos', blank=True, null = True, verbose_name = "Иконка")
	class Meta:
		verbose_name = "Предмет"
		verbose_name_plural = "Предметы"
	def __str__(self):
		return self.subjectName + u' [' + self.exam.examName + u']'

class chapter(Model):
	subject = ForeignKey(subject, on_delete=CASCADE,verbose_name = "Предмет")
	chapterName = CharField(max_length=250, verbose_name = "Раздел")
	chapterLogo = ImageField(upload_to='exam/images/chapterLogos', blank=True, null = True, verbose_name = "Иконка")
	class Meta:
		verbose_name = "Раздел"
		verbose_name_plural = "Разделы"
	def __str__(self):
		return self.chapterName + ' [' + self.subject.subjectName + ']'

class problem(Model):
	chapter = ForeignKey(chapter, on_delete=CASCADE, verbose_name = "Раздел")
	problemText = TextField(verbose_name = "Условие задачи")	
	problemAverageDificulty = PositiveSmallIntegerField(blank=True, null=True, verbose_name = "Средняя сложность")
	
	class Meta:
		verbose_name = "Задача"
		verbose_name_plural = "Задачи"

	def __str__(self):
		return self.chapter.chapterName +  '(' + str(self.id) + ')'

		

class comments(Model):	
	problem = ForeignKey(problem, on_delete=CASCADE, verbose_name = 'Задача')
	problemDificulty = PositiveSmallIntegerField(blank=True, null=True, verbose_name = "Сложность")
	problemNumber = PositiveSmallIntegerField(blank=True, null=True, verbose_name = "Номер задачи")
	problemSolutionImg = ImageField(upload_to='exam/images/problemSolutions', blank=True, null = True, verbose_name = "Решение(картинка)")
	problemSolutionText = TextField(blank=True, null = True, verbose_name = "Решение(текст)")
	commentRating = PositiveSmallIntegerField(blank=True, null=True, verbose_name = "Рейтинг комментария")
	userID = PositiveSmallIntegerField(blank=True, null=True, verbose_name = "ID пользователя")
	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"
	def __str__(self):
		return str(self.id)