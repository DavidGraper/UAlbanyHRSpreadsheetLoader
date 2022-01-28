import ProcessDBRecords

def DeletePersonDegreeAreasAndTypes(personid, **kwargs)

    logmessage = "Deleting person degree areas and types for personid {0}".format(personid)

    try:

        if "datasourceid" in kwargs:
            strSQL = "delete from data_person_biologydegreeareas where personid = {0} and datasourceid = {1}".format(personid, kwargs["datasourceid"])
            logmessage += " datasourceid = {0}".kwargs["datasourceid"]
        else:
            strSQL = "delete from data_person_biologydegreeareas where personid = {0}".format(personid)

        fieldnames = []
        obj1 = ProcessDBRecords.ExecuteSQLCommand(strSQL, fieldnames)
        obj1.ExecuteSQLCommandNoReturnValue()
        del obj1

    except Exception as e:
        logmessage = "*ERROR* " + logmessage + ": '{0}'".format(e)

    LogDBAction(logmessage)


def DeleteExistingAdvisors(personid, **kwargs):

    logmessage = "Deleting person existing advisors for personid {0}".format(personid)

    try:

        if "datasourceid" in kwargs:
            strSQL = "delete from data_person_biologydegreeareas where personid = {0} and datasourceid = {1}".format(personid, kwargs["datasourceid"])
            logmessage += " datasourceid = {0}".kwargs["datasourceid"]
        else:
            strSQL = "delete from data_person_biologydegreeareas where personid = {0}".format(personid)

        fieldnames = []
        obj1 = ProcessDBRecords.ExecuteSQLCommand(strSQL, fieldnames)
        obj1.ExecuteSQLCommandNoReturnValue()
        del obj1

    except Exception as e:
        logmessage = "*ERROR* " + logmessage + ": '{0}'".format(e)

    LogDBAction(logmessage)


def LogDBAction(personid, notes):

    try:

        # Slug values
        tableupdated = "datapersons"
        fieldupdated = ""
        textbeforeupdate = ""
        textafterupdate = ""


        strSQL = "insert into log_reconciliations (excelfilename, tableupdated, fieldupdated, textbeforeupdate, " \
            "textafterupdate, updated, notes, lastname, firstname, key) values ('{0}', '{1}', '{2}', '{3}', '{4}', " \
            "'{5}', '{6}', '{7}', '{8}', '{9}');".format(excelfilename, tableupdated, fieldupdated, textbeforeupdate, \
            textafterupdate, date.today(), notes, lastname, firstname, personid)

        fieldnames = []
        obj1 = ProcessDBRecords.ExecuteSQLCommand(strSQL, fieldnames)
        obj1.ExecuteSQLCommandNoReturnValue()

    except Exception as e:
        print(e)
