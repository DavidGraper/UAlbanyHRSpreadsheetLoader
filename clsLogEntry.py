class LogEntry:
    def __init__(self, id, excelfilename, key, lastname, firstname, tableupdated, fieldupdated, textbeforeupdate,
                 textafterupdate, updated, notes):
        self._excelfilename = excelfilename
        self._key = key
        self._lastname = lastname
        self._firstname = firstname
        self._tableupdated = tableupdated
        self._fieldupdated = fieldupdated
        self._textbeforeupdate = textbeforeupdate
        self._textafterupdate = textafterupdate
        self._updated = updated
        self._notes = notes

    @property
    def excelfilename(self):
        print("getter called for excelfilename")
        return self._excelfilename

    @excelfilename.setter
    def excelfilename(self, new_excelfilename):
        print("setter called for excelfilename")
        self._excelfilename = new_excelfilename

    @excelfilename.deleter
    def excelfilename(self):
        print('calling the deleter on excelfilename')
        self.excelfilename = None

    @property
    def key(self):
        print("getter called for key")
        return self._key

    @key.setter
    def key(self, new_key):
        print("setter called for key")
        self._key = new_key

    @key.deleter
    def key(self):
        print('calling the deleter on key')
        self.key = None

    @property
    def lastname(self):
        print("getter called for lastname")
        return self._lastname

    @lastname.setter
    def lastname(self, new_lastname):
        print("setter called for lastname")
        self._lastname = new_lastname

    @lastname.deleter
    def lastname(self):
        print('calling the deleter on lastname')
        self.lastname = None

    @property
    def firstname(self):
        print("getter called for firstname")
        return self._firstname

    @firstname.setter
    def firstname(self, new_firstname):
        print("setter called for firstname")
        self._firstname = new_firstname

    @firstname.deleter
    def firstname(self):
        print('calling the deleter on firstname')
        self.firstname = None

    @property
    def tableupdated(self):
        print("getter called for tableupdated")
        return self._tableupdated

    @tableupdated.setter
    def tableupdated(self, new_tableupdated):
        print("setter called for tableupdated")
        self._tableupdated = new_tableupdated

    @tableupdated.deleter
    def tableupdated(self):
        print('calling the deleter on tableupdated')
        self.tableupdated = None

    @property
    def fieldupdated(self):
        print("getter called for fieldupdated")
        return self._fieldupdated

    @fieldupdated.setter
    def fieldupdated(self, new_fieldupdated):
        print("setter called for fieldupdated")
        self._fieldupdated = new_fieldupdated

    @fieldupdated.deleter
    def fieldupdated(self):
        print('calling the deleter on fieldupdated')
        self.fieldupdated = None

    @property
    def textbeforeupdate(self):
        print("getter called for textbeforeupdate")
        return self._textbeforeupdate

    @textbeforeupdate.setter
    def textbeforeupdate(self, new_textbeforeupdate):
        print("setter called for textbeforeupdate")
        self._textbeforeupdate = new_textbeforeupdate

    @textbeforeupdate.deleter
    def textbeforeupdate(self):
        print('calling the deleter on textbeforeupdate')
        self.textbeforeupdate = None

    @property
    def textafterupdate(self):
        print("getter called for textafterupdate")
        return self._textafterupdate

    @textafterupdate.setter
    def textafterupdate(self, new_textafterupdate):
        print("setter called for textafterupdate")
        self._textafterupdate = new_textafterupdate

    @textafterupdate.deleter
    def textafterupdate(self):
        print('calling the deleter on textafterupdate')
        self.textafterupdate = None

    @property
    def updated(self):
        print("getter called for updated")
        return self._updated

    @updated.setter
    def updated(self, new_updated):
        print("setter called for updated")
        self._updated = new_updated

    @updated.deleter
    def updated(self):
        print('calling the deleter on updated')
        self.updated = None

    @property
    def notes(self):
        print("getter called for notes")
        return self._notes

    @notes.setter
    def notes(self, new_notes):
        print("setter called for notes")
        self._notes = new_notes

    @notes.deleter
    def notes(self):
        print('calling the deleter on notes')
        self.notes = None

# @property
# def director(self):
#     print("getter called for director")
#     return self._director
#
# @director.setter
# def director(self, new_director):
#     print("setter called for director")
#     self._director = new_director
#
# @director.deleter
# def director(self):
#     print('calling the deleter on director')
#     self.director = None
#
# @property
# def cost(self):
#     print("Getter called for cost")
#     return self._cost
#
# @cost.setter
# def cost(self, new_cost):
#     print("setter called for cost")
#     self._cost = new_cost
#
# @cost.deleter
# def cost(self):
#     print("deleter called for director")
#     self._cost = None
#
# @property
# def revenue(self):
#     print("Getter called for revenue")
#     return self._revenue
#
# @revenue.setter
# def revenue(self, new_revenue):
#     print("setter called for revenue")
#     self._revenue = new_revenue
#
# @revenue.deleter
# def revenue(self):
#     print("deleter called for revenue")
#     self._revenue = None
