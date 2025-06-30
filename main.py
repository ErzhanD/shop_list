import flet as ft
from db import main_db

main_db.init_db()

def main(page: ft.Page):
    page.title = "Список покупок"

    items_column = ft.Column()

    def load_items():
        items_column.controls.clear()
        items = main_db.get_items()
        for item in items:
            item_id = item[0]
            name = item[1]
            quantity = item[2]
            is_bought = item[3]

            def checkbox_changed(e, iid=item_id):
                main_db.update_status(iid, e.control.value)
                load_items()
                page.update()

            def delete_clicked(e, iid=item_id):
                main_db.delete_item(iid)
                load_items()
                page.update()

            label = name + " (" + str(quantity) + ")"

            row = ft.Row([
                ft.Checkbox(label=label, value=bool(is_bought), on_change=checkbox_changed),
                ft.IconButton(icon=ft.icons.DELETE, on_click=delete_clicked)
            ])

            items_column.controls.append(row)

        page.update()

    input_name = ft.TextField(label="Товар")
    input_quantity = ft.TextField(label="Количество", value="1", width=100)

    def add_clicked(e):
        if input_name.value != "" and input_quantity.value.isdigit():
            main_db.add_item(input_name.value, int(input_quantity.value))
            input_name.value = ""
            input_quantity.value = "1"
            load_items()
            page.update()

    add_button = ft.ElevatedButton(text="Добавить", on_click=add_clicked)

    page.add(
        ft.Text("Список покупок", size=30),
        ft.Row([input_name, input_quantity, add_button]),
        items_column
    )

    load_items()

ft.app(target=main)