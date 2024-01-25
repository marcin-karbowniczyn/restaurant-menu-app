from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


# To retrieve objects from your database, construct a QuerySet via a Manager on your model class.
# A QuerySet represents a collection of objects from your database. It can have zero, one or many filters.
# Filters narrow down the query results based on the given parameters. In SQL terms, a QuerySet equates to a SELECT statement, and a filter is a limiting clause such as WHERE or LIMIT.
# You get a QuerySet by using your model’s Manager. Each model has at least one Manager, and it’s called objects by default.


class MenuListView(generic.ListView):
    # queryset wil store the list of data to display. We are basically querying the data from database table
    queryset = Item.objects.order_by("date_created")
    template_name = 'index.html'

    # AFAIU context are variables we want to display on the view, like render(req, template, dict_context)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meal_types'] = MEAL_TYPE
        return context

    # def get_context_data(self, *, object_list=queryset, **kwargs):
    #     context = dict()
    #     context['meal_types'] = MEAL_TYPE
    #     context['item_list'] = object_list
    #     return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'
