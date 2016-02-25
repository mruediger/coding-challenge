from django.shortcuts import render
from django.http import HttpResponse

class MockDB(object):

    OK = 1
    USER_UNKNOWN = 2
    PASS_UNKNOWN = 3
    TOKEN_UNKNOWN = 4


    def __init__(self):
        self.users = {
            "testuser" : "password"
        }

        self.2factors = {
            "testuser" : "code"
        }
        self.tokens = set()

    def generateToken(self):
        pass

    def matches(self, user, password, 2factor=None):
        if user in self.users:
            if 2factor:
                if 2factor != 2factors[user]:
                    return (None, TOKEN_UNKNOWN)

            if password == self.users[user]:
                token = generateToken()
                self.tokens.add(token)
                return (token, OK)
            else:
                return (None, PASS_UNKNOWN)
        else:
            return (None, USER_UNKNOWN)

    def deleteToken(self, token):
        self.tokens.remove(token)


    def validateToken(self, token):
        if token in self.tokens:
            return status



userdb = MockDB()

def index(request):
    return HttpResponse("Hello World. Hello Dubsmash!")


def login_with_token(request):
    user = request.getParam(user)
    password = request.getParam(password)
    token,status = userdb.matches(user,password)

    if status == MockDB.OK:
        return JsonResponse({"token": token})

    if status == MockDB.USER_UNKNONW:
        return JsonResponse(status=401)

    if status == MockDB.PASS_UNKNOWN:
        return JsonResponse({"msg":"wrong password"}, status=401)

    return JsonResponse(status=500)

def lo

def logout(request):
    status = userdb.deleteToken(request.getParam(token))
    if status == MockDB.OK:
        return JsonResponse(status=200)

    return JsonResponse(status=500)


def validate(request):
    status = userdb.validateToken(request.getParam(token))
    if status == MockDB....
