def check(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    last_seen_s = {}
    last_seen_t = {}

    for i, (char_s, char_t) in enumerate(zip(s, t)):
        if last_seen_s.get(char_s) != last_seen_t.get(char_t):
            return False

        last_seen_s[char_s] = i
        last_seen_t[char_t] = i

    return True


def primes(n : int) -> list:
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]


s = input()

p = primes(9999999)

for t in p :
    if check(s, str(t)): 
        print(t)
        exit(0)

print(-1)