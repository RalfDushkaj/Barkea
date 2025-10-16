from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
    
class Reach_out(models.Model):
    main_title = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    whatsap = models.CharField(max_length=20) 
    email = models.EmailField() 
    instagram = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    tiktok = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    location_map = models.URLField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.main_title
    
class Vilat(models.Model):
    main_title=models.CharField(max_length=100, null=True, blank=True)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='vilat/')
    description=models.TextField()
    sub_description1=models.TextField()
    sub_description2=models.TextField()
    status=models.CharField(max_length=50)
    vendndodhja=models.CharField(max_length=50)
    lloji=models.CharField(max_length=50)
    sip_vila=models.CharField(max_length=50)
    sip_parcela=models.CharField(max_length=50)
    numri_tipologjive=models.CharField(max_length=50)
    kati_0_img=models.ImageField(upload_to='vilat/')
    kati_1_img=models.ImageField(upload_to='vilat/')
    kati_2_img=models.ImageField(upload_to='vilat/')
    slug=models.SlugField(unique=True, max_length=50, null=True, blank=True)
        
    def __str__(self):
        return self.title
    
class About(models.Model):
    main_title=models.CharField(max_length=10)
    title1=models.CharField(max_length=20)
    description1=models.TextField()
    title2=models.CharField(max_length=20)
    description2=models.TextField()   
    title3=models.CharField(max_length=20)
    description3=models.TextField()   
    title4=models.CharField(max_length=20)
    description4=models.TextField()  
    
    def __str__(self):
        return self.main_title    

class Footer(models.Model):
    instagram = models.URLField(max_length=100, null=True, blank=True)
    facebook = models.URLField(max_length=100, null=True, blank=True) 
    tiktok = models.URLField(max_length=100, null=True, blank=True)      
    
    def __str__(self):
     return "Footer Links"
        
    
    
    
    
    