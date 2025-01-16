from django.db import models


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        "customuser.CustomUser", on_delete=models.CASCADE, related_name="comments"
    )
    team = models.ForeignKey("teams.Team", on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
