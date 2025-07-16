from .imports import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def CategoryList(request):
    try:
        category = Category.objects.all() #change category / Category change model
        paginator = CategoryPagination()
        page_obj = paginator.paginate_queryset(category, request)
        seri = CategorySerializer(page_obj, many=True) # change CategorySerializer
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":f"{e}"}, status=500)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CategoryCreate(request):
    seri = CategorySerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def CategoryUpdate(request, pk):
    try:
        task = Category.objects.get(pk=pk)
    except Exception:
        return Response({"error":"Category not found!"}, status=204)
    seri = CategorySerializer(task, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def CategoryDetail(request, pk):
    try:
        task = Category.objects.get(pk=pk)
        seri = CategorySerializer(task)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"error":"Category not found!"}, status=204)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def CategoryDelete(request, pk):
    try:
        task = Category.objects.get(pk=pk)
    except Exception:
        return Response({"error":"Category not found!"}, status=204)
    task.delete()
    return Response({"message":"Delete Successfully"},status=200)