from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


import json
# Create your views here.
from .models import Product

class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=None):

        response = {'status':'List Empty','products':[]}

        if id:
            print(id)
            product = Product.objects.filter(id=id).first()
            if product:
                response = {'status':'Success','product':model_to_dict(product)}

        else:
            products = list(Product.objects.values())
            if len(products)>0:
                response = {'status':'Success','products':products}

        return JsonResponse(response)
        
    def post(self,request):
        data = json.loads(request.body)
        new_product = Product.objects.create(**data)
        new_product_data = model_to_dict(new_product)
        return JsonResponse({'new_product':new_product_data},status=200)
        
    def put(self,request,id):
        data = json.loads(request.body)
        print(data)
        response = {'status':'Product Not Found'}
        product = Product.objects.filter(id=id).first()
        if product:
            for attr, value in data.items():
                setattr(product, attr, value)
            product.save()
            response = {'status':'Success'}

        return JsonResponse(response)
    
    def delete(self,request,id):
        response = {'status':'Not Found'}
        product = Product.objects.filter(id=id).first()
        if product:
            product.delete()
            response = {'status':'Deleted'}

        return JsonResponse(response)