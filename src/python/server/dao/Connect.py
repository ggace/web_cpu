import pymysql

con = None

def connect():
    global con;
    # STEP 2: MySQL Connection 연결
    con = pymysql.connect(host='localhost', port=3307, user='pyCPUid', password='pyCPUpw1234',
                        db='cpuServer', charset='utf8',
                        autocommit=True,
                      cursorclass=pymysql.cursors.DictCursor)

def execute(sql):
    global con
    # STEP 3: Connection 으로부터 Cursor 생성
    cur = con.cursor()
    
    # STEP 4: SQL문 실행 및 Fetch
    
    cur.execute(sql)
    
    # 데이타 Fetch
    rows = cur.fetchall()
    return rows     # 전체 rows

def closeDB():
    global con
    # STEP 5: DB 연결 종료
    con.close()
    
