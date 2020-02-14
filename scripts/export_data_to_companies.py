import pandas as pd
import re
from company.models import RegCompany as reg

comps = reg.objects.all()

for comp in comps:
    data = []    
    comp_name = comp.name
    print(comp_name)
    profiles = comp.apply_profile.all()
    for profile in profiles:
        roles = re.sub(r'\d+-',"", profile.applied_roles) 
        student = profile.student
        name = student.name
        entry_number = student.entry_number
        email = student.email
        contact_number = student.contact_number
        college_year = student.college_year
        cv_link = "https://storage.googleapis.com/internfairiitrpr-266720.appspot.com/" + str(student.cv)
        data.append({
            "Name": name,
            "Entry Number": entry_number,
            "Email": email,
            "Contact Number": contact_number,
            "CV Link": cv_link,
            "College Year": college_year,
            "Applied Roles": roles
        })
    pd.DataFrame(data).to_excel("sheets/" + comp_name +".xls")
    data.clear()