"""
    File generators for tasks
    Cause repeating oneself is bad :)
    Copyright (C) 2017,  Nova Trauben, noah.trauben@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import random
import os


def task3_servers():
    nlist = ['Benny Wells', 'Rene Roy', 'Erma Gray', 'Cassandra Bradley',
             'Mildred Butler', 'Bob Farmer', 'Roxanne Gardner', 'Manuel Riley',
             'Samantha Byrd', 'Nelson Snyder', 'Alfred Haynes', 'Sheri Pittman',
             'Timothy Neal', 'Kelli Lucas', 'Alexandra Higgins', 'Gustavo Cain',
             'Claude Tyler', 'Shannon Vega', 'Troy Watts', 'Byron Campbell',
             'Gwen Arnold', 'Mary Bryant', 'Jaime Jackson', 'Kerry Carr', 'Ira Klein',
             'Danny Kim', 'Brent Torres', 'Wesley Delgado', 'Elena Carpenter',
             'Melvin Norton', 'Angela Mcdaniel', 'Mandy Hodges', 'Nick Webb',
             'Francisco Warren', 'Sadie Nichols', 'Ron Hunter', 'Bradley Fox',
             'Elvira Harrington', 'Chuck Norris', 'Todd Kelley', 'Gary Lyons',
             'Josefina Meyer', 'Frankie Rowe', 'Lee Abbott', 'Willis Sims',
             'Margaret Johnston', 'Sara Ball', 'Deborah Maxwell', 'Heidi Brady',
             'Adrian Gibson', 'Ramona Phillips', 'Alex Carroll', 'Bert Wallace',
             'Delia Martin', 'Milton Newton', 'Denise Park', 'David Gilbert',
             'Maxine Rice', 'Pamela Watson', 'Stella Moran', 'Jeannie Cruz',
             'Albert EstradaElijah', 'Lindsey Jane', 'Fields Emma', 'Clayton Sue',
             'Silva Roman', 'Patterson Sandra', 'Burns Tabitha', 'Frazier Patty',
             'Harper Dallas', 'Barton Dustin', 'Perez Rufus', 'Morris Jeremy',
             'Manning Mae', 'Reynolds Raymond', 'Collins Pete', 'Price Colin',
             'Hogan Zachary', 'Dunn Shaun', 'Griffith Flora', 'Ramirez Henry',
             'Gonzales Dexter', 'Hale Nathaniel', 'Daniels Maureen', 'Mckinney Dewey',
             'Ortiz Toni', 'Bush Ervin', 'Tucker Louise', 'Drake Roderick',
             'Alvarado Leslie', 'Henderson Casey', 'Coleman Sally', 'White Maurice',
             'George Wilma', 'Walsh Calvin', 'Bell Felicia', 'Perry Santiago',
             'Tate Raquel', 'Johnson Ana']
    random.shuffle(nlist)
    for i in range(96):
        os.makedirs('../dynamics/servers/58.53.146.' + str(124 + i) + '/home/')
        f = open('../dynamics/servers/58.53.146.' + str(124 + i) + '/home/README.txt', 'w+')
        f.write("this is " + nlist[i] + "'s work station")
        f.close()
    return
