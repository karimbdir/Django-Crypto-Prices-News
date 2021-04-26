from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json
    #Crypto Prices
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,EOS,LTC&tsyms=TND')
    price = json.loads(price_request.content)
    #Crypto news
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request,"home.html", {'api': api, 'price':price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=TND")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote':quote, 'crypto':crypto})
    else:
        notfound = "Enter a Valid Crypto Symbol.."
        return render(request,'prices.html', {"notfound":notfound})
    
