from django.forms import ModelForm
from .models import QuesModel

class AddQuestionForm(ModelForm):
    class Meta:
        model = QuesModel
        fields = "__all__"
