word = input()
start = int(input())
end = int(input()) + 1
slice = word[start:end]

print(slice*(len(word)//len(slice)+1))