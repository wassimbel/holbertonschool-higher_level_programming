#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
s = dir(hidden_4)
for i in range(1, len(s)):
    if s[i][:1] != '_':
        print("{:s}".format(s[i]))
