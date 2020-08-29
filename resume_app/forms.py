from django import forms
from django.forms import  formset_factory






class ProfileInfo(forms.Form):
    FirstName=forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class":"form-control nwd",
                "placeholder":"First name",
                "required":"required"
            }
        ),label=""
    )

    LastName = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control nwd",
                "placeholder":"Last name",
                "required": "required"
            }
        ),label=""
    )
    Address=forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Address",
                "required": "required"
            }
        ),label=""
    )
    city=forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "City",
                "required": "required"
            }
        ),label=""
    )

    Zipcode=forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Zipcode",
                "required": "required"
            }
        ),label=""
    )

    Country=forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Country",
                "required": "required"
            }
        ),label=""
    )

    EmailId=forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control ned",
                "placeholder": "Email Id",
                "required": "required"
            }
        ),label=""
    )
    PhoneNumber=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Phone Number",
                "required": "required"
            }
        )
    )
    Github=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder": "Github (optional)"
            }
        )
    )

    img_field=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form_profile_image",
                "id":"dec_sec_profile",
                 "type":"Hidden"


            }
        )
    )

BookFormset0=formset_factory(ProfileInfo,extra=1)

class Education(forms.Form):
    title=forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
            "class":"form-field-input  form-control",
            "placeholder":"Degree & Field of Study",
            "required": "required"


        }

    ),label="")
    schclgname=forms.CharField(max_length=100,widget=forms.TextInput(

        attrs={
            "class":"form-field-input  form-control",
            "placeholder":"School/College Institution Name",
            "required": "required"

        }

    ),label="")
    yearStart=forms.IntegerField(widget=forms.NumberInput(
        attrs={
            "class":"form-field-input  form-control",
            "placeholder":"Year-Start",
            "required": "required"

        }
    ),label="")
    yearEnd=forms.IntegerField(widget=forms.NumberInput(
        attrs={
            "class":"form-field-input  form-control",
            "placeholder": "Year-End",
            "required": "required"
        }
    ),label= "")



BookFormset1=formset_factory(Education,extra=1)


class Experience(forms.Form):
    designation=forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
            "class":"form-field-output form-control",
            "placeholder":"Designation",
            "required": "required"

        }
    ),label="")
    companyName=forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={
            "class":"form-field-output form-control",
            "placeholder":"Company Name",
            "required": "required"


        }
    ),label="")

    yearsworked=forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-field-output form-control",
            "placeholder":"From Year",
            "required": "required"


        }
    ),label="")
    lastworkedyear=forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-field-output form-control",
            "placeholder":"To year",
            "required": "required"

        }
    ),label="")

BookFormset2=formset_factory(Experience,extra=1)


class Languages(forms.Form):
    known_languages=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-field-output-4",
                "placeholder": "Add Known Language",
                "id": "lang_id",
                "required": "required"
            }
        ),label=""
    )

    how_strong = forms.IntegerField(
        max_value=20,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control  form-field-output-4",
                "placeholder": "proficiency",
                "id":"val_id",
                "required": "required"
            }
        ),label="",min_value=3
    )

BookFormset3=formset_factory(Languages,extra=1)

class Skills(forms.Form):
    skill_set=forms.CharField(
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "class":"form-control form-field-output-4",
                "placeholder":"Add your Skill",
                "id":"lang_id",
                "required": "required"
            }
        ),label=""

    )
    skill_level=forms.IntegerField(
        max_value=5,
        widget=forms.NumberInput(
            attrs={
                "class":"form-control form-field-output-4",
                "placeholder":"Skill Level",
                "id":"val_id",
                "required": "required",

             }
        ),min_value=1
    )

BookFormset4=formset_factory(Skills,extra=1)

class projects(forms.Form):
    project_data=forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-field-output form-control",
                "cols":"50",
    "rows":"2",
                "required": "required",

            }
        )
    )
BookFormset5=formset_factory(projects,extra=1)


class About(forms.Form):
    aboutme = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"md-textarea form-control",
                "row":"8",
                "cols":"60",
                "required": "required",
            }
        )

)
BookFormset6 = formset_factory(About, extra=1)