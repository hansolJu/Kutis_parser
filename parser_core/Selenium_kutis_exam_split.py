import re
from bs4 import BeautifulSoup
from selenium import webdriver


id='201511868'
pw='10197112'

base_url = "http://kutis.kyonggi.ac.kr/webkutis/view/indexWeb.jsp"
login_url = "http://kutis.kyonggi.ac.kr/webkutis/view/indexWeb.jsp"
studentInfoUrl='http://kutis.kyonggi.ac.kr/webkutis/view/hs/wshj1/wshj111s.jsp?submenu=1&m_menu=wsco1s02&s_menu=wshj111s'
studentHopeCareersUrl='http://kutis.kyonggi.ac.kr/webkutis/view/hs/wshj1/wshj190s.jsp?m_menu=wsco1s02&s_menu=wshj190s'
studentgradeUrl='http://kutis.kyonggi.ac.kr/webkutis/view/hs/wssj1/wssj170s.jsp?submenu=2'
page = str(1)
year = str(2018)
semester = str(10)
scheduleUrl = "http://kutis.kyonggi.ac.kr/webkutis/view/hs/wssu2/wssu222s.jsp?curPage="+page+"&hakgwa_cd=91017&gyear="+year+"&gwamok_name=&ghakgi="+semester
subjectUrl = "http://kutis.kyonggi.ac.kr/webkutis/view/hs/wssu5/wssu511s.jsp?year=2018&hakgi=10&jojik=A1000&gwamok_no=1199&gyosu_no=20100118&gwajung=1"

driverPath = 'C:/Users/hanso/Downloads/chromedriver.exe'
driver = webdriver.Chrome(driverPath)
driver.implicitly_wait(3)

def login():
    # url에 접근한다.
    driver.get(base_url)

    # 아이디/비밀번호를 입력해준다.
    driver.find_element_by_name("id").send_keys(id)
    driver.find_element_by_name('pw').send_keys(pw)

    # 로그인 버튼을 눌러주자.
    btn = driver.find_element_by_css_selector('#login_scroll > form > fieldset > p > a')
    btn.click()

    # 로그인이 됬는지 확인 하기.
    try:
        driver.get(studentInfoUrl)
    except:
        print("Kutis password 가 틀렸습니다.")
        return False



def get_original_data(url):
    """Get source from web and returns BeautifulSoup object."""
    driver.get(url)
    html = driver.page_source
    return BeautifulSoup(html, "html.parser")


def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def parse_infos_item(url):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    i=0
    infos = dict()
    resultTd = []
    resultTh= []
    tables = soup.findAll("table", {'class': 'list06'})

    for table in tables:
        # print(type(table))
        tds = table.findAll("td")
        ths = table.findAll("th")
        for th in ths:
            removeTag = remove_html_tags(str(th))
            resultTh.append(removeTag)
        for td in tds:
            removeTagTd = remove_html_tags(str(td))
            removeTagTd = removeTagTd.replace('\xa0', "")
            removeTagTd = removeTagTd.replace('\n', "")
            removeTagTd = removeTagTd.replace('\t', "")
            removeTagTd = removeTagTd.replace('변동내역', "")
            removeTagTd = removeTagTd.replace('※ 본인인증은 개인정보 변경에서 하시기 바랍니다.', "")
            print(removeTagTd)
            resultTd.append(removeTagTd)
    i=0
    for th in resultTh:
        print("%d" % i, th)
        i += 1
    i=0
    for td in resultTd:
        print("%d" % i, td)
        i += 1
    # 학번
    infos['hukbun'] = resultTd[1]
    # 성명
    infos['name'] = resultTd[2]
    # 주민등록번호
    infos['jumin'] = resultTd[3]
    # 한자성명
    infos['name_Hanja'] = resultTd[4]
    # 영문성명
    infos['name_English'] = resultTd[5]
    # 과정구분
    # 캠퍼스구분
    infos['campus'] = resultTd[7]
    # 주야구분
    infos['dayNight'] = resultTd[8]
    # 학적구분
    infos['state'] = resultTd[9]
    # 학적변동
    infos['variance'] = resultTd[10]
    # 졸업학점
    infos['graduationCredit'] = resultTd[11]
    # 전공
    infos['major'] = resultTd[12]
    # 지도교수
    infos['advisor'] = resultTd[13]
    # 학생구분14
    # 산업체여부15
    # 학점교류구분116
    # 병역구분17
    # 현 학년학기
    infos['currentGrade'] = resultTd[18]
    # 이수학기 / 편입인정학기
    infos['compleSemester'] = resultTd[19]
    # 조기졸업대상여부
    infos['earlyGraduation'] = resultTd[20]
    # 특기자구분21
    # 입학구분22
    # 입학일자23
    infos['admission'] = resultTd[23]
    # 인증구분
    infos['enginCertification'] = resultTd[24]
    # 본인인증25
    # 본적지주소26
    # 거주지주소27
    infos['address'] = resultTd[27]
    # 전화번호
    infos['phone'] = resultTd[28]
    # 전자우편
    infos['email'] = resultTd[29]
    # 휴대폰30
    infos['cellPhone'] = resultTd[30]
    # 카카오톡ID31
    # 메신저QQ32
    # blank 33
    # 보호자34
    # 관계35
    # 근무지36
    # 보호자주소37
    # 보호자전화번호38
    infos['parentsPhone'] = resultTd[38]
    # 취미39
    # 특기40
    # 혈액형41
    return infos


def parse_Hope_item(url):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    i = 0
    hope1 = dict()
    hope2 = dict()
    hope3 = dict()
    list = []
    resultTd = []
    resultTh = []
    tables = soup.findAll("table", {'class': 'list06'})

    for table in tables:
        # print(type(table))
        tds = table.findAll("td")
        ths = table.findAll("th")
        for th in ths:
            removeTag = remove_html_tags(str(th))
            resultTh.append(removeTag)
        for td in tds:
            removeTagTd = remove_html_tags(str(td))
            removeTagTd = removeTagTd.replace('\xa0', "")
            removeTagTd = removeTagTd.replace('\n', "")
            removeTagTd = removeTagTd.replace('\t', "")
            removeTagTd = removeTagTd.replace('변동내역', "")
            removeTagTd = removeTagTd.replace('※ 본인인증은 개인정보 변경에서 하시기 바랍니다.', "")
            print(removeTagTd)
            resultTd.append(removeTagTd)
    i = 0
    for th in resultTh:
        print("%d" % i, th)
        i += 1
    i = 0
    for td in resultTd:
        print("%d" % i, td)
        i += 1
    # 0
    # 진로구분
    hope1['careers'] = resultTd[0]
    # 지망순위
    hope1['ranking'] = resultTd[1]
    # 직업(중분류)

    # 직업(소분류)
    hope1['job'] = resultTd[3]
    # 희망기업
    hope1['Enterprise'] = resultTd[4]
    # 희망연봉
    hope1['Salary'] = resultTd[5]
    # 희망근무지역
    hope1['Address'] = resultTd[6]
    list.append(hope1)

    # 진로구분
    hope2['careers'] = resultTd[7]
    # 지망순위
    hope2['ranking'] = resultTd[8]
    # 직업(중분류)

    # 직업(소분류)
    hope2['job'] = resultTd[10]
    # 희망기업
    hope2['Enterprise'] = resultTd[11]
    # 희망연봉
    hope2['Salary'] = resultTd[12]
    # 희망근무지역
    hope2['Address'] = resultTd[13]
    list.append(hope2)
    # 진로구분
    hope3['careers'] = resultTd[14]
    # 지망순위
    hope3['ranking'] = resultTd[15]
    # 직업(중분류)

    # 직업(소분류)
    hope3['job'] = resultTd[17]
    # 희망기업
    hope3['Enterprise'] = resultTd[18]
    # 희망연봉
    hope3['Salary'] = resultTd[19]
    # 희망근무지역
    hope3['Address'] = resultTd[20]
    list.append(hope3)
    return list

def parse_grade_item(url):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    i=0
    infos = dict()
    resultTd = []
    resultTh= []
    tables = soup.findAll("table", {'class': 'list06'})

    for table in tables:
        # print(type(table))
        tds = table.findAll("td")
        ths = table.findAll("th")
        for th in ths:
            removeTag = remove_html_tags(str(th))
            resultTh.append(removeTag)
        for td in tds:
            removeTagTd = remove_html_tags(str(td))
            removeTagTd = removeTagTd.replace('\xa0', "")
            removeTagTd = removeTagTd.replace('\n', "")
            removeTagTd = removeTagTd.replace('\t', "")
            removeTagTd = removeTagTd.replace('변동내역', "")
            removeTagTd = removeTagTd.replace('※ 본인인증은 개인정보 변경에서 하시기 바랍니다.', "")
            print(removeTagTd)
            resultTd.append(removeTagTd)
    i=0
    for th in resultTh:
        print("%d" % i, th)
        i += 1
    i=0
    for td in resultTd:
        print("%d" % i, td)
        i += 1

    return infos

# 기본정보 크롤
login()
info = parse_infos_item(studentInfoUrl)
print(info)
hope = parse_Hope_item(studentHopeCareersUrl)
print(hope)
grade = parse_infos_item(studentgradeUrl)

