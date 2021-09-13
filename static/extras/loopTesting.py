import psycopg2
import psycopg2.extras
import time

conn_string = "host='localhost' dbname='postgres' user='postgres' password='123heythere'"
conn = psycopg2.connect(conn_string)

# HERE IS THE IMPORTANT PART, by specifying a name for the cursor
# psycopg2 creates a server-side cursor, which prevents all of the
# records from being downloaded at once from the server.
cursor = conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
cursor.execute("SELECT * FROM complete LIMIT 50000")

#doctorsList = []
#row_count = 0

loopStartTime = time.time()
'''
for row in cursor:
    # assigning
    firNam, lasNam, mailZip, busZip, pn, fx = str(row[4]), str(row[5]), str(row[11]), str(row[16]), str(row[20]), str(row[12])
    # first/lastname
    if (firNam == "None" and lasNam == "None"):
        firNam, lasNam = str(row[6]), str(row[7])
    # zipcodes
    if (len(mailZip) > 5):
        mailZip = "-".join([str(row[11])[:5], str(row[11])[5:]])
    if (len(busZip) > 5):
        busZip = "-".join([str(row[16])[:5], str(row[16])[5:]])
    # phone number
    if(len(pn) == 0) or (pn[0] == "("):
        continue
    else:
        pn = "-".join([str(row[20])[:3], str(row[20])[3:6], str(row[20])[6:]])
    # fax number
    if (len(fx) > 4):
           fx = "-".join([str(row[12])[:3], str(row[12])[3:6], str(row[12])[6:]])
    doctorsList.append(dict(npi = str(row[0]), firstname = firNam, lastname = lasNam, classification = str(row[2]), mailingAddress = str(row[8]), mailingCityState = ", ".join([str(row[9]), str(row[10])]), mailingZipcode = mailZip, phone = pn, gender = str(row[19]), businessAddress = str(row[13]), businessCity = str(row[14]), businessZipcode = busZip, businessCountry = str(row[18]), grouping = str(row[1]), definition = str(row[3]), businessName = str(row[18]), fax = fx, businessState = str(row[15])))
'''
doctorsList = [dict(npi = str(row[0]), firstname = str(row[6]) if str(row[4]) == "None" else str(row[4]), lastname = str(row[7]) if str(row[5]) == "None" else str(row[4]), classification = str(row[2]), mailingAddress = str(row[8]), mailingCityState = ", ".join([str(row[9]), str(row[10])]), mailingZipcode = str(row[11]) if len(str(row[11])) < 6 else "-".join([str(row[11])[:5], str(row[11])[5:]]), phone = str(row[20]) if(len(str(row[20])) == 0) or (str(row[20])[0] == "(") else "-".join([str(row[20])[:3], str(row[20])[3:6], str(row[20])[6:]]), gender = str(row[19]), businessAddress = str(row[13]), businessCity = str(row[14]), businessZipcode = str(row[16]) if len(str(row[16])) < 6 else "-".join([str(row[16])[:5], str(row[16])[5:]]), businessCountry = str(row[18]), grouping = str(row[1]), definition = str(row[3]), businessName = str(row[18]), fax = str(row[12]) if len(str(row[12])) < 5 else "-".join([str(row[12])[:3], str(row[12])[3:6], str(row[12])[6:]]), businessState = str(row[15])) for row in cursor]
#doctorsList = map(dict(npi = str(row[0]), firstname = str(row[6]) if str(row[4]) == "None" else str(row[4]), lastname = str(row[7]) if str(row[5]) == "None" else str(row[5]), classification = str(row[2]), mailingAddress = str(row[8]), mailingCityState = ", ".join([str(row[9]), str(row[10])]), mailingZipcode = str(row[11]) if len(str(row[11])) < 6 else "-".join([str(row[11])[:5], str(row[11])[5:]]), phone = str(row[20]) if(len(str(row[20])) == 0) or (str(row[20])[0] == "(") else "-".join([str(row[20])[:3], str(row[20])[3:6], str(row[20])[6:]]), gender = str(row[19]), businessAddress = str(row[13]), businessCity = str(row[14]), businessZipcode = str(row[16]) if len(str(row[16])) < 6 else "-".join([str(row[16])[:5], str(row[16])[5:]]), businessCountry = str(row[17]) if str(row[17]) != "None" else " ", grouping = str(row[1]), definition = str(row[3]), businessName = str(row[18]), fax = str(row[12]) if len(str(row[12])) < 5 else "-".join([str(row[12])[:3], str(row[12])[3:6], str(row[12])[6:]]), businessState = str(row[15])), cursor)
loopFinishTime = time.time() - loopStartTime
print("loopFinishTime: " + str(loopFinishTime))
#print(doctorsList[0])
#Doctor.objects.bulk_create(doctorsList) # bulk_create method
#Doctor.objects.all().delete()
#print("Deleting all doctor/provider objects")