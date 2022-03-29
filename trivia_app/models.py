from django.db import models
from django.contrib.auth.models import User


class Stats(models.Model):
    user_ref = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    questions_attempted = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    cat9_attempted = models.IntegerField(default=0)
    cat9_correct = models.IntegerField(default=0)
    cat10_attempted = models.IntegerField(default=0)
    cat10_correct = models.IntegerField(default=0)
    cat11_attempted = models.IntegerField(default=0)
    cat11_correct = models.IntegerField(default=0)
    cat12_attempted = models.IntegerField(default=0)
    cat12_correct = models.IntegerField(default=0)
    cat14_attempted = models.IntegerField(default=0)
    cat14_correct = models.IntegerField(default=0)
    cat15_attempted = models.IntegerField(default=0)
    cat15_correct = models.IntegerField(default=0)
    cat17_attempted = models.IntegerField(default=0)
    cat17_correct = models.IntegerField(default=0)
    cat21_attempted = models.IntegerField(default=0)
    cat21_correct = models.IntegerField(default=0)
    cat22_attempted = models.IntegerField(default=0)
    cat22_correct = models.IntegerField(default=0)
    cat23_attempted = models.IntegerField(default=0)
    cat23_correct = models.IntegerField(default=0)

    def update(self, data):
        questions_attempted = data['questions_attempted']
        correct_answers = data['correct_answers']
        cat = data['category']
        self.questions_attempted += questions_attempted
        self.correct_answers += correct_answers
        if cat == 9:
            self.cat9_attempted += questions_attempted
            self.cat9_correct += correct_answers
        elif cat == 10:
            self.cat10_attempted += questions_attempted
            self.cat10_correct += correct_answers
        elif cat == 11:
            self.cat11_attempted += questions_attempted
            self.cat11_correct += correct_answers
        elif cat == 12:
            self.cat12_attempted += questions_attempted
            self.cat12_correct += correct_answers
        elif cat == 14:
            self.cat14_attempted += questions_attempted
            self.cat14_correct += correct_answers
        elif cat == 15:
            self.cat15_attempted += questions_attempted
            self.cat15_correct += correct_answers
        elif cat == 17:
            self.cat17_attempted += questions_attempted
            self.cat17_correct += correct_answers
        elif cat == 21:
            self.cat21_attempted += questions_attempted
            self.cat21_correct += correct_answers
        elif cat == 22:
            self.cat22_attempted += questions_attempted
            self.cat22_correct += correct_answers
        elif cat == 23:
            self.cat23_attempted += questions_attempted
            self.cat23_correct += correct_answers
        

    def percent_correct(self, category):
        if category == 0:
            if self.questions_attempted == 0:
                return 0
            else:
                return self.correct_answers / self.questions_attempted
        elif category == 9:
            if self.cat9_attempted == 0:
                return 0
            else:
                return self.cat9_correct / self.cat9_attempted
        elif category == 10:
            if self.cat10_attempted == 0:
                return 0
            else:
                return self.cat10_correct / self.cat10_attempted
        elif category == 11:
            if self.cat11_attempted == 0:
                return 0
            else:
                return self.cat11_correct / self.cat11_attempted
        elif category == 12:
            if self.cat12_attempted == 0:
                return 0
            else:
                return self.cat12_correct / self.cat12_attempted
        elif category == 14:
            if self.cat14_attempted == 0:
                return 0
            else:
                return self.cat14_correct / self.cat14_attempted
        elif category == 15:
            if self.cat15_attempted == 0:
                return 0
            else:
                return self.cat15_correct / self.cat15_attempted
        elif category == 17:
            if self.cat17_attempted == 0:
                return 0
            else:
                return self.cat17_correct / self.cat17_attempted
        elif category == 21:
            if self.cat21_attempted == 0:
                return 0
            else:
                return self.cat21_correct / self.cat21_attempted
        elif category == 22:
            if self.cat22_attempted == 0:
                return 0
            else:
                return self.cat22_correct / self.cat22_attempted
        elif category == 23:
            if self.cat23_attempted == 0:
                return 0
            else:
                return self.cat23_correct / self.cat23_attempted


    def __str__(self):
        return (self.user_ref.username + " stats")


    def __repr__(self):
        return (str(self.user_ref) + " " +  str(self.questions_attempted) + " " +str(self.correct_answers))
