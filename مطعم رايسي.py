from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,  ScreenManager
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineIconListItem, ThreeLineIconListItem , IconLeftWidget, OneLineAvatarListItem, ImageLeftWidget , ThreeLineAvatarIconListItem
Window.size=(400, 620)

KV='''
ScreenManager:
    Main:
        
       
<Main>:
    name: 'Main'
    BoxLayout:
        orientation: 'vertical'
        spacing: 5
        MDTopAppBar:
            title: 'Requests section'
            pos_hint: {'top': 1}
            elevation: 1
            md_bg_color: 'orange'
        
        MDChip:
            id: button
            text: 'dfv'  
            pos_hint: {'center_x':0.5}
            on_press: root.one_list() 
            
            MDChipText:
                text: 'Requests'
            MDChipLeadingIcon:
                icon: 'cart-variant'     
                    
        BoxLayout:
            orientation: 'vertical'
            id: secodary
            
# حل مشكلتك لا سضهر list   مره ةتانيه
            
            
''' 
try:
    item_menu=[]


    with open('menu.text','r') as user:
        for line in user:
            line=line.strip()
            if not line:
                continue
            
            
            parts= line.split(',')
            if len(parts) ==4:
                name, qty, price, icon = parts
                item_menu.append({
                    "name": name,
                    "qty": qty,
                    "price": price,
                    "icon": icon
                        
                
                })
except:
    print('There are no requests. Try adding a request first.')


class Main(Screen):
   
    def one_list(self):
        self.ids.secodary.clear_widgets() # يمسح الي قبلها ويرحع الجديد بدون تكرار
        
        
        
        scrool=ScrollView()
        list=MDList()
        scrool.add_widget(list)

        
        for item in item_menu:
            items=ThreeLineIconListItem(text=f'    {item['name']}', secondary_text=f'    ${item['price']}',secondary_theme_text_color='Custom',secondary_text_color='green'
                                        ,tertiary_text=f'   Quantity ({item['qty']})',tertiary_theme_text_color='Custom',tertiary_text_color='red')
            items.add_widget(ImageLeftWidget(source=item['icon'], size_hint=(None, None),size=(60, 60)))
            list.add_widget(items)
        self.ids.secodary.add_widget(scrool)


class Mainmenu(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    
Mainmenu().run()    


    
