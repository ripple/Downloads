import sys, sqlite3

if len(sys.argv) < 4:
    print 'Usage: python %s <skype datadir> <chatname> <export filename> [author1] [author2] ...' % sys.argv[0]
    sys.exit(1)

sql = "SELECT datetime(`Messages`.`timestamp`, 'unixepoch', 'localtime'), `Messages`.`from_dispname`, `Messages`.`body_xml`  FROM `Messages`, `Chats`"
sql += " WHERE `Messages`.`chatname` = `Chats`.`name` AND `Chats`.`friendlyname` LIKE ? "
if len(sys.argv) > 4:
    sql += ' AND `Messages`.`author` IN (?' + ',?'*(len(sys.argv)-5) + ') '
sql += "ORDER BY `Messages`.`timestamp`"

params = ['%' + sys.argv[2] + '%']
for i in range(4, len(sys.argv)):
    params.append(sys.argv[i])

conn = sqlite3.connect('%s/main.db' % sys.argv[1])
c = conn.cursor()
file = open(sys.argv[3], 'w')
for row in c.execute(sql, params):
    msg = '(%s) %s: %s\n' % (row[0], row[1], row[2])
    file.write(msg.encode('utf8'))
