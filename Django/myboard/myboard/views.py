from django.shortcuts import redirect, render
from django.utils import timezone
from django.core.paginator import Paginator                                 # 페이지 번호
from django.contrib.auth.hashers import make_password, check_password       # 암호화(해시테이블), 비밀번호 확인
from .models import MyBoard, MyMember

def index(request):
    myboard = MyBoard.objects.all().order_by('-id')         # 내림차순
    paginator = Paginator(myboard, 5)
    page_num = request.GET.get('page', 1)                   # value값이 없으면 default 1

    # 페이지에 맞는 모델 가져오기
    page_obj = paginator.get_page(page_num)

    # 관련 메서드
    print(type(page_obj))
    print(page_obj.count)
    print(page_obj.paginator.num_pages)
    print(page_obj.paginator.page_range)
    print(page_obj.has_next())
    print(page_obj.has_previous())
    try:
        print(page_obj.next_page_number())
        print(page_obj.previous_page_number())
    except:
        pass
    print(page_obj.start_index())
    print(page_obj.end_index())
    return render(request, 'index.html', {'list': page_obj})

def insert_form(request):
    return render(request, 'insert.html')

def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

    if result:
        return redirect('index')
    else:
        return redirect('insertform')

def detail(request):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})

def update_form(request):
    return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})

def update_res(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)
    result_title=myboard.update(mytitle=mytitle)
    result_content=myboard.update(mycontent=mycontent)

    if result_title + result_content ==2:
        return redirect('detail/' +id)
    else:
        return redirect('updateform/'+id)

def delete(request, id):
    result_delete=MyBoard.objects.filter(id=id).delete()
    if result_delete[0]:
        return redirect('index')
    else:
        return redirect('/detail/' +id) 

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        myname = request.POST['myname']
        mypw = request.POST['mypw']
        myemail = request.POST['myemail']
        mymember = MyMember(myname=myname, mypw=make_password(mypw), myemail=myemail)
        mymember.save()

        return redirect('/')
    return redirect('/')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        myname = request.POST['myname']
        mypw = request.POST['mypw']
        mymember = MyMember.objects.get(myname=myname)
        if check_password(mypw, mymember.mypw):                 # 암호화한 값이 전달된 값과 같은지
            request.session['myname'] = mymember.myname
            return redirect('/')
        else:
            return redirect('/login')

def logout(request):
    del request.session['myname']
    return redirect('/')