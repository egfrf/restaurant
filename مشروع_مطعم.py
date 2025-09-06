from kivymd.app import  MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineIconListItem, OneLineListItem, TwoLineIconListItem, IconLeftWidget, ImageLeftWidget, ThreeLineAvatarIconListItem,  IconRightWidget
from kivymd.uix.bottomsheet import MDBottomSheet, MDCustomBottomSheet

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatIconButton, MDFloatingActionButton, MDIconButton, MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.label import Label

Window.size=(380, 600)

KV=('''  
ScreenManager:
    Ham:
    Addwid: # ضيفهم في كلاسس ScreemManager
    
<Ham>:
    name: 'Ham'
    MDBoxLayout:
        orientation: 'vertical'   
        spacing: 5
        
        
        ScrollView:
            size_hint_y: None
            height: '60dp'
            pos_hint: {'x': 0.0, 'y': 0.9}
            do_scroll_x: True
            do_scroll_y: False
             
            MDBoxLayout:
                orientation: 'horizontal'
                md_bg_color: 1, 0.5, 0, 1
                spacing: 10
                padding: '10dp'
                height: '25dp'
                size_hint_x: None
                height: self.minimum_height
                width: self.minimum_width
            
                MDChip:
                    text: 'Hamburgr'
                    type: 'input'
                    on_release: root.open_list('Hamburgar')
                    MDChipText:
                        text: 'Hamburgr'
                    MDChipLeadingIcon:
                        icon: 'hamburger'
                        color: 'orange'
                        
                        
                MDChip:
                    text: 'Drinks'
                    type: 'input'
                    on_release: root.open_list('Deinks')
                    MDChipText:
                        text: 'drinks'
                    MDChipLeadingIcon:
                        icon: 'glass-fragile'
                        color: 'blue'
                        
                        
                            
                MDChip:
                    text: 'Cake'
                    type: 'input'
                    on_release: root.open_list('Cakes')
                    MDChipText:
                        text: 'cake'
                    MDChipLeadingIcon:
                        icon: 'cupcake'
                        color: 'red'
                
                MDChip:
                    text: 'Hutfood'
                    on_release: root.open_list('Hutfood')
                    MDChipText:
                        text: 'HotFood'
                    MDChipLeadingIcon:
                        icon: 'food-turkey'
                        color: 'darkorange'
                        
        
                
        MDTextField:
            id: text_shert
            hint_text: 'Shert Enter Name ?'
            mode: 'round'
            size_hint: None, None
            size: 300, 100
            pos_hint: {'x': 0.1}
            on_text_validate: app.shert(self.text)
            
            
        
                                
        ScrollView:     
            id: list_contenyr    
                 
          
<Addwid>:
    name: "Addwid"
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Requests section'
            pos_hint: {'top': 1}
            md_bg_color: 1, 0.5, 0, 1
        
        MDIconButton:
            icon: 'arrow-left'
            on_release: root.goto_scr_main()

        BoxLayout:
            orientation: 'vertical'
            id: cotayner

    MDIconButton:
        icon: 'plus-circle'
        pos_hint: {'x': 0.75, 'y': 0.1}
        icon_size: 40
        theme_icon_color: 'Custom'
        icon_color: 1, 0.5, 0, 1
        on_press: root.goto_scr_main()
            
        
        

    MDChip:
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
        on_release: root.open_list_add()
        
        MDChipText:
            text: 'Requests'
            
        MDChipLeadingIcon:
            icon: 'cart'
            color: 'red'
            
      
  
    
                    
                    
                
                
    

''')

user_window={
            "Hamburgar":[
                {'name': 'Hamborgr', 'icon': 'ico_ham//bata.ico', 'price': '10.0', 'info':'meat +\nvegetables + \nFish eggs'},
                {'name': 'Fingar', 'icon': 'ico_ham//fingar.ico', 'price': '8.0', 'info':'Batatis +\nvegetables + \ncola'},
                {'name': 'Burgarme', 'icon': 'ico_ham//brja2.ico', 'price': '8.50','info':'meat +\ninsia + \nVegetable'},
                {'name': 'Burjar', 'icon': 'ico_ham//brjr.ico', 'price': '5.50','info':'Chickenmeat +\insia + \nVegetable'},
                {'name': 'Broom', 'icon': 'ico_ham//bromm.ico', 'price': '4.0','info':'Chest +\ninsia + \nChickens'},
                {'name': 'Custom', 'icon': 'ico_ham//cuscus.ico', 'price': '6.0','info':'bulgur +\nspices + \nCuscus'},
                {'name': 'Lahem', 'icon': 'ico_ham//lahem.ico', 'price': '1.20','info':'meat +\nspices + \nDiet'},
                {'name': 'Hamburgr', 'icon': 'ico_ham//hamborgar.ico', 'price': '1.20','info':'meat +\nspices + \nhefi'},
                {'name': 'Piza', 'icon': 'ico_ham//piza.ico', 'price': '1.20','info':'meat +\nspices'}
                
            ],
            "Deinks":[
                {'name':'Yenap', 'icon': 'ico_drk//dcar.ico', 'price': '1.50','info':'peach +\niced'},
                {'name':'Cola', 'icon': 'ico_drk//dcola.ico', 'price': '2.50','info':'cola +\npipsy'},
                {'name':'Orange', 'icon': 'ico_drk//ddri.ico', 'price': '3.0','info':'orang +\niced'},
                {'name':'Farola', 'icon': 'ico_drk//dfaro.ico', 'price': '6.0','info':'Strawberry +\niced'},
                {'name':'Jhay', 'icon': 'ico_drk//djay.ico', 'price': '7.0','info':'Shahi +\nHot Mahil'},
                {'name':'Lamon', 'icon': 'ico_drk//dkash.ico', 'price': '8.0','info':'lamoon +\niced'},
                {'name':'Dorick', 'icon': 'ico_drk//dlame.ico', 'price': '2.0','info':'rashe +\niced'},
                {'name':'Apple', 'icon': 'ico_drk//dora.ico', 'price': '1.0','info':'lamoon +\niced'},
                {'name':'Cahoa', 'icon': 'ico_drk//dqah.ico', 'price': '3.50','info':'apple +\niced'}
            ],
            "Cakes": [
                {'name': "Maose", 'icon': 'ico_cyk//kblo.ico', 'price': '2.30','info':'panana +\nmilk'},
                {'name': "Holebol", 'icon': 'ico_cyk//kdcc.ico', 'price': '4.50','info':'cayko +\nmilk'},
                {'name': "Monert", 'icon': 'ico_cyk//kkan.ico', 'price': '8.50','info':'walnut +\nmilk'},
                {'name': "Almaje", 'icon': 'ico_cyk//kred.ico', 'price': '10.50','info':'Strawberry +\nmilk'},
                {'name': "Samje", 'icon': 'ico_cyk//ksan.ico', 'price': '2.50','info':'cocoa +\nmilk'},
                {'name': "Layun", 'icon': 'ico_cyk//ksd.ico', 'price': '1.10','info':'cocoa +\nmilk'},
                {'name': "Moneta", 'icon': 'ico_cyk//ksxs.ico', 'price': '9.50','info':'milkjoz +\nmilk'},
                {'name': "Redbol", 'icon': 'ico_cyk//kwd.ico', 'price': '11.50','info':'hory +\nmilk'},
                {'name': "Taijer", 'icon': 'ico_cyk//kyan.ico', 'price': '5.0','info':'tiger +\nmilk'},
            ],
            'Hutfood': [
                {'name': 'Andome', 'icon': 'hut//edede1.ico', 'price': '12.5','info':'andome +\nspices'},
                {'name': 'Fish', 'icon': 'hut//fhish.ico', 'price': '22.5','info':'Fish grills +\nFish with,oil'},
                {'name': 'Frice', 'icon': 'hut//edede.ico', 'price': '40.0','info':'Crab meat +\nspices'},
                {'name': 'Chikn', 'icon': 'hut//chikn.ico', 'price': '10.0','info':'Grilled chicken + \nKentucky + \n Chicken breast'},
            ]
        } 
        
cart_items=[]

class Ham(MDScreen):
    
    def open_list(self, category):
        
        self.ids.list_contenyr.clear_widgets()
        
 
           
           
        scrool=ScrollView()
        list=MDList() 
            
        scrool.add_widget(list)
            
        for i in user_window[category]:
            item=(TwoLineIconListItem(text=f'      {i['name']}', secondary_text=f'      $ {i['price']}' 
            , secondary_theme_text_color='Custom',secondary_text_color=(0, 0.392, 0 ,1),
                  on_release=lambda x, p=i: self.item_clicked(p)))
            
            
            
            
            item.add_widget((IconLeftWidget(icon=i['icon'],icon_size='60sp')))
            
            list.add_widget(item)
      
            
            
        self.ids.list_contenyr.add_widget(scrool)
        

           
        return user_window       
           
           
        
# عند الضغط اعلى list

    def item_clicked(self, i):
        
        layout=RelativeLayout(size_hint_y=None, height=250)
        layout.add_widget(Image(source=i['icon'], size_hint=(None, None), size=(120, 120), pos_hint={'x':0.0 , 'y': 0.55}))
        layout.add_widget(MDIconButton(icon='close-circle-outline',pos_hint={'center_x': 0.5*2, 'y': 0.55*2}, on_release=lambda x: self.dialog.dismiss()))
        layout.add_widget(Label(text=f'{i['name']}', pos_hint={'x': 0.2, 'y': 0.4}))
        
        layout.add_widget(Label(text=f'$ {i['price']}', pos_hint={'x': 0.17, 'y': 0.3}, color=(0, 0.392, 0 ,1), font_size=22))
        
        layout.add_widget(Label(text=i['info'], pos_hint={'x': 0.28, 'y': 0.15}, color=(0,1,0,1), font_size=15))
        
        self.label_eroor=Label(text='', color=(1,0,0,1), pos_hint={'x':0.22 , 'y': 0.6})
        layout.add_widget(self.label_eroor)
       
        
        layout2=BoxLayout(orientation='horizontal', pos_hint={'x': 0.0, 'y':0.2}, spacing=5)
        
        layout2.add_widget(MDIconButton(icon='minus', on_release=self.muse_numbt))
        self.qty_button=MDRectangleFlatIconButton(text='1', size_hint=(0.4, 0.0))
        layout2.add_widget(self.qty_button)
        layout2.add_widget(MDIconButton(icon='plus', on_release=self.pluse_number))
        
        self.butmin=MDRectangleFlatIconButton(text='Add carte', icon='plus', pos_hint={'x':0.25, 'y': 0.01},disabled=True,
                                    text_color='black', icon_color='green', on_press= lambda x,
                                    item=i:self.goto_add(item))
        layout.add_widget(self.butmin)
        
        self.text_fild=MDTextField(hint_text='int',mode='round',max_text_length=2, input_filter='int')     
        self.text_fild.bind(text= self.on_text_change)
        layout2.add_widget(self.text_fild)
        
        
 
        layout.add_widget(layout2)
        
        self.dialog=MDDialog(title=i['name'], 
                            type="custom",
                            size_hint=(0.8, 0.5),
                          
                        content_cls=layout)
        self.dialog.open()
              
    def pluse_number(self, instance):
        value=int(self.qty_button.text)   
        if value <3:
         
            self.qty_button.text=str(value +1)
            
    def muse_numbt(self, instance):
        value=int(self.qty_button.text)
        if value > 1:
            self.qty_button.text=str(value -1)
            
    def goto_add(self, item):
        cart_items.append({
            'name': item['name'],
            'icon': item['icon'],
            'price': item['price'],
            'qty': self.qty_button.text,
            'tabl': self.text_fild.text,
     
            
        })
         
        table_none=self.text_fild.text.strip() # اد مدخل ليس فارغ
        
        
        
   
        if table_none: #حققstrip True  اد مدخل متروس يعني  
            self.manager.current='Addwid'
            self.dialog.dismiss()
            self.butmin.disabled=False 

                
        else:    
            self.butmin.disabled=True
            self.label_eroor.text='Eroor\nEnter your numbre Table'
          
    def on_text_change(self, instance, value):
        if len(value) > 0 and len(value) < 3:
            self.butmin.disabled=False
            
        else:
            self.butmin.disabled=True       
            
    
      
      
             
class Addwid(MDScreen):
    def goto_scr_main(self):
        self.manager.current='Ham'
        
    def open_list_add(self):
        carrent=self.ids.cotayner
        scrol=ScrollView()
        listn=MDList()
        scrol.add_widget(listn)
        carrent.clear_widgets()
        
        for item in cart_items:
            
            items=ThreeLineAvatarIconListItem(text=f'    {item['name']}  x {item['qty']}', secondary_text=f'    $ {item['price']}',secondary_theme_text_color='Custom',secondary_text_color='green', tertiary_text=f'    Table({item['tabl']})',tertiary_theme_text_color='Custom',tertiary_text_color='blue')
            
            items.add_widget(IconLeftWidget(icon=item['icon'],icon_size='55sp'))
            items.add_widget(IconRightWidget(icon='delete-circle',theme_icon_color='Custom', icon_color=(1,0,0,1), on_release=lambda x, p=item: self.open_dealog(item)))
          
            
            listn.add_widget(items)
            with open('menu.text','a') as name:
                
                name.write(f'{item['name']}, {item['qty']}, {item['price']},{item['icon']}\n')
                
                
        carrent.add_widget(scrol)  
     
    def of_dialog(self, instance):
        self.dealog.dismiss()
        
    def delet_req(self, instance): # اد مخزن item يتبق داخلها مخزون كل الطلبات ادخل في cart_items امسح منها الي سويت اضافه عليها

#                  مخزن item يعني تمرير الزر  يتطبق مع مخزن الاضافانت
        if self.item_to_delete in cart_items:
            cart_items.remove(self.item_to_delete)
            
            self.dealog.dismiss()
            self.open_list_add() # اعاده تشغيل رسم القائمه  
            
            with open('menu.text','a') as name:
                name.write(f'{self.item_to_delete['name']}, {self.item_to_delete['qty']}, {self.item_to_delete['price']},{self.item_to_delete['icon']}\n')

        
               
    def open_dealog(self, item):
        layoutdi=RelativeLayout()
        img=IconLeftWidget(icon=item['icon'], icon_size='40sp')

        layoutdi.add_widget(img)
        
        self.dealog=MDDialog(
                title=f'{item['name']} Do you want to remove the request?',
                type='custom',
                content_cls=layoutdi,
                buttons=[MDRoundFlatButton(text='cance', on_press=self.of_dialog),
                         MDRoundFlatButton(text='Ok', on_press=self.delet_req)]
                    
        ) 
        self.dealog.open()      
            
        self.item_to_delete= item    
            
           




class Main(MDApp):
    def build(self):
   
        return Builder.load_string(KV)
           
       

    def shert(self, text):
        
        screen=self.root.get_screen('Ham')
        screen.ids.list_contenyr.clear_widgets()
        
        
        listn=MDList() 
        found=False
        
        for category, items in user_window.items():
            if any(item['name'] == text for item in items):
                for item in items:
                    if item['name'] == text:
                        itmin=TwoLineIconListItem(text=item['name'], secondary_text=item['price'], on_press=lambda x, item=item:screen.item_clicked(item))
                        itmin.add_widget(IconLeftWidget(icon=item['icon'], icon_size='40sp'))
                        listn.add_widget(itmin)
                        found=True
           
        if found:        
            screen.ids.list_contenyr.add_widget(listn)
            screen.ids.text_shert.error=False
        else:
            screen.ids.text_shert.error=True
       
           
                 
           
        return None
            
   
        

Main().run()