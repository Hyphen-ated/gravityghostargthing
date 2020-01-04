
anna = open("annalemma.cfg", "r")
fool = open("fool.cfg", "r")
outf = open("index.html", "w")

annas = anna.readlines()
fools = fool.readlines()

aout = ""
fout = ""


for i in range(139):
    aline = annas[i].rstrip('\n\r')
    fline = fools[i].rstrip('\n\r')
    for ci in range(160):
        ac = aline[ci] if ci < len(aline) else "X"
        fc = fline[ci] if ci < len(fline) else "X"
        awrite = ac
        fwrite = fc
        if ac != fc:          
            awrite = "<span>" + ac + "</span>"
            fwrite = "<span>" + fc + "</span>"
        if awrite != "X":
            aout += awrite
        if fwrite != "X":
            fout += fwrite

        
    aout += "<br>"
    fout += "<br>"

outf.write("""
<html>
<head>
  <link rel="stylesheet" href="style.css">
</head>
<p id='fool'>""" + fout + "</p><br><br><br><p id='anna'>" + aout + "</p></html>")

outf.close()
