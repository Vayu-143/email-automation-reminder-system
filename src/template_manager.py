def load_template(template_path):

    with open(
        template_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def personalize_template(
    template,
    data
):

    return template.format(
        name=data["name"],
        subject=data["subject"],
        reminder_date=data["reminder_date"],
        department=data["department"]
    )