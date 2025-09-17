import re

def check_strength(pw):
    score = 0
    if len(pw) >= 8: score += 1
    if re.search(r"[a-z]", pw): score += 1
    if re.search(r"[A-Z]", pw): score += 1
    if re.search(r"\d", pw): score += 1
    if re.search(r"[^\w\s]", pw): score += 1

    levels = ["Very Weak", "Weak", "Fair", "Strong", "Excellent"]
    return levels[score]

print(check_strength("Hello123"))   # Strong
print(check_strength("abc"))        # Very Weak
