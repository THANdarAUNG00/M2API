from .imports import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AttributeList(request):
    try:
        attribute = Attribute.objects.all() #change attribute / Attribute change model
        paginator = AttributePagination()
        page_obj = paginator.paginate_queryset(attribute, request)
        seri = AttributeSerializer(page_obj, many=True) # change AttributeSerializer
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":f"{e}"}, status=500)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AttributeCreate(request):
    seri = AttributeSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def AttributeUpdate(request, pk):
    try:
        task = Attribute.objects.get(pk=pk)
    except Exception:
        return Response({"error":"Attribute not found!"}, status=204)
    seri = AttributeSerializer(task, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AttributeDetail(request, pk):
    try:
        task = Attribute.objects.get(pk=pk)
        seri = AttributeSerializer(task)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"error":"Product not found!"}, status=204)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def AttributeDelete(request, pk):
    try:
        task = Attribute.objects.get(pk=pk)
    except Exception:
        return Response({"error":"Attribute not found!"}, status=204)
    task.delete()
    return Response({"message":"Delete Successfully"},status=200)