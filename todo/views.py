from todo.models import Number, Item, Priority

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["GET", "POST"])
def voice(request):
    return render(request, 'todo/voice.xml')


@csrf_exempt
@require_http_methods(["GET", "POST"])
def text(request):
    post = request.POST
    fro = post.get("From").strip()
    body = post.get("Body").strip()

    try:
        number = Number.objects.get(number=fro)
    except Number.DoesNotExist:
        return render(request, 'todo/text.error.xml', {})

    item = Item.objects.create(
        who=number.who,
        description=body,
        priority=Priority.objects.get(name='default'),
    )
    item.save()

    return render(request, 'todo/text.xml', {
        "who": who,
        "item": item,
    })
