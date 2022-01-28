import ProcessDBRecords

def IsEmpIDInBiologyDatabase(ualbanyempid):
    fields = ["ualbanyempid"]
    p1 = ProcessDBRecords.ExecuteSQLCommand("select ualbanyempid from data_persons where ualbanyempid = '{0}'".format(ualbanyempid), fields)
    return1 = p1.ExecuteSQLCommandReturnDictionaryCollection()

    p1.printsqlstring()
    p1.printfields()
    del p1

    if len(return1) == 1:
        return True
    else:
        return False


def GetPersonIDByLastnameFirstname(lastname, firstname):
    fields = ["id"]
    p1 = ProcessDBRecords.ExecuteSQLCommand("select id from data_persons where lastname = '{0}' and firstname = '{1}'".format(lastname, firstname), fields)
    return1 = p1.ExecuteSQLCommandReturnDictionaryCollection()

    p1.printsqlstring()
    p1.printfields()
    del p1

    if len(return1) == 1:
        return return1[0]["id"]
    else:
        return ""
