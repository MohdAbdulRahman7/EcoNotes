# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm, EnrollmentForm


@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('events:events_list')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})


@login_required
def enroll_event(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            event_id = form.cleaned_data['event_id']
            event = get_object_or_404(Event, id=event_id)
            if not event.is_full():
                event.enrolled_users.add(request.user)
                return redirect('events:events_list')
    return redirect('events:events_list')


@login_required
def unenroll_event(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            event_id = form.cleaned_data['event_id']
            event = get_object_or_404(Event, id=event_id)
            if request.user in event.enrolled_users.all():
                event.enrolled_users.remove(request.user)
                return redirect('events:events_list')
    return redirect('events:events_list')


def events_list(request):
    events = Event.objects.all().order_by('-datetime')
    return render(request, 'events/events_list.html', {'events': events})


@login_required
def my_events(request):
    user = request.user
    events = user.enrolled_events.all().order_by('-datetime')
    return render(request, 'events/my_events.html', {'events': events})
