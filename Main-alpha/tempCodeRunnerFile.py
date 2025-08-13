def log_message(*args, **kwargs):
    with open('logs.txt', 'a', encoding='utf-8') as f:
        print(*args, **kwargs, file=f)