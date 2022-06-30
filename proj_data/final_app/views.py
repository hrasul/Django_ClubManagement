from django.shortcuts import render, HttpResponse
from .models import Studentbody, Role, Department, Wings, Equipement, Equipment_user


# Create your views here.
def index(request):
    return render(request, 'index.html')


def view_admin(request):
    std = Studentbody.objects.all()
    context = {
        'std': std

    }
    print(context)
    return render(request, 'view_admin.html', context)


def add_admin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        wing = int(request.POST['wing'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_admin = Studentbody(first_name=first_name, last_name=last_name, dept_id=dept, wing_id=wing, role_id=role,
                                phone=phone)
        new_admin.save()
        return HttpResponse('Admin added successfully')
    elif request.method == 'GET':
        context = {
            "depts": Department.objects.all(),
            "wngs": Wings.objects.all(),
            "roles": Role.objects.all()
        }
        return render(request, 'add_admin.html', context)
    else:
        return HttpResponse("An Exception Occured")


def remove_admin(request, stds_id=0):
    if stds_id:
        try:
            stds_to_be_removed = Studentbody.objects.get(id=stds_id)
            stds_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Enter valid admin id")

    std = Studentbody.objects.all()
    context = {
        'std': std

    }
    print(context)
    return render(request, 'remove_admin.html', context)


def viewequipment(request):
    equips = Equipement.objects.all()
    context = {
        'equips': equips

    }
    print(context)
    return render(request, 'viewequipment.html', context)


def add_equipment(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        new_equipment = Equipement(name=name, description=description)
        new_equipment.save()
        return HttpResponse('Equipment added successfully')
    elif request.method == 'GET':
        return render(request, 'add_equipment.html')
    else:
        return HttpResponse("An Exception Occured")


def remove_equipment(request, eqp_id=0):
    if eqp_id:
        try:
            eqpt_to_be_removed = Equipement.objects.get(id=eqp_id)
            eqpt_to_be_removed.delete()
            return HttpResponse("Equipment removed successfully")
        except:
            return HttpResponse("Enter valid equipment id")

    equipmnts = Equipement.objects.all()
    context = {
        'equipmnts': equipmnts

    }

    return render(request, 'remove_equipment.html', context)


def borrow_equipment(request):
    if request.method == 'POST':
        issue_reason = request.POST['issue_reason']
        user = int(request.POST['admin'])
        wing = int(request.POST['wing'])
        equip = int(request.POST['borroww'])
        e = Equipement.objects.get(id=equip)
        e.is_available = False
        e.save()
        e_user = Equipment_user(issue_reason=issue_reason, user_id=user, wing_id=wing, equip_id=equip)
        e_user.save()
        return HttpResponse('Equipment borrowed successfully')
    else:

        borroww = Equipement.objects.all()
        context = {
            'borroww': borroww,
            'admin': Studentbody.objects.all(),
            "wngs": Wings.objects.all(),

        }

        return render(request, 'borrow_equipment.html', context)
