from django.shortcuts import render, redirect
from .models import Post, PostImage
from .forms import PostForm, ImageForm
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.urls import reverse_lazy, reverse
from django.forms import modelformset_factory
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy


# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'sdgs/post_list.html'
    ordering = ['-created_at']
    context_object_name = 'posts'
    paginate_by = 6


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'posts'


@login_required
def post(request):
    ImageFormSet = modelformset_factory(PostImage, fields=('modelimage',), labels={'modelimage': 'Image'}, extra=3, min_num=1)
    if request.method == 'POST':

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.author = request.user
            post_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['modelimage']
                    photo = PostImage(post=post_form, modelimage=image)
                    photo.save()
            messages.success(request, "Post Created!")
            return redirect('sdgs:post_detail', pk=post_form.pk)
        else:
            messages.info(request, 'Please attach atleast one photo starting with the first photo box')

    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=PostImage.objects.none())
    return render(request, 'sdgs/post_create.html', {'postForm': postForm, 'formset': formset})



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['text']
    template_name = 'sdgs/post_update.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={
            'pk': self.object.pk, })

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('sdgs:post_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
