#Imports

import mysql.connector as mysql
import webview

#----------------------------------------------------------------------------------------------------#

#SQL Connection

mydb=mysql.connect(host="localhost",user="root",password="",database="BlackHoles")
mycursor=mydb.cursor()

#----------------------------------------------------------------------------------------------------#

#Offline Values:
'''
#Black Hole Table
mycursor.execute("Create table Blackholes(BName varchar(35) Primary key,Image varchar(200),Type varchar(30),Location varchar(200),Distance varchar(150))")

#Basic Info Table
mycursor.execute("Create table Info(BName varchar(35) Primary Key,Mass varchar(100),Size varchar(100),Method varchar(100),Facts varchar(3000))")

#Offline Values:

mycursor.execute("Insert into Blackholes Values('4U 1543-47','http://blackholes.stardate.org/images/binary_artist_impression.jpg','Stellar mass','In the constellation Lupus','25,000 light-years (7500 parsecs)')")
mycursor.execute("Insert into Info Values('4U 1543-47','9 times the mass of the Sun','Diameter roughly equal to the size of a large city','Detection of an accretion disk','Once every decade or so, the star system 4U 1543-47 erupts, producing a powerful torrent of X-rays. The first eruption was recorded by the Uhuru X-ray satellite in 1971, with subsequent bursts in 1983, 1992, and 2002. At its maximum, the system shines up to 20 million times brighter in X-rays during these outbursts than during the years-long quiet time between them. The system consists of the black hole plus a companion star, discovered after the 1983 eruption, that is roughly twice as massive as the Sun. The two orbit each other once every 1.1 days.')")

#mycursor.execute("Insert into Blackholes Values('Cygnus X-1','http://blackholes.stardate.org/images/cygnus_x1.jpg','Stellar mass','In the constellation Cygnus','7,200 light-years')")
#mycursor.execute("Insert into Info Values('Cygnus XR-1','21 times the mass of the Sun','Diameter 78 miles (126 km), equal to the size of a large American county','Measuring the motions of gas','Several thousand light-years away, near the "heart" of Cygnus, the swan, two stars are locked in a gravitational embrace. One star is a blue supergiant, known as HDE 226868. It is more than 40 times as massive as the Sun and 300,000 times brighter. The other star is more than 20 times the mass of the Sun, but it's extremely small. The object must be the collapsed core of a star. Its mass is too great to be a white dwarf or a neutron star, though, so it must be a black hole -- the corpse of a star that once resembled the supergiant. The system is called Cygnus X-1, indicating it was the first source of X-rays discovered in the constellation Cygnus. Discovered by a small rocket launched from New Mexico in 1964 and studied extensively by the Uhuru X-ray satellite in 1971, it was the first suspected black hole.')")

mycursor.execute("Insert into Blackholes Values('Omega Centauri','http://blackholes.stardate.org/images/eso1119b.jpg','Intermediate mass','In the constellation Centaurus','17,000 light-years')")
mycursor.execute("Insert into Info Values('Omega Centauri','40,000 times the mass of the Sun','Diameter 150,000 miles (240,000 km), about two-thirds of the distance from Earth to the Moon','Measuring the motions of stars','For almost two centuries, astronomers have classified Omega Centauri as a globular cluster -- a dense collection of stars packed into a spherical region of space only a few dozen light-years across. Yet in more recent years, they have started having doubts, because Omega Centauri is unlike any other globular cluster in the Milky Way galaxy. For one thing, it is by far the largest and most massive globular in the galaxy -- about 10 million times the mass of the Sun, compared to a few hundred thousand solar masses for most other globulars. For another, it is more flattened than any other globular cluster. And while other globulars contain only very old stars, Omega Centauri has a mixed population that includes many younger stars. All of this evidence has suggested that Omega Centauri may really be a small galaxy that was captured by the Milky Way. And a finding from 2008 appears to seal the deal: a black hole about 40,000 times as massive as the Sun appears to inhabit its core.')")

mycursor.execute("Insert into Blackholes Values('NGC 224','http://blackholes.stardate.org/images/m31y.jpg','Supermassive','in the constellation Andromeda','2.5 million light-years')")
mycursor.execute("Insert into Info Values('NGC 224','30 million times the mass of the Sun','Diameter roughly equal to the orbit of Venus.','Measuring the motions of stars','Our home galaxy, the Milky Way, is part of a collection of about three dozen galaxies known as the Local Group. These galaxies move through space as a single unit bound together by their mutual gravitational pull. The largest member of the Local Group is the Andromeda Galaxy, M31. Like the Milky Way, Andromeda is a giant spiral galaxy, so it looks like a pinwheel spinning through space. It spans about 125,000 light-years, and contains several hundred billion stars. At a distance of about 2.4 million light-years, it is the closest large galaxy to the Milky Way, and the only one that is visible to the unaided eye.')")

mycursor.execute("Insert into Blackholes Values('M77','http://blackholes.stardate.org/images/ngc1068_comp.jpg','Supermassive','in the constellation Cetus','50 million to 60 million light-years')")
mycursor.execute("Insert into Info Values('M77','15 million times the mass of the Sun','Slightly smaller than Mercurys orbit around the Sun','Measuring the motions of gas','M77 is one of the most intensively studied galaxies in the sky. It was among the first galaxies for which astronomers measured a large redshift, which indicated that the galaxy is moving away from us at high speed as part of the general expansion of the universe. Later observations of the galaxys core showed strong spectral emission lines -- specific patterns of wavelengths that are generated when atoms of hydrogen, oxygen, or nitrogen are bombarded by high-energy radiation. Furthermore, these emission lines were very broad, indicating that the gas clouds that contain the atoms were moving at hundreds of thousands of miles per hour. Strong radio signals also were detected from a tiny point in M77s nucleus. From all these lines of evidence, astronomers suspected that a large power source must lie in the core of this galaxy -- probably a supermassive black hole.')")

mydb.commit()
'''
#----------------------------------------------------------------------------------------------------#

class api:
    a=""
#Admin Functions
    
    def Pass_Check(self,password):
        if password=="123":
            return True
        else:
            return False
    
    def insert_Blackhole(self,name,image,typ,loc,dis,mass,size,meth,facts):
        try:
            mycursor.execute("Insert into Blackholes Values('{}','{}','{}','{}','{}')".format(name,image,typ,loc,dis))
            mycursor.execute("Insert into Info Values('{}','{}','{}','{}','{}')".format(name,mass,size,meth,facts))
            mydb.commit()
            return True
        except:
            return False

    def Search_Blackholes(self):
        try:
            html=""
            mycursor.execute("Select * from Blackholes")
            for rec in mycursor.fetchall():
                html=html+'''<li id='{}' onclick='Display_Pop_Up_Blackhole(this.id)'>

                    <div><img src="{}" width="50" height="50"></div>
                    <div>{}</div>
                    <div>{}</div>
                    <div>{}</div>
                    <div>{}</div>   
                 
                </li>'''.format(rec[0],rec[1],rec[0],rec[2],rec[3],rec[4])
            return html
        except Exception as e:
            print(e)
    
    def search_specific_blackhole(self,name,type):
        html=""
        try:
            if name is not None and type is not None:
                mycursor.execute("Select * from blackholes where Bname='{}' or Type='{}'".format(name,type))
                for rec in mycursor.fetchall():
                    html=html+'''<li id='{}' onclick='Display_User_Specific(this.id)'>

                    <div><img src="{}" width="50" height="50"></div>
                    <div>{}</div>
                    <div>{}</div>
                    <div>{}</div>
                    <div>{}</div>   
                 
                </li>'''.format(rec[0],rec[1],rec[0],rec[2],rec[3],rec[4])
                return True,html

            elif name is not None and type is None:
                mycursor.execute("Select * from blackholes where Bname='{}'".format(name))
                for rec in mycursor.fetchall():
                    html=html+'''<li id='{}' onclick='Display_User_Specific(this.id)'>

                    <div><img src="{}" width="50" height="50"></div>
                    <div>{}</div>
                    <div>{}</div>
                    <div>{}</div>
                    <div>{}</div>   
                 
                </li>'''.format(rec[0],rec[1],rec[0],rec[2],rec[3],rec[4])
                return True,html

            elif name is None and type is not None:
                mycursor.execute("Select * from blackholes where Type='{}'".format(type))
                for rec in mycursor.fetchall():
                    html=html+'''<li id='{}' onclick='Display_User_Specific(this.id)'>

                    <div><img src="{}" width="50" height="50"></div>
                    <div>{}</div>
                    <div>{}</div>
                    <div>{}</div>
                    <div>{}</div>   
                 
                </li>'''.format(rec[0],rec[1],rec[0],rec[2],rec[3],rec[4])
                return True,html

            else:
                return False,0
        except Exception as e:
            return False
            print(e)
            
    def pop_up_data(self,name): 
        try:
            print("appending")
            mycursor.execute("select b.BName,type,image,location,distance,mass,size,method,facts from Blackholes b,Info i where b.BName= i.BName and b.BName ='{}'".format(name))
            q = mycursor.fetchone()
            return q
        except Exception as e:
            print(e)
    
    def Update_Blackholes(self,id,name,ntype,img,loc,dis,mass,size,meth,facts):
        try:
            print("updating")
            if name!=id:
                c="Update Blackholes set BName='{}' where BName='{}'".format(name,id)
                mycursor.execute(c)
                c="Update Info set BName='{}' where BName='{}'".format(name,id)
                mycursor.execute(c)
            else:
                pass
            c="Update Blackholes set Image='{}' where BName='{}'".format(img,name)
            mycursor.execute(c)
            c="Update Blackholes set Type='{}' where BName='{}'".format(ntype,name)
            mycursor.execute(c)
            c="Update Blackholes set Location='{}' where BName='{}'".format(loc,name)
            mycursor.execute(c)
            c="Update Blackholes set Distance='{}' where BName='{}'".format(dis,name)
            mycursor.execute(c)
            c="Update Info set Mass='{}' where BName='{}'".format(mass,name)
            mycursor.execute(c)
            c="Update Info set Size='{}' where BName='{}'".format(size,name)
            mycursor.execute(c)
            c="Update Info set Method='{}' where BName='{}'".format(meth,name)
            mycursor.execute(c)
            c="Update Info set Facts='{}' where BName='{}'".format(facts,name)
            mycursor.execute(c)
            mydb.commit()
        except Exception as e:
            print(e)
        
    def Search_Blackholes_User(self):
        try:
            html=""
            mycursor.execute("Select * from Blackholes")
            for rec in mycursor.fetchall():
                html=html+'''<li id='{}' onclick='Display_User_Blackhole(this.id)'>

                    <div><img src="{}" width="50" height="50"></div>
                    <div>{}</div>
                    <div>{}</div>
                    <div>{}</div>
                    <div>{}</div>   
                 
                </li>'''.format(rec[0],rec[1],rec[0],rec[2],rec[3],rec[4])
            return html
        except Exception as e:
            print(e)
    
    def User_Display(self,name):
        try:
            mycursor.execute("select b.BName,type,image,location,distance,mass,size,method,facts from Blackholes b,Info i where b.BName= i.BName and b.BName ='{}'".format(name))
            q = mycursor.fetchone()
            print(q)
            return q
        except Exception as e:
            print(e)


api = api()
with open("Black holes.html", "r") as f:
    r = f.read()
    webview.create_window(title='Black holes', html=r, js_api=api)
    webview.start(debug=True)
