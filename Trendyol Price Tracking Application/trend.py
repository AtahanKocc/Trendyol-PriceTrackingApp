import requests
from bs4 import BeautifulSoup
from send_mail import sendMail

url1="https://www.trendyol.com/mooodcase/samsung-a51-harita-desenli-premium-silikonlu-siyah-telefon-kilifi-p-89513405?boutiqueId=595080&merchantId=233527"

headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

page = requests.get(url1, headers=headers)  #sayfanın içeriğini alıyoruz

htmlPage = BeautifulSoup(page.content,'html.parser') #yukarıdaki sayfanın içeriğini alacagız

productTitle= htmlPage.find("h1", class_="pr-new-br").getText()


price = htmlPage.find("span",class_="prc-slg").getText()

image = htmlPage.find("img",)

convertedPrice = float(price.replace(",",".").replace(" TL",""))

if(convertedPrice <= 225):
    print("The product price decreased.", class_="ürün class yaz.")
    htmlEmailContent= """\<
    <html>
    <head> </head>
    <body>
    <h3>{0}</h3>
    <br/>
    {1}  #resim kısmı
      <br/>
      <p> Ürün Linki: {2} </p>
    </body>
    </html>
    """.format(productTitle,image,url1)
    sendMail("koccata@gmail.com","The product price decreased", htmlEmailContent)
print(convertedPrice)
"""
User Agent (Kullanıcı Aracısı) interneti kullanan kişiler ile web içerikleri arasında köprü vazifesi gören tarayıcı anahtarı olarak tanımlanabilir. User Agent, internet ortamındaki kullanıcının mevcut olan bilgilerini taşımaktadır.
"""