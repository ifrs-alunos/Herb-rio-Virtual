import json

import requests
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, TemplateView

from alerts.forms import AlertsForDiseasesForm
from whatsapp_messages.functions import (
    get_whatsapp_qr_code,
    get_whatsapp_status,
    send_whatsapp_message, set_webhook,
    start_whatsapp_session,
)
from whatsapp_messages.models.message_confirmation import (
    CODE_LENGTH,
    MessageConfirmation,
)
from whatsapp_messages.types import WhatsappEvent

headers = {"token": settings.WHATSAPP_TOKEN}


@csrf_exempt
def whatsapp_webhook(request):
    event_data = json.loads(request.POST.get("jsonData"))
    event = WhatsappEvent.from_dict(event_data)

    print(event)

    if event.type == "Message":
        number = event.sender.split(":")[0][2:]
        if len(event.conversation) == CODE_LENGTH:
            mc = MessageConfirmation.objects.get(
                code=event.conversation,
            )
            print(number)
            print(mc.phone_number)
            mc.verified = True
            mc.save()
            send_whatsapp_message(number, "Seu número foi vinculado com sucesso!")

    return HttpResponse("ok")


class WhatsappLogoutView(View):
    def get(self, request):
        requests.post(settings.WHATSAPP_API_URL + "/session/logout", headers=headers)
        return redirect("whatsapp_messages:connect")


# Criação de sessão por parte de um administrador, como se fosse conectar ao WhatsApp web
class WhatsappConnectionView(TemplateView):
    template_name = "whatsapp_messages/whatsapp_connection.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        status = get_whatsapp_status()

        context["status"] = status

        if status.Connected and status.LoggedIn:
            context["connected"] = True
            set_webhook(self.request)

        if not status.Connected:
            start_whatsapp_session()

        if not status.LoggedIn:
            qr = get_whatsapp_qr_code()
            context["qr_code"] = qr

        context["link"] = "whatsapp-connection"

        return context


class LinkUserWhatsappView(TemplateView):
    template_name = "whatsapp_messages/link.html"

    def get_context_data(self, **kwargs):
        profile = self.request.user.profile
        try:
            mc = MessageConfirmation.objects.get(profile=profile)
            if mc.has_expired() and not mc.verified:
                mc.delete()
                mc = MessageConfirmation(profile=profile)
                mc.save()
        except MessageConfirmation.DoesNotExist:
            mc = MessageConfirmation(profile=profile)
            mc.save()

        context = super().get_context_data(**kwargs)
        context["message_confirmation"] = mc
        context["bot_whatsapp_number"] = settings.WHATSAPP_NUMBER
        context["link"] = "link-whatsapp"

        form = AlertsForDiseasesForm(profile=profile)
        context["form"] = form

        return context


class AlertsForDiseasesView(View):
    form_class = AlertsForDiseasesForm

    def post(self, request):
        profile = request.user.profile
        form = self.form_class(request.POST, profile=profile)

        if form.is_valid():
            profile.alerts_for_diseases.set(form.cleaned_data["alerts_for_diseases"])
            profile.save()

        return redirect("whatsapp_messages:link")
