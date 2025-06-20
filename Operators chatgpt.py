"""
✅ পাইথনের অপারেটরগুলো মূলত ৭ প্রকারের:
ক্র.	অপারেটর টাইপ	বাংলা ব্যাখ্যা
1	Arithmetic Operators	গাণিতিক অপারেটর
2	Assignment Operators	মান সেট করার অপারেটর
3	Comparison Operators	তুলনা করার অপারেটর
4	Logical Operators	লজিক্যাল (যুক্তি ভিত্তিক) অপারেটর
5	Identity Operators	আইডেন্টিটি যাচাই
6	Membership Operators	সদস্যতা যাচাই
7	Bitwise Operators	বিট ভিত্তিক অপারেটর

1️⃣ Arithmetic Operators (গাণিতিক অপারেটর)
অপারেটর	কাজ	উদাহরণ	ফলাফল
+	যোগ	5 + 3	8
-	বিয়োগ	5 - 3	2
*	গুণ	5 * 3	15
/	ভাগ	5 / 2	2.5
//	পূর্ণসংখ্যায় ভাগ	5 // 2	2
%	ভাগশেষ	5 % 2	1
**	ঘাত	2 ** 3	8

2️⃣ Assignment Operators (মান সেট করার অপারেটর)
অপারেটর	কাজ	উদাহরণ	সমতুল্য
=	মান নির্ধারণ	x = 5	-
+=	যোগ করে মান সেট	x += 2	x = x + 2
-=	বিয়োগ করে মান সেট	x -= 2	x = x - 2
*=	গুণ করে মান সেট	x *= 2	x = x * 2
/=	ভাগ করে মান সেট	x /= 2	x = x / 2
//=	পূর্ণসংখ্যায় ভাগ	x //= 2	x = x // 2
%=	ভাগশেষ নির্ধারণ	x %= 2	x = x % 2
**=	ঘাত নির্ধারণ	x **= 3	x = x ** 3

3️⃣ Comparison Operators (তুলনামূলক অপারেটর)
অপারেটর	কাজ	উদাহরণ	ফলাফল
==	সমান কিনা	x == y	True বা False
!=	সমান না কিনা	x != y	True বা False
>	বড় কিনা	x > y	True
<	ছোট কিনা	x < y	False
>=	বড় বা সমান	x >= y	True
<=	ছোট বা সমান	x <= y	False

4️⃣ Logical Operators (যুক্তি ভিত্তিক অপারেটর)
অপারেটর	কাজ	উদাহরণ	ফলাফল
and	দুটি শর্তই সত্য হলে	x > 3 and x < 10	True
or	যেকোনো একটি সত্য হলেই	x > 3 or x < 2	True
not	সত্যকে মিথ্যা করে	not(x > 3)	False

5️⃣ Identity Operators (পরিচয় যাচাই করে)
অপারেটর	কাজ	উদাহরণ	ফলাফল
is	একই অবজেক্ট কিনা	x is y	True
is not	আলাদা অবজেক্ট কিনা	x is not y	True

📝 দুই ভেরিয়েবল একই ভ্যালু রাখলেও তারা একই অবজেক্ট কিনা সেটা is দিয়ে চেক করা হয়।

6️⃣ Membership Operators (সদস্যতা যাচাই)
অপারেটর	কাজ	উদাহরণ	ফলাফল
in	সদস্য আছে কিনা	'a' in 'ratul'	True
not in	সদস্য নেই কিনা	'z' not in 'ratul'	True

7️⃣ Bitwise Operators (বিটে কাজ করে)
অপারেটর	নাম	কাজ
&	AND	দুই বিটেই ১ হলে ১
`	`	OR
^	XOR	একটাই ১ হলে ১
~	NOT	বিট উল্টে দেয়
<<	Left Shift	বিট বাঁয়ে সরায়
>>	Right Shift	বিট ডানে সরায়
"""




'''
পাইথনের ৭ প্রকার অপারেটর: উদাহরণসহ


1️⃣ Arithmetic Operators (গাণিতিক অপারেটর)

a = 10
b = 3

print("যোগ (a + b):", a + b)
print("বিয়োগ (a - b):", a - b)
print("গুণ (a * b):", a * b)
print("ভাগ (a / b):", a / b)
print("পূর্ণ ভাগ (a // b):", a // b)
print("ভাগশেষ (a % b):", a % b)
print("ঘাত (a ** b):", a ** b)
2️⃣ Assignment Operators (মান সেট অপারেটর)

x = 5
print("x =", x)

x += 2
print("x += 2 →", x)

x -= 1
print("x -= 1 →", x)

x *= 3
print("x *= 3 →", x)

x /= 2
print("x /= 2 →", x)

x %= 4
print("x %= 4 →", x)

x **= 2
print("x **= 2 →", x)



3️⃣ Comparison Operators (তুলনামূলক অপারেটর)

a = 10
b = 7

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
4️⃣ Logical Operators (যুক্তি নির্ভর অপারেটর)

x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# বাস্তব শর্ত উদাহরণ
age = 20
print("বয়স 18 থেকে 25 এর মধ্যে?", age >= 18 and age <= 25)


5️⃣ Identity Operators (পরিচয় যাচাই)

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x == y:", x == y)    # মান একই
print("x is y:", x is y)    # আলাদা অবজেক্ট
print("x is z:", x is z)    # একই অবজেক্ট
print("x is not y:", x is not y)

6️⃣ Membership Operators (সদস্যতা যাচাই)

my_list = [10, 20, 30, 40]

print("20 in my_list:", 20 in my_list)
print("50 in my_list:", 50 in my_list)
print("50 not in my_list:", 50 not in my_list)



7️⃣ Bitwise Operators (বিট অপারেটর)

a = 5    # Binary: 0101
b = 3    # Binary: 0011

print("a & b:", a & b)   # 0101 & 0011 = 0001 → 1
print("a | b:", a | b)   # 0101 | 0011 = 0111 → 7
print("a ^ b:", a ^ b)   # 0101 ^ 0011 = 0110 → 6
print("~a:", ~a)         # ~0101 = -(5+1) = -6
print("a << 1:", a << 1) # 0101 → 1010 → 10
print("a >> 1:", a >> 1) # 0101 → 0010 → 2


🟢 সংক্ষেপে মনে রাখার ট্রিক:
অপারেটর টাইপ	প্রধান কাজ

Arithmetic	যোগ-বিয়োগ-গুণ-ভাগ
Assignment	মান সেট করা
Comparison	তুলনা করা
Logical	শর্ত পরীক্ষা
Identity	একই অবজেক্ট কিনা
Membership	লিস্টে আছে কিনা
Bitwise	বিট লেভেল অপারেশন
'''
