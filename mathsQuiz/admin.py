from django.contrib import admin
from mathsQuiz.models import Quiz, Question, CompletionLog
from django.contrib.admin.filters import DateFieldListFilter
from django.utils import timezone
from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _


admin.site.site_header = "Quiz Dashboard"
admin.site.site_title = "Quiz Dashboard"
admin.site.index_title = "Quiz Dashboard"

admin.site.register(Quiz)
admin.site.register(Question)

# Class extension to the default date filter to more relevant timescales for the quizzes

class dateCompleteFilter(DateFieldListFilter):

    def __init__(self, *args, **kwargs):
        super(dateCompleteFilter, self).__init__(*args, **kwargs)

        now = timezone.now()
        # When time zone support is enabled, convert "now" to the user's time
        # zone so Django's definition of "Today" matches what the user expects.
        if timezone.is_aware(now):
            now = timezone.localtime(now)

        today = now.date()

        self.links = ((
            (_('Any date'), {}),
            (_('Last Hour'),
            {
                self.lookup_kwarg_since: str(now - datetime.timedelta(hours=1)),
                self.lookup_kwarg_until: str(now)
            }),
            (_('Last Two Hours'),
            {
                self.lookup_kwarg_since: str(now - datetime.timedelta(hours=2)),
                self.lookup_kwarg_until: str(now)
            }),
            (_('Today'),
            {
                self.lookup_kwarg_since: str(today),
                self.lookup_kwarg_until: str(now)
            })
        ))

@admin.register(CompletionLog)
class CompletionLogAdmin(admin.ModelAdmin):
    list_display = ('quiz','dateComplete', 'name', 'score', 'timeTaken' )
    list_filter = ('quiz', ('dateComplete', dateCompleteFilter))
