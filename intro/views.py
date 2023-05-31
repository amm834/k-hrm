from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'intro/home.html'
home = HomeView.as_view()

class FeaturesView(TemplateView):
    template_name = 'intro/features.html'
features = FeaturesView.as_view()

class PricingView(TemplateView):
    template_name = 'intro/pricing.html'
pricing = PricingView.as_view()

class AboutView(TemplateView):
    template_name = 'intro/about.html'
about = AboutView.as_view()
    
class ContactView(TemplateView):
    template_name = 'intro/contact.html'
contact = ContactView.as_view()