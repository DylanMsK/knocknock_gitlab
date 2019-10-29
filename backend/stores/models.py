# from django.db import models
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import Partner, Client


class Category(models.Model):
    main_category = models.CharField('대분류', max_length=30)
    sub_category = models.CharField('중분류', max_length=30)

    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리'
        ordering = ['id']

    def __str__(self):
        return f'{self.main_category} | {self.sub_category}'



class Option(models.Model):
    name = models.CharField('옵션명', max_length=20)

    class Meta:
        verbose_name = '옵션'
        verbose_name_plural = '옵션'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


class Store(models.Model):
    origin_id = models.CharField('네이버 아이디', max_length=20, unique=True)
    name = models.CharField('이름', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='카테고리')
    description = models.TextField('설명', blank=True, default='')
    lon = models.FloatField('경도', validators=[MaxValueValidator(180), MinValueValidator(-180)])
    lat = models.FloatField('위도', validators=[MaxValueValidator(90), MinValueValidator(-90)])
    location = models.PointField('위치', srid=4326)
    thumbnail = models.TextField('대표 사진', blank=True, default='')
    contact = models.CharField('전화번호', max_length=15, blank=True, default='')
    road_addr = models.CharField('도로명 주소', max_length=50, blank=True)
    common_addr = models.CharField('시구', max_length=50)
    addr = models.CharField('지번 주소', max_length=50, blank=True)
    tags = models.TextField('태그', blank=True, default='')
    price_avg = models.IntegerField('가격대', default=0)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, default=None, null=True, blank=True, verbose_name='파트너')
    review_cnt = models.IntegerField('네이버 리뷰갯수', default=0)
    view_cnt = models.IntegerField('조회수', default=0)
    options = models.ManyToManyField(Option, verbose_name='옵션', blank=True)
    updated_at = models.DateTimeField('마지막 수정일', auto_now=True)

    class Meta:
        verbose_name = '가게'
        verbose_name_plural = '가게'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.name}'


class BusinessHour(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='business_hours', verbose_name='가게')
    day = models.CharField('요일', max_length=5)
    is_dayoff = models.BooleanField('휴업', default=False)
    start = models.TimeField('영업 시작', null=True)
    end = models.TimeField('영업 종료', null=True)
    start_break = models.TimeField('브레이크타임 시작', null=True)
    end_break = models.TimeField('브레이크타임 종료', null=True)
    last_order = models.TimeField('라스트오더', null=True)
    memo = models.TimeField('비고', null=True)

    class Meta:
        verbose_name = '영업일 영업시간'
        verbose_name_plural = '영업일 영업시간'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.store}'


class PublicHoliday(models.Model):
    name = models.CharField('명칭', max_length=20)
    date = models.DateField('날짜')

    class Meta:
        verbose_name = '법정 공휴일'
        verbose_name_plural = '법정 공휴일'
        ordering = ['date']
    
    def __str__(self):
        return f'{self.name}'



class HolidayHour(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='holiday_hours', verbose_name='가게')
    public_holiday = models.ForeignKey(PublicHoliday, on_delete=models.CASCADE, related_name='holiday_hours', verbose_name='명칭')
    is_dayoff = models.BooleanField('휴업', default=False)
    start = models.TimeField('영업 시작', null=True)
    end = models.TimeField('영업 종료', null=True)
    start_break = models.TimeField('브레이크타임 시작', null=True)
    end_break = models.TimeField('브레이크타임 종료', null=True)
    last_order = models.TimeField('라스트오더', null=True)
    memo = models.TimeField('비고', null=True)

    class Meta:
        verbose_name = '공휴일 영업시간'
        verbose_name_plural = '공휴일 영업시간'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.store}'


class Dayoff(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='dayoffs')
    expiry = models.DateTimeField(null=True)

    class Meta:
        verbose_name = '휴무일'
        verbose_name_plural = '휴무일'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.store}'


class ClientReview(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='가게', related_name='comments')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='클라이언트', related_name='comments')
    content = models.CharField('내용', max_length=300)
    created_at = models.DateTimeField('작성일', auto_now_add=True)

    class Meta:
        verbose_name = '가게 리뷰'
        verbose_name_plural = '가게 리뷰'
        ordering = ['id']

    def __str__(self):
        return f'{self.store.name} | {self.client.nickname} | {self.content}'


class PartnerFeedback(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='가게', related_name='partner_comments')
    review = models.ForeignKey(ClientReview, on_delete=models.CASCADE, verbose_name='답글', related_name='partner_comments')
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name='파트너', related_name='partner_comments')
    content = models.CharField('내용', max_length=300)
    created_at = models.DateTimeField('작성일', auto_now_add=True)
