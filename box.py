import flet as ft


def main(pag):
    tittle = ft.Text("Bom dia!")
    window_tittle = ft.Text("Bem vindo!")
    chat = ft.Column()

    def send_mensage_tunnel(mensage):
        chat_text = ft.Text(mensage)
        chat.controls.append(chat_text)
        pag.update()

    pag.pubsub.subscribe(send_mensage_tunnel)

    def send_mensage(event):
        mensage_text = mensage_field.value
        user_name = user_name_field.value
        mensage = f"{user_name}: {mensage_text}"
        pag.pubsub.send_all(mensage)

        mensage_field.value = ""
        pag.update()

    mensage_field = ft.TextField(label="Digite sua mensagem", on_submit=send_mensage)    
    send_mensage_button = ft.ElevatedButton("Enviar", on_click=send_mensage)
    mensage_line = ft.Row([mensage_field, send_mensage_button])

    def enter_chat(event):
        pag.remove(tittle, button_start)
        window.open = False
        mensage = f"{user_name_field.value} entrou no chat!"
        pag.pubsub.send_all(mensage)
        show_user_name = ft.Text(f"Você: {user_name_field.value}")
        pag.add(show_user_name, mensage_line, chat)
        pag.update()

    user_name_field = ft.TextField(label="Escreva o nome no chat", on_submit=enter_chat)
    window_button = ft.ElevatedButton("Entrar no chat", on_click=enter_chat)
    window = ft.AlertDialog(title=window_tittle,content=user_name_field, actions=[window_button])

    def start_chat(event):
        pag.dialog = window
        window.open = True
        pag.update()

    button_start = ft.ElevatedButton("Iniciar chat", on_click=start_chat)
    pag.add(tittle, button_start)

#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)