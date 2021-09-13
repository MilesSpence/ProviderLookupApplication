/* Hit ctrl-F5 on the website if webpages aren't updating
 with changes from this file or from .css files */
// Used for the clear btn
function cleardata() {
    document.getElementById("firstname").value="";
    document.getElementById("lastname").value="";
    document.getElementById("descriptionDropDown").selectedIndex=0;
    document.getElementById("city").value="";
    document.getElementById("state").selectedIndex=0;
    document.getElementById("zip").value="";
    document.getElementById("max").value="250";
}

/* Used to collect the information from the input fields
and then writes them in the proper form to the URL */
function retrieveInput() {
    // Collect the info
    var firstname=document.getElementById("firstname").value;
    var lastname=document.getElementById("lastname").value;
    var fdescription=document.getElementById("descriptionDropDown");
    var desc=fdescription.options[fdescription.selectedIndex].value;
    var city=document.getElementById("city").value;
    var fstate=document.getElementById("state");
    var state=fstate.options[fstate.selectedIndex].value;
    var zip=document.getElementById("zip").value;
    var max=document.getElementById("max").value;
    var toUrlString = "";

    /* Checking each of the input fields for info,
    if there is then add it to toUrlString.
    Between each add add '='' symbol because this 
    will be how we split the url later. */
    if (firstname != "") {
        toUrlString = toUrlString + firstname.toUpperCase();
    }
    toUrlString = toUrlString + "=";
    if (lastname != "") {
        toUrlString = toUrlString + lastname.toUpperCase();
    }
    toUrlString = toUrlString + "=";
    if (desc != "") {
        toUrlString = toUrlString + String(desc);
    }
    toUrlString = toUrlString + "=";
    if (city != "") {
        toUrlString = toUrlString + city.toUpperCase();
    }
    toUrlString = toUrlString + "=";
    if (state != "") {
        toUrlString = toUrlString + String(state);
    }
    toUrlString = toUrlString + "=";
    if (zip != "") {
        toUrlString = toUrlString + zip.toUpperCase();
    }
    toUrlString = toUrlString + "=";
    if (max == "") {
        max = 250;
    }

    // Writing to the URL
    window.location.href = "http://localhost:8000/" + toUrlString + max + "/";
}

// For sorting the search table
function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("searchedTable");
    switching = true;
    // Set the sorting direction to ascending:
    dir = "asc";
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        rows = table.rows;
        /* Loop through all table rows (except the
        first, which contains table headers): */
        for (i = 1; i < (rows.length - 1); i++) {
            // Start by saying there should be no switching:
            shouldSwitch = false;
            /* Get the two elements you want to compare,
            one from current row and one from the next: */
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            /* Check if the two rows should switch place,
            based on the direction, asc or desc: */
            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    // If so, mark as a switch and break the loop:
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    // If so, mark as a switch and break the loop:
                    shouldSwitch = true;
                    break;
                }
            } 
        }
        if (shouldSwitch) {
            /* If a switch has been marked, make the switch
            and mark that a switch has been done: */
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            // Each time a switch is done, increase this count by 1:
            switchcount ++;
        } else {
            /* If no switching has been done AND the direction is "asc",
            set the direction to "desc" and run the while loop again. */
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

/* After a user hits the search button and
loads a new webpage, this will rewrite the
inputs from before in the inputs fields */
function populateInputFields() {
    var path = window.location.pathname.split("=");
    var stateAbbs = ["","AA","AK","AL","AP","AR","AZ","BAJA CALIFORNIA","CADIZ","CA","CO","CT","DC","DE","FL","GA","GU","GUAYAS","HI","IA","ID","IL","IN","KINGSTON","KS","KY","LA","MA","MD","ME","MI","MN","MO","MP","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","ONTARIO","OR","PA","PR","PW","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA","WI","WV","WY"];
    var descriptionValues = ["","Multi-Specialty","Single Specialty","Allergy & Immunology","Anesthesiology","Clinical Pharmacology","Colon & Rectal Surgery","Dermatology","Electrodiagnostic Medicine","Emergency Medicine","Family Medicine","General Practice","Hospitalist","Independent Medical Examiner","Internal Medicine","Legal Medicine","Medical Genetics","Neurological Surgery","Neuromusculoskeletal Medicine & OMM","Neuromusculoskeletal Medicine, Sports Medicine","Nuclear Medicine","Obstetrics & Gynecology","Ophthalmology","Oral & Maxillofacial Surgery","Orthopaedic Surgery","Otolaryngology","Pain Medicine","Pathology","Pediatrics","Phlebology","Physical Medicine & Rehabilitation","Plastic Surgery","Preventive Medicine","Psychiatry & Neurology","Radiology","Surgery","Thoracic Surgery (Cardiothoracic Vascular Surgery)","Transplant Surgery","Urology","Assistant Behavior Analyst","Behavior Technician","Behavior Analyst","Clinical Neuropsychologist","Counselor","Drama Therapist","Marriage & Family Therapist","Poetry Therapist","Psychoanalyst","Psychologist","Social Worker","Chiropractor","Advanced Practice Dental Therapist","Dental Assistant","Dental Hygienist","Dental Laboratory Technician","Dental Therapist","Dentist","Denturist","Oral Medicinist","Dietary Manager","Dietetic Technician, Registered","Dietitian, Registered","Nutritionist","Emergency Medical Technician, Basic","Emergency Medical Technician, Intermediate","Emergency Medical Technician, Paramedic","Personal Emergency Response Attendant","Optometrist","Technician@Technologist","Licensed Practical Nurse","Licensed Psychiatric Technician","Licensed Vocational Nurse","Registered Nurse","Adult Companion","Chore Provider","Day Training@Habilitation Specialist","Doula","Home Health Aide","Homemaker","Nurse's Aide","Nursing Home Administrator","Religious Nonmedical Nursing Personnel","Religious Nonmedical Practitioner","Technician","Acupuncturist","Case Manager@Care Coordinator","Clinical Ethicist","Community Health Worker","Contractor","Driver","Funeral Director","Genetic Counselor, MS","Health & Wellness Coach","Health Educator","Homeopath","Interpreter","Lactation Consultant, Non-RN","Midwife, Lay","Mechanotherapist","Midwife","Military Health Care Provider","Naprapath","Naturopath","Peer Specialist","Medical Genetics, Ph.D. Medical Genetics","Prevention Professional","Reflexologist","Sleep Specialist, PhD","Specialist","Veterinarian","Pharmacist","Pharmacy Technician","Advanced Practice Midwife","Anesthesiologist Assistant","Clinical Nurse Specialist","Nurse Anesthetist, Certified Registered","Nurse Practitioner","Physician Assistant","Assistant, Podiatric","Podiatrist","Anaplastologist","Art Therapist","Clinical Exercise Physiologist","Dance Therapist","Developmental Therapist","Kinesiotherapist","Massage Therapist","Mastectomy Fitter","Music Therapist","Occupational Therapist","Occupational Therapy Assistant","Orthotic Fitter","Orthotist","Pedorthist","Physical Therapist","Physical Therapy Assistant","Prosthetist","Pulmonary Function Technologist","Recreation Therapist","Recreational Therapist Assistant","Rehabilitation Counselor","Rehabilitation Practitioner","Respiratory Therapist, Certified","Respiratory Therapist, Registered","Specialist@Technologist","Audiologist","Audiologist-Hearing Aid Fitter","Hearing Instrument Specialist","Speech-Language Pathologist","Student in an Organized Health Care Education@Training Program","Perfusionist","Radiologic Technologist","Radiology Practitioner Assistant","Specialist@Technologist Cardiovascular","Specialist@Technologist, Health Information","Specialist@Technologist, Other","Specialist@Technologist, Pathology","Technician, Cardiology","Technician, Health Information","Technician, Other","Technician, Pathology","Case Management","Community@Behavioral Health","Day Training, Developmentally Disabled Services","Early Intervention Provider Agency","Foster Care Agency","Home Health","Home Infusion","Hospice Care, Community Based","In Home Supportive Care","Local Education Agency (LEA)","Nursing Care","Program of All-Inclusive Care for the Elderly (PACE) Provider Organization","Public Health or Welfare","Supports Brokerage","Voluntary or Charitable","Clinic@Center","Epilepsy Unit","Medicare Defined Swing Bed Unit","Psychiatric Unit","Rehabilitation Unit","Rehabilitation, Substance Use Disorder Unit","Christian Science Sanitorium","Chronic Disease Hospital","General Acute Care Hospital","Long Term Care Hospital","Military Hospital","Psychiatric Hospital","Rehabilitation Hospital","Religious Nonmedical Health Care Institution","Special Hospital","Clinical Medical Laboratory","Dental Laboratory","Military Clinical Medical Laboratory","Physiological Laboratory","Exclusive Provider Organization","Health Maintenance Organization","Point of Service","Preferred Provider Organization","Alzheimer Center (Dementia Center)","Assisted Living Facility","Christian Science Facility","Custodial Care Facility","Hospice, Inpatient","Intermediate Care Facility, Mentally Retarded","Intermediate Care Facility, Mental Illness","Nursing Facility@Intermediate Care Facility","Skilled Nursing Facility","Lodging","Meals","Community Based Residential Treatment Facility, Mental Illness","Community Based Residential Treatment Facility, Intellectual and@or Developmental Disabilities","Psychiatric Residential Treatment Facility","Residential Treatment Facility, Emotionally Disturbed Children","Residential Treatment Facility, Intellectual and@or Developmental Disabilities","Residential Treatment Facility, Physical Disabilities","Substance Abuse Rehabilitation Facility","Respite Care","Blood Bank","Department of Veterans Affairs (VA) Pharmacy","Durable Medical Equipment & Medical Supplies","Emergency Response System Companies","Eye Bank","Eyewear Supplier","Hearing Aid Equipment","Home Delivered Meals","Indian Health Service@Tribal@Urban Indian Health (I@T@U) Pharmacy","Medical Foods Supplier","Military@U.S. Coast Guard Pharmacy","Non-Pharmacy Dispensing Site","Organ Procurement Organization","Pharmacy","Portable X-ray and@or Other Portable Diagnostic Imaging Supplier","Prosthetic@Orthotic Supplier","Air Carrier","Ambulance","Bus","Military@U.S. Coast Guard Transport","Non-emergency Medical Transport (VAN)","Private Vehicle","Secured Medical Transport (VAN)","Taxi","Train","Transportation Broker","Transportation Network Company"];
    /* Need to replace the %20 that come about when spaces are in the input.
    This is done for firstname, lastname, and city */
    document.getElementById("firstname").value = path[0].substring(1).replaceAll("%20", " ");
    document.getElementById("lastname").value = (path[1]).replaceAll("%20", " ");
    var newPathTwo = path[2].replaceAll("%20", " ");
    for(let i = 0; i < descriptionValues.length; i++) {
        if(descriptionValues[i] === newPathTwo) {
            document.getElementById("descriptionDropDown").selectedIndex=i;
       }
    }
    document.getElementById("city").value = (path[3]).replaceAll("%20", " ");
    var newPathFour = path[4].replaceAll("%20", " ");
    for(let i = 0; i < stateAbbs.length; i++) {
        if(stateAbbs[i] === newPathFour) {
            document.getElementById("state").selectedIndex=i;
       }
    }
    document.getElementById("zip").value = path[5];
    document.getElementById("max").value = path[6].substring(0, path[6].length - 1);
}

/* For the show more results btn, it 
simply adds 250 more to the max */
function showAllSearchMatches() {
    var firstname=document.getElementById("firstname").value;
    var lastname=document.getElementById("lastname").value;
    var fdescription=document.getElementById("descriptionDropDown");
    var desc=fdescription.options[fdescription.selectedIndex].value;
    var city=document.getElementById("city").value;
    var fstate=document.getElementById("state");
    var state=fstate.options[fstate.selectedIndex].value;
    var zip=document.getElementById("zip").value;
    var max=document.getElementById("max").value;
    var toUrlString = "";
    if (firstname != "") {
        toUrlString = toUrlString + firstname.toUpperCase();
    }
    toUrlString = toUrlString + "=";
    if (lastname != "") {
        toUrlString = toUrlString + lastname.toUpperCase();
    }
    toUrlString = toUrlString + "=";
    if (desc != "") {
        toUrlString = toUrlString + String(desc);
    }
    toUrlString = toUrlString + "=";
    if (city != "") {
        toUrlString = toUrlString + city.toUpperCase();
    }
    toUrlString = toUrlString + "=";
    if (state != "") {
        toUrlString = toUrlString + String(state);
    }
    toUrlString = toUrlString + "=";
    if (zip != "") {
        toUrlString = toUrlString + zip.toUpperCase();
    }
    toUrlString = toUrlString + "=";
    if (max == "") {
        max = 250;
    }
    let finishedMax = parseInt(max) + 250;
    window.location.href = "http://localhost:8000/" + toUrlString + finishedMax + "/";
}

// The following two functions are for the to top btn
function topFunction() {
    // Takes the user back to the top of the page
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
function scrollFunction() {
    // Can change the number to change when the btn appears
    if (document.body.scrollTop > 600 || document.documentElement.scrollTop > 600) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}