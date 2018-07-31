from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import author,category,post # মডেল  থেকে  সকল  ফিল্ড  ইম্পোর্ট করে নিতে হবে
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    post1 = post.objects.all() #  পোষ্ট মডেলের সমস্ত অবজেক্ট নিয়ে এসে post1 ভেরিয়েবলে রাখবে
    context = {
        'post1':post1       #  কন্টেক্সট ভেরিয়েবলে সেগুলো ষ্টোর করা
    }
    return render(request,'index.html', context) #  কনটেক্সট ভেরিয়েবলটি ট্যামপ্লেটে পাঠানো

def getAuthor(request, name):
    p_author = get_object_or_404(User, username=name)
    auth = get_object_or_404(author, name=p_author.id)
    post1 = post.objects.filter(post_author=auth.id)
    context = {
        'auth':auth,
        'post1':post1
    }
    return render(request,'author.html', context) #

def PostDetail(request, id):
    post1 = get_object_or_404(post, pk=id)      #   প্রাইমারি কী অনুসারে পোষ্ট মডেল থেকে আইডি অনুসারে পোষ্ট দেখানোর কুয়েরী চালনা
    first = post.objects.first()                # পোষ্ট মডেলের প্রথম পোষ্টটি দেখানোর  কুয়েরী
    last = post.objects.last()                  # পোষ্ট মডেলের  সর্বশেষ পোষ্টটি দেখানোর  কুয়েরী
    related = post.objects.filter(post_category=post1.post_category).exclude(id=id)[:4]  # আমাদের পোষ্টের রিলেটেড পোষ্ট গুলো দেখানোর  জন্য এই ভেরিয়েবলটি  নেওয়া হয়েছে
    context ={                                  #  কন্টেক্সট ভ্যেরিয়েবলে উপরের ভ্যারিয়েবলগুলো ঢুকিয়ে দেওয়া হয়েছে
        "post1":post1,
        "first":first,
        "last":last,
        "related":related
    }
    return render(request,'post_detail.html', context) #  কন্টেক্সট ভ্যেরিয়েবলে থাকা ভ্যালুগুলো ট্যামপ্লেটে পাঠানো হয়েছে

def PostTopic(request, name):
    topic = get_object_or_404(category, name=name)       #  ক্যাটাগরি মডেল থেকে ক্যাটাগরির নাম উপরের name প্যারামিটারের যুক্ত করে দিয়েছি
    post1 = post.objects.filter(post_category=topic.id)  #  একই ক্যাটাগরির পোষ্ট দেখার জন্য ফিল্টারের মধ্যে post_category মডেলের সাথে ক্যাটাগরির id যুক্ত করে দিয়েছি
    return render(request,'category.html', {"post1":post1, "topic":topic }) #   দুটি  ভ্যারিয়েবলকে ট্যামপ্লেটে পাঠানো হয়েছে

def LogIn(request):      #(অথেনটিকেশন এর জন্য from django.contrib.auth import authenticate, login, logout এই মডিউলটি এড  করে নিতে হবে )
    if request.user.is_authenticated:                    # ইউজার যদি অথেন্টিকেটেড হয়
        return redirect('blog:index')                    # তাহলে index  পেজে রিডাইরেক্ট হবে
    else:                                               #  আর যদি ইউজার অথেন্টিকেটেড না হয়
        if request.method == "POST":                     #  যদি রিকোয়েস্ট ম্যাথডটি পোষ্ট হয়
            user = request.POST.get('user')      #  লগ ইন ট্যামপ্লেটের ইউজার নেমকে user ভ্যেরিয়েবলে নিয়ে  নেবে
            password = request.POST.get('pass')  #  লগ ইন ট্যামপ্লেটের  পাসওয়ার্ড নেমকে password ভ্যেরিয়েবলে নিয়ে  নেবে
            auth = authenticate(request, username=user, password=password)  # auth ভেরিয়েবলে ইউজারের  ইউজার নেম ও পাসওয়ার্ড  দ্বারা অথেনটিকেশন চেক করা হবে
            if auth is not None:                 #  যদি  অথেনটিকেশন None না হয়
                login(request, auth)             # তবে আমরা লগ ইন করব
                return redirect('blog:index')    #  সফলভাবে লগ ইন হলে index পেজে রিডাইরেক্ট হবে (get_object_or_404 এর পরে redirect মডিউলটি এড করে নিতে হবে)
    return render(request,'login.html')         #  আর যদি সফলভাবে লগ ইন না হয় তাহলে সে login পেজে পাঠিয়ে দিবে

def LogOut(request):
    logout(request)               # পেজ থেকে লগ আউট করে নিয়ে  আসবে
    return redirect('blog:index') # পেজ থেকে লগ আউট করে index পেজে রিডাইরেক্ট করবে