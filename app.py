import MySQLdb
import datetime 
import config
db = MySQLdb.connect(config.host,
		    config.user,
		    config.passwd,
		    config.db)

cur = db.cursor()

def monthly_unique_users():
    cur.execute("SELECT COUNT(DISTINCT uuid) from analytics")
    print "monthly active"
    for row in cur.fetchall():
	print row[0]

def weekly_unique_users():
    weeks = ["2014-07-01", "2014-07-08", "2014-07-15", "2014-07-22", "2014-07-31"]
    print "start","end","\t","active"
    print "-----","---","\t","------"
    for w in xrange(len(weeks)-1):
	start = weeks[w]
	end = weeks[w+1]
	cur.execute("SELECT COUNT(DISTINCT uuid) from analytics where date between %s and %s", (start,end,))
	for row in cur.fetchall():
	    print start,end,"\t",row[0]


def daily_unique_users():
    print "start","end","\t","active"
    print "-----","---","\t","------"
    for w in xrange(30):
	start = "2014-07-"+str(w)
	end = "2014-07-"+str(w+1)
	cur.execute("SELECT COUNT(DISTINCT uuid) from analytics where date between %s and %s", (start,end,))
	for row in cur.fetchall():
	    print start,end,"\t",row[0]

def monthly_active_users(k):
    """
	k = minimum events to count as active
    """
    pass

def daily_active_users(k):
    users = {}
    print "start\t","end","\t","active"
    print "-----\t","---","\t","------"
    for w in xrange(30):
	daily_count = 0
	start = "2014-07-"+str(w+1)
	end = "2014-07-"+str(w+2)
	cur.execute("SELECT uuid, handle from analytics where date between %s and %s", (start,end,))
	for row in cur.fetchall():
	    if row[0] not in users:
		users[row[0]] = 0
	    users[row[0]] += 1
	    
	    if users[row[0]] > k:
		daily_count += 1
		break
	
	print start, "\t", end, "\t", str(daily_count)

daily_active_users(3)
