from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Homework, Topic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, request
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Test, Question, Answer, Grade
from .forms import TestForm, QuestionForm, AnswerForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Test, Question, Answer, StudentAnswer
from django.contrib.auth.models import Group


def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_400(request, exception):
    return render(request, 'errors/400.html', status=400)

# Представление для отправки домашнего задания
class HomeworkSubmitView(LoginRequiredMixin, CreateView):
    model = Homework
    fields = ['file', 'link']
    template_name = 'homework_submit.html'

    def form_valid(self, form):
        topic = get_object_or_404(Topic, pk=self.kwargs['topic_id'])
        form.instance.student = self.request.user
        form.instance.topic = topic
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_homeworks')
    
# Представление для теста

class TestCreateView(LoginRequiredMixin, CreateView):
    model = Test
    form_class = TestForm
    template_name = 'courses/test_create.html'
    success_url = reverse_lazy('test_list')


class TestListView(LoginRequiredMixin, ListView):
    model = Test
    template_name = 'courses/test_list.html'

    def get_queryset(self):
        return Test.objects.filter(course__instructor=self.request.user)

# Для студентов — прохождение теста
@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if request.method == 'POST':
        for question in test.questions.all():
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                answer = Answer.objects.get(id=selected_answer_id)
                StudentAnswer.objects.create(
                    student=request.user,
                    question=question,
                    answer=answer
                )
        return redirect('test_results', test_id=test.id)
    return render(request, 'courses/take_test.html', {'test': test})


# Для студентов — результаты теста
@login_required
def test_results(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    student_answers = StudentAnswer.objects.filter(student=request.user, question__test=test)
    correct_count = sum(1 for answer in student_answers if answer.answer.is_correct)
    total_questions = test.questions.count()
    return render(request, 'courses/test_results.html', {
        'test': test,
        'student_answers': student_answers,
        'correct_count': correct_count,
        'total_questions': total_questions,
    })

# Представление для проверки домашнего задания
class HomeworkReviewView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Homework
    fields = ['comment']
    template_name = 'homework_review.html'

    def test_func(self):
        # Проверяем, что текущий пользователь — преподаватель, связанный с курсом
        homework = self.get_object()
        return homework.topic.course.instructor == self.request.user

    def get_success_url(self):
        return reverse_lazy('course_homeworks', kwargs={'course_id': self.object.topic.course.id})
    
    def register(request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически авторизуем пользователя после регистрации
            return redirect('home')  # Перенаправление после регистрации
        else:
            form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})