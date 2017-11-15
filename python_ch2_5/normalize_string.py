import re

states = [
    'Alabama',
    ' Georgia!',
    'Georgia ',
    'georgia',
    'FlOrIda',
    'south carolina   ',
    'West virginia?']

# 문자열에 필터를 걸어 특정 문자열만 뽑아내고 싶을 때 두 가지 방법

# 1번

def clean_strings(strings):
    results = []
    for string in strings:
        string = string.strip()
        string = re.sub('[!#?]', '', string)
        string = string.title()
        results.append(string)

    return results


results = clean_strings(states)
print(results)

# 2번, 이 방법을 선호한다. (단, 정규식은 아래처럼 함수로 정의해 준 다음 함수객체를 넘겨주면 됨)
def remove_specialchar(string):
    return re.sub('[!#?]', '', string)


def clean_strings2(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)

    return results

results = clean_strings2(
    states,
    str.strip,
    str.title,
    remove_specialchar)
print(results)