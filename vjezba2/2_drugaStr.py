#! python.exe 

import cgi
params = cgi.FieldStorage()
pass1 = params.getvalue("pwd1")
pass2 = params.getvalue("pwd2")
if(pass1 != pass2):
    print('Location: vj2registracija.py')
    
print ('''
<!DOCTYPE html>
<html>
<head>
</head>
<body>
    <form action="vj2trecaStr.py" method='post'>
            <label>Status:</label>
            <input type="radio" name="student_status" id = "st1 "value="Redovan"> 
            <label for="st1">Redovan</label>
            <input type="radio" name="student_status" id = "st2" value="Izvanredan">
            <label for="st1">Izvanredan</label>
            <br>
            <label>E-mail:</label>
            <input type="email" value="abc@oss.unist.hr" name="mail">
            <br>
            <label>Smjer:</label>
            <select name="smjer">
            <option value="baze podataka">Baze podataka</option>
            <option value="programiranje">programiranje</option>
            <option value="mreze">mreze</option>
            <option value="informacijski_sustavi">informacijski sustavi</option>
            </select>
            <br>
            <label>Zavrsni</label>
            <input type="checkbox" name="zavrsni" value="zavrsni">
            <br>
            ''')
print ('    <input type="hidden" name="ime" value="' + params.getvalue("name") + '">')
print('''
    <button type="submit">Next</button>
    </form>  
</body>
</html>
''')


