import flet as ft 
from flet import Column, Row
#from design1 import hype
def main(page: ft.Page):
    page.title = "Calculator"
    page.window_width=325
    page.window_height=580
    page.theme_mode="dark"
    page.padding = 20
    #page.window_bgcolor="#b3b3b3"
    page.bgcolor="#000000"
    page.update()
    
    
    # Button function        
    def keybord(e):
        data = e.control.data 
        if data in ["1","2","3","4","5","6","7","8","9","0",".","+","-","*","/"]:
            note.value = str(note.value) + str(data)
            page.update()
        if data == "%":
            note.value = float(note.value) / 100
            page.update()
        if data == "+/-":
            if float(note.value) > 0:
                note.value = "-" + str(note.value)
                page.update()
        
        if data == "=":
            note.value = str(eval(note.value))
            page.update()
        
        if data == "e":
            st = list(note.value)
            st.pop()
            note.value = "".join(map(str,st))
            page.update()
            
        if data == "AC":
            note.value = ""
            page.update()
            
            
    # The Text Field       
    note =ft.Text(value="",size=30, text_align="end")
        
    hentai = Column(
            controls=[
                Row(controls=[note], alignment="end"),
                ft.Row([
                    ft.Text("__________", size=30)
                ],alignment="center"),
                ft.Row([
                    ft.IconButton(ft.icons.DELETE_ROUNDED, width=60, height=60, icon_color="#66ccff", data="AC", on_click=keybord),
                    ft.IconButton(ft.icons.ARROW_BACK, width=60, height=60, icon_color="#66ccff", data="e", on_click=keybord),
                    ft.IconButton(ft.icons.EXPOSURE, width=60, height=60, icon_color="#66ccff", data="+/-", on_click=keybord),
                    ft.TextButton(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(value="/", size=25,color="#e68a00"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=5,
                            ),
                            padding=ft.padding.all(10),
                        ),
                        data="/", 
                        on_click=keybord,
                        width=60,
                        height=60
                    ),
                    
                ]), 
                ft.Row([
                   
                    ft.ElevatedButton(text="7", width=60, height=60, color="#ffffff", data="7", on_click=keybord),
                    ft.ElevatedButton(text="8", width=60, height=60, color="#ffffff", data="8", on_click=keybord),
                    ft.ElevatedButton(text="9", width=60, height=60, color="#ffffff", data="9", on_click=keybord),
                    ft.IconButton(ft.icons.CLEAR, width=60, height=60, icon_color="#e68a00", data="*", on_click=keybord),
                
                ]),
                ft.Row([
                    ft.ElevatedButton(text="4", width=60, height=60, color="#ffffff", data="4", on_click=keybord),
                    ft.ElevatedButton(text="5", width=60, height=60, color="#ffffff", data="5", on_click=keybord),
                    ft.ElevatedButton(text="6", width=60, height=60, color="#ffffff", data="6", on_click=keybord),
                    ft.IconButton(ft.icons.HORIZONTAL_RULE_ROUNDED, width=60, height=60, icon_color="#e68a00", data="-", on_click=keybord)
                ]),
                ft.Row([
                    ft.ElevatedButton(text="1", width=60, height=60, color="#ffffff", data="1", on_click=keybord),
                    ft.ElevatedButton(text="2", width=60, height=60, color="#ffffff", data="2", on_click=keybord),
                    ft.ElevatedButton(text="3", width=60, height=60, color="#ffffff", data="3", on_click=keybord),
                    ft.IconButton(ft.icons.ADD, width=60, height=60, icon_color="#e68a00", data="+", on_click=keybord)
                ]),
                ft.Row([
                    ft.IconButton(ft.icons.PERCENT_ROUNDED, width=60, height=60, icon_color="#66ccff", data="%", on_click=keybord),
                    ft.ElevatedButton(text="0", width=60, height=60, color="#ffffff", data="0", on_click=keybord),
                    ft.IconButton(ft.icons.WIFI_1_BAR_ROUNDED, width=60, height=60, icon_color="#66ccff", data=".", on_click=keybord),
                    ft.IconButton(ft.icons.DRAG_HANDLE_ROUNDED, width=60, height=60, icon_color="#ffffff",bgcolor="#ff3300", data="=", on_click=keybord)
                ]),      
            ]
        )

    
    
    page.add(
        note,
        hentai
        

        
    )


ft.app(target=main)