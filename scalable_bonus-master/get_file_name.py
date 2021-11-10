import requests

res = requests.get("https://cs7ns1.scss.tcd.ie/index.php?download=noresume_speed&shortname=bonus")

with open('filenames.csv', mode='wb') as f:
        f.write(res.content)

