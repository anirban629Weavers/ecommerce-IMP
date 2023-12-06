from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email, phone, password=None, **kwargs):
        
        if not email:
            raise ValueError("Email is required")

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phone, password, **kwargs):
        user = self.create_user(
            email=self.normalize_email(email),
            phone=phone,
            password = password,
            **kwargs
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser= True
        user.save(using=self._db)
        return user

