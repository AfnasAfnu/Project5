from django import forms
from store.models import Person, Courses


items = (('pen', 'Pen'), ('pencil', 'Pencil'), ('exam pappers', 'Exam pappers'), ('Debit Notebook', 'Debit Notebook'))


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Age': forms.NumberInput(attrs={'class': 'form-control'}),
            'Mobile_Number': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'Address': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Address, City, Country', 'rows': 2}),
            'pin_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'departments': forms.Select(attrs={'class': 'form-select'}),
            'courses': forms.Select(attrs={'class': 'form-select'}),
            'DOB': forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
            'purpose': forms.Select(attrs={'class': 'form-select'}),
            'Materials_Provided': forms.CheckboxSelectMultiple(choices=items)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courses'].queryset = Courses.objects.none()

        if 'departments' in self.data:
            try:
                departments_id = int(self.data.get('departments'))
                self.fields['courses'].queryset = Courses.objects.filter(departments_id=departments_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['courses'].queryset = self.instance.departments.courses_set.order_by('name')
