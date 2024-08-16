from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm 
# Create your views here.

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return redirect(request, 'eventsapp/create_event.html',{'form':form})

def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'Post':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
        return render(request, 'eventsapp/update_event.html', {'form':form})
    
def event_list(request):
    events = Event.objects.all()
    return render(request, 'eventsapp/event_list.html',{'events':events})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'eventsapp/delete_event.html', {'event':event})