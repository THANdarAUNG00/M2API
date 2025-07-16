from .imports import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TagList(request):
    try:
        tag_qs = Tag.objects.all() #change tag / Tag change model
        paginator = TagPagination()
        page_obj = paginator.paginate_queryset(tag_qs, request)
        seri = TagSerializer(page_obj, many=True) # change TagSerializer
        return paginator.get_paginated_response(seri.data)
    except Exception as e:
        return Response({"error":f"{e}"}, status=500)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def TagCreate(request):
    seri = TagSerializer(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=201)
    else:
        print(seri.errors)
        return Response(seri.errors, status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def TagUpdate(request, pk):
    try:
        task = Tag.objects.get(pk=pk)
    except Exception:
        return Response({"error":"Tag not found!"}, status=204)
    seri = TagSerializer(task, data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data, status=200)
    else:
        return Response(seri.errors, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tagDetail(request, pk):
    try:
        task = Tag.objects.get(pk=pk)
        seri = TagSerializer(task)
        return Response(seri.data, status=200)
    except Exception:
        return Response({"error":"Tag not found!"}, status=204)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def TagDelete(request, pk):
    try:
        task = Tag.objects.get(pk=pk)
    except Exception:
        return Response({"error":"Tag not found!"}, status=204)
    task.delete()
    return Response({"message":"Delete Successfully"}, status=200)