
import flet as ft


def main(page: ft.Page):
    page.title = "Two-View Greeting App"

    # Store the user's name inside main
    entered_name = ""

    # Create the name input field
    name_field = ft.TextField(
        label="Enter your name",
        width=300
    )

    # Function to handle the Continue button
    async def continue_click(e):
        nonlocal entered_name

        entered_name = name_field.value.strip()

        # Check whether the name field is empty
        if entered_name == "":
            dialog = ft.AlertDialog(
                modal=True,
                title=ft.Text("Missing Name"),
                content=ft.Text("Please enter your name before continuing."),
                actions=[
                    ft.Button(
                        "OK",
                        on_click=lambda e: page.pop_dialog()
                    )
                ]
            )

            page.show_dialog(dialog)
            return

        # Navigate to the Greeting view
        await page.push_route("/greeting")

    # Function to return to the Home view
    async def back_click(e):
        await page.push_route("/")

    # Function that builds the views based on the route
    def route_change(e=None):
        page.views.clear()

        # HOME VIEW
        home_view = ft.View(
            route="/",
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            "Welcome to My Greeting App",
                            size=25,
                            weight=ft.FontWeight.BOLD
                        ),
                        name_field,
                        ft.Button(
                            "Continue",
                            on_click=continue_click
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                )
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        page.views.append(home_view)

        # GREETING VIEW
        if page.route == "/greeting":
            greeting_view = ft.View(
                route="/greeting",
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(
                                f"Hello, {entered_name}!",
                                size=28,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Button(
                                "Back",
                                on_click=back_click
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )

            page.views.append(greeting_view)

        page.update()

    # Listen for route changes
    page.on_route_change = route_change

    # Display the initial Home view
    route_change()


ft.run(main)
