from django.forms import ModelForm
from reserve.models import Patient, Reserve

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('pid', 'pname', 'pnamekana', 'birthdate', 'psex', 'memo',)
        labels = {
            'pid':'患者ID', 'pname':'氏名', 'pnamekana':'氏名カナ', 'birthdate':'生年月日', 'psex':'性別', 'memo':'備考',
        }

class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        fields = ('patient', 'start_datetime', 'end_datetime','reserve_type', 'memo',)
        labels = {
            'patient':'患者ID', 'start_datetime':'予約日時始', 'end_datetime':'予約日時終', 'reserve_type':'予約区分', 'memo':'備考',
        }
