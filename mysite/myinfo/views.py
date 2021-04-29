from django.http import JsonResponse

def student_info(request):
    data = {

        "Name" : "Jarla Kornegay",

        "Track" : "Backend(Python)",

        "Message" : "Hi mentor, I hope this works!"

    }
    return JsonResponse(data)
    




# Create your views here.
