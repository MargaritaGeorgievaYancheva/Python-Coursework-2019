def mutate_string(string, position, character):
 listOFStrings=list(string)
 listOFStrings[position]=character
 string=''.join(listOFStrings)
 return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)