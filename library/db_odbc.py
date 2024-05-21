import pyodbc

def connect(_driver, _server, _db, _usr, _pwd):
    _Cn = ('DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
           % (_driver, _server, _db, _usr, _pwd))
    return pyodbc.connect(_Cn)


class rst:
    Cn = None
    Cur = None
    Fld = []
    wRec = None
    TotRec = 0
    ActRec = 0
    Eof = 0

    def __init__(self, conn):
        self.Cur = conn.cursor()

    def exec_sql(self, cmd_sql):
        x_sql = str(cmd_sql)
        # print x
        self.Cur.execute(x_sql)

    # ----------------------------------------------
    def sp_exec(self, zCmd, wP=None):
        self.Eof = False
        if wP == None:
            self.Cur.execute(str(zCmd))
        else:
            self.Cur.execute(str(zCmd), *wP)
        zDes = self.Cur.description
        self.Fld = []
        for z in zDes:
            self.Fld.append(z[0].upper())
        self.wRec = self.Cur.fetchall()
        self.TotRec = len(self.wRec)

    # ----------------------------------------------

    def read(self, zCmd, wP=None):
        self.Eof = False
        if wP == None:
            self.Cur.execute(str(zCmd))
        else:
            self.Cur.execute(str(zCmd), wP)
        zDes = self.Cur.description
       
        self.Fld = []
        for z in zDes:
            self.Fld.append(z[0].upper())
        self.wRec = self.Cur.fetchall()
        self.TotRec = len(self.wRec)

    def fetchRecNum(self, zN):
        self.Rec = {}
        r = self.wRec[zN - 1]
        self.ActRec = zN
        i = 0
        for fld in self.Fld:
            exec("self." + fld + "=r[i]")
            i += 1

    def fetchFirst(self):
        self.fetchRecNum(1)

    def fetchLast(self):
        self.fetchRecNum(self.TotRec)

    def fetchNext(self):
        if self.TotRec > self.ActRec:
            self.fetchRecNum(self.ActRec + 1)

        else:
            self.Eof = 1
