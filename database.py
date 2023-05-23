import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    port=3310,
    user='root',
    password='your_password',
    database='your_module'
)

cursor = cnx.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS movies (
    ID INT,
    MOVIE VARCHAR(255),
    DATE VARCHAR(255),
    MCU_PHASE VARCHAR(255)
)
'''
cursor.execute(create_table_query)

data = [
    ['1', 'IronMan', 'May2,2008', 'Phase1'],
    ['2', 'TheIncredibleHulk', 'June13,2008', 'Phase1'],
    ['3', 'IronMan2', 'May7,2010', 'Phase1'],
    ['4', 'Thor', 'May6,2011', 'Phase1'],
    ['5', 'CaptainAmerica:TheFirstAvenger', 'July22,2011', 'Phase1'],
    ['6', "Marvel'sTheAvengers", 'May4,2012', 'Phase1'],
    ['7', 'IronMan3', 'May3,2013', 'Phase2'],
    ['8', 'Thor:TheDarkWorld', 'November8,2013', 'Phase2'],
    ['9', 'CaptainAmerica:TheWinterSoldier', 'April4,2014', 'Phase2'],
    ['10', 'GuardiansoftheGalaxy', 'August1,2014', 'Phase2'],
    ['11', 'Avengers:AgeofUltron', 'May1,2015', 'Phase2'],
    ['12', 'Ant-Man', 'July17,2015', 'Phase2'],
    ['13', 'CaptainAmerica:CivilWar', 'May6,2016', 'Phase3'],
    ['14', 'DoctorStrange', 'May5,2017', 'Phase3'],
    ['16', 'Spider-Man:Homecoming', 'July7,2017', 'Phase3'],
    ['17', 'Thor:Ragnarok', 'November3,2019', 'Phase3'],
    ['18', 'BlackPanther', 'February16,2018', 'Phase3'],
    ['19', 'Avengers:InfinityWar', 'April27,2018', 'Phase3'],
    ['20', 'Ant-ManandtheWasp', 'July6,2018', 'Phase3'],
    ['21', 'CaptainMarvel', 'March8,2019', 'Phase3'],
    ['22', 'Avengers:Endgame', 'April26,2019', 'Phase3']
]

insert_query = "INSERT INTO movies (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)"

for row in data:
    cursor.execute(insert_query, row)

cnx.commit()
cursor.close()
cnx.close()


#In order for this code to work please create schema named your_module in your mysql workbench and make sure your password is correct and port is correct