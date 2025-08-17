from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=32, blank=True)

    company_name = models.CharField(max_length=160, blank=True)   # ← NEW
    designation  = models.CharField(max_length=120, blank=True)   # ← NEW

    country_code = models.CharField(max_length=8, blank=True) 

    business_type = models.CharField(max_length=80, blank=True)
    materials = models.JSONField(default=list, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"
 # __str__ is a special Python method (“dunder str”) that tells Django/Python how to display your object as a human-readable string.

# Without it, printing a Lead (e.g., in the admin or shell) shows something unhelpful like: Lead object (1).

# With it, you’ll see: Ankit Verma <ankit@example.com> — much nicer in the Django admin, logs, shell, and form dropdowns.

# It’s not stored in the database; it’s just for display.

