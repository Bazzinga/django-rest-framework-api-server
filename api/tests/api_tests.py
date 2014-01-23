from django_webtest import WebTest
from django.contrib.auth.models import User


class APIGetApiKey(WebTest):

    def testLoginAnGetUsers(self):
        User.objects.create_user("prairiedogg", **{"password": "my_$pecial_password"})

        username_and_password = {"username": "prairiedogg",
                                 "password": "my_$pecial_password"}
        login_response = self.app.post_json('/api/auth/token/',
                                            username_and_password,
                                            status=200)
        token = login_response.json_body['token']

        headers = {'Authorization': str('Token %s' % token)}

        users_response = self.app.get('/api/users/',
                                      headers=headers,
                                      status=200)
        number_of_users = len(users_response.json)
        first_user = users_response.json[0]

        self.assertEqual(first_user["username"], "prairiedogg")
