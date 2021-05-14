from Book.models import Book
import random

# To read data
# all_data = Book.objects.all()
# print(all_data)
# for book in all_data:
#     print("-----------Details for ID Number:",book.id,"----------")
#     print("Book name:-",book.name)
#     print("Book Author:-",book.author)
#     print("Book Qty:-",book.qty)
#     print("Book Price:-",book.price)
    #print('-' * 50)

# Single Data           
# sid = 2
# b0 = Book.objects.get(id=sid)
# print(bo)
# print('-' * 50)

# # Update Data
# sid =5
# b1 = Book.objects.get(id=sid)
# b1.name = 'Kharanshu'
# b1.author ="Namrata"
# b1.save()
# print('-' * 50)

# # Delete Data
# sid = 4
# b2 = Book.objects.get(id=sid)
# b2.delete()
# print("Record Deleted...!!!")

# To print only required feilds
# all_data = Book.objects.all().values("id","name","qty") 
# for i in all_data:
#     print(i)

# Print SET
# all_data = Book.objects.values_list()
# print(all_data)




# Command to Execute Python File
#exec(open("D:\AI Course\Code\Django\Book_Library\Book\db_shell.py").read())

# for i in range(1, 36):
#     b = Book(name=(chr(random.randint(65,90)))* 5,author="ABC",qty=random.randint(15,85),price=random.randint(200,900))
#     b.save()

# books = Book.objects.filter(id__gte=15)    #gt,lt,gte,lte,name__startswith,name__endswith,name__isstartswith,name__isendswith
# for i in books: 
#     print(i.__dict__)

# b = Book.objects.all().order_by("-name")     #ASC,DSC
# for i in b:
#     print(i)

# b = Book.objects.count()     #len(),count()
# print(b)

# Book.objects.bulk_create([
#     Book(name='Java1',author="AAA",qty=43,price=261),
#     Book(name='Java2',author="BBB",qty=51,price=361),
#     Book(name='Java3',author="CCC",qty=23,price=461),
#     Book(name='Java4',author="DDD",qty=62,price=161),
#     Book(name='Java5',author="EEE",qty=36,price=761),    
# ])


######### ORM QUERIES #########

