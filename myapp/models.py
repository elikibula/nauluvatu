from django.db import models 

from django.core.validators import MinValueValidator, MaxValueValidator

#-------------------------------------------------------------------------

gender_Choice = (
    ("Tgn", "Tagane"),
    ("Ylw", "Yalewa")
)

tutu_Choice = (
    ("sigadina", "Siga Dina"),
    ("sigatuberi", "Siga Tuberi"),
    ("lwnvks", "Leweni Vavakoso")
)

tavi_Choice = (
    ("talcg", "Talatala Vakacegu"),
    ("talyc","Talata Yaco"),
    ("taltv","Talatala Vakatovolei"),
    ("vktwcg","Vakatawa Vakacegu"),
    ("vktwyc", "Vakatawa Yaco"),
    ("vktwtv", "Vakatawa Vakatovolei"),
    ("dvnyc", "Dauvunau Yaco"),
    ("dvntv", "Dauvunau Vakatovolei"),
    ("dcms", "Daucaka Masumasu"),
    ("lwnvk","Leweni Vavakoso")
)

toki_Choice = (
    ("tm", "Toki Mai"),
    ("ty", "Toki Yani")

)

#---------------------------------------------------------------------------

class Lewenilotu(models.Model):
    id = models.AutoField(primary_key=True)
    yaca_ni_vuvale = models.CharField(max_length=255)
    lewenilotu = models.CharField (max_length=255)
    tiki_ni_siganisucu = models.DateField(max_length=255)
    tagane_se_yalewa =models.CharField(choices=gender_Choice, max_length=50)
    phone_contact = models.CharField(max_length=255)
    email_contact = models.CharField(max_length=255)
    Adress = models.TextField(max_length=255)
    tutu_vakalotu =models.CharField(choices=tutu_Choice, max_length=50)
    tavi_vakalotu =models.CharField(choices=tavi_Choice, max_length=50)
    matasiga = models.ForeignKey('Matasiga', null=True, on_delete=models.CASCADE)
    veitokani = models.ForeignKey('Veitokani', null=True, on_delete=models.CASCADE)
    valenilotu = models.ForeignKey('Valenilotu', null=True, on_delete=models.CASCADE)
    vuli_keina_cakacaka = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.lewenilotu}, {self.valenilotu} {self.phone_contact}"

    class Meta:
        verbose_name_plural = "Lewenilotu"


class Matasiga(models.Model):
    id = models.AutoField(primary_key=True)
    matasiga = models.CharField(max_length=255)
    liuliu_ni_matasiga = models.CharField(max_length=255)
    valenilotu = models.ForeignKey('Valenilotu', on_delete=models.CASCADE)
    vanua_dau_soqoni_kina = models.TextField(max_length=255)
    veika_dau_qaravi = models.TextField(max_length=255)
    vakamacala_tale_eso =models.TextField(max_length=255)

    def __str__(self):
        return f"{self.matasiga}, {self.valenilotu}"

    class Meta:
        verbose_name_plural = "Matasiga"


class Veitokani(models.Model):
    id = models.AutoField(primary_key=True)
    veitokani = models.CharField(max_length=255)
    liuliu_ni_veitokani = models.CharField(max_length=255)
    vunivola_ni_veitokani = models.CharField(max_length=255)
    dauniyau_ni_veitokani = models.CharField(max_length=255)
    valenilotu = models.ForeignKey('Valenilotu', on_delete=models.CASCADE)
    levu_ni_lavo_bula = models.CharField(max_length=255)
    veika_dau_qaravi = models.TextField(max_length=255)
    vakamacala_tale_eso =models.TextField(max_length=255)

    def __str__(self):
        return f"{self.veitokani}, {self.valenilotu}"

    class Meta:
        verbose_name_plural = "Veitokani"


class Valenilotu(models.Model):
    id = models.AutoField(primary_key=True)
    valenilotu = models.CharField(max_length=255)
    yaca_ni_vakatawa = models.CharField(max_length=255)
    vukevuke_ni_vakatawa = models.CharField(max_length=255)
    tuirara = models.CharField(max_length=255)
    vukevuke_ni_tuirara = models.CharField(max_length=255)
    vunivola = models.CharField(max_length=255)
    dauniyau = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_contact = models.CharField(max_length=255)
    vakamacala_tale_eso =models.TextField(max_length=255)

    def __str__(self):
        return f"{self.valenilotu}, {self.address}"

    class Meta:
        verbose_name_plural = "Valenilotu"


class Veitosoyaki(models.Model):
    id = models.AutoField(primary_key=True)
    yacana = models.CharField(max_length=255)
    lewenilotu = models.ForeignKey('Lewenilotu', on_delete=models.CASCADE)
    toki =models.CharField(choices=toki_Choice, max_length=50)
    siga_e_yaco_kina = models.DateField(max_length=50)
    vola = models.FileField(upload_to='documents/veitosoyaki/%Y/%m/%d/', null=True, blank=True)
    vakamacala_tale_eso =models.TextField(max_length=255)

    def __str__(self):
        return f"{self.yacana}, {self.toki}"

    class Meta:
        verbose_name_plural = "Veitosoyaki"


class Veivakalotutaki(models.Model):
    id = models.AutoField(primary_key=True)
    yacani_program = models.CharField(max_length=255)
    gauna_vakayacori_kina = models.TextField(max_length=50)
    vakamacala_tale_eso =models.TextField(max_length=255)

    def __str__(self):
        return f"{self.yacani_program}"

    class Meta:
        verbose_name_plural = "Veivakalotutaki"


class Bulararaba(models.Model):
    id = models.AutoField(primary_key=True)
    veika_e_vakayacori = models.CharField(max_length=255)
    gauna_vakayacori_kina = models.TextField(max_length=50)
    vakamacala_tale_eso =models.TextField(max_length=255)

    def __str__(self):
        return f"{self.veika_e_vakayacori}"

    class Meta:
        verbose_name_plural = "Bula Raraba"





    
