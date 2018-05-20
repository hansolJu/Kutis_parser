from django.db import models
# Create your models here.

class StudentInfo(models.Model):
    """개인 신상정보 -- 학생 기본 정보"""
    hukbun = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    jumin =models.CharField(max_length=30)
    name_Hanja =models.CharField(max_length=30, blank=True,null=True)
    name_English = models.CharField(max_length=30, blank=True,null=True)

    campus = models.CharField(max_length=30, blank=True,null=True)
    dayNight= models.CharField(max_length=30, blank=True,null=True)
    state = models.CharField(max_length=30, blank=True,null=True)
    variance= models.CharField(max_length=30, blank=True,null=True)
    #나중에 인티져로 변경.
    graduationCredit =models.CharField(max_length=30, blank=True,null=True)
    major =models.CharField(max_length=30, blank=True,null=True)
    advisor =models.CharField(max_length=30, blank=True,null=True)
    currentGrade = models.CharField(max_length=30, blank=True, null=True)
    compleSemester = models.CharField(max_length=30, blank=True, null=True)
    earlyGraduation = models.CharField(max_length=30, blank=True, null=True)
    # 나중에 데이트필드 변경.
    admission = models.CharField(max_length=30, blank=True, null=True)
    enginCertification = models.CharField(max_length=30, blank=True,null=True)

    address = models.CharField(max_length=100, blank=True,null=True)
    phone = models.CharField(max_length=50, blank=True,null=True)
    email = models.EmailField()
    cellPhone = models.CharField(max_length=50, blank=True,null=True)
    parentsPhone = models.CharField(max_length=50, blank=True,null=True)

    def __str__(self):
        return self.hukbun


class LatestUpdate(models.Model):
    """Save last update date for a cable movie channel"""

    StudentInfo = models.ForeignKey('StudentInfo', on_delete=models.CASCADE)
    latest_update = models.DateTimeField(null=True)



class StudentGrade(models.Model):
    hukbun = models.ForeignKey(StudentInfo,on_delete=models.CASCADE)
    #이수구분
    eisu = models.CharField(max_length=50, blank=True,null=True)
    # 인증구분
    certification = models.CharField(max_length=50, blank=True,null=True)
    # 년도학기
    yearNsemester = models.CharField(max_length=50, blank=True,null=True)
    # 학수코드
    subject_code = models.CharField(max_length=50, blank=True,null=True)
    # 교과목명
    subject = models.CharField(max_length=50, blank=True,null=True)
    # 학점
    score = models.CharField(max_length=50, blank=True,null=True)
    # 설계학점
    grade_design = models.CharField(max_length=50, blank=True,null=True)
    # 등급
    grade = models.CharField(max_length=50, blank=True,null=True)
    # 유효구분
    valid = models.CharField(max_length=50, blank=True,null=True)


