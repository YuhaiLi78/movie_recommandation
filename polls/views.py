from django.shortcuts import render, redirect
from . import final

# Create your views here.
def recommand(request):
    res = ""
    col_res = ""
    options = final.movie_names()
    name = ""
    if request.method == 'POST':
        if request.POST.get('pred_button'):
            name = request.POST['movie']
            res = final.content_rec(str(name))
            res = res.values.tolist()
            col_res = final.col_rec(name)
        else:
            redirect('homepage')
            res = ""
            col_res = ""
    else:
        print("Error Occurred")

    return render(request, "first.html", {'movie': name, 'options': options,'result': res, 'col_result' : col_res})