text = tuple(map(str, input()))
text_info = dict()

for symbol in text:
    if symbol not in text_info:
        text_info[symbol] = text.count(symbol)

sorted_dict = dict(sorted(text_info.items()))

for k, v in sorted_dict.items():
    print(f'{k}: {v} time/s')
