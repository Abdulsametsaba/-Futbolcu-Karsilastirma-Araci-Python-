from PIL import Image
from  io import BytesIO
import requests
class Futbolcu:
    def __init__(self,name,pac,sho,pas,dri,dEf,phy):
        self.pac=pac
        self.sho=sho
        self.dri=dri
        self.pas=pas    
        self.dEf=dEf
        self.phy=phy
        self.name=name
    def ozellik_hazirla(self):
        return ",".join([str(self.pac),
                  str(self.sho),
                  str(self.dri),
                  str(self.pas),
                  str(self.dEf),
                  str(self.phy),
                  str(self.pac)])
    def kiyasla(self,hedef_veri):
        grafik_araci_URL='https://image-charts.com/chart'
        payload={'chco':'3092de,027182',
                 'chd':'t:'+self.ozellik_hazirla()+'|'+hedef_veri.ozellik_hazirla(),
                 'chdl':self.name+'|'+hedef_veri.name,
                 'chdlp':'b',
                 'chs':'480x480',
                 'cht':'r',
                 'chtt':'Futbolcu Özellikleri',
                 'chl':'hiz|sut|top_surus|pas|defans|fizik',
                 'chxl':'0:|0|20|40|60|80|100',
                 'chxt':'x',
                 'chxr':'0,0.0,100.0',
                 'chm':'B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0'
                }
        response=requests.post(grafik_araci_URL,data=payload)
        image=Image.open(BytesIO(response.content))
        image.show()

def main():
  messi=Futbolcu("Lionel Messi ",87,90,93,96,39,71)
  ronaldo=Futbolcu("Cristiano Ronaldo",91,96,88,92,42,90)
  messi.kiyasla(ronaldo)
if __name__=='__main__':
  main()
