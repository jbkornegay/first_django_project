from django.http import HttpResponse

def student_info(request):
    data = {

        "Name" : "Jarla Kornegay",

        "Track" : "Backend(Python)",

        "Message" : "Hi mentor, I hope this works!"

    }
    
    return HttpResponse("Name:  %s \nTrack:  %s \nMessage:  %s" %(data["Name"], data["Track"], data["Message"]))

    

# Create your views here.
