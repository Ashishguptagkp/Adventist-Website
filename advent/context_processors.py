from website.models import Category

def category(request):
    return {'categories':Category.objects.all()}