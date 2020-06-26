from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView, ListView

from .form import OrderForm
from .models import Order


class OrdreDetailView(DetailView):
    # model = Order.objects.filter(status='active').first()

    def get(self, request, **kwargs):
        sq = request.GET.get('status')
        if sq:
            order = Order.objects.filter(status='active').first()
            # list(Order.objects.all())
        else:
            order = Order.objects.all()

        context_data = {
            'order': order.status,
        }
        return render(request, 'filter.html', context=context_data)


class IndexView(ListView):
    model = Order
    template_name = 'index.html'
    context_object_name = 'orders'

    def get_queryset(self):
        pk = Order.objects.get(pk=1)
        # pk.id =
        return pk
        '''Order.objects.all()[:1]'''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'Order by status'
        return context


@login_required
def create_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Your order has been create successfully!')
            return redirect('create_order')
    else:
        form = OrderForm()
    return render(request, 'form_template.html', {'form': form})
