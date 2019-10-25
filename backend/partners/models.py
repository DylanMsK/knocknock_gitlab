from django.db import models
from accounts.models import Partner
from stores.models import Store

class BusinessRegistration(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE, verbose_name='가게')
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name='파트너')
    company_name = models.CharField('상호', max_length=100)
    business_registration_number = models.CharField('등록번호', max_length=10)
    representative_name = models.CharField('대표자명', max_length=30)
    business_address = models.CharField('업장소재지', max_length=100)
    registration_image = models.ImageField('사업자 등록증', upload_to='partners/certificates')
    business_commencement_date = models.DateField('영업개시일', null=True)
    business_type = models.CharField('업태', max_length=30, null=True)
    business_item = models.CharField('종목', max_length=30, null=True)

    class Meta:
        verbose_name = '사업자등록증'
        verbose_name_plural = '사업자등록증'
        ordering = ['id']

    def __str__(self):
        return f'{self.company_name} | {self.partner.name}'
