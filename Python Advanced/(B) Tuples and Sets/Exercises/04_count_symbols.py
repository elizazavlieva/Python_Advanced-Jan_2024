text = tuple(map(str, input()))
text_info = {symbol: text.count(symbol) for symbol in text}
sorted_dict = dict(sorted(text_info.items()))

for k, v in sorted_dict.items():
    print(f'{k}: {v} time/s')
