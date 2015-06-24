# TransPy
small opendata project - get connections leaving from a specific location currently by ID

#How to use it
To start using the script first checkout the code from the github repository
```
git clone git@github.com:avarx/TransPy.git
```

Let’s run stationboard.py

```
[user]$ python stationboard.py -i <ID>
```
#Get a location ID
```
http://transport.opendata.ch/v1/locations?query=<Stationname>
E.g.
http://transport.opendata.ch/v1/locations?query=Bern
```

#Source
http://transport.opendata.ch/