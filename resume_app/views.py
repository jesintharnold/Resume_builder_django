from django.shortcuts import render
from resume_app.forms import BookFormset0,BookFormset1,BookFormset2,BookFormset3,BookFormset4,BookFormset5,BookFormset6
from formtools.wizard.views import SessionWizardView
from django.views.generic import ListView,DetailView
from  .models import Resume_template_data,Resume_home_data

class index(ListView):
    model = Resume_home_data

class preview(DetailView):
    model = Resume_template_data

FORMS=[
    ("step1",BookFormset0),
    ("step2",BookFormset1),
    ("step3",BookFormset2),
    ("step4",BookFormset3),
    ("step5",BookFormset4),
    ("step6",BookFormset5),
    ("step7",BookFormset6)
]

TEMPLATES={
    "step1":"formpart_1.html",
    "step2":"formpart_2.html",
    "step3":"formpart_3.html",
    "step4":"formpart_4.html",
    "step5":"formpart_5.html",
    "step6":"formpart_6.html",
    "step7":"formpart_7.html"
}

class Resume_Forms(SessionWizardView):



    def get_template_names(self):
        print(TEMPLATES[self.steps.current])
        return[TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):

        step1,step2,step3,step4,step5,step6,step7=form_list

        if step1.is_valid():
            for form in step1:
                firstname = form.cleaned_data["FirstName"]
                lastname = form.cleaned_data["LastName"]
                address = form.cleaned_data["Address"]
                city = form.cleaned_data["city"]
                zipcode = form.cleaned_data["Zipcode"]
                country = form.cleaned_data["Country"]
                emailid = form.cleaned_data["EmailId"]
                phonenumber = form.cleaned_data["PhoneNumber"]
                github = form.cleaned_data["Github"]
                img_data=form.cleaned_data["img_field"]



        else:
            print("Step-1-Error")

        if step2.is_valid():
            school_data=[]
            for form0 in step2:
                title = form0.cleaned_data["title"]
                schoolname = form0.cleaned_data["schclgname"]
                yearstart = form0.cleaned_data["yearStart"]
                yearEnd = form0.cleaned_data["yearEnd"]

                school_data.append({
                    "title":title,
                    "schoolname":schoolname,
                    "yearstart":yearstart,
                    "yearEnd":yearEnd
                })

        else:
            print("Step-2-Error")

        if step3.is_valid():
            experience_data=[]
            for form1 in step3:
                designation=form1.cleaned_data["designation"]
                companyName=form1.cleaned_data["companyName"]
                yearsworked=form1.cleaned_data["yearsworked"]
                lastworkedyear=form1.cleaned_data["lastworkedyear"]
                experience_data.append({
                    "designation":designation,
                    "companyname":companyName,
                    "yearsworked":yearsworked,
                    "lastworked":lastworkedyear,
                })

        else:
            print("Step-3-Error")

        if step4.is_valid():
            languages_data=[]
            for form2 in step4:
                languages=form2.cleaned_data["known_languages"]
                how_strong=form2.cleaned_data["how_strong"]

                languages_data.append({
                    "language":languages,
                    "lang_lev":how_strong
                })


        else:
            print("Step-4-Error")

        if step5.is_valid():
            skills_data=[]
            for form3 in step5:
               skills=form3.cleaned_data["skill_set"]
               skill_lev = form3.cleaned_data["skill_level"]

               skills_data.append({
                   "skilled_in":skills,
                   "skilled_lev":skill_lev
               })
        else:
            print("Step-5-Error")

        if step6.is_valid():
            project_data=[]
            for form4 in step6:
                project=form4.cleaned_data["project_data"]

                project_data.append(project)
        else:
            print("step-6-Error")

        if step7.is_valid():

            for form5 in step7:
                aboutme = form5.cleaned_data["aboutme"]

        else:
            print("step-7-error")




        return  render(self.request,"Resume-{}.html".format(self.kwargs['pk']),context = {

            "firstname": firstname,
            "lastname": lastname,
            "address": address,
            "city": city,
            "zipcode": zipcode,
            "country": country,
            "emailid": emailid,
            "phonenumber": phonenumber,
            "github": github,
            "img_data": img_data,
            "school_data": school_data,
            "experience_data": experience_data,
            "language_data": languages_data,
            "skill_data": skills_data,
            "img_data": img_data,
            "project_data": project_data,
            "aboutme": aboutme
        })


