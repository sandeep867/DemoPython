from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Todoapp.forms import TodoForm
from Todoapp.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.


class TaskView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'show'


class TaskDetail(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'show'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'show'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk': self.object.id})


class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


# def add(request):
#     show = Task.objects.all()
#     if request.method == 'POST':
#         task = request.POST.get('Task', '')
#         priority = request.POST.get('Priority', '')
#         date = request.POST.get('Date', '')
#         task1 = Task(name=task, priority=priority, date=date)
#         task1.save()
#     return render(request, 'index.html', {'show': show})

#
# def delete(request, taskid):
#     if request.method == 'POST':
#         contain = Task.objects.get(id=taskid)
#         contain.delete()
#         return redirect('/')
#     return render(request, 'delete.html')
#
#
# def update(request, id):
#     task = Task.objects.get(id=id)
#     form = TodoForm(request.POST or None, instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, 'update.html', {'form': form})
