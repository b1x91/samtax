# -*- coding: utf-8 -*-
import io

HEAD = ('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        '<link rel="stylesheet" href="app.css"></head><body>\n')
FOOT = '</div>\n</body></html>\n'

ICON = ('<svg class="ic" width="15" height="15" viewBox="0 0 16 16" fill="none">'
        '<circle cx="7" cy="7" r="4.6" stroke="#8795A8" stroke-width="1.4"/>'
        '<path d="M10.6 10.6L14 14" stroke="#8795A8" stroke-width="1.4" stroke-linecap="round"/></svg>')

PRODUCTS = [
    ('세무조정', '345'), ('법인세', '221'), ('세무조사지원', '212'), ('이전가격(TP)', '141'),
    ('세무진단', '128'), ('부가가치세', '118'), ('경정청구', '96'), ('필라2', '88'),
    ('개인소득세', '72'), ('상속 · 증여', '61'), ('국제조세', '54'), ('지방세', '37'),
]

def nav(active=None):
    rows = ['<div class="sl">프로덕트</div>',
            '<div class="si all%s">전체<span class="c">1,573</span></div>' % (' on' if active == '전체' else '')]
    for name, cnt in PRODUCTS:
        on = ' on' if name == active else ''
        rows.append('<div class="si%s">%s<span class="c">%s</span></div>' % (on, name, cnt))
    return '<nav class="side">\n' + '\n'.join(rows) + '\n</nav>'

def top(mid, right, admin=False, logo='TQA'):
    cls = 'top adm' if admin else 'top'
    return ('<div class="%s">\n  <div class="topl">%s</div>\n'
            '  <div class="topc">%s</div>\n  <div class="topr">%s</div>\n</div>' % (cls, logo, mid, right))

SEARCH = '<div class="search">%s질문을 검색하거나 바로 작성하세요<span class="kc">Ctrl K</span></div>' % ICON
R_USER = '<span class="topit">알림 3</span><span class="topit">내 프로필</span><span class="btn">글쓰기</span>'
WM = '<span class="wm">TQA</span>'
WM_ADM = '<span class="wm">TQA</span><span class="adm-tag" style="margin-left:10px;">ADMIN CONSOLE</span>'

TH = {
 'a': ('<svg viewBox="0 0 104 84" preserveAspectRatio="xMidYMid slice">'
       '<rect width="104" height="84" fill="#E9E4D6"/>'
       '<rect x="15" y="11" width="56" height="64" fill="#FFFFFF" opacity=".5"/>'
       '<rect x="25" y="17" width="56" height="64" fill="#FFFFFF"/>'
       '<rect x="33" y="26" width="29" height="3.2" fill="#2A3545"/>'
       '<rect x="33" y="36" width="40" height="2.4" fill="#AEB4BC"/>'
       '<rect x="33" y="43" width="33" height="2.4" fill="#AEB4BC"/>'
       '<rect x="33" y="50" width="40" height="2.4" fill="#AEB4BC"/>'
       '<rect x="33" y="57" width="21" height="2.4" fill="#AEB4BC"/>'
       '<rect x="25" y="68" width="56" height="6.5" fill="#B8511A"/></svg>'),
 'b': ('<svg viewBox="0 0 104 84" preserveAspectRatio="xMidYMid slice">'
       '<rect width="104" height="84" fill="#DEE3E0"/>'
       '<rect x="19" y="13" width="66" height="58" fill="#FFFFFF"/>'
       '<rect x="27" y="23" width="9.5" height="9.5" fill="#B8511A"/>'
       '<path d="M29.4 28.1l1.9 1.9 3.2-3.5" stroke="#FFFFFF" stroke-width="1.7" fill="none" stroke-linecap="round"/>'
       '<rect x="42" y="26" width="33" height="2.6" fill="#8C958F"/>'
       '<rect x="27" y="38" width="9.5" height="9.5" fill="#B8511A"/>'
       '<path d="M29.4 43.1l1.9 1.9 3.2-3.5" stroke="#FFFFFF" stroke-width="1.7" fill="none" stroke-linecap="round"/>'
       '<rect x="42" y="41" width="26" height="2.6" fill="#8C958F"/>'
       '<rect x="27" y="53" width="9.5" height="9.5" fill="none" stroke="#BCC1BD" stroke-width="1.5"/>'
       '<rect x="42" y="56" width="33" height="2.6" fill="#C6CBC7"/></svg>'),
 'c': ('<svg viewBox="0 0 104 84" preserveAspectRatio="xMidYMid slice">'
       '<rect width="104" height="84" fill="#D9DEE7"/>'
       '<circle cx="50" cy="42" r="25" fill="#FFFFFF"/>'
       '<circle cx="50" cy="42" r="25" fill="none" stroke="#5A6578" stroke-width="1.7"/>'
       '<ellipse cx="50" cy="42" rx="10" ry="25" fill="none" stroke="#5A6578" stroke-width="1.2"/>'
       '<line x1="25" y1="42" x2="75" y2="42" stroke="#5A6578" stroke-width="1.2"/>'
       '<path d="M30 30h40" stroke="#5A6578" stroke-width="1" opacity=".55"/>'
       '<path d="M30 54h40" stroke="#5A6578" stroke-width="1" opacity=".55"/>'
       '<circle cx="71" cy="24" r="7.5" fill="#B8511A"/></svg>'),
}

def news(key, title, dek, date, views):
    return ('<div class="news"><div class="thw">' + TH[key] + '</div><div class="bd">'
            '<div class="nt">%s</div><div class="nd">%s</div><div class="sp"></div>'
            '<div class="nm">%s &nbsp;·&nbsp; 조회 %s</div></div></div>'
            % (title, dek, date, views))

def w(fn, body):
    io.open(fn, 'w', encoding='utf-8').write(HEAD + body + FOOT)
    print('wrote', fn)

# ───────────────────────── HOME ─────────────────────────
w('home.html', top(SEARCH, R_USER, logo=WM) + '\n<div class="shell">\n' + nav('전체') + '''
<main class="main">
  <section class="card acc">
    <div class="hd"><h2>답변을 기다리는 질문</h2><span class="cnt mono">12</span>
      <span class="mt">구독 중인 프로덕트</span><span class="sp"></span><span class="more">전체 보기</span></div>
    <div class="rows">
      <div class="row">
        <div class="meta"><span class="hdl"><b>푸른고래58</b><span class="rk">SA</span></span>
          <span class="chip">세무조정</span><span class="mt mono">Q-2026-00417</span><span class="mt">2시간 전</span></div>
        <div class="qt">업무무관가지급금 인정이자 계산 기준일 문의</div>
      </div>
      <div class="row">
        <div class="meta"><span class="hdl"><b>은빛여우07</b><span class="rk">M</span></span>
          <span class="chip">세무조사지원</span><span class="mt mono">Q-2026-00415</span><span class="mt">5시간 전</span></div>
        <div class="qt">세무조사 자료제출 요구 범위에 전자문서 원본이 포함되는지</div>
      </div>
      <div class="row">
        <div class="meta"><span class="hdl"><b>검은돌고래40</b><span class="rk">SM</span></span>
          <span class="chip">필라2</span><span class="mt mono">Q-2026-00398</span><span class="mt">1일 전</span></div>
        <div class="qt">GloBE 정보신고서 제출 기한과 과세연도 매칭</div>
      </div>
    </div>
  </section>

  <section class="card">
    <div class="hd"><h2>새로운 소식</h2><span class="mt">TAX 트렌드 · 인더스트리 팁</span>
      <span class="sp"></span><span class="more">전체 보기</span></div>
    <div class="newsgrid">''' + news('a', '2026년 세법개정 주요 쟁점 정리', '실무에 바로 걸리는 일곱 가지', '11.12.', '412')
       + news('b', '제조업 세무진단 체크포인트 10', '진단 착수 전에 먼저 확인하는 항목', '11.08.', '287')
       + news('c', '필라2 적용 첫 해, 막히는 지점', '신고서 작성 순서와 자료 요청 범위', '11.05.', '331') + '''
    </div>
  </section>

  <section class="card">
    <div class="hd"><h2>최신 질문</h2><span class="sp"></span><span class="more">전체 보기</span></div>
    <div class="rows">
      <div class="row">
        <div class="meta"><span class="hdl"><b>회색기러기12</b><span class="rk">P</span></span>
          <span class="chip">경정청구</span><span class="mt">답변 <span class="mono">3</span> · 좋아요 <span class="mono">8</span></span></div>
        <div class="qt">기한 도과 후 후발적 경정청구 사유 해당 여부</div>
      </div>
      <div class="row">
        <div class="meta"><span class="hdl"><b>붉은여우31</b><span class="rk">SA</span></span>
          <span class="chip">이전가격(TP)</span><span class="mt">답변 <span class="mono">2</span> · 좋아요 <span class="mono">5</span></span></div>
        <div class="qt">정상가격 산출방법 변경 시 사전승인 필요 여부</div>
      </div>
    </div>
  </section>
</main>

<aside class="rail">
  <div class="rl">
    <h3>이번 주 리더보드</h3>
    <div class="rrow"><span class="no mono">1</span><span class="hdl"><b>푸른고래58</b><span class="rk">SA</span></span><span class="sp"></span><span class="v sc">2,418</span></div>
    <div class="rrow"><span class="no mono">2</span><span class="hdl"><b>은빛여우07</b><span class="rk">M</span></span><span class="sp"></span><span class="v sc">2,106</span></div>
    <div class="rrow"><span class="no mono">3</span><span class="hdl"><b>검은돌고래40</b><span class="rk">SM</span></span><span class="sp"></span><span class="v sc">1,874</span></div>
    <div class="quiet" style="margin-top:2px;">내 순위 <b style="color:#B8511A;">42위</b> <span class="dl up">▲5</span> · 점수 <span class="sc">1,284</span></div>
    <div class="more">전체 순위 보기</div>
  </div>
  <div class="rl">
    <h3>우수 Q&amp;A</h3>
    <div class="qt" style="font-size:14px;">필라2 적용대상 판정 기준</div>
    <div class="mt">세법 기준일 <span class="mono">2026.09.</span></div>
    <div class="qt" style="font-size:14px; margin-top:4px;">가지급금 인정이자 기중 변동분 안분</div>
    <div class="mt">세법 기준일 <span class="mono">2026.06.</span></div>
  </div>
  <div class="rl">
    <h3>내 구독</h3>
    <div class="chips"><span class="chip">세무조정</span><span class="chip">이전가격(TP)</span><span class="chip">필라2</span></div>
  </div>
</aside>
''')

# ───────────────────────── DETAIL ─────────────────────────
w('detail.html', top(SEARCH, R_USER, logo=WM) + '\n<div class="shell">\n' + nav('세무조정') + '''
<main class="main">
  <section class="q-card">
    <div class="who">
      <span class="hdl"><b style="font-size:14.5px;">푸른고래58</b><span class="rk">SA</span></span>
      <span class="mt">2시간 전</span><span style="flex:1"></span>
      <span class="subs sm"><span class="dot"></span>구독 중</span></div>
    <div class="meta"><span class="chip a">질문</span><span class="chip">세무조정</span>
      <span class="mt mono">Q-2026-00417</span></div>
    <div style="font-size:21px; font-weight:600; color:var(--ink); line-height:1.4;">업무무관가지급금 인정이자 계산 기준일 문의</div>
    <div class="tx">기중에 가지급금이 변동된 경우 인정이자 계산의 기준일을 어떻게 잡는지 실무 기준이 궁금합니다. 변동일 기준으로 안분하는 것이 맞는지 확인 부탁드립니다.</div>
    <div class="chips"><span class="chip">#인정이자</span><span class="chip">#가지급금</span><span class="chip">#기중변동</span></div>
    <div class="meta"><span class="chip">좋아요 <span class="mono">4</span></span><span class="chip">스크랩</span>
      <span class="mt">조회 <span class="mono">342</span> · 답변 <span class="mono">3</span> · 댓글 <span class="mono">5</span></span></div>
  </section>

  <div class="hd" style="padding:2px 0 0 2px;"><h2>답변 <span class="mono">3</span>개</h2>
    <span class="chips"><span class="chip a">근거 1</span><span class="chip">경험 1</span><span class="chip">의견 1</span></span>
    <span class="sp"></span><span class="more">좋아요순</span></div>

  <section class="a-card best">
    <div class="a-lab">답변 · 근거 제시</div>
    <div class="who">
      <span class="hdl"><b style="font-size:14.5px;">은빛여우07</b><span class="rk">M</span></span>
      <span class="mt">1시간 전</span><span style="flex:1"></span>
      <span class="chip a">좋아요 <span class="mono">12</span></span></div>
    <div class="tx">일수 계산이 원칙이고, 기중 변동분은 변동일을 기준으로 나누어 산정합니다. 기말 잔액 기준으로 일괄 계산하면 조사 단계에서 쟁점이 됩니다.</div>
    <div class="src"><span class="k">법령</span><span style="font-size:13.5px; color:var(--txt);">법인세법 시행령 제89조 제3항</span></div>
    <div class="src"><span class="k">예규</span><span style="font-size:13.5px; color:var(--txt);">서면-2024-법인-0412 (2024.07.)</span></div>
  </section>

  <section class="a-card">
    <div class="a-lab">답변 · 경험 공유</div>
    <div class="who">
      <span class="hdl"><b style="font-size:14.5px;">검은돌고래40</b><span class="rk">SM</span></span>
      <span class="mt">40분 전</span><span style="flex:1"></span>
      <span class="mt">좋아요 <span class="mono">5</span></span></div>
    <div class="tx">같은 쟁점으로 조사 대응을 한 적이 있습니다. 안분 자료를 미리 준비해 두면 설명이 훨씬 빠릅니다.</div>
  </section>
</main>

<aside class="rail">
  <div class="rl">
    <h3>이 글에 참여한 사용자 <span class="mono">5</span></h3>
    <div class="pt-row"><span class="n"><span class="hdl"><b>푸른고래58</b><span class="rk">SA</span></span></span><span class="mt">질문자</span></div>
    <div class="pt-row"><span class="n"><span class="hdl"><b>은빛여우07</b><span class="rk">M</span></span></span><span class="mt">근거</span></div>
    <div class="pt-row"><span class="n"><span class="hdl"><b>검은돌고래40</b><span class="rk">SM</span></span></span><span class="mt">경험</span></div>
    <div class="pt-row"><span class="n"><span class="hdl"><b>회색기러기12</b><span class="rk">P</span></span></span><span class="mt">의견</span></div>
    <div class="pt-row"><span class="n"><span class="hdl"><b>붉은여우31</b><span class="rk">SA</span></span></span><span class="mt">댓글 2</span></div>
  </div>
  <div class="rl">
    <h3>이 글에 관심 있는 직급</h3>
    <div class="rrow"><span class="no mono">1</span><span class="rk">SA</span><span class="sp"></span><span class="v mono">41%</span></div>
    <div class="rrow"><span class="no mono">2</span><span class="rk">M</span><span class="sp"></span><span class="v mono">27%</span></div>
    <div class="rrow"><span class="no mono">3</span><span class="rk">SM</span><span class="sp"></span><span class="v mono">18%</span></div>
    <div class="mt">조회 <span class="mono">342</span>건 기준</div>
  </div>
  <div class="rl">
    <h3>관련 글</h3>
    <div class="tx" style="font-size:13.5px;">가지급금 인정이자 기중 변동분 안분</div>
    <div class="mt"><span class="mono">Q-2026-00188</span> · 답변 <span class="mono">4</span></div>
    <div class="tx" style="font-size:13.5px; margin-top:4px;">특수관계 소멸 시 인정이자 처리</div>
    <div class="mt"><span class="mono">Q-2026-00241</span> · 답변 <span class="mono">2</span></div>
  </div>
  <div class="rl">
    <h3>고유번호</h3>
    <div class="meta"><span class="mono" style="font-size:13.5px; color:var(--txt);">Q-2026-00417</span><span class="btn q sm">복사</span></div>
  </div>
</aside>
''')

# ───────────────────────── WRITE ─────────────────────────
NOTICE = ('<div class="search" style="background:rgba(224,118,47,0.16); color:#E9A472; width:620px;">'
          '<span style="font-size:13px;">작성자는 닉네임과 직급으로만 표시됩니다</span>'
          '<span style="margin-left:auto; font-weight:700; color:#F0B589;">푸른고래58 · SA</span></div>')
w('write.html', top(NOTICE, '<span class="topit">내 프로필</span>', logo=WM) + '\n<div class="shell">\n' + nav() + '''
<main class="main">
  <section class="card">
    <div style="display:flex; gap:44px;">
      <div style="display:flex; flex-direction:column; gap:10px;">
        <div class="mt">말머리 <span style="color:var(--acc); font-weight:600;">필수</span></div>
        <div class="chips"><span class="chip w">질문</span><span class="chip">답변</span></div>
      </div>
      <div style="width:1px; background:rgba(18,26,38,0.11);"></div>
      <div style="display:flex; flex-direction:column; gap:10px; flex:1;">
        <div class="mt">프로덕트 <span style="color:var(--acc); font-weight:600;">1개 필수</span></div>
        <div class="chips"><span class="chip d">세무조정</span><span class="chip">법인세</span><span class="chip">세무조사지원</span>
          <span class="chip">이전가격(TP)</span><span class="chip">세무진단</span><span class="chip">경정청구</span><span class="chip">필라2</span></div>
      </div>
    </div>
  </section>

  <section class="card">
    <div class="field" style="font-size:16px; color:var(--ink); font-weight:500;">업무무관가지급금 인정이자 계산 기준일</div>
    <div class="ui-sel" style="background:var(--acc-sf); border:1px solid var(--acc-ln); padding:10px 12px; display:flex; flex-direction:column; gap:4px;">
      <div style="font-size:13px; font-weight:600; color:var(--acc);">비슷한 질문이 이미 있습니다</div>
      <div class="mt">가지급금 인정이자 기중 변동분 안분 &nbsp;·&nbsp; <span class="mono">Q-2026-00188</span> · 답변 <span class="mono">4</span> · 좋아요 <span class="mono">19</span></div>
    </div>
    <div class="field big" style="min-height:132px; position:relative;">기중에 가지급금이 변동된 경우 인정이자 계산의 기준일을 어떻게 잡는지 실무 기준이 궁금합니다. 고객사 사업자등록번호 <span style="background:rgba(184,81,26,0.14); padding:0 2px;">123-45-67890</span> 건에서 변동일이 두 번 있었습니다.
      <span class="btn q sm" style="position:absolute; right:12px; bottom:12px;">이미지 첨부</span></div>
    <div class="warn">고객 식별정보로 보이는 내용이 있습니다 — 사업자등록번호 형식 1건. 확인 후 수정해 주세요</div>
  </section>

  <section class="card">
    <div class="meta"><span class="btn">등록</span><span class="btn q">임시저장</span>
      <span style="flex:1"></span><span class="mt">고객 식별정보를 포함하지 않았습니다</span><span class="chip a">확인함</span></div>
  </section>
</main>

<aside class="rail">
  <div class="rl">
    <h3>임시저장 <span class="mono">2</span> / 3</h3>
    <div class="dslot"><span class="no">1</span><span class="bd"><span class="t">필라2 적용대상 판정 시 매출 기준</span><span class="d">11.14. 17:22</span></span><span class="ld">불러오기</span></div>
    <div class="dslot"><span class="no">2</span><span class="bd"><span class="t">조사 자료요청 범위 질의 초안</span><span class="d">11.12. 09:40</span></span><span class="ld">불러오기</span></div>
    <div class="dslot empty"><span class="t">비어 있는 슬롯 1개</span></div>
  </div>
  <div class="rl">
    <h3>작성 가이드</h3>
    <div class="tx" style="font-size:13px;">업무 관련 내용만 올려 주세요</div>
    <div class="tx" style="font-size:13px;">고객명 · 담당자 · 소속팀은 쓰지 않습니다</div>
    <div class="tx" style="font-size:13px;">오답은 비난이 아닌 정정 대상입니다</div>
  </div>
  <div class="rl">
    <h3>자동 검사 항목</h3>
    <div class="mt">사업자등록번호 · 주민번호 패턴</div>
    <div class="mt">이메일 · 전화번호</div>
    <div class="mt">주요 고객 법인명</div>
    <div class="mt">첨부 이미지 EXIF</div>
  </div>
</aside>
''')

# ───────────────────────── LEADERBOARD ─────────────────────────
ROWS = [(1,'푸른고래58','SA','세무조정 · TP','up',1,86,41,412,'2,418'),
        (2,'은빛여우07','M','세무조사지원','dn',1,74,38,366,'2,106'),
        (3,'검은돌고래40','SM','필라2','up',4,61,27,318,'1,874'),
        (4,'회색기러기12','P','경정청구','sm',0,58,22,291,'1,702'),
        (5,'붉은여우31','SA','이전가격(TP)','up',2,52,19,264,'1,588'),
        (6,'푸른사슴09','M','법인세','dn',3,47,16,238,'1,471'),
        (7,'흰기러기02','SA','경정청구','up',6,44,21,219,'1,402'),
        (8,'검은여우77','SM','세무진단','sm',0,41,14,206,'1,338'),
        (9,'노란수달13','M','부가가치세','up',1,39,18,197,'1,274'),
        (10,'푸른매21','SA','국제조세','dn',2,36,11,184,'1,205'),
        (11,'회색늑대64','S','세무조정','up',9,34,15,172,'1,147'),
        (12,'붉은두루미05','SM','상속 · 증여','dn',1,31,9,158,'1,081')]

def delta(kind, n):
    if kind == 'sm':
        return '<span class="dl sm">&mdash;</span>'
    ar = '&#9650;' if kind == 'up' else '&#9660;'
    return '<span class="dl %s"><span class="ar">%s</span><span class="vn">%d</span></span>' % (kind, ar, n)

tr = []
for r in ROWS:
    tr.append('<tr><td class="mono">%d</td><td class="dc">%s</td>'
              '<td><span class="hdl"><b>%s</b><span class="rk">%s</span></span></td>'
              '<td class="mt">%s</td><td class="n mono">%d</td><td class="n mono">%d</td>'
              '<td class="n mono">%d</td><td class="n sc">%s</td></tr>'
              % (r[0], delta(r[4], r[5]), r[1], r[2], r[3], r[6], r[7], r[8], r[9]))

w('board.html', top(SEARCH, R_USER, logo=WM) + '\n<div class="shell">\n' + nav() + '''
<main class="main">
  <div class="hd" style="padding:0 2px;">
    <h2 style="font-size:19px;">리더보드</h2>
    <span class="chips"><span class="chip d">주</span><span class="chip">월</span><span class="chip">분기</span><span class="chip">기간 지정</span></span>
    <span class="sp"></span><span class="mt"><span class="mono">11월 2주</span> · 확정 · 상위 <span class="mono">100</span>명 공개</span>
  </div>

  <section class="card acc" style="padding:14px 18px;">
    <div class="meta">
      <span class="mt">내 순위</span>
      <span style="font-size:22px; font-weight:700; color:var(--acc);" class="mono">42위</span>
      <span class="dl up"><span class="ar">&#9650;</span><span class="vn">5</span></span>
      <span class="mt">지난주 47위</span>
      <span style="flex:1"></span>
      <span class="mt">내 점수</span><span class="sc" style="font-size:20px; color:var(--ink);">1,284</span>
      <span class="dl up"><span class="ar">&#9650;</span><span class="vn">62</span></span>
    </div>
  </section>

  <section class="card">
    <table class="tight">
      <tr><th style="width:52px;">순위</th><th style="width:58px; text-align:center;">변동</th><th>닉네임</th><th style="width:146px;">주력 프로덕트</th>
        <th class="n" style="width:62px;">답변</th><th class="n" style="width:62px;">근거</th><th class="n" style="width:70px;">좋아요</th><th class="n" style="width:84px;">점수</th></tr>
      ''' + '\n      '.join(tr) + '''
    </table>
  </section>
</main>

<aside class="rail">
  <div class="rl">
    <h3>점수는 이렇게 쌓입니다</h3>
    <div class="sg">
      <div class="sgr"><span class="k">답변 작성</span><span class="v">+3</span></div>
      <div class="sgr"><span class="k">근거 제시</span><span class="v">+2</span></div>
      <div class="sgr hi"><span class="k">근거 있는 답변 1건</span><span class="v">+5</span></div>
      <div class="sgr"><span class="k">받은 좋아요</span><span class="v">+1</span></div>
      <div class="sgr"><span class="k">질문 · 정정 댓글</span><span class="v">+1</span></div>
      <div class="sgr"><span class="k">우수 Q&amp;A 선정</span><span class="v">+10</span></div>
    </div>
    <div class="sgn"><b>반감기 180일</b><span>6개월 활동이 없으면 점수가 절반이 됩니다. 지금 쓰는 사람이 위로 옵니다</span></div>
  </div>
  <div class="rl">
    <h3>이번 주 상승 폭</h3>
    <div class="rrow"><span class="hdl"><b>검은돌고래40</b><span class="rk">SM</span></span><span class="sp"></span><span class="dl up">▲4</span></div>
    <div class="rrow"><span class="hdl"><b>붉은여우31</b><span class="rk">SA</span></span><span class="sp"></span><span class="dl up">▲2</span></div>
    <div class="rrow"><span class="hdl"><b>푸른고래58</b><span class="rk me">SA</span></span><span class="sp"></span><span class="dl up">▲5</span></div>
  </div>
  <div class="rl">
    <h3>미답변 · 지연</h3>
    <div class="tx" style="font-size:13.5px;">72시간 초과 <span class="sc" style="color:var(--acc);">7</span>건</div>
    <div class="more">목록 보기</div>
  </div>
</aside>
''')

# ───────────────────────── MY PAGE ─────────────────────────
w('mypage.html', top(SEARCH, R_USER, logo=WM) + '\n<div class="shell">\n' + nav() + '''
<main class="main">
  <section class="card acc">
    <div class="meta">
      <span class="av" style="width:44px; height:44px; border-radius:50%; background:#DDD9CE; display:inline-block;"></span>
      <div style="display:flex; flex-direction:column; gap:3px;">
        <span class="hdl"><b style="font-size:18px;">푸른고래58</b><span class="rk me">SA</span></span>
        <span class="mt">[본인 성명] · [사번] — 본인에게만 보입니다</span>
      </div>
      <span style="flex:1"></span>
      <div style="display:flex; flex-direction:column; align-items:flex-end; gap:2px;">
        <span class="mt">내 점수</span>
        <span class="sc" style="font-size:30px; color:var(--acc); line-height:1.1;">1,284</span>
        <span class="dl up">이번 주 ▲62 · 42위</span>
      </div>
    </div>
  </section>

  <div class="stats">
    <div class="stat"><span class="k">내 질문</span><span class="v mono">7</span></div>
    <div class="stat"><span class="k">내 답변</span><span class="v mono">86</span></div>
    <div class="stat"><span class="k">근거 제시</span><span class="v mono">41</span></div>
    <div class="stat"><span class="k">받은 좋아요</span><span class="v mono">412</span></div>
  </div>

  <section class="card">
    <div class="hd"><h2>최근 작성한 글</h2><span class="sp"></span><span class="more">전체 보기</span></div>
    <table>
      <tr><th style="width:92px;">유형</th><th>제목</th><th style="width:130px;">프로덕트</th><th class="n" style="width:80px;">좋아요</th><th class="n" style="width:92px;">작성일</th></tr>
      <tr><td><span class="chip a">근거 답변</span></td><td>인정이자 계산 기준일</td><td class="mt">세무조정</td><td class="n mono">12</td><td class="n mt mono">11.15.</td></tr>
      <tr><td><span class="chip">경험 답변</span></td><td>전자문서 원본 제출 범위</td><td class="mt">세무조사지원</td><td class="n mono">9</td><td class="n mt mono">11.13.</td></tr>
      <tr><td><span class="chip a">질문</span></td><td>특수관계 소멸 시 인정이자 처리</td><td class="mt">세무조정</td><td class="n mono">7</td><td class="n mt mono">11.11.</td></tr>
      <tr><td><span class="chip">의견 답변</span></td><td>조사 자료요청 대응 순서</td><td class="mt">세무조사지원</td><td class="n mono">5</td><td class="n mt mono">11.08.</td></tr>
      <tr><td><span class="chip a">근거 답변</span></td><td>가지급금 기중 변동분 안분</td><td class="mt">세무조정</td><td class="n mono">4</td><td class="n mt mono">11.05.</td></tr>
    </table>
  </section>
</main>

<aside class="rail">
  <div class="rl">
    <h3>내 점수 구성</h3>
    <div class="rrow"><span class="mt">답변 86건</span><span class="sp"></span><span class="v mono">258</span></div>
    <div class="rrow"><span class="mt">근거 41건</span><span class="sp"></span><span class="v mono">82</span></div>
    <div class="rrow"><span class="mt">받은 좋아요 412</span><span class="sp"></span><span class="v mono">412</span></div>
    <div class="rrow"><span class="mt">질문 · 댓글</span><span class="sp"></span><span class="v mono">34</span></div>
    <div class="rrow"><span class="mt">기간 감쇠</span><span class="sp"></span><span class="v mono" style="color:#B5433A;">−502</span></div>
    <div class="quiet">반감기 <span class="mono">180</span>일 적용 후 <span class="sc">1,284</span></div>
  </div>
  <div class="rl">
    <h3>내 정보 관리</h3>
    <div class="meta"><span class="mt" style="flex:1">알림 수신</span><span class="chip a">일간 요약</span></div>
    <div class="meta"><span class="mt" style="flex:1">구독 프로덕트</span><span class="chip">3개</span></div>
    <div class="meta"><span class="mt" style="flex:1">닉네임</span><span class="mt">변경 불가</span></div>
    <div class="meta"><span class="mt" style="flex:1">실명 공개</span><span class="chip">하지 않음</span></div>
  </div>
  <div class="rl">
    <h3>스크랩 · 알림</h3>
    <div class="mt">스크랩한 질문 <span class="mono">12</span></div>
    <div class="mt">알림 받는 질문 <span class="mono">5</span></div>
  </div>
</aside>
''')

# ───────────────────────── ADMIN ─────────────────────────
def admnav(active):
    items = [('운영', None),
             ('미답변 관리', 'ops'), ('콘텐츠 발행', 'ops'), ('신고 검토', 'ops'), ('몰아주기 모니터링', 'ops'),
             ('사용자', None),
             ('사용자 관리', 'usr'), ('신원 열람 승인', 'usr'),
             ('설정', None),
             ('프로덕트 말머리', 'set'), ('우수 Q&A · FAQ', 'set'), ('공지 · 운영규칙', 'set')]
    out = []
    for name, grp in items:
        if grp is None:
            out.append('<div class="sl">%s</div>' % name)
        else:
            out.append('<div class="si%s">%s</div>' % (' on' if name == active else '', name))
    return '<nav class="side">\n' + '\n'.join(out) + '\n</nav>'

ADM_SEARCH = '<div class="search">%s미답변 · 신고 · 사용자 검색<span class="kc">Ctrl K</span></div>' % ICON
R_ADM = '<span class="topit">운영 간사</span><span class="topit">내 프로필</span>'

w('admin.html', top(ADM_SEARCH, R_ADM, admin=True, logo=WM_ADM) + '\n<div class="shell">\n' + admnav('미답변 관리') + '''
<main class="main">
  <div class="stats">
    <div class="stat"><span class="k">전체 미답변</span><span class="v mono">24</span></div>
    <div class="stat hot"><span class="k">72시간 초과</span><span class="v mono">7</span></div>
    <div class="stat"><span class="k">24시간 내 첫 답변률</span><span class="v mono">68%</span></div>
    <div class="stat"><span class="k">주간 고유 답변자</span><span class="v mono">41</span></div>
  </div>

  <section class="card">
    <div class="hd"><h2>지연 질문</h2><span class="cnt mono">7</span>
      <span class="mt">세무조사지원 6 · 필라2 5 · TP 4 · 세무조정 3</span><span class="sp"></span><span class="more">전체 보기</span></div>
    <table>
      <tr><th>질문</th><th style="width:132px;">프로덕트</th><th class="n" style="width:92px;">경과</th><th class="n" style="width:124px;">조치</th></tr>
      <tr><td>전자문서 원본 제출 범위 <span class="mt mono" style="margin-left:8px;">Q-2026-00402</span></td>
        <td class="mt">세무조사지원</td><td class="n"><span class="chip w">5일</span></td><td class="n"><span class="btn sm">큐레이터 지정</span></td></tr>
      <tr><td>GloBE 정보신고서 기한 <span class="mt mono" style="margin-left:8px;">Q-2026-00398</span></td>
        <td class="mt">필라2</td><td class="n"><span class="chip w">4일</span></td><td class="n"><span class="btn sm">큐레이터 지정</span></td></tr>
      <tr><td>이전가격 사전승인 신청 범위 <span class="mt mono" style="margin-left:8px;">Q-2026-00391</span></td>
        <td class="mt">이전가격(TP)</td><td class="n"><span class="chip">3일</span></td><td class="n"><span class="btn q sm">큐레이터 지정</span></td></tr>
    </table>
    <div class="quiet">필라2는 2주째 적체 — 큐레이터 지정을 권장합니다</div>
  </section>

  <section class="card">
    <div class="hd"><h2>콘텐츠 발행</h2><span class="sp"></span><span class="more">작성 · 예약 · 노출 관리</span></div>
    <table>
      <tr><th style="width:108px;">상태</th><th>제목</th><th class="n" style="width:168px;">일시</th></tr>
      <tr><td><span class="chip a">발행 예정</span></td><td>2026년 세법개정 주요 쟁점 정리</td><td class="n mt mono">11.18. 08:00</td></tr>
      <tr><td><span class="chip">초안</span></td><td>제조업 세무진단 체크포인트 10</td><td class="n mt">작성 중</td></tr>
      <tr><td><span class="chip">발행됨</span></td><td>필라2 적용 첫 해, 실무에서 막히는 지점</td><td class="n mt mono">11.05. 08:00</td></tr>
    </table>
  </section>
</main>

<aside class="rail">
  <div class="rl">
    <h3>주간 다이제스트</h3>
    <div class="mt">월요일 <span class="mono">08:00</span> 발송</div>
    <div class="tx" style="font-size:13px;">구독자별 미답변 Top <span class="mono">5</span> + 그 주 새로운 소식</div>
    <span class="btn q sm" style="align-self:flex-start;">미리보기</span>
  </div>
  <div class="rl">
    <h3>신고 검토</h3>
    <div class="rrow"><span class="mt">대기</span><span class="sp"></span><span class="v mono">2</span></div>
    <div class="rrow"><span class="mt">고객정보 의심</span><span class="sp"></span><span class="v mono" style="color:var(--acc);">1</span></div>
    <div class="quiet">고객정보 신고는 1건으로 즉시 블라인드됩니다</div>
  </div>
  <div class="rl">
    <h3>몰아주기 플래그</h3>
    <div class="rrow"><span class="mt">검토 대기</span><span class="sp"></span><span class="v mono">0</span></div>
    <div class="mt">자동 제재 없이 사람이 검토합니다</div>
  </div>
</aside>
''')

USERS = [('푸른고래58','SA','2026.03.','세무조정','7','86','1,284','0','정상'),
         ('은빛여우07','M','2025.11.','세무조사지원','12','74','2,106','0','정상'),
         ('검은돌고래40','SM','2026.01.','필라2','4','61','1,874','1','정상'),
         ('잿빛두루미88','S','2026.07.','법인세','21','3','142','4','검토 필요'),
         ('회색기러기12','P','2025.08.','경정청구','3','58','1,702','0','정상'),
         ('붉은여우31','SA','2026.02.','이전가격(TP)','9','52','1,588','0','정상'),
         ('푸른사슴09','M','2025.12.','법인세','6','47','1,471','1','정상'),
         ('노란수달13','M','2026.04.','부가가치세','11','39','1,274','0','정상'),
         ('검은올빼미56','S','2026.09.','세무진단','17','2','96','3','검토 필요'),
         ('회색늑대64','S','2026.06.','세무조정','8','34','1,147','0','정상'),
         ('흰기러기02','SA','2025.09.','경정청구','2','9','318','0','휴면 예정')]
urows = []
for u in USERS:
    warn = ' class="me-row"' if u[8] == '검토 필요' else ''
    urows.append('<tr%s><td><span class="hdl"><b>%s</b><span class="rk">%s</span></span></td>'
                 '<td class="mt mono">%s</td><td class="mt">%s</td><td class="n mono">%s</td><td class="n mono">%s</td>'
                 '<td class="n sc">%s</td><td class="n mono">%s</td><td class="n"><span class="chip%s">%s</span></td>'
                 '<td class="n"><span class="btn q sm">관리</span></td></tr>'
                 % (warn, u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], ' w' if u[8] == '검토 필요' else '', u[8]))

w('admin-users.html', top(ADM_SEARCH, R_ADM, admin=True, logo=WM_ADM) + '\n<div class="shell">\n' + admnav('사용자 관리') + '''
<main class="main">
  <div class="stats">
    <div class="stat"><span class="k">전체 사용자</span><span class="v mono">1,342</span></div>
    <div class="stat"><span class="k">이번 주 활성</span><span class="v mono">412</span></div>
    <div class="stat hot"><span class="k">신고 누적 3건 이상</span><span class="v mono">2</span></div>
    <div class="stat"><span class="k">6개월 미활동</span><span class="v mono">87</span></div>
  </div>

  <section class="card">
    <div class="hd"><h2>사용자 관리</h2>
      <span class="chips"><span class="chip d">전체</span><span class="chip">검토 필요</span><span class="chip">휴면</span><span class="chip">전출</span></span>
      <span class="sp"></span><span class="more"><span class="mono">1,342</span>명 중 <span class="mono">10</span>명 · HR 동기화 <span class="mono">11.15. 04:00</span></span></div>
    <table class="tight">
      <tr><th>닉네임</th><th style="width:86px;">가입</th><th style="width:118px;">주력</th>
        <th class="n" style="width:56px;">질문</th><th class="n" style="width:56px;">답변</th>
        <th class="n" style="width:76px;">점수</th><th class="n" style="width:56px;">신고</th>
        <th class="n" style="width:92px;">상태</th><th class="n" style="width:72px;">조치</th></tr>
      ''' + '\n      '.join(urows) + '''
    </table>
  </section>
</main>

<aside class="rail">
  <div class="rl">
    <h3>선택 사용자</h3>
    <div class="card" style="padding:13px 15px; gap:9px;">
      <span class="hdl"><b style="font-size:15px;">잿빛두루미88</b><span class="rk">S</span></span>
      <div class="mt"><span class="mono">2026.07.</span>부터 활동 · 법인세</div>
      <div class="meta"><span class="mt" style="flex:1">점수</span><span class="sc">142</span></div>
      <div class="meta"><span class="mt" style="flex:1">신고 누적</span><span class="sc" style="color:var(--acc);">4</span></div>
    </div>
    <div class="quiet">실명 · 사번은 표시되지 않습니다</div>
    <span class="btn q sm" style="align-self:flex-start;">실명 열람 신청 — 2인 승인</span>
  </div>
  <div class="rl">
    <h3>신고 이력</h3>
    <div class="pt-row"><span class="n tx" style="font-size:13px;">업무 무관 게시</span><span class="mt mono">11.12.</span></div>
    <div class="pt-row"><span class="n tx" style="font-size:13px;">오정보</span><span class="mt mono">11.09.</span></div>
    <div class="pt-row"><span class="n tx" style="font-size:13px;">업무 무관 게시</span><span class="mt mono">11.02.</span></div>
  </div>
  <div class="rl">
    <h3>조치</h3>
    <div class="meta"><span class="btn q sm">경고 발송</span><span class="btn q sm">작성 제한</span></div>
    <div class="meta"><span class="btn q sm">닉네임 재발급</span><span class="btn q sm">휴면 전환</span></div>
    <div class="mt">모든 조치는 감사 로그에 남습니다</div>
  </div>
</aside>
''')
