from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from . models import Video
from . forms import VideoUploadForm


class VideoCreateView(CreateView):
    model = Video
    success_url = "/"
    template_name = 'video/video_create.html'
    fields = ['title', 'creator', 'description', 'category', 'video']


class VideoListView(ListView):
    model = Video
    template_name = 'video/video_list.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']


def search(request):
    if request.method == "POST":
        query = request.POST.get('title', None)
        if query:
            results = Video.objects.filter(title__contains=query)
            return render(request, 'video/search.html', {'videos': results})

    return render(request, 'video/search.html')


def video_update(request, pk):
    obj = get_object_or_404(Video, pk=pk)
    form = VideoUploadForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'video/video_update.html', context)


class VideoDeleteView(DeleteView):
    template_name = "video/video_delete.html"
    success_url = "/"
    model = Video


class VideoDetailView(DetailView):
    template_name = "video/video_detail.html"
    model = Video
