from django.shortcuts import render,HttpResponse
from .models import Blog_Post,BlogComment

# Create your views here.
def Index(request):
    post = Blog_Post.objects.all()
    return render(request,'blog/blog.html',{'Posts':post})
def BlogPost(request,bid):
    p = Blog_Post.objects.filter(id=bid)
    
    try:
        p_n = Blog_Post.objects.filter(id__gte=bid).order_by('id')[1:2]
        next_p = p_n[0]
    except:
        next_p = p_n
    try:
        p_p = Blog_Post.objects.filter(id__lte=bid).order_by('id')[::-1][1:2]
        previous = p_p[0]
    except:     
        previous = p_p
    comment = BlogComment.objects.filter(post=p.first())[:10:-1]
    return render(request,'blog/blog-details.html',{'Post':p[0],'Next_Post':next_p,'Previous_Post':previous,'comments':comment})
def Blogcomment(request,bid):
    if request.is_ajax():
        comment = request.GET.get("comment",'')
        post = Blog_Post.objects.filter(id=bid).first()
        c = BlogComment(comment=comment,user=request.user,post=post)
        c.save()
        comments = BlogComment.objects.filter(post=post)
        import json
        send = json.dumps(product_load(comments))
        return HttpResponse(send)
def product_load(obj):
    item_list = []
    for comment in obj:
        item_list.append({'Username':str(comment.user),'comment':comment.comment,'timestamp':str(comment.timestamp.date())})
    return item_list