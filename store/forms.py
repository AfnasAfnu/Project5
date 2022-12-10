from django import forms

from store.models import Person, Courses


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
        #            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #
        #            # 'Age': forms.DateInput(),
        #            # 'Mobile_Number': forms.NumberInput(attrs={'class': 'form-select'}),
        #            'Address': forms.Textarea(attrs={'rows':2}),
        #            # 'zip_code': forms.CharField(attrs={'class': 'form-select'}),
        #            # 'gender': forms.ChoiceField(),
        #             'departments': forms.Select(attrs={'class': 'form-select'}),
        #            'courses': forms.Select(attrs={'class': 'form-select'}),
        #            'DOB': forms.NumberInput(attrs={'type':'date'}),
        #            }

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

