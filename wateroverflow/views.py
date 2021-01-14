from django.shortcuts import render
from wateroverflow.forms import overFlowForm

# Create your views here.
def overflow(request):
    form = overFlowForm()
    res_string = None
    if(request.POST):
        result = None
        i = int(request.POST['row'])
        j = int(request.POST['glass'])
        K = request.POST['water']

        res = liquidMeter(i, j, K)

        if res is not -1:
            if float(res) <= 0.0:
                res_string = 'No water filled on this glass location.'
            else:
                res_string = "The liquid poured in (" + str(j) + ")nth glass of (" + str(i) + ")nth row is: " + str(res) + "L"
        else:
            res_string = "Invalid Input"

        return render(request, "view.html", context={"form": form, "result" : res_string})
    return render(request, "view.html", context={"form": form, "result" : res_string})

def liquidMeter(i, j, K):
    # start i and j from 1 since the position of i from the picture starts from zero
    # i = i + 1
    # j = j + 1

    if (j > i):
        return -1
 
    # create an array of empty glasses
    glass_triangle = [0] * int(i *(i + 1) / 2)

    index = 0
    glass_triangle[index] = K

    glass_limit = .25 #liter
 
    for row in range(1,i):
        for col in range(1,row+1):

            current = float(glass_triangle[index])
            remaining = 0.0

            if current >= glass_limit:
                glass_triangle[index] = glass_limit
                remaining = current - glass_limit

            glass_triangle[row + index] += remaining / 2
            glass_triangle[row + index + 1] += remaining / 2
            index += 1

    return min(glass_triangle[int(i * (i - 1) / 2) + j - 1], float(glass_limit))