from django.shortcuts import redirect, render
from .forms import ContactUsForm, MassageForm
from .models import Massage, OurInformation


def contact(request):
    if request.method == 'POST':
        form = MassageForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            email = form.cleaned_data["email"]
            Massage.objects.create(title=title, text=text, email=email)
            return redirect("contact_app:contact")
    else:
        form = MassageForm()
    info = OurInformation.objects.get(id=1)
    return render(request, "contact/contact.html", {'form': form, 'info': info})
