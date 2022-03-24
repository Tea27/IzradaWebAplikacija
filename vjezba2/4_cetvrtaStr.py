#! python.exe 
import cgi
params = cgi.FieldStorage()


tekstic = params.getvalue("tekst")
if(tekstic is None):
    tekstic = "Nema napomena"

print ('''
<!DOCTYPE html>
<html>
<head>
</head>
<body>
        <h1>Uneseni podaci:</h1>
            <label>Ime: ''' + params.getvalue("name") + '''</label> 
            <br>
            <label>E-mail: ''' + params.getvalue("Email") + '''</label>
            <br>
            <label>Status: ''' + params.getvalue("status_st") + '''</label>
            <br>
            <label>Smjer: ''' + params.getvalue("student_smjer") + '''</label>
            <br>
            <label>Zavrsni rad: ''' + params.getvalue("zavrsni_rad") +  '''</label>
            <br>
            <label>Napomene: ''' + tekstic +  '''</label>
            <br>
            <a href="vj2registracija.py">Na pocetak</a>
</body>
</html>
''')