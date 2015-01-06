from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Resolution

import random


class ResolutionView(TemplateView):

    def get(self, request, **kwargs):

        """ Show all resolutions received
        """

        template = 'resolutions.html'

        resolutions_count = Resolution.objects.count()
        resolution_id = random.randint(1, resolutions_count)

        try:
            resolution = Resolution.objects.get(id=resolution_id)
        except Exception:
            resolution = "Failed to load resolution."

        context = {
            'resolution': resolution,
            'resolutions_count': resolutions_count,
            'resolution_id': resolution_id,
        }

        return render(request, template, context)

    def post(self, request, **kwargs):

        """ Used by the Twilio API to receive a text message and save a resolution.
        """

        resolution = request.POST.get('Body')

        if resolution:
            new_resolution = Resolution(text=resolution)
            new_resolution.save()

        template = 'response.html'
        context = {}
        return render(request, template, context)
