from django.shortcuts import render
from django.views import View
from apps.cars.models import Car
from apps.dealers.models import Dealer


class ListOfCarsViews(View):
    def get(self, request, **kwargs):
        dealer_id = request.GET.get('dealer_id')
        if dealer_id:
            list_cars = Car.objects.filter(DealerID=dealer_id)
            return render(request, 'list_car.html', {'list': list_cars})
        else:
            list_cars = Car.objects.all()
            return render(request, 'list_car.html', {'list': list_cars})


class CarInfo(View):
    def get(self, request, **kwargs):
        id = request.GET.get('id')
        if id is not None:
            list_cars = Car.objects.filter(carId=id)
            dil = Car.objects.get(carId=id)
            dealer_list = Dealer.objects.get(DealerId=dil.DealerID.pk)
            # 'dealer_info_car.html'
            return render(request, 'dealer_info_car.html', {'list': list_cars, 'dealer' : dealer_list})
        else:
            list_cars = Car.objects.all()
            return render(request, 'dealer_info_car.html', {'list': list_cars})
