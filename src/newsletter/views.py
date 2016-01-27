from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import SignUpForm , UserForm, sellerProfileForm,loginForm,NotificationForm
from .models import sellerprofile,notifications
from django_tables2   import RequestConfig
from .tables  import PersonTable,NotifTable
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    title = "welcome u"
    form = SignUpForm(request.POST or None)
    context = {'title':title,
               'form':form
    }
    if form.is_valid():
        form.save()
        context = {'title' : "Your Response Has Been Recorded"}
    return render(request,"home.html",context)
	
# request.GET or None
def contact(request):
    registered = False
    title = 'welcome'
    user_form = UserForm(request.POST or None)
    profile_form = sellerProfileForm(request.POST or None)
    context = {
      'userform':user_form,
      'profileform':profile_form,
      'title':title
      }
    
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save()
        user.set_password(user.password)
        user.save()
        profile=profile_form.save(commit=False)
        profile.seller = user
        profile.save()
        context = {'title' : "Your Response Has Been Recorded"}
    return render(request,"contact.html",context)


def search(request):
    table = PersonTable(project.objects.all())
    RequestConfig(request,paginate={"per_page": 25}).configure(table)
    return render(request, "search.html", {'table': table})



def sellerlogin(request):
    login_form = loginForm(request.POST or None)
    title='Login'
    context = {
     'form':login_form,
     'title':title
    }
    if login_form.is_valid():
        usern = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(username=usern, password=password)
        if user is not None:
        	if user.is_active:
        		login(request, user)
        		if user.is_superuser:
        			table= PersonTable(sellerprofile.objects.all())
        			RequestConfig(request,paginate={"per_page": 25}).configure(table)
        			return render(request, "loggedin.html", {'table': table})
        		user=User.objects.get(username=usern)
        		table= NotifTable(notifications.objects.filter(idno=user.sellerprofile.id))
        		RequestConfig(request,paginate={"per_page": 25}).configure(table)
        		return render(request, "loggedin.html", {'table': table})
        		#print sellerprofile.seller.Username
        		# print s.id
        		#return render(request, "loggedin.html", {})
        	else:
        		context = {'title':'Account is currently disabled'}

        else:
        	context = {'title':'Username and Password mismatch'}

    return render(request,"login.html",context)


def logout(request):
	logout(request)
	context = {'title':'logging you out'}
	return render(request,"logout.html",context)

def notify(request,num):
    # table= PersonTable(sellerprofile.objects.filter(id=num))
    # RequestConfig(request,paginate={"per_page": 25}).configure(table)
    form = NotificationForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
    	# s=sellerprofile.objects.filter(id=num)
    	# print s
    	instance = form.save(commit=False)
    	instance.idno = num
    	instance.save()
    return render(request, "notify.html", context)
# def test(request):
#     table= PersonTable(project.objects.filter(member_names='drone'))
#     RequestConfig(request,paginate={"per_page": 25}).configure(table)
#     return render(request, "test.html", {'table': table})

# def test(request):
# 	title = 'welcome'
# 	form = ContactForm(request.POST or None)
# 	context = {
# 	  'form':form,
# 	  'title':title
# 	}
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		print instance.member_names
# 		name=instance.member_names
# 		table= PersonTable(project.objects.filter(member_names=name))
# 		RequestConfig(request,paginate={"per_page": 25}).configure(table)
# 		context = {'table' : table}
# 	return render(request,"test.html",context)
	
