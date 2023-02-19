import datetime
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from taskapp.models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer
from .filters import TaskFilterSet


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilterSet


def close_task(request, pk):
    task = Task.objects.get(id=pk)
    task.status = True
    task.end = datetime.datetime.now()
    task.save()
    return redirect("/")


def return_task(request, pk):
    task = Task.objects.get(id=pk)
    task.status = False
    task.end = None
    task.save()
    return redirect("/")


class TaskList(ListView):
    """Представление для отображения множества корзин.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview
    """

    model = Task
    context_object_name = "tasks_"
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Task.objects.filter(status=False)


class TaskDetail(DetailView):
    """Представление для отображения одной корзины.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#detailview
    """

    model = Task
    template_name = "task_detail.html"
    pk_url_kwarg = "pk"
    context_object_name = "task"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskDelete(DeleteView):
    model = Task
    template_name = "index.html"
    success_url = "/"


class TaskUpdate(UpdateView):
    model = Task
    fields = [
        "status",
        "title",
    ]
    template_name = "task_update.html"
    pk_url_kwarg = "pk"
    context_object_name = "task_up"
    success_url = "/"

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(TaskUpdate, self).form_valid(form)


class TaskCreate(CreateView):
    """Представление для создания одной корзины.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
    """

    model = Task
    fields = ["title"]
    template_name = "task_add.html"
    success_url = "/"
