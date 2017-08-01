from household_dashboard.view_mixins import HouseholdViewMixin as BaseHouseholdViewMixin
from plot.utils import get_anonymous_plot


class HouseholdViewMixin(BaseHouseholdViewMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plot = get_anonymous_plot()
        household = plot.household_set.all().last()
        try:
            context['household_identifier'] = household.household_identifier
        except AttributeError:
            context['household_identifier'] = None
        return context
