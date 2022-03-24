#! python.exe 

import cgi
params = cgi.FieldStorage()
zavrsni = params.getvalue("zavrsni")
tekst = ""
if(zavrsni):
    tekst = "Da"
else:
    tekst = "Ne"
    
print ('''
<!DOCTYPE html>
<html>
<head>
</head>
<body>
   <form action="vj2cetvrtaStr.py" method='post'>
            <label>Napomene:</label>
            <textarea name="tekst" value="" placeholder="Prelazak na izvanredni studij..." rows="4" cols="50"></textarea>
            <br>
            ''')
print ('<input type="hidden" name="name" value="' + params.getvalue("ime") + '">')
print ('<input type="hidden" name="status_st" value="' + params.getvalue("student_status") + '">')
print ('<input type="hidden" name="Email" value="' + params.getvalue("mail") + '">')
print ('<input type="hidden" name="student_smjer" value="' + params.getvalue("smjer") + '">')
print ('<input type="hidden" name="zavrsni_rad" value="' + tekst + '">')
print('''
    <button type="submit">Next</button>
    </form>  
</body>
</html>
''')