import ProcessDBRecords

def GetBIODBDegreeAreaAndType(UniversityDegreeAreatext):

    #  Degree Type
    #  1 = PhD
    #  2 = MS
    #  3 = Non-Degree
    #
    #  Degree Area
    #  1 = MCDN
    #  2 = EEB
    #  3 = Forensic Biology
    #  4 = Biodiversity
    #  5 = Biological Sciences

    DegreeAreaType = (-1, -1)

    if UniversityDegreeAreatext == "BIO-MS":
        DegreeTypeID = 2
        DegreeAreaID = 5
    elif UniversityDegreeAreatext == "BIO-MSFBM":
        DegreeTypeID = 2
        DegreeAreaID = 3
    elif UniversityDegreeAreatext == "BIO-MSFOR":
        DegreeTypeID = 2
        DegreeAreaID = 3
    elif UniversityDegreeAreatext == "BIO-NON":
        DegreeTypeID = 3
        DegreeAreaID = 5
    elif UniversityDegreeAreatext == "BIO-PHD":
        DegreeTypeID = 1
        DegreeAreaID = 1
    else:
        DegreeTypeID = -1
        DegreeAreaID = -1

    DegreeAreaType = (DegreeTypeID, DegreeAreaID)

    return DegreeAreaType


def GetBIODBSemesterID(UniversityAdmitTerm):

    fields = ["id"]
    p1 = ProcessDBRecords.ExecuteSQLCommand("select id from code_semesters where univcode = {0}".format(UniversityAdmitTerm), fields)
    return1 = p1.ExecuteSQLCommandReturnDictionaryCollection()

    p1.printsqlstring()
    p1.printfields()
    del p1

    if len(return1) == 1:
        return return1[0]["id"]
    else:
        return ""
