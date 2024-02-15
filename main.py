from nicegui import ui
import time


file_name = ""


@ui.page("/")
def index():
    ui.colors(primary="#0b2341", secondary="#e86100")
    with ui.header():
        ui.label("AI Contract Review").style(
            "font-size: 30px; text-align: center; margin-left: 600px;"
        )

    with ui.row():
        with ui.element().style(
            "margin: 5px 5px; background: #0b2341;  border-radius: 20px; justify-content: center; align-items: center; display: flex; flex-direction: column; padding: 20px;"
        ):
            ui.label("Upload your contract").style(
                "font-size: 18px; color: white; padding: 10px 0; text-align: center;"
            )
            ui.upload(on_upload=lambda e: process_file()).style(
                "width: 600px; border: 2px solid; border-color: #e86100; border-radius: 10px; padding: 10px; margin: 10px 0;"
            )

        with ui.element().style(
            "margin: 5px 5px; background: #0b2341;  border-radius: 20px; justify-content: center; align-items: center; display: flex; flex-direction: column; padding: 20px;"
        ):
            ui.label("Processing").style(
                "font-size: 18px; color: white; padding: 10px 0; text-align: center;"
            )
            ui.log().style(
                "width: 600px; border: 2px solid; border-color: #e86100; border-radius: 10px; padding: 10px; margin: 10px 0;"
            )


def process_file():
    ui.notify("Processing file...this may take a while.")
    time.sleep(7)
    ui.notify("File processed successfully.")


ui.run()
