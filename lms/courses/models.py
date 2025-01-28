from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, related_name='instructor_courses', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    course = models.ForeignKey(Course, related_name='groups', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(User, related_name='student_groups')

    def __str__(self):
        return f"{self.name} - {self.course.name}"


class Attendance(models.Model):
    group = models.ForeignKey(Group, related_name='attendances', on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='attendances', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField()

    def __str__(self):
        return f"{self.student.username} - {self.group.name} - {self.date}"


class Topic(models.Model):
    course = models.ForeignKey(Course, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Homework(models.Model):
    student = models.ForeignKey(User, related_name='homeworks', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic', related_name='homeworks', on_delete=models.CASCADE)
    file = models.FileField(upload_to='homeworks/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Homework by {self.student.username} for {self.topic.title}"
    

class Test(models.Model):
    course = models.ForeignKey('Course', related_name='tests', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class StudentAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.question.text} - {self.answer.text}"


class Grade(models.Model):
    student = models.ForeignKey(User, related_name='grades', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='grades', on_delete=models.CASCADE)
    score = models.FloatField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.test.title} - {self.score}"