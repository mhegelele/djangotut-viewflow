from material.frontend import views

from . import models


class QuestionViewSet(views.ModelViewSet):
    model = models.Question
