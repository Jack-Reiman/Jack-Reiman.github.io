with open('assets/index-BwGDr2zK.js', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('page__fig')
print(text[idx-5000:idx-2500].encode('ascii', errors='replace').decode())
