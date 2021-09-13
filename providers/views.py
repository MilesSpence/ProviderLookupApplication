# Imports for webpage creation #
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Import the models we are using #
from .models import ProviderFull
# Imports for connecting to the Postgres DB #
import psycopg2
import psycopg2.extras
# Unneccesary import, but helpful for checking speed #
#import time

# This is for adding the providers from the Postgres DB to Djangos ORM #
# Check if the ORM is empty #
if str(ProviderFull.objects.all()) == "<QuerySet []>" or str(ProviderFull.objects.all()) == "<CopyQuerySet []>":
    print("ORM is empty")
    from io import StringIO
    import pandas as pd
    from contextlib import closing
    def in_memory_csv(data):
        ''' Creates an in-memory csv.
        Assumes `data` is a list of dicts
        with native python types. '''
        mem_csv = StringIO()
        pd.DataFrame(data).to_csv(mem_csv, index=False)
        mem_csv.seek(0)
        return mem_csv
    print("*******************************************")
    states = ['AA', 'AK', 'AL', 'AP', 'AR', 'AZ', 'BAJA CALIFORNIA', 'CA', 'CADIZ', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'GUAYAS', 'HI', 'IA', 'ID', 'IL', 'IN', 'KINGSTON', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'ONTARIO', 'OR', 'PA', 'PR', 'PW', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY']
    # Connecting to the DB #
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='123heythere'"
    print("Connecting to database. conn_string: " + str(conn_string))
    conn = psycopg2.connect(conn_string)
    # For each state in the states list add the providers to the ORM #
    for state in states:
        # Using str(state) because it has to be a unique cursor for every DB query #
        cursor = conn.cursor(str(state), cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM complete WHERE ProviderBusinessPracticeLocationAddressStateName = %s", [state])
        print("\nBeginning loading for " + str(state))
        # List comprehension of dictionary elements #
        providersListStoring = [dict(npi = str(row[0]), firstname = str(row[6]) if str(row[4]) == "None" else str(row[4]), lastname = str(row[7]) if str(row[5]) == "None" else str(row[5]), classification = str(row[2]), mailingAddress = str(row[8]), mailingCityState = ", ".join([str(row[9]), str(row[10])]), mailingZipcode = str(row[11]) if len(str(row[11])) < 6 else "-".join([str(row[11])[:5], str(row[11])[5:]]), phone = str(row[20]) if(len(str(row[20])) == 0) or (str(row[20])[0] == "(") else "-".join([str(row[20])[:3], str(row[20])[3:6], str(row[20])[6:]]), gender = str(row[19]), businessAddress = str(row[13]), businessCity = str(row[14]), businessZipcode = str(row[16]) if len(str(row[16])) < 6 else "-".join([str(row[16])[:5], str(row[16])[5:]]), businessCountry = str(row[17]) if str(row[17]) != "None" else " ", grouping = str(row[1]), definition = str(row[3]), businessName = str(row[18]), fax = str(row[12]) if len(str(row[12])) < 5 else "-".join([str(row[12])[:3], str(row[12])[3:6], str(row[12])[6:]]), businessState = str(row[15])) for row in cursor]
        print("Beginning csv")
        # Adding the elements of providersListStoring to the ORM #
        mem_csv = in_memory_csv(providersListStoring)
        with closing(mem_csv) as csv_io:
            ProviderFull.objects.from_csv(csv_io)
        print("Finished " + str(state))
    print("******************************************* \n")

#latest_questio_list = "" # For cached search #

# For individual provider's page #
def indProviderPage(request, npix):
    #providersList = latest_questio_list.get(npi = npix) # For cached search #
    providersList = ProviderFull.objects.all().get(npi = npix)

    # Replacing '#' symbols because they cause errors with the Google Map #
    if '#' in providersList.businessAddress:
        providersList.businessAddress = providersList.businessAddress.replace('#', '') 
    context = {'providersList': providersList}
    return render(request, 'single.html', context)

# For cached search #
#cachedStates = []
#for state in states:
#    cachedStates.append(ProviderFull.objects.all().filter(businessState = state))

#cadiz = ProviderFull.objects.all().filter(businessState = "CADIZ")

# For a search #
def searchedHome(request, searchedHome):
    # Create a list of the elements we need from the passed in url#
    results = searchedHome.split('=')
    # Some prints for debugging and confirmation #
    print("searchedHome: " + str(searchedHome))
    print("results: " + str(results))

    # For saving filters of the providers #
    first = ""
    second = ""
    third = ""
    fourth = ""
    fifth = ""
    filterString = ""
    # For keeping track of the number of filters we will do #
    anyQuery = 0
    
    # Filter firstname #
    if results[0] != "":
        filterString = ProviderFull.objects.all().filter(firstname = str(results[0]))
        anyQuery = 1

    # Filter lastname #
    if results[1] != "" and anyQuery == 1:
        first = filterString.filter(lastname = str(results[1]))
        anyQuery = 2
    elif results[1] != "": 
        filterString = ProviderFull.objects.all().filter(lastname = str(results[1]))
        anyQuery = 1

    # Filter classification #
    if results[2] != "" and anyQuery == 2:
        second = first.filter(classification = str(results[2]))
        anyQuery = 3
    elif results[2] != "" and anyQuery == 1:
        second = filterString.filter(classification = str(results[2]))
        anyQuery = 3
    elif results[2] != "":
        filterString = ProviderFull.objects.all().filter(classification = str(results[2]))
        anyQuery = 1

    # Filter city #
    if results[3] != "" and anyQuery == 3:
        third = second.filter(businessCity = str(results[3]))
        anyQuery = 4
    elif results[3] != "" and anyQuery == 2:
        third = first.filter(businessCity = str(results[3]))
        anyQuery = 4
    elif results[3] != "" and anyQuery == 1:
        third = filterString.filter(businessCity = str(results[3]))
        anyQuery = 4
    elif results[3] != "":
        filterString = ProviderFull.objects.all().filter(businessCity = str(results[3]))
        anyQuery = 1

    # Filter state #
    if results[4] != "" and anyQuery == 4:
        fourth = third.filter(businessState = str(results[4]))
        anyQuery = 5
    elif results[4] != "" and anyQuery == 3:
        fourth = second.filter(businessState = str(results[4]))
        anyQuery = 5
    elif results[4] != "" and anyQuery == 2:
        fourth = first.filter(businessState = str(results[4]))
        anyQuery = 5
    elif results[4] != "" and anyQuery == 1:
        fourth = filterString.filter(businessState = str(results[4]))
        anyQuery = 5
    elif results[4] != "":
        filterString = ProviderFull.objects.all().filter(businessState = str(results[4]))
        anyQuery = 1

    # Filter zipcode #
    if results[5] != "" and anyQuery == 5:
        fifth = fourth.filter(businessZipcode = str(results[5]))
        anyQuery = 6
    elif results[5] != "" and anyQuery == 4:
        fifth = third.filter(businessZipcode = str(results[5]))
        anyQuery = 6
    elif results[5] != "" and anyQuery == 3:
        fifth = second.filter(businessZipcode = str(results[5]))
        anyQuery = 6
    elif results[5] != "" and anyQuery == 2:
        fifth = first.filter(businessZipcode = str(results[5]))
        anyQuery = 6
    elif results[5] != "" and anyQuery == 1:
        fifth = filterString.filter(businessZipcode = str(results[5]))
        anyQuery = 6
    elif results[5] != "":
        filterString = ProviderFull.objects.all().filter(businessZipcode = str(results[5]))
        anyQuery = 1

    #global latest_questio_list # for cached search
    ''' Depending upon the number of times we filtered, 
    save the providers we want into providersList '''
    if anyQuery == 0:
        providersList = ProviderFull.objects.all()
    elif anyQuery == 1:
        providersList = filterString
    elif anyQuery == 2:
        providersList = first
    elif anyQuery == 3:
        providersList = second
    elif anyQuery == 4:
        providersList = third
    elif anyQuery == 5:
        providersList = fourth
    elif anyQuery == 6:
        providersList = fifth
    totalMatches = ""

    ''' If there were no inputs then set totalMatches to be above 
    5 million so that in the HTML it will ask for inputs '''
    if anyQuery == 0:
        totalMatches = 5100000
    else:
        totalMatches = providersList.count()

    # Limit the number of providers passed based on the max #
    providersList = providersList[:int(results[6])]

    # Give context the list of providers as well as the total number of providers passed #
    context = {'providersList': providersList, 'totalMatches': totalMatches}
    return render(request, 'homeSearched.html', context)

# For the regular home #
def homePage(request):
    return render(request, 'base.html')

# For the full unedited list of providers #
def fullProvidersList(request):
    providersList = ProviderFull.objects.all()[:10000]
    context = {'providersList': providersList}
    return render(request, 'provider.html', context)

# For different sorts for full list of providers #
def reorderedProvidersList(request, orderedWord):
    providersList = ProviderFull.objects.order_by(orderedWord)[:10000]
    context = {'providersList': providersList}
    return render(request, 'provider.html', context)