"""
To make it easier to apply and understand, the only changes I made to the requirement are:
    instead of 72 hours, I limited the time to 10 seconds
    in jsons at timer, 1 second is equivalent to one hour

customers who stay less than or equal to 3 seconds are those who stay "less than 2 hours" in the parking lot:
    time <=3 sec => 2 hr

customers who stay between 3 and 7 seconds are those who "exceed 2 hours":
    3 sec < time < 7 sec => 2+ hours

Customers who stay longer than 7 seconds are those who stay "3 days":
    7 sec <= time => 3 days

Customers who have exceeded 7 seconds, a.k.a. "3 days," will have their pariah changed from False to True

Otherwise, everything is exactly as in the project requirement (I hope)
We already have 10 customers sorted. If we run the main function, it will add 10 more and sort them.
In the end, we will have 20 customers, all nicely sorted in their place.

I tried to explain as best I could everything I did.
All my drafts are nothing important.
"""

from clients import clients

if __name__ == "__main__":
    filepath = "JSON/data/clients.json"
    clients(filepath, "Lynn", "Newton", "(206) 342-8631", "Seattle, WA")
    clients(filepath, "Genaro", "Willis", "(717) 550-1675", "Harrisburg, PA")
    clients(filepath, "Rosanne", "Maldonado", "(248) 762-0356", "Farmington Hills, MIV")
    clients(filepath, "Pauline", "Figueroa", "(253) 644-2182", "Auburn, WA")
    clients(filepath, "Rickey", "Clements", "(212) 658-3916", "New York City, NY")
    clients(filepath, "Jeanne", "Wolf", "(209) 300-2557", "Ceres, CA")
    clients(filepath, "Dustin", "Carrillo", "(262) 162-1585", "Menomonee Falls, WI")
    clients(filepath, "Sally", "Reeves", "(252) 258-3799", "Greenville, NC")
    clients(filepath, "Jaclyn", "Andersen", "(234) 109-6666", "Akron, OH")
    clients(filepath, "Esteban", "Shelton", "(201) 874-8593", "Bayonne, NJ")
