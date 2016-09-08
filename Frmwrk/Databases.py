GEN_CON = '''
*General Information
********************
Connection Name: %s
Host name / IP address: %s
Port: %d
User name: %s
Encoding: %s
'''

class mysql(object):
    def __init__(self,engine=None):
        self.engine = engine
        self.con = None

    def __call__(self, *args, **kwargs):
        import MySQLdb
        print GEN_CON % (kwargs['name'],kwargs['host'],int(kwargs['port']),kwargs['user'],kwargs['encode'])
        try:
            self.con = MySQLdb.connect(charset=kwargs['encode'],host=kwargs['host'],user=kwargs['user'],
                                passwd=kwargs['passwd'],db=kwargs['db'],port=int(kwargs['port']))
            return self
        except:
            raise

    def __del__(self):
        if self.con:
            self.con.close()

    def execute(self,sql):
        cur = self.con.cursor()
        cur.execute(sql)
        cur.close()

    def __str__(self):
        return "FTT dbs connection"

    def __repr__(self):
        return "FTT dbs connection"