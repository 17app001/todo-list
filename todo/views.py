from django.shortcuts import get_object_or_404, render
from .models import Todo
# Create your views here.


def view(request, id):
    todo = get_object_or_404(Todo, id=id)
    print(todo)
    return render(request, './todo/view.html', {'todo': todo})


def todo(request):
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)

    return render(request, './todo/todo.html', {'todos': todos})
