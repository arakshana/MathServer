from django.shortcuts import render

def churn_rate(request):
    l = int(request.POST.get('lost', '0'))
    i = int(request.POST.get('initial', '0'))

    churnrate = (l/i)*100 if request.method == "POST" else 0

    print("Customerslost =", l)
    print("InitialCustomers =", i)
    print("ChurnRate =", churnrate)

    return render(
        request,
        'myapp/rakshana.html',
        {'l': l, 'i': i, 'churnrate': churnrate}
    )
