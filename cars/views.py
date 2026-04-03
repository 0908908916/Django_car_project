from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Car, Brand, Inquiry
from .forms import InquiryForm, RegisterForm, LoginForm, CarSearchForm


def car_list(request):
    """車款列表 + 搜尋篩選"""
    cars = Car.objects.filter(is_available=True).select_related('brand')
    form = CarSearchForm(request.GET)

    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        fuel_type = form.cleaned_data.get('fuel_type')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if keyword:
            cars = cars.filter(
                Q(name__icontains=keyword) | Q(brand__name__icontains=keyword)
            )
        if fuel_type:
            cars = cars.filter(fuel_type=fuel_type)
        if min_price:
            cars = cars.filter(price__gte=min_price)
        if max_price:
            cars = cars.filter(price__lte=max_price)

    return render(request, 'cars/car_list.html', {'cars': cars, 'form': form})


def car_detail(request, pk):
    """車款詳細頁"""
    car = get_object_or_404(Car, pk=pk, is_available=True)
    related_cars = Car.objects.filter(
        brand=car.brand, is_available=True).exclude(pk=pk)[:3]
    return render(request, 'cars/car_detail.html', {'car': car, 'related_cars': related_cars})


def inquiry(request, pk):
    """詢價 / 預約表單"""
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry_obj = form.save(commit=False)
            inquiry_obj.car = car
            inquiry_obj.save()
            messages.success(request, '✅ 詢價資料已送出，我們將盡快與您聯絡！')
            return redirect('car_detail', pk=pk)
    else:
        form = InquiryForm()

    return render(request, 'cars/inquiry.html', {'car': car, 'form': form})


def register_view(request):
    """會員註冊"""
    if request.user.is_authenticated:
        return redirect('car_list')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'歡迎加入，{user.username}！')
            return redirect('car_list')
    else:
        form = RegisterForm()

    return render(request, 'cars/register.html', {'form': form})


def login_view(request):
    """會員登入"""
    if request.user.is_authenticated:
        return redirect('car_list')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'歡迎回來，{user.username}！')
            return redirect('car_list')
    else:
        form = LoginForm()

    return render(request, 'cars/login.html', {'form': form})


def logout_view(request):
    """登出"""
    logout(request)
    messages.info(request, '已成功登出。')
    return redirect('car_list')
