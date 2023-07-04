from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Menu, Attracs, MultipleImage
from .forms import PostForm, MenuForm, KidsForm
from django.shortcuts import redirect
from django.contrib import messages



def base(request):
    return render(request, 'news/main.html')

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'news/post_list.html', {'posts': posts})

def menu_detail(request):
    menu = Menu.objects.all()
    return render(request, 'news/menu.html', {'menu': menu})
def kids_detail(request):
    menu=Attracs.objects.all()
    return render(request, 'news/kids.html', {'menu': menu})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    images = MultipleImage.objects.filter(postid = pk)
    return render(request, 'news/post_detail.html', {'post': post, 'images': images})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'news/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'news/post_edit.html', {'form': form})
def menu_new(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('menu_detail')
    else:
        form = MenuForm()
    return render(request, 'news/menu_edit.html', {'form': form})
def menu_edit(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('menu_detail')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'news/menu_edit.html', {'form': form})


def menu_delete(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    context = {'menu': menu}
    if request.method == 'GET':
        return render(request, 'news/menu_confirm_delete.html', context)
    elif request.method == 'POST':
        menu.delete()
        messages.success(request, 'The post has been deleted successfully.')
        return redirect('menu_detail')

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    images = MultipleImage.objects.filter(postid = pk)
    context = {'post': post}
    if request.method == 'GET':
        return render(request, 'news/post_confirm_delete.html', context)
    elif request.method == 'POST':
        post.delete()
        images.delete()
        messages.success(request, 'The post has been deleted successfully.')
        return redirect('post_list')
def kids_new(request):
    if request.method == "POST":
        form = KidsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('kids_detail')
    else:
        form = KidsForm()
    return render(request, 'news/kids_edit.html', {'form': form})
def kids_edit(request, pk):
    menu = get_object_or_404(Attracs, pk=pk)
    if request.method == "POST":
        form = KidsForm(request.POST,request.FILES, instance=menu)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('kids_detail')
    else:
        form = KidsForm(instance=menu)
    return render(request, 'news/kids_edit.html', {'form': form})


def kids_delete(request, pk):
    menu = get_object_or_404(Attracs, pk=pk)
    context = {'menu': menu}
    if request.method == 'GET':
        return render(request, 'news/kids_confirm_delete.html', context)
    elif request.method == 'POST':
        menu.delete()
        messages.success(request, 'The post has been deleted successfully.')
        return redirect('kids_detail')

def upload(request,pk):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            MultipleImage.objects.create(images=image, postid = pk)
        return redirect('post_detail', pk=pk)
    images = MultipleImage.objects.all()
    return render(request, 'news/post_add_photo.html', {'images': images})




