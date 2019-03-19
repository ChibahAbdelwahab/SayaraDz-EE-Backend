from rest_auth.views import LoginView
from django.contrib.auth.models import User


# Edit default rest auth response for the authentification
class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"admin": self.user.is_staff, 'firstName': self.user.first_name, 'lastName': self.user.last_name,
                  "email": self.user.last_name}
        orginal_response.data.update(mydata)
        return orginal_response
