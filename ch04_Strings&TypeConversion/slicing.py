"""
-->String Slicing
Slicing cuts out a piece of a string. 
Syntax: string[start : stop : step] — note that stop index is excluded.
If start is omitted, it defaults to 0. If stop is omitted, it defaults to the length of the string. If step is omitted, it defaults to 1.
Agar poora string chahiye to start ko 0 aur stop ko length of string rakhna hoga.
Agar string ko reverse karna hai to step ko -1 rakhna hoga. 
Agar hello string me hme poora word chahiye to start ko 0 aur stop ko 5 rakhna hoga, kyunki stop index exclude hota hai. Agar hme sirf ell chahiye to start ko 1 aur stop ko 4 rakhna hoga, kyunki stop index exclude hota hai.
Hame jaha tak jana usse ek index aage rakhna hoga, kyunki stop index exclude hota hai.
a = "hello"
print(a[1:4])    # ell  (index 1,2,3 — 4 excluded) Isme h index 1 se start hoga aur 4 se pehle khatam hoga, isliye 1,2,3 index ke characters print honge.
print(a[:4])     # hell  (start default 0 se hoga) 
print(a[::-1])   # olleh  (reversed!)
"""
# C O L L E G E
# 0 1 2 3 4 5 6
a = "COLLEGE" # Suppose we want to slice the string "COLLEGE" to get "LEG"
print(a[3:6:1]) # LEG (index 3,4,5 — 6 excluded)
print(a[0:7])  # COLLEGE (index 0,1,2,3,4,5,6 — 7 excluded)
print(a[3:6])   # LEG (step default 1)
print(a[3:])    # LEGE (start index 3 se hoga aur stop index default length of string hoga)
print(a[:6])    # COLLEG (start index default 0 se hoga aur stop index 6 se hoga, kyunki stop index exclude hota hai)
print(a[3:6:2]) # LG (index 3,5 — 6 excluded, step 2 hone ki wajah se index 4 skip hoga)
print(a[6:3:-1]) # EGE (reverse me index 6 se start hoga aur 3 se pehle khatam hoga, isliye index 6,5,4 ke characters print honge)
print(a[::]) # COLLEGE (start default 0 se hoga, stop default length of string hoga, step default 1 hoga)
print(a[::-1]) # EGELLOC (reverse of the string)
print(a[::2]) # CLEE (index 0,2,4,6 — step 2 hone ki wajah se index 1,3,5 skip honge)
print(a[0:7:2]) # CLEE (index 0,2,4,6 — step 2 hone ki wajah se index 1,3,5 skip honge)

b = "Hello how are you?"
#    01234 5 678 9 101112 13 14151617
# Task is to print how then you then Hello
print(b[6:9]) # how (index 6,7,8 — 9 excluded)
print(b[14:18]) # you (index 14,15,16,17 — 18 excluded)
print(b[:5]) # Hello (start default 0 se hoga aur stop index 5 se hoga, kyunki stop index exclude hota hai)