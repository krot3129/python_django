from django.shortcuts import render

def main_page(reqest, *args, **kwargs):
    return render(reqest, 'Announcements/home_page.html', {})

def Announcements_list(reqest, *args, **kwargs):
    return render(reqest, 'Announcements/Announcements_list.html', {})

def Announcements_1(reqest, *args, **kwargs):
    return render(reqest, 'Announcements/Announcements_1.html', {})

def Announcements_2(reqest, *args, **kwargs):
    return render(reqest, 'Announcements/Announcements_2.html', {})

def Announcements_3(reqest, *args, **kwargs):
    return render(reqest, 'Announcements/Announcements_3.html', {})

def Announcements_4(reqest, *args, **kwargs):
    return render(reqest, 'Announcements/Announcements_4.html', {})

def Announcements_5(reqest, *args, **kwargs):
    return render(reqest, 'Announcements/Announcements_5.html', {})
