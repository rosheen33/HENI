import pandas as pd
import pandasql as ps


def main():
    flights = pd.read_csv("Data_Engineer_test/candidateEvalData/flights.csv")
    airports = pd.read_csv("Data_Engineer_test/candidateEvalData/airports.csv")
    weather = pd.read_csv("Data_Engineer_test/candidateEvalData/weather.csv")
    airlines = pd.read_csv("Data_Engineer_test/candidateEvalData/airlines.csv")

    sql = '''
    SELECT *
    FROM flights
    '''
    result = ps.sqldf(sql)
    print(result.head(10))

    # Add full airline name to the flights dataframe and
    # show the arr_time, origin, dest and the name of the airline.
    sql_task1 = '''
    SELECT air_time, origin, dest, name
    FROM flights
    INNER JOIN airlines 
    ON flights.carrier=airlines.carrier 
    '''

    result = ps.sqldf(sql_task1)
    print(result.head(10))

    # Filter resulting data.frame to include only flights
    # containing the word JetBlue
    sql_task2 = '''
    SELECT air_time, origin, dest, name
    FROM flights
    INNER JOIN airlines 
    ON flights.carrier=airlines.carrier 
    WHERE airlines.name LIKE "%JetBlue%"
    '''

    result = ps.sqldf(sql_task2)
    print(result.head(10))

    # Summarise the total number of flights by origin in ascending.
    sql_task3 = '''
    SELECT origin, count(flight) as numFlights
    FROM flights
    INNER JOIN airlines 
    ON flights.carrier=airlines.carrier 
    WHERE airlines.name LIKE "%JetBlue%"
    GROUP BY origin
    ORDER BY numFlights
    '''

    result = ps.sqldf(sql_task3)
    print(result.head(10))

    # Filter resulting data.frame to return only origins with more than 100 flights.
    sql_task4 = '''
    SELECT origin, count(flight) as numFlights
    FROM flights
    INNER JOIN airlines 
    ON flights.carrier=airlines.carrier 
    WHERE airlines.name LIKE "%JetBlue%"
    GROUP BY origin
    HAVING count(origin) > 100
    ORDER BY numFlights
    '''

    result = ps.sqldf(sql_task4)
    print(result.head(10))


if __name__ == "__main__":
    main()
