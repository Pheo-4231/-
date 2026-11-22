import re

with open("07-02. 전주대 대동제 및 해커톤 통합운영 데이터 로그.txt",
          "r", encoding="utf-8") as f:
    text = f.read()

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+\b'
emails = re.findall(email_pattern, text)

phone_pattern = r'\b010[-. ]\d{4}[-. ]\d{4}\b'
phones = re.findall(phone_pattern, text)

# 3. 학번과 학과 추출
student_pattern = r'\[(202\d{6})\s*/\s*([^\]]+)\]'
students = re.findall(student_pattern, text)

github_pattern = r'https?://github\.com/[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+'
githubs = re.findall(github_pattern, text)

coupon_pattern = r'\bFEST-2026-[A-Z0-9]{4}\b'
coupons = re.findall(coupon_pattern, text)

sales_pattern = r'- (.+?) 매출:\s*([\d,]+)원'
sales = re.findall(sales_pattern, text)

total_sales = 0

print("=" * 50)
print("1. 유효한 이메일")
print("=" * 50)

for email in emails:
    print(email)


print("\n" + "=" * 50)
print("2. 휴대폰 번호")
print("=" * 50)

for phone in phones:
    print(phone)


print("\n" + "=" * 50)
print("3. 학번 / 학과")
print("=" * 50)

for student_id, department in students:
    print((student_id, department))


print("\n" + "=" * 50)
print("4-1. GitHub 저장소")
print("=" * 50)

for github in githubs:
    print(github)


print("\n" + "=" * 50)
print("4-2. 유효 쿠폰")
print("=" * 50)

for coupon in coupons:
    print(coupon)


print("\n" + "=" * 50)
print("5. 부스별 총 매출액")
print("=" * 50)

for booth, amount in sales:
    amount = int(amount.replace(",", ""))
    total_sales += amount

    print(f"{booth}: {amount:,}원")


print("\n전체 매출 합계:", f"{total_sales:,}원")