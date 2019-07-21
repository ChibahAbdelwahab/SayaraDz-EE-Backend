from rest_auth.views import LoginView
from django.contrib.auth.models import User


# Edit default rest auth response for the authentification
class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super(CustomLoginView).get_response()
        try:
            fabricant = self.user.profile.fabricant.nom
            marqueid = self.user.profile.fabricant.marque.id
            marque = self.user.profile.fabricant.marque.nom
            image = self.user.profile.fabricant.marque.image
        except:
            fabricant = ""
            marqueid = ""
            marque = ""

        mydata = {
            "admin": self.user.is_staff,
            'firstName': self.user.first_name,
            'lastName': self.user.last_name,
            "email": self.user.last_name,
            'fabricant': fabricant,
            "marqueid": marqueid,
            "marque": marque,
            'image': image

        }
        orginal_response.data.update(mydata)
        return orginal_response
