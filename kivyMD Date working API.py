from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout

# Define the shop API data
shop_api_data = [{
        "shop_id": 1,
        "shop_name": "Shop A",
        "data": [
            {
                "date": "01-01-2010",
                "outstanding": 200.00,
                "products": [
                    {
                        "product_id": 1,
                        "product_name": "Product A",
                        "quantity": 100,
                        "weight": 500,
                        "rate": 10.50,
                        "amount": 1050.00,
                    },
                    {
                        "product_id": 2,
                        "product_name": "Product B",
                        "quantity": 50,
                        "weight": 250,
                        "rate": 12.00,
                        "amount": 600.00,
                    },
                    {
                        "product_id": 3,
                        "product_name": "Product C",
                        "quantity": 75,
                        "weight": 300,
                        "rate": 11.20,
                        "amount": 840.00,
                    }
                ]
            },
            {
                "date": "02-01-2010",
                "outstanding": 100.00,
                "products": [
                    {
                        "product_id": 1,
                        "product_name": "Product A",
                        "quantity": 150,
                        "weight": 750,
                        "rate": 11.25,
                        "amount": 1687.50,
                    },
                    {
                        "product_id": 2,
                        "product_name": "Product B",
                        "quantity": 75,
                        "weight": 375,
                        "rate": 13.50,
                        "amount": 1012.50,
                    },
                    {
                        "product_id": 3,
                        "product_name": "Product C",
                        "quantity": 90,
                        "weight": 450,
                        "rate": 9.75,
                        "amount": 877.50,
                    }
                ]
            },
            {
                "date": "03-01-2010",
                "outstanding": 400.00,
                "products": [
                    {
                        "product_id": 1,
                        "product_name": "Product A",
                        "quantity": 130,
                        "weight": 650,
                        "rate": 10.25,
                        "amount": 1332.50,
                    },
                    {
                        "product_id": 2,
                        "product_name": "Product B",
                        "quantity": 60,
                        "weight": 300,
                        "rate": 14.00,
                        "amount": 840.00,
                    },
                    {
                        "product_id": 3,
                        "product_name": "Product C",
                        "quantity": 80,
                        "weight": 400,
                        "rate": 11.50,
                        "amount": 920.00,
                    }
                ]
            }
        ]
    }
]

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: "10dp"
    BoxLayout:
        orientation: 'horizontal'   
        padding: "10dp"     
        Spinner:
            id: date_spinner
            text: 'Select Date'
            values: [f'{i:02}' for i in range(1, 32)]
            size_hint_y: None
            height: '30dp'        
        Spinner:
            id: month_spinner
            text: 'Select Month'
            values: [f'{i:02}' for i in range(1, 13)]
            size_hint_y: None
            height: '30dp'
        Spinner:
            id: year_spinner
            text: 'Select Year'
            values: [str(i) for i in range(2010, 2023)]
            size_hint_y: None
            height: '30dp'
    MDRaisedButton:
        text: "Submit"
        on_release: app.show_selected_date()
        pos_hint: {'center_x': 0.5}
    BoxLayout:
        id: table_layout
        orientation: 'vertical'
        

'''

class SpinnerDateApp(MDApp):
    selected_date = StringProperty("")

    def build(self):
        return Builder.load_string(KV)

    def show_selected_date(self):
        date = self.root.ids.date_spinner.text
        month = self.root.ids.month_spinner.text
        year = self.root.ids.year_spinner.text

        if date != 'Select Date' and month != 'Select Month' and year != 'Select Year':
            selected_date = f"{date}-{month}-{year}"

            # Find data for the selected date
            for shop in shop_api_data:
                for data in shop['data']:
                    if data['date'] == selected_date:
                        self.selected_date = selected_date
                        self.display_data(data)
                        return

            # If no data found for the selected date
            self.selected_date = "No data available for the selected date"

    def display_data(self, data):
        # Clear previous table
        self.root.ids.table_layout.clear_widgets()
        
         # Create a new horizontal box layout for Date and Outstanding labels
        labels_layout = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        
        # Create MDLabel for Date and Outstanding
        date_label = MDLabel(text=f"Date: {data['date']}")
        outstanding_label = MDLabel(text=f"Outstanding: ₹ {data['outstanding']}",halign= 'right')
        
        # Add the Date and Outstanding labels to the horizontal layout
        labels_layout.add_widget(date_label)
        labels_layout.add_widget(outstanding_label)

        # Create a new table with GridLayout
        table = GridLayout(cols=5, size_hint_y=None, row_default_height=30)
        table.add_widget(MDLabel(text='Product'))
        table.add_widget(MDLabel(text='Quantity'))
        table.add_widget(MDLabel(text='Weight (kg)'))
        table.add_widget(MDLabel(text='Rate'))
        table.add_widget(MDLabel(text='Amount'))

        for product in data['products']:
            table.add_widget(MDLabel(text=product['product_name']))
            table.add_widget(MDLabel(text=str(product['quantity'])))
            table.add_widget(MDLabel(text=str(product['weight'])))
            table.add_widget(MDLabel(text=str(product['rate'])))
            table.add_widget(MDLabel(text=str(product['amount'])))
            
        # Add the horizontal layout containing Date and Outstanding labels to the layout
        self.root.ids.table_layout.add_widget(labels_layout)

        # Add the table to the layout Scroll View
        table_scrollview = MDScrollView(size_hint=(1, 1))
        table_scrollview.add_widget(table)
        
        self.root.ids.table_layout.add_widget(table_scrollview)

if __name__ == '__main__':
    SpinnerDateApp().run()
