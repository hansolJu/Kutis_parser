from django.db import models
# Create your models here.


class Student(models.Model):
    hukbun = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.hukbun


class StudentInfo(models.Model):
    """개인 신상정보 -- 학생 기본 정보"""
    # 0 학번
    # 1 성명
    # 2 주민등록번호
    # 3 한자성명
    # 4 영문성명
    # 5 과정구분
    # 6 캠퍼스구분
    # 7 주야구분
    # 8 학적구분
    # 9 학적변동
    # 10 졸업학점
    # 11 전공
    # 12 지도교수
    # 13 학생구분
    # 14 산업체여부
    # 15 학점교류구분
    # 16 병역구분
    # 17 현 학년학기
    # 18 이수학기/편입인정학기
    # 19 조기졸업대상여부
    # 20 특기자구분
    # 21 입학구분
    # 22 입학일자
    # 23 인증구분
    # 24 본인인증
    # 25 본적지주소
    # 26 거주지주소
    # 27 전화번호
    # 28 전자우편
    # 29 휴대폰
    # 30 카카오톡ID
    # 31 메신저QQ ID
    # 32  
    # 33 보호자
    # 34 관계
    # 35 근무지
    # 36 보호자주소
    # 37 보호자전화번호
    # 38 취미
    # 39 특기
    # 40 혈액형
    hukbun = models.CharField(max_length=15, unique= True)
    name = models.CharField(max_length=30, unique=True)
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


class StudentHopeCareers(models.Model):
    "개인 신상정보 -- 학생취업신상정보"
    student = models.ForeignKey('StudentInfo',on_delete=models.CASCADE)
    # 진로구분
    course = models.CharField(max_length=50, blank=True,null=True)
    # 지망순위
    ranking = models.IntegerField()
    # 직업(중분류)

    # 직업(소분류)
    job = models.CharField(max_length=50, blank=True, null=True)
    # 희망기업
    Enterprise = models.CharField(max_length=50, blank=True,null=True)
    # 희망연봉
    Salary = models.CharField(max_length=50, blank=True,null=True)
    # 희망근무지역
    Address = models.CharField(max_length=50, blank=True,null=True)

    def __str__(self):
        return self.student.hukbun


class StudentGrade(models.Model):
    student = models.ForeignKey('StudentInfo',on_delete=models.CASCADE)
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

    def __str__(self):
        return self.student.hukbun


class Schedule(models.Model):
    # 과목번호
    subjectCode = models.IntegerField()
    # 과목이름
    subjectName = models.CharField(max_length=50, blank=True,null=True)
    # 학년
    grade = models.IntegerField()
    # 이수구분
    eisu = models.CharField(max_length=50, blank=True,null=True)
    # 학점
    score = models.IntegerField()
    # 담당교수
    professor = models.CharField(max_length=50, blank=True,null=True)
    # 비고
    remarks = models.CharField(max_length=50, blank=True, null=True)
    # 교시
    time = models.CharField(max_length=50, blank=True,null=True)
    # 강의실
    lectureRoom = models.CharField(max_length=100, blank=True,null=True)

    def __str__(self):
        return self.subjectName