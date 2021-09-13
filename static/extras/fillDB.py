import psycopg2
#from .models import Doctor

con = psycopg2.connect(database="postgres", user="postgres", password="123heythere", host="127.0.0.1", port="5432")
print("Database opened successfully")

cur = con.cursor()
#sql_file = open("postgres.sql")
sql_file = open("justCompTable.sql")
sql_as_string = sql_file.read()
sqlCommands = sql_as_string.split(";")
print("Beginning commands")
for command in sqlCommands[:-1]:
    print(command)
    #try:
    cur.execute(command)
    #except msg:
    #    print("Command skipped: " + str(OperationalError) + " " + str(msg))#, OperationalError
print("All commands executed")

#Doctor.objects.all().delete()
'''
cur.execute("SELECT * FROM complete")

#values = [0,1]
#psycopg2.extras.execute_batch(cursor, "SELECT * FROM complete", values)

# Because cursor objects are iterable we can just call 'for - in' on
# the cursor object and the cursor will automatically advance itself
# each iteration.
#start_time = time.time()
doctorsList = []
#row_count = len(r_count)
row_count = 0

for row in cur:
    row_count += 1
    #r_count.append(row_count)
    #names
    firNam = str(row[7])
    lasNam = str(row[6])
    if (firNam == "None" and lasNam == "None"):
        firNam = str(row[20])
        lasNam = str(row[21])
    #mailing address
    aa = str(row[8])
    ab = str(row[9])
    ac = str(row[10])
    cs = ab + ", " + ac
    ad = str(row[11])
    #business address
    baa = str(row[14])
    bab = str(row[15])
    bac = str(row[16])
    bcs = str(row[15]) + ", " + str(row[16])
    bad = str(row[17])
    #phone number
    pn = str(row[22])
    if(pn[0] == "("):
         continue
    elif(len(pn) > 4):
        pnn = pn[:6] + '-' +  pn[6:]
        pn = pnn[:3] + '-' +  pnn[3:]
    else:
        pn = str(row[12])
    #fax number
    fan = str(row[13])
    if (len(fan) > 4):
        fay = fan[:6] + '-' +  fan[6:]
        fan = fay[:3] + '-' +  fay[3:]          
    #business zipcode
    if (len(bad) > 5):
        bae = bad[:5] + '-' +  bad[5:]
        bad = bae
    if (len(ad) > 5):
        ae = ad[:5] + '-' +  ad[5:]
        ad = ae     
    a = Doctor(npi = str(row[0]), firstname = firNam, lastname = lasNam, classification = str(row[2]), mailingAddress = aa, mailingCityState = cs, mailingZipcode = ad, phone = pn, gender = str(row[19]), businessAddress = baa, businessCityState = bcs, businessZipcode = bad, businessCountry = str(row[18]), grouping = str(row[1]), definition = str(row[4]), businessName = str(row[5]), fax = fan)
    doctorsList.append(a)
    #a.save()
'''
#finish_time = time.time() - start_time
#print(doctorsList[5])

#print(sql_as_string)

con.commit()
con.close()
print("Committed and closed")


#latest_question_list = Doctor.objects.bulk_create(doctorsList)
#print("All selected objects saved. Object count: " + str(row_count))
