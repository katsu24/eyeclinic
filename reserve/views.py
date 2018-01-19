from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from reserve.models import Patient, Reserve
from reserve.forms import PatientForm, ReserveForm

def patient_list(request):
    patients = Patient.objects.all().order_by('pid')
    return render(request, 
                'reserve/patient_list.html',
                {'patients':patients})

def patient_edit(request, patient_id=None):
    if patient_id:
        patient = get_object_or_404(Patient, pk=patient_id)
    else:
        patient = Patient()

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('reserve:patient_list')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'reserve/patient_edit.html', dict(form=form, patient_id=patient_id))

def patient_del(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    patient.delete()
    return redirect('reserve:patient_list')

def reserve_list(request):
    reserves = Reserve.objects.all().order_by('start_datetime')
    return render(request,
                'reserve/reserve_list.html',
                { 'reserves':reserves })

def reserve_edit(request, reserve_id=None):
    if reserve_id:
        reserve = get_object_or_404(Reserve, pk=reserve_id)
    else:
        reserve = Reserve()

    if request.method == 'POST':
        form = ReserveForm(request.POST, instance=reserve)
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.save()
            return redirect('reserve:reserve_list')
    else:
        form = ReserveForm(instance=reserve)
    return render(request, 'reserve/reserve_edit.html', dict(form=form, reserve_id=reserve_id))

def reserve_del(request, reserve_id):
    reserve = get_object_or_404(Reserve, pk=reserve_id)
    reserve.delete()
    return redirect('reserve:reserve_list')

