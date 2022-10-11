from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment, Alumni, Wall
# Create your views here.
all_alumni = Alumni()

def index_view(request):
    if request.method == 'POST':
        mail = request.POST['email']
        note = request.POST['note']
        if len(mail) > 1 and len(note) > 1:
            all_alumni.number += 1
            all_alumni.save();
    return render(request,'index.html')

def alumni_view(request):
    return HttpResponse(all_alumni.number)

def json_view(request):
    return HttpResponse('omor e choke')

def comments(request):
    if request.method == 'POST':
        author = request.POST['name']
        text = request.POST['comments']
        if(len(author) > 1 and len(text) > 1):
            user_comment = Comment(author=author,text=text)
            user_comment.save();
    comments_dem = Comment.objects.all()
    return render(request,'comments/comments.html',context={
        'comments':comments_dem
    })

fonts_array = [
  "serif",
  "sans-serif",
  "monospace",
  "cursive",
  "fantasy",
  "system-ui",
  "Times New Roman",
  "Courier New",
  "Lucida Sans",
  "Almendra SC,serif",
  "Amatic SC,cursive",
  "Arbutus,cursive",
  "Bangers,cursive",
  "Caesar Dressing,cursive",
  "Comforter Brush,cursive",
  "Cormorant SC,serif",
  "DynaPuff,cursive",
  "Exo,sans-serif",
  "Hanalei Fill,cursive",
  "Josefin Sans,sans-serif",
  "Lato,sans-serif",
  "Limelight,cursive",
  "Marvel,sans-serif",
  "Open Sans,sans-serif",
  "Podkova,serif",
  "Poppins,sans-serif",
  "Rubik Moonrocks,cursive",
  "Shadows Into Light,cursive",
  "Share,cursive",
  "Yanone Kaffeesatz,sans-serif",
]
def cswall(request):
    if request.method == 'POST':
        username = request.POST['name']
        font = request.POST['font']
        grid = request.POST['gridnumber']
        social_link = request.POST['link']
        if font in fonts_array:
            user_obj = {
                'name':username,
                'font':font,
                'grid':grid,
                'link':social_link
            }
            json_user = Wall(user_stuff = user_obj)
            json_user.save();
    return render(request,'cswall/cswall.html')

def gallery(request):
    return render(request,'fangallery/fangallery.html')