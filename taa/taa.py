import os
import re
from neo4j import GraphDatabase

class HelloWorldExample:

    dir_path = os.path.dirname ( os.path.realpath(__file__))

    month = {  "January": "01",
               "February": "02",
               "March": "03",
               "April": "04",
               "May": "05",
               "June": "06",
               "July": "07",
               "August": "08",
               "September": "09",
               "October": "10",
               "November": "11",
               "December": "12" }

    def __init__(self, uri, user, password):
        uri="bolt:localhost:7687"
        self.driver = GraphDatabase.driver(uri, auth=(user,password))

    @staticmethod
    def _create_and_return_show(tx, date):
        result = tx.run ("MERGE (a:Show { date : $date }) "
                         "RETURN a.date + ', from node ' + id(a)", date=date)
        return result.single()[0]

    @staticmethod
    def _create_and_return_song(tx, date, artist, title):
        result = tx.run("MERGE (s:Song { artist : $artist, title : $title }) "
                    "RETURN s.title +', from node ' + id(s)", artist=artist, title =title)
        result = tx.run("MATCH (a:Show) WHERE a.date = $date "
                    "MATCH (s:Song) WHERE s.title = $title AND s.artist = $artist "
                    "MERGE (s) - [:at] -> (a) RETURN a,s", date=date, artist=artist, title =title)

        return result.single()[0]


    def main(self):


        print (self.dir_path)
        with open( r"F:/ATEXT/PRIV/MusikVerwaltung/us_charts.txt",  mode="r", encoding="utf-8") as file:
            lines = file.readlines()

        with self.driver.session() as session:

            for line in lines:
                if len(line) > 0:
                    m = re.search(r'US Top 40 Singles Week (.*)', line.strip())
                    if ( not m is None):
                        print (m[0])
                        dxx = m[0].split()
                        date = dxx[8] + "-" + self.month[dxx[7]] + "-" + dxx[6]
                        print ( "day", dxx[6], dxx[7],dxx[8], date)

                        greeting = session.execute_write(self._create_and_return_show, date)

        #                session.run ("MERGE (a:Show) "
        #                            "SET a.date = $date "
        #                            "RETURN a.message + ', from node ' + id(a)", date=date)

                    m = re.search( r'(US....|....):(..?):(.*):(.*)', line.strip())
                    if ( not m is None):
                        pos = m[2]
                        if int(pos)<41:
                            artist = m[3]
                            title = m[4]
                            print (date , pos, artist, title)
                            greeting = session.execute_write(self._create_and_return_song, date, artist, title)


            session.close()



    def close(self):
            self.driver.close()

if __name__ == "__main__":
    greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "m2")
    greeter.main()
    greeter.close()