from django.shortcuts import render, redirect
from .models import LinkInfo
import uuid
from django.contrib import messages
#from django.shortcuts import get_object_or_404

# comment = get_object_or_404(Comment, pk=comment_id)

# Create your views here.
def home(request):
	context ={}
	return render(request, 'home.html', context)



def add(request):
	if request.method == 'POST':
		link = request.POST.get('expand')
		link_id = str(uuid.uuid4())[:5]
		link_id = link_id
		url = LinkInfo.objects.filter(link=link)
		if not url :
			url = LinkInfo.objects.create(link=link, link_id=link_id)
			url.save()
		else :
			url = LinkInfo.objects.get(link=link)
			if url.link_id == None:
				url = LinkInfo.objects.get(link=url.link, link_id=link_id)
				url.save()
			else :
				messages.warning(request, 'This link has been entered!')
				url = LinkInfo.objects.get(link=link)
		context = {'url':url}
		return render(request, 'home.html', context)


def shorten(request,pk):
	link_id = LinkInfo.objects.get(link_id=pk)
	return redirect(link_id.link)
