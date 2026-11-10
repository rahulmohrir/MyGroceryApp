import kivy
kivy.require('2.3.1')


from kivy.config import Config
Config.set('graphics', 'window_state', 'visible')
Config.set('graphics', 'fullscreen', '0')
import os
from kivy.app import App
from kivy.core.window import Window
# Tell the OS to push the UI up so the focused text input is visible above the keyboard
##Window.softinput_mode = "below_target"
from kivy.utils import platform


from kivy.uix.widget import Widget
from kivy.uix.layout import Layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem, TabbedPanelStrip
from kivy.uix.recycleview import RecycleView, RecycleDataModelBehavior, RecycleViewBehavior, RecycleDataModel
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from functools import partial

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore

from kivy.lang.builder import Builder



class MyLabel(Label):
    pass
class MyDisplayLabel(Label):
    pass
class MyLabelForAddPopup(Label):
    pass
class BGLayoutForRV(BoxLayout):
    pass
class BGLayoutForDisplay(BoxLayout):
    pass
class MyTextInputLayout(BoxLayout):
    pass
class MyTextInput(TextInput):
    pass
class MyMoveItemPopup(Popup):
    pass
class MyAddItemPopupForCurrentTab(Popup):
    pass
class MyClearListPopup(Popup):
    pass
class MyItemExitsPreviousPopup(Popup):
    pass
class MyItemExitsOnebeforePopup(Popup):
    pass
class MyItemExitsBothPopup(Popup):
    pass
class MyItemMovedToCurrentPopup(Popup):
    pass
class MyRecycleLabel(Label):
    text = StringProperty('')
    pass
class MyTabPanel(TabbedPanel):
    pass
class MyTabItem(TabbedPanelItem):
    pass
class MyTabbedPanelStrip(TabbedPanelStrip):
    pass
class MyMainTabBoxLayout(BoxLayout):
    pass
class MyAddItemPopup(Popup):
    pass
class MyRecycleViewClassForDisplay(BoxLayout, RecycleDataViewBehavior, MyRecycleLabel):
    item_name = StringProperty('')
    quantity = StringProperty('')
    price = StringProperty('')
    pass

class MyRecycleViewClass(BoxLayout, RecycleDataViewBehavior, MyRecycleLabel):
    item_name = StringProperty('')
    quantity = StringProperty('')
    price = StringProperty('')
   
    selected_row = ObjectProperty(None)
    # Initialize index as a property (defaults to None or a fallback number)
    index = NumericProperty(None, allownone=True)
    def __init__(self, **kwargs):
        super(MyRecycleViewClass, self).__init__(**kwargs)
        
        
## Function to access the index of the item of recycleview       
    def refresh_view_attrs(self, rv, index, data):
        """ Catch and store the current data index when this widget is recycled """
        self.index = index
        return super(MyRecycleViewClass, self).refresh_view_attrs( rv, index, data)
## Function to select a row when clicked        
    def on_row_click(self, index):
        self.index = index
        """ Use the index to look up or alter data """
        app = App.get_running_app()
        rv = app.root.my_recycle_view_1
        
        return  self.index 
class MyRecycleViewClassForCurrent(BoxLayout, RecycleDataViewBehavior, MyRecycleLabel):
    item_name = StringProperty('')
    quantity = StringProperty('')
    price = StringProperty('')
    index = NumericProperty(None, allownone=True)
       
    selected_row = ObjectProperty(None)
    def __init__(self, **kwargs):
            super(MyRecycleViewClassForCurrent, self).__init__(**kwargs)

    ## Function to access the index of the item of recycleview       
    def refresh_view_attrs(self, rv, index, data):
        """ Catch and store the current data index when this widget is recycled """
        self.index = index
        return super(MyRecycleViewClassForCurrent, self).refresh_view_attrs( rv, index, data)
## Function to select a row when clicked        
    def on_row_click(self, index):
        self.index = index
        """ Use the index to look up or alter data """
        app = App.get_running_app()
        rv = app.root.my_recycle_view_2
        # Access the RecycleView's full dataset using the tracked index
        self.selected_row = app.root.my_recycle_view_2.data[self.index]
       
        return self.selected_row, self.index 
    pass           
class MySelectableRecycleBoxLayout(LayoutSelectionBehavior, RecycleBoxLayout):
    pass  
    
class MyRecycleView(RecycleView):
   
    
    pass
class MyLimitItemPopup(Popup):
    pass
class MyItemExitPopup(Popup):
    pass
class MainScreen(Screen):
    pass

class RootWidget(BoxLayout):
    text = StringProperty('')
    max_rows = NumericProperty(100)
    index = NumericProperty(None, allownone=True)
    selected_row = ObjectProperty(None)
    recycleview_instance = ObjectProperty(None)
    new_item = ObjectProperty(None)
    
    
    
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
## Instantiate the first screen
        self.main_screen = MainScreen()
## Instantiate the first popup which addes the item to the first recycleview 
        self.add_item_popup = MyAddItemPopup()
## Instance of the second popup which opens after clicking the add item button
        self.move_item_popup = MyMoveItemPopup()
## Instance of the add item pop up for the current tab
        self.add_item_popup_currenttab = MyAddItemPopupForCurrentTab()

## Instance of the first recycleview        
        self.my_recycle_view_1= self.main_screen.ids.recycleview_1_id
## Instance of the first recycleview        
        self.my_recycle_view_2= self.main_screen.ids.recycleview_2_id
## Instance of the clear list popup of the current tab
        self.my_clear_list = MyClearListPopup()
## Instance of the info label for previous tab
        self.my_info_previoustab = MyItemExitsPreviousPopup()
## Instance of the infolabel for one before tab
        self.my_info_onebeforetab = MyItemExitsOnebeforePopup()
## Instance of the info label informing the item successfully moved to current lisy
        self.my_info_itemmovedcurrent = MyItemMovedToCurrentPopup()
        ## Instance of the viewclass
        ##self.recycle_viewclass = MyRecycleViewClass()
## Instance of info label informing about maximum row limit reached
        self.limit_item_popup = MyLimitItemPopup()
## Instance of info popup informing the item already exits in the list
        self.exit_item_popup = MyItemExitPopup()
## Instance of a info popup informing the item exists in both the lists
        self.my_info_bothitem = MyItemExitsBothPopup()
## Create a list to store the item name,  quantity and price
        self.item_list = []
## Set the number of rows that can be added to the recycleview
        self.row_count = 0
        
        
        self.add_widget(self.main_screen)
## Function to open the first popup after clicking the add item button
    def open_add_item_popup(self):
        self.add_item_popup.open()
        
    def add_item_textinput_focus(self, dt):
       
        self.add_item_popup.ids.item_name_id.focus = True
       
       
## Function to get the item text entered by the user
    def get_list_main(self):
        print('Get list')

        item_name = self.add_item_popup.ids.item_name_id.text
        quantity = self.add_item_popup.ids.quantity_id.text
        price = self.add_item_popup.ids.price_id.text
        
       
        item_list = [item_name, quantity, price]
       
        Clock.schedule_once(lambda dt :self.recycle_callback_main(item_list), 0)
## Function to add the item once to the recycleview
    def recycle_callback_main(self, item_list):
        
        self.recycleview_instance = self.main_screen.ids.recycleview_1_id
        # Check if the limit has been reached
        if len(self.recycleview_instance.data) >= self.max_rows:
           
            self.limit_item_popup.open()
            Clock.schedule_once(self.dismiss_limit_popup, 3)
            self.cancel_add_item_popup()
            return
        # Add new data dynamically
        self.row_count += 1
        new_item = {'item_name': item_list[0], 'quantity': item_list[1], 'price':item_list[2]}
        # Check if any existing dict in data matches your new item's unique key
        if not any(d['item_name'] == new_item['item_name'] for d in self.recycleview_instance.data):
            self.recycleview_instance.data.append(new_item)
            self.recycleview_instance.data.sort(key = lambda x : (x['item_name'].isdigit(),x['item_name'].lower()))
        else:
            
            self.exit_item_popup.open()
            Clock.schedule_once(self.dismiss_exit_popup, 3)
            self.cancel_add_item_popup()

       
        
        # Refresh the widget to show updates
        self.recycleview_instance.refresh_from_data()
        self.add_item_popup.dismiss()

## Function to dismiss the info popup informing the item exists in the list         
    def dismiss_exit_popup(self, dt):
        self.exit_item_popup.dismiss()
## Function to dismiss the info popup informing the number of add item limit is reached
    def dismiss_limit_popup(self, dt):
        self.limit_item_popup.dismiss()

    
## Function to cancel the first popup        
    def cancel_add_item_popup(self):
        self.add_item_popup.dismiss()
## Function to open the second popup with option to move, edit and delete the item
    def open_move_item_popup(self, index):
        self.move_item_popup.open()
        self.index = index
       
        self.selected_row_data = self.main_screen.ids.recycleview_1_id.data[self.index]
        self.selected_row = self.main_screen.ids.recycleview_1_id.view_adapter.get_visible_view(self.index)
        
        self.move_item_popup.ids.get_name_id.text = self.selected_row_data['item_name']
        self.move_item_popup.ids.get_quantity_id.text = self.selected_row_data['quantity']
        self.move_item_popup.ids.get_price_id.text = self.selected_row_data['price']
        return self.index, self.selected_row         
## Function to cancel the second popup with option to move, edit and delete the item    
    def cancel_move_item_popup(self):
        self.move_item_popup.dismiss()
    
## Function to first select the row from the recycleview and get the items text
    def move_item(self):
        item_name = self.move_item_popup.ids.get_name_id.text
        quantity = self.move_item_popup.ids.get_quantity_id.text
        price = self.move_item_popup.ids.get_price_id.text
        item_list = [item_name, quantity, price]
        if len(self.main_screen.ids.recycleview_2_id.data) >= self.max_rows:
            
            self.limit_item_popup.open()
            Clock.schedule_once(self.dismiss_limit_popup, 3)
            self.cancel_move_item_popup()
            return
                # Add new data dynamically
        self.row_count += 1
        new_item = {'item_name': item_list[0], 'quantity': item_list[1], 'price':item_list[2]}
        if any(d['item_name'] == new_item['item_name'] for d in self.main_screen.ids.recycleview_4_id.data) and  any(d['item_name'] == new_item['item_name'] for d in self.main_screen.ids.recycleview_3_id.data):
            print('item in both')
            self.my_info_bothitem.open()
            self.instance_boundfun = partial(self.move_add_item_callback, new_item)
            self.my_info_bothitem.bind(on_dismiss =self.instance_boundfun)
            
            
            Clock.schedule_once(self.dismiss_myinfo_bothtab, 3)
            self.cancel_move_item_popup()
        elif any(d['item_name'] == new_item['item_name'] for d in self.main_screen.ids.recycleview_4_id.data):
           
           
            
            self.my_info_previoustab.open()
            self.instance_boundfun = partial(self.move_add_item_callback, new_item)
            self.my_info_previoustab.bind(on_dismiss =self.instance_boundfun)
            
           
            Clock.schedule_once(self.dismiss_myinfo_previous, 3)
            self.cancel_move_item_popup()
            
            
            
        elif any(d['item_name'] == new_item['item_name'] for d in self.main_screen.ids.recycleview_3_id.data):
           
           
            
            self.my_info_onebeforetab.open()
           
            self.instance_boundfun = partial(self.move_add_item_callback, new_item)
            self.my_info_onebeforetab.bind(on_dismiss = self.instance_boundfun)
            
            Clock.schedule_once(self.dismiss_myinfo_onebeforetab, 3)
            self.cancel_move_item_popup()
            
        else :
            self.move_add_item_callback(new_item)
           
    def move_add_item_callback(self,new_item, *args):

        if not any(d['item_name'] == new_item['item_name'] for d in self.main_screen.ids.recycleview_2_id.data):
            self.main_screen.ids.recycleview_2_id.data.append(new_item)
            self.main_screen.ids.recycleview_2_id.data.sort(key = lambda x : (x['item_name'].isdigit(),x['item_name'].lower()))
            
            Clock.schedule_once(self.callback_moved_current, 0)
        else:
            
            self.exit_item_popup.open()
            Clock.schedule_once(self.dismiss_exit_popup, 3)
            self.cancel_move_item_popup()
        
        
        # Refresh the widget to show updates
        self.main_screen.ids.recycleview_2_id.refresh_from_data()
        self.cancel_move_item_popup()
       
    def callback_moved_current(self, dt):
        self.my_info_itemmovedcurrent.open()
        Clock.schedule_once(self.dismiss_myinfo_moveditemcurrent, 3)

## Function to dismiss the info popup informing the item moved successfully to the current list
    def dismiss_myinfo_moveditemcurrent(self, dt):
        self.my_info_itemmovedcurrent.dismiss()
    def open_myinfo_previous(self, dt):
        self.my_info_previoustab.open()
    def open_myinfo_onebeforetab(self, dt):
        self.my_info_onebeforetab.open()
## Function to inform that the item added to the current list is in the previous list and close after 3 seconds
    def dismiss_myinfo_previous(self, dt):
        self.my_info_previoustab.dismiss()
        
## Function to inform that the item added to the current list is in the one before list and close after 3 seconds
    def dismiss_myinfo_onebeforetab(self, dt):
        self.my_info_onebeforetab.dismiss()
    def dismiss_myinfo_bothtab(self, dt):
        self.my_info_bothitem.dismiss()
## Function to delete an item from the main list recycleview   
    def delete_item_main(self, index):
        self.index = index

        self.main_screen.ids.recycleview_1_id.data.pop(self.index)
        
        
        self.move_item_popup.dismiss()
## Function to delete an item from the current list recycleview
    def delete_item_current(self, index):
        self.index = index
       
        Clock.schedule_once(lambda dt : self.delete_item_current_callback(self.index), 0)

    def delete_item_current_callback(self,index):
        self.index = index
        self.main_screen.ids.recycleview_2_id.data.pop(self.index)
        
## Function to open popup after clicking the add item button on the current list tab
    def open_add_item_popup_currenttab(self):
        self.add_item_popup_currenttab.open()
    ## Function to get the item text entered by the user
    def get_list_currenttab(self):
        

        item_name = self.add_item_popup_currenttab.ids.item_name_current.text
        quantity = self.add_item_popup_currenttab.ids.quantity_current.text
        price = self.add_item_popup_currenttab.ids.price_current.text
        
        
        item_list = [item_name, quantity, price]
       
        Clock.schedule_once(lambda dt :self.recycle_callback_currenttab(item_list), 0)
## Function to add the item once to the recycleview
    def recycle_callback_currenttab(self, item_list):
       
        self.recycleview_instance = self.main_screen.ids.recycleview_2_id
        # Check if the limit has been reached
        if len(self.recycleview_instance.data) >= self.max_rows:
            
            self.limit_item_popup.open()
            Clock.schedule_once(self.dismiss_limit_popup, 3)
            self.cancel_add_item_popup_currenttab()
            return
        # Add new data dynamically
        self.row_count += 1
        new_item = {'item_name': item_list[0], 'quantity': item_list[1], 'price':item_list[2]}
        if any(d['item_name'] == new_item['item_name'] for d in self.main_screen.ids.recycleview_4_id.data):
           
            self.my_info_previoustab.open()
            Clock.schedule_once(self.dismiss_myinfo_previous, 3)
            self.add_item_popup.dismiss()
            
        if any(d['item_name'] == new_item['item_name'] for d in self.main_screen.ids.recycleview_3_id.data):
           
            self.my_info_onebeforetab.open()
            Clock.schedule_once(self.dismiss_myinfo_onebeforetab, 3)
            self.cancel_add_item_popup_currenttab()
            
        # Check if any existing dict in data matches your new item's unique key
        if not any(d['item_name'] == new_item['item_name'] for d in self.recycleview_instance.data):
            self.recycleview_instance.data.append(new_item)
            self.recycleview_instance.data.sort(key = lambda x : (x['item_name'].isdigit(),x['item_name'].lower()))
            self.cancel_add_item_popup_currenttab()
        else:
           
            self.exit_item_popup.open()
            Clock.schedule_once(self.dismiss_exit_popup, 3)
            self.cancel_add_item_popup_currenttab()

        
        
        # Refresh the widget to show updates
        self.recycleview_instance.refresh_from_data()
        
    def cancel_add_item_popup_currenttab(self):
        self.add_item_popup_currenttab.dismiss()

    def clear_list(self):
        self.my_clear_list.open()
    def cancel_clear_list_popup(self):
        self.my_clear_list.dismiss()

    
    def select_all_items(self):
        recycleview_instance_current = self.main_screen.ids.recycleview_2_id # Get reference to your RecycleView
        recycleview_instance_previous = self.main_screen.ids.recycleview_4_id
        recycleview_instance_onebefore = self.main_screen.ids.recycleview_3_id
## Store the current item data of the three widgets
        recycleview_instance_current_data = [item.copy() for item in recycleview_instance_current.data]
        recycleview_instance_previous_data = [item.copy() for item in recycleview_instance_previous.data]
           
    # 1. Update the underlying data source to 'selected'
        for item in recycleview_instance_current.data:
            item['selected'] = True
            
        # 2. Tell the Layout Manager to select the nodes visually
        recycleview_instance_current.layout_manager.clear_selection()
        for index in range(len(recycleview_instance_current.data)):
            recycleview_instance_current.layout_manager.select_node(index)
            
        # 3. Refresh the view
        recycleview_instance_current.refresh_from_data()
        
        
        self.duplicate_recycleview_data_previous(recycleview_instance_current,recycleview_instance_previous, recycleview_instance_current_data)
        self.delete_all_items(recycleview_instance_current)
        self.duplicate_recycleview_data_onebefore(recycleview_instance_previous, recycleview_instance_onebefore, recycleview_instance_previous_data)
        self.my_clear_list.dismiss()
    def delete_all_items(self, instance):
        recycleview_instance_current = instance # Get reference to your RecycleView
    
    # 1. Clear the active selection states from layout management
        recycleview_instance_current.layout_manager.clear_selection()
    
    # 2. Clear the actual data list
        recycleview_instance_current.data = [] 
    
    # 3. Force the RecycleView to redraw an empty state
        recycleview_instance_current.refresh_from_data()
    def duplicate_recycleview_data_previous(self,source_rv, dest_rv, data):
        recycleview_instance_current = source_rv
        recycleview_instance_previous = dest_rv
        # 1. Update the underlying data source to 'selected'
        for item in recycleview_instance_previous.data:
            item['selected'] = True
            
        # 2. Tell the Layout Manager to select the nodes visually
        recycleview_instance_previous.layout_manager.clear_selection()
        for index in range(len(recycleview_instance_previous.data)):
            recycleview_instance_previous.layout_manager.select_node(index)
            
        # 3. Refresh the view
        recycleview_instance_previous.refresh_from_data()
# 1. Clear the active selection states from layout management
        recycleview_instance_current.layout_manager.clear_selection()
    
    # 2. Clear the actual data list
        recycleview_instance_current.data = [] 
        
        recycleview_instance_previous.data = data
        recycleview_instance_previous.refresh_from_data()
    def duplicate_recycleview_data_onebefore(self, source_rv, dest_rv, data):
        recycleview_instance_previous = source_rv
        recycleview_instance_onebefore = dest_rv
        # 1. Update the underlying data source to 'selected'
        for item in recycleview_instance_onebefore.data:
            item['selected'] = True
            
        # 2. Tell the Layout Manager to select the nodes visually
        recycleview_instance_onebefore.layout_manager.clear_selection()
        for index in range(len(recycleview_instance_onebefore.data)):
            recycleview_instance_onebefore.layout_manager.select_node(index)
            
        # 3. Refresh the view
        recycleview_instance_onebefore.refresh_from_data()
        # 1. Clear the active selection states from layout management
        recycleview_instance_onebefore.layout_manager.clear_selection()
    
    # 2. Clear the actual data list
        recycleview_instance_onebefore.data = [] 
        
        recycleview_instance_onebefore.data = data
        recycleview_instance_onebefore.refresh_from_data()
    
            
class MyGroceryApp(App):
    def build(self):
        # Set a standard phone resolution (e.g., iPhone 8 / Pixel dimensions)
        PHONE_WIDTH = 360
        PHONE_HEIGHT = 640
        ## Json File for Storing the Tree Structure
        self.path = self.user_data_dir
        file_path = os.path.join(self.path, 'app_state.json')
        
        
        self.store = JsonStore(file_path)
       
       
        
        return RootWidget()

     ## Function to save data on pause
    def on_pause(self):
        self.on_save()
        
    ## Function to save data on stop
    def on_stop(self):
        self.on_save()

    def on_save(self):
        self.serialize_app_data()
    def serialize_app_data(self):
        serialized_data = {}
        maintab_data = self.root.main_screen.ids.recycleview_1_id.data
        
        currenttab_data = self.root.main_screen.ids.recycleview_2_id.data # Get reference to your RecycleView
        previoustab_data = self.root.main_screen.ids.recycleview_4_id.data
        onebefore_data = self.root.main_screen.ids.recycleview_3_id.data
        
        serialized_data = {'main_tab' : maintab_data, 'current_tab' : currenttab_data, 'previous_tab' : previoustab_data, 'onebefore_tab' : onebefore_data}
        data_save  = self.store.put('items', app_state = serialized_data )

## Function to load data on start    
    def on_start(self):
        if self.store.exists('items'):
            retrieved_data = self.store.get('items')['app_state']
            maintab_data = self.root.main_screen.ids.recycleview_1_id
   
            currenttab_data = self.root.main_screen.ids.recycleview_2_id # Get reference to your RecycleView
            previoustab_data = self.root.main_screen.ids.recycleview_4_id
            onebefore_data = self.root.main_screen.ids.recycleview_3_id
            for item in retrieved_data:
                
                maintab_data.data = retrieved_data['main_tab']
                currenttab_data.data = retrieved_data['current_tab']
                previoustab_data.data = retrieved_data['previous_tab']
                onebefore_data.data = retrieved_data['onebefore_tab']
        
        else:
            print('Loading Defaults')

       
    

if __name__ == '__main__':
    MyGroceryApp().run()