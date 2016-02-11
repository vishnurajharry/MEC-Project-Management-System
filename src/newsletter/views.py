from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from .forms import SignUpForm , UserForm, sellerProfileForm,loginForm,NotificationForm,memberProfileForm,MyForm,DocumentForm
from .models import sellerprofile,notifications,student_details,Document
from django_tables2   import RequestConfig
from django.forms import formset_factory
from .tables  import PersonTable,NotifTable,sellerTable
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.
def home(request):
    title = "welcome u"
    form = SignUpForm(request.POST or None)
    context = {'title':title,
               'form':form
    }
    table = sellerTable(sellerprofile.objects.all())
    RequestConfig(request,paginate={"per_page": 25}).configure(table)
    return render(request,"home.html",{'table': table})

memberFormSet = formset_factory(memberProfileForm, extra=2)	
# request.GET or None
def contact(request):
    registered = False
    title = 'welcome'
    user_form = UserForm(request.POST or None)
    profile_form = sellerProfileForm(request.POST or None)
    member_form = memberFormSet(request.POST or None)
    context = {
      'userform':user_form,
      'profileform':profile_form,
      'memberform':member_form,
      'title':title
      }

    if user_form.is_valid() and profile_form.is_valid() and member_form.is_valid():
        user = user_form.save()
        user.set_password(user.password)
        user.save()
        profile=profile_form.save(commit=False)
        profile.seller = user
        profile.save()
        for form in member_form:
              member = form.save(commit=False)
              member.group =  profile
              member.save()
        context = {'title' : "Your Response Has Been Recorded"}
    return render(request,"contact.html",context)


def search(request):
    table = PersonTable(project.objects.all())
    RequestConfig(request,paginate={"per_page": 25}).configure(table)
    return render(request, "search.html", {'table': table})

def myview(request):
    if request.method == 'POST':
    	print request.POST.get('extra_field_count')
        form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            print "valid!"
    else:
        form = MyForm()
    return render(request, "test1.html", { 'form': form })



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
                #print {{ser.username}}
                
                if user.is_superuser:
                    return HttpResponseRedirect('/login/admin/'+usern+'/')
                return HttpResponseRedirect('/login/'+usern+'/')    
                user=User.objects.get(username=usern)
                table= NotifTable(notifications.objects.filter(idno=user.sellerprofile.id))
                RequestConfig(request,paginate={"per_page": 25}).configure(table)
                table1= NotifTable(notifications.objects.filter(category='public'))
                RequestConfig(request,paginate={"per_page": 25}).configure(table)
                return render(request, "loggedin.html", {'table': table,'table1':table1})

        		#print sellerprofile.seller.Username
        		#print s.id
        		#return render(request, "loggedin.html", {})
            else:
        	    context = {'title':'Account is currently disabled'}

        else:
            context = {'title':'Username and Password mismatch'}

    return render(request,"login.html",context)


def loggout(request):
	logout(request)
	context = {'title':'logging you out'}
	return HttpResponseRedirect('/')

def notify(request,num):
    
    details=[]
    # table= PersonTable(sellerprofile.objects.filter(id=num))
    # RequestConfig(request,paginate={"per_page": 25}).configure(table)
    form = NotificationForm(request.POST or None)
    
    p=sellerprofile.objects.get(id = num)
    d = Document.objects.filter(gpno = num)
    try:
     s = student_details.objects.filter(group=p)
     for sh in s:     
     	l=[]
        l.extend([sh.name,sh.rollno,sh.email])	
        details.append(l)
        print details
    except student_details.DoesNotExist:
     s = None
    context={
        'form':form,
        'details':details,
        'documents':d
    }
    # s=student_details.objects.get(group=p)
    # print s.group
    if form.is_valid():
    	# s=sellerprofile.objects.filter(id=num)
    	# print s
    	instance = form.save(commit=False)
    	instance.idno = num
    	instance.save()
    return render(request, "notify.html", context)

def userpage(request,username):
    user=User.objects.get(username=username)
    table= NotifTable(notifications.objects.filter(idno=user.sellerprofile.id))
    RequestConfig(request,paginate={"per_page": 25}).configure(table)
    table1= NotifTable(notifications.objects.filter(category='public'))
    RequestConfig(request,paginate={"per_page": 25}).configure(table)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            user=User.objects.get(username=username)
            print user.sellerprofile.id
            print 'hellloooo'
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.gpno = user.sellerprofile.id
            newdoc.save()
            
            
            # Redirect to the document list after POST
            # return HttpResponseRedirect(reverse('newsletter.views.userpage'))
    else:
        form = DocumentForm() # A empty, unbound form
    documents = Document.objects.filter(gpno=user.sellerprofile.id)
    print documents
    return render(request, "loggedin.html", {'table': table,'table1':table1,'form':form,'documents':documents})

def adminpage(request,username):
    user=User.objects.get(username=username)
    batch = user.adminregister.Managing_class
    p_type = user.adminregister.project_type
    print batch
    print p_type 
    
    # try:
    #  s = sellerprofile.objects.get(batch = batch)
    # except sellerprofile.DoesNotExist:
    #  s = None 
    table = PersonTable(sellerprofile.objects.filter(Q(batch = batch)&Q(ptype = p_type)))
    RequestConfig(request,paginate={"per_page": 25}).configure(table)
    notform = NotificationForm(request.POST or None)
    if notform.is_valid():
        print 'hai'
        instance = notform.save(commit=False)
        instance.category='public'
        instance.save()
        return render(request, "loggedin.html", {'table': table,'form':notform})

    return render(request, "loggedin.html", {'table': table,'form':notform})
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
	
