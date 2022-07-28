from django.shortcuts import render
from .models import Data

def base_page(request):

    return render(request,'form/base.html')

def input_page(request):
    if request.method == 'POST':
        parameters = {key: value for key, value in request.POST.items() if 'key' in key}
        values = {key: value for key, value in request.POST.items() if 'value' in key}
        data = {}
        list1 = []
        list2 = []
        for v in parameters.values():
            list1.append(v)
        for v in values.values():
            list2.append(v)
        for i in range(len(list1)):
            data[list1[i]] = list2[i]
        Data(data=data).save()

    return render(request, 'form/input_information.html')

def output_page(request):
    if request.method == 'POST':
        Data.objects.all().delete()
    all_data = list(Data.objects.all())
    return render(request, 'form/output_information.html', {'all_data': all_data})
