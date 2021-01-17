from plyer import notification


def sendCompletionNote(photo_path):
    notification.notify(title="Schedule Captured",
                        message="Schedule Portal has successfully captured a copy of your schedule."
                                "\nYour Schedule Can Be Found Here:"
                                "\n" + photo_path,
                        app_name="Schedule Portal",
                        app_icon="",
                        timeout=10,
                        ticker="Schedule Portal has successfully captured a copy of your schedule.",
                        toast=False)


def sendErrorNote(error_description):
    notification.notify(title="An Error Occured",
                        message=error_description,
                        app_name="Schedule Portal",
                        app_icon="",
                        timeout=10,
                        ticker=error_description,
                        toast=False
                        )