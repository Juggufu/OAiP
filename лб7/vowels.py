def vowels(s):
    if not s:    return 0
    return (1 if s[0] in 'йуеыаояиюЙУЕОАЫЯИЮaeiouAEIOU' else 0) + vowels(s[1:])



