from django import forms


class YourForm(forms.Form):
    name = forms.CharField(label='Name')
    dob = forms.DateField(label='DOB')
    age = forms.IntegerField(label='Age')

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)

    phone_number = forms.CharField(label='Phone Number', max_length=10)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address')

    DEPARTMENT_CHOICES = [
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('arts', 'Arts'),
    ]
    department = forms.ChoiceField(label='Department', choices=DEPARTMENT_CHOICES)

    COURSES_CHOICES = {
        'science': ['Physics', 'Chemistry', 'Biology'],
        'commerce': ['BBA', 'BCom', 'Accounting'],
        'arts': ['History', 'Literature', 'Philosophy'],
    }
    course = forms.ChoiceField(label='Courses', choices=[], required=False)

    purpose_choices = [
        ('enquiry', 'For Enquiry'),
        ('order', 'Place Order'),
        ('return', 'Return'),
    ]
    purpose = forms.ChoiceField(label='Purpose', choices=purpose_choices)

    materials_provide = forms.MultipleChoiceField(
        label='Materials Provide',
        choices=[('notebook', 'Notebook'), ('pen', 'Pen'), ('exam_papers', 'Exam Papers')],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
