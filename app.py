import MySQLdb
import datetime 
import config
db = MySQLdb.connect(config.host,
		    config.user,
		    config.passwd,
		    config.db)

cur = db.cursor()

def monthly_active_users(cur):
    """
	currently defining active as having registered at least one event
    """
    cur.execute("SELECT COUNT(DISTINCT uuid) from analytics")
    print "monthly active"
    for row in cur.fetchall():
	print row[0]

def weekly_active_users(cur):
    weeks = ["2014-07-01", "2014-07-08", "2014-07-15", "2014-07-22", "2014-07-31"]
    print "start","end","\t","active"
    print "-----","---","\t","------"
    for w in xrange(len(weeks)-1):
	start = weeks[w]
	end = weeks[w+1]
	cur.execute("SELECT COUNT(DISTINCT uuid) from analytics where date between %s and %s", (start,end,))
	for row in cur.fetchall():
	    print start,end,"\t",row[0]


def daily_active_users(cur):
    print "start","end","\t","active"
    print "-----","---","\t","------"
    for w in xrange(30):
	start = "2014-07-"+str(w)
	end = "2014-07-"+str(w+1)
	cur.execute("SELECT COUNT(DISTINCT uuid) from analytics where date between %s and %s", (start,end,))
	for row in cur.fetchall():
	    print start,end,"\t",row[0]


monthly_active_users(cur)
weekly_active_users(cur)
daily_active_users(cur)
