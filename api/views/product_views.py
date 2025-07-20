from .imports import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ProductList(request):
    try:
        product = Product.objects.all() #change product / Product change model
        paginator = ProductPagination()
        page_obj = paginator.paginate_queryset(product, request)
        seri = ProductSerializer(page_obj, many=True) # change ProductSerializer
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":f"{e}"}, status=500)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ProductCreate(request):
    seri = ProductSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def ProductUpdate(request, pk):
    try:
        task = Product.objects.get(pk=pk)
    except Exception:
        return Response({"error":"Product not found!"}, status=204)
    seri = ProductSerializer(task, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ProductDetail(request, pk):
    try:
        task = Product.objects.get(pk=pk)
        seri = ProductSerializer(task)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"error":"Product not found!"}, status=204)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def ProductDelete(request, pk):
    try:
        task = Product.objects.get(pk=pk)
    except Exception:
        return Response({"error":"Product not found!"}, status=204)
    task.delete()
    return Response({"message":"Delete Successfully"},status=200)