class AuthManager:
    def authenticate(self, username):
        return {"user": username, "status": "authenticated"}

    def authorize(self, role):
        return role in ["admin", "user"]
