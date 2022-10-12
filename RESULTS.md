1-create some artists
::python manage.py shell
from artists.models import Artists
object=Artists(Name='hossam hassan',Link='www.com')
object.save()
object.Name
'hossam hassan'
object.Link
'www.com'
***************************************************************************************
2-list down all artists
Artists.objects.all()
<QuerySet [<Artists: hossam hassan>, <Artists: Ahmed Hassan>, <Artists: mohame Hassan>]>
*****************************************************************************************
3-list down all artists sorted by name
 Artists.objects.order_by("Name")
<QuerySet [<Artists: Ahmed Hassan>, <Artists: hossam hassan>, <Artists: mohame Hassan>]>
****************************************************************************************
4-list down all artists whose name starts with `a`
 Artists.objects.filter(Name__startswith='a')              
<QuerySet [<Artists: Ahmed Hassan>]>
*****************************************************************************************
5-in 2 different ways, create some albums and assign them to any artists (hint: use `objects` manager and use the related object reference) get the latest released album
way-1
Amrdaib=Artists(Name='amr diab')                     
Amrdaib.save() 
from albums.models import Album       
album1=Album(Albumname="Alaila",Creationdatetime=datetime.datetime(2022,10,7,15,30),Releasedatetime=datetime.datetime(2022,10,7,15,30),Cost=200.7,Artistname=Amrdaib)
album1.save()
way-2
****************************************************************************************
6-get the latest released album
 Album.objects.latest('Releasedatetime')
<Album: Album object (1)>
*********************************************
7-get all albums released before today
 from datetime import date
Album.objects.filter( Releasedatetime__lt=date.today())  
<QuerySet [<Album: Album object (2)>, <Album: Album object (3)>]>
********************************************************************************
8-get all albums released today or before but not after today
Album.objects.filter(Releasedatetime__lte=date.today())  
<QuerySet [<Album: Album object (1)>, <Album: Album object (2)>, <Album: Album object (3)>]>
**********************************************************************************************************
9-count the number of albums (hint: count in an optimized manner)
Album.objects.count()
3
********************************************************************************************************* 
10-in 2 different ways, for each artist, list down all of his/her albums (hint: use `objects` manager and use the related object reference)
first_method:
>>> for artist in Artists.objects.all():  
...  artist.album_set.all()
<QuerySet []>
<QuerySet []>
<QuerySet []>
<QuerySet [<Album: Album object (1)>, <Album: Album object (2)>, <Album: Album object (3)>]>
second_method:
for artist in Artists.objects.all():
 Album.objects.filter(Artistname_id=artist.id) 
<QuerySet []>
<QuerySet []>
<QuerySet []>
<QuerySet [<Album: Album object (1)>, <Album: Album object (2)>, <Album: Album object (3)>]>
*********************************************************************************************************
11-list down all albums ordered by cost then by name (cost has the higher priority)
 Album.objects.order_by('Cost', 'Albumname')  
************************************************** 