# Import list -
import csv
import datetime
with open('populate2.txt', 'rU') as f:
    reader = csv.reader(f,delimiter="\t")
    your_list = list(reader)

cnx = mysql.connector.connect(user = "abhit", password = "testpass", host = "localhost", database = "db_solarfamilyorg", buffered = True)
cursor = cnx.cursor()
query = 'Insert into tab_mapdatarecs(DatasourceID, Latitude, Longitude, Name, Email, Address, UserType, DateSimulatedStart, InstallSystemType, ConversionFactor, PVPanelMake, PVPanelSize, PVPanelInclineAngle, InverterMake, created_at, updated_at) values '
values = ''

for i in range(1, 129):
    DatasourceID = 20150001 + i
    i = your_list[i]
    Latitude = 'NULL' if i[11] == '' else i[11][:-4]
    Longitude = 'NULL' if i[12] == '' else i[12][:-4]
    Name = 'NULL' if i[1] == '' else i[1]
    Email = 'NULL' if i[3] == '' else i[3]
    Address = 'NULL' if i[2] == '' else i[2]
    user_type = (1 if ("LT2" or "L T2") in i[4] else 2)
    DateSimulatedStart = datetime.datetime.now().strftime("%Y-%m-%d")
    InstallSystemType = 1
    ConversionFactor = 0.15
    PVPanelMake = 'NULL' if i[9] == '' else i[9]
    PVPanelSize = 'NULL' if i[6] == '' else i[6].replace(",", ".")
    PVPanelInclineAngle = 12
    InverterMake = 'NULL' if i[10] == '' else i[10]
    created_at = datetime.datetime.now().replace(microsecond=0)
    updated_at = datetime.datetime.now().replace(microsecond=0)
    value = '({DatasourceID}, {Latitude}, {Longitude}, '"'{Name}'"', '"'{Email}'"', '"'{Address}'"', {UserType}, '"'{DateSimulatedStart}'"', {InstallSystemType}, {ConversionFactor}, '"'{PVPanelMake}'"', {PVPanelSize}, {PVPanelInclineAngle}, '"'{InverterMake}'"', '"'{created_at}'"', '"'{updated_at}'"'), '.format(DatasourceID = DatasourceID, Latitude = Latitude, Longitude = Longitude, Name = Name, Email = Email, Address = Address, UserType = user_type, DateSimulatedStart = DateSimulatedStart, InstallSystemType = InstallSystemType, ConversionFactor = ConversionFactor, PVPanelMake = PVPanelMake, PVPanelSize = PVPanelSize, PVPanelInclineAngle = PVPanelInclineAngle, InverterMake = InverterMake, created_at = created_at, updated_at = updated_at)
    values = values + value

values = values[: -2]
query = query + values
cursor.execute(query)
cnx.commit()
