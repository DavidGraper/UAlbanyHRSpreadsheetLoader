from datetime import date
import ProcessDBRecords


def addlogentry(excelfilename, firstname, lastname, personid, notes, updatedvalue):

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


def addgradstudentrecordfrom_UADW_GRAD_AVNS_ADDR_RowDict(DictIn):

    # ID               (UAlbany Empid)
    # Last (lastname)
    # First Name(firstname)
    # Desc             (Description => always "Graduate")
    # Dept1            (Department => always "BIOSCI")
    # Plan10           (Biology field/degree:  BIO-MS (Master's), BIO-MSFBM (Master's Forensic Molecular Biology), BIO-MSFOR (Master's Forensics), BIO-NON (Grad students enrolled to take grad classes but not admitted to program), BIO-PHD (PhD program))
    # Subpln10         (Always blank)
    # AVN              (?? UNKNOWN ??)
    # Registered       (?? UNKNOWN ?? : Either "Y" or "N")
    # Pres Reg         (?? UNKNOWN ?? : Either "Y" or "N")
    # Advisor          (Advisor name : "<lname>,<fname>")
    # Advisor2         (2nd Advisor name : "<lname>,<fname>")
    # Admit Term       (Admitted term - First is always the #2, then year (e.g. 21), then either 1=Winter 3=Spring 6=Summer 9=Fall (2219 == Fall 2021)
    # Month            (Month of admission)
    # Year             (Year of admission)
    # PriAdrType       (Primary address type:  DORM, LOCAL, PERM)
    # Prio Addr1       (Address text 2)
    # Prio Addr2       (Address text 2)
    # Prio Addr3       (Address text 3)
    # Prio Addr4       (Address text 4)
    # Prio City        (Address text City)
    # Prio State       (Two-letter code, includes some non-US codes [AB, AP, UP])
    # Prio Zip         (Zip code text [dirty])
    # Prio Cntry       (Country [AZE, CAN, GHA, IND, NGA, TWN, USA])
    # Camp email       (Campus email [all albany.edu])
    # Statute Term     (Statute term - First is always the #2, then year (e.g. 21), then either 1=Winter 3=Spring 6=Summer 9=Fall (2219 == Fall 2021)
    # Plan20 (Empty)
    # Loc Phone        (Local phone)
    # Perm Phone       (Permanent phone)

    ACTIVE = "1"
    UNIVERSITYDATASOURCE = "1"
    BIOLOGYPERSONTYPE = "3" # Graduate student

    try:
        strSQL = "insert into data_persons (lastname, firstname, ualbanyempid, active, persontypeid, datasourceid)" \
            " values ('{0}', '{1}', '{2}', {3}, {4}, {5});".format(DictIn["Last"],
                                                                   DictIn["First Name"],
                                                                   DictIn["ID"],
                                                                   ACTIVE,
                                                                   BIOLOGYPERSONTYPE,
                                                                   UNIVERSITYDATASOURCE)

        fieldnames = []
        obj1 = ProcessDBRecords.ExecuteSQLCommand(strSQL, fieldnames)
        obj1.ExecuteSQLCommandNoReturnValue()

    except Exception as e:
        print(e)
