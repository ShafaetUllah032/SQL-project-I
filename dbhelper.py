import mysql.connector

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password="#define cse 2018331032;",
                port='3306',
                database='flights'
            )
            self.mycursor = self.conn.cursor()
            print('\t and connection done ___ ')

        except:
            print('connection error')

    def fetch_city_names(self):


        city=[]
        self.mycursor.execute("""
                SELECT DISTINCT(Destination) FROM flights.flights
                UNION
                SELECT DISTINCT(Source) FROM flights.flights
                """)
        data = self.mycursor.fetchall()
        for i in data:
            city.append(i[0])

        return city

    def fetch_all_flights(self,source_city,destination_city):

        details=[]
        self.mycursor.execute("""
        select airline,route,dep_time,Duration,price from flights.flights 
        where Source='{}' and Destination='{}'
        order by Price asc , Duration asc ,Dep_Time asc
        """.format(source_city,destination_city))

        data=self.mycursor.fetchall()

        return data

    def fetch_airline_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute(
            """
            SELECT Airline,COUNT(*) FROM flights
            GROUP BY Airline
            """
        )
        data=self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency

    def busy_airport(self):

        city = []
        frequency = []

        self.mycursor.execute("""
                SELECT Source,COUNT(*) FROM (SELECT Source FROM flights
        							UNION ALL
        							SELECT Destination FROM flights) t
                GROUP BY t.Source
                ORDER BY COUNT(*) DESC
                """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_frequency(self):

        date = []
        frequency = []

        self.mycursor.execute("""
                SELECT Date_of_Journey,COUNT(*) FROM flights
                GROUP BY Date_of_Journey
                """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency