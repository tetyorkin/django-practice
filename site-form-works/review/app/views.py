from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    if 'reviewed_products' not in request.session:
        request.session['reviewed_products'] = []
    reviews = (
        Review.objects.all().filter(product=Product.objects.get(id=product.id))
    )
    form = ReviewForm
    if request.method == 'POST':
        request.session['reviewed_products'].append(product.id)
        request.session.save()
        text = request.POST['text']
        review = Review(text=text, product=Product.objects.get(id=product.id))
        review.save()

    if product.id not in request.session['reviewed_products']:
        context = {
            'form': form,
            'product': product,
            'reviews': reviews
        }
        return render(request, template, context)

    context = {
        'product': product,
        'is_review_exist': True,
        'reviews': reviews
    }

    return render(request, template, context)
