

from django.shortcuts import redirect, render
from django.views import View


class About(View):

    def get(self, request,*args, **kwargs):
        
        return render(request, 'about.html')

    def post(self, request, *args, **kwargs):
        """
        users can contact admin direct with the form added to the about page
        """
        return redirect('/')