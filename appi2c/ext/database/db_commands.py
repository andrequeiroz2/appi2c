import click
from appi2c.ext.database import db
from appi2c.ext.auth.auth_models import User # noqa
from appi2c.ext.device.device_models import DeviceType
from appi2c.ext.icon.icon_models import Icon


def init_app(app):

    @app.cli.command()
    def create_db():
        """Starting Data Base"""
        db.create_all()
        click.echo(click.style("Success", fg="green")+": Started Data Base")

    @app.cli.command()
    def insert_type():
        """Isert Type Device"""
        while True:
            user_input = input("Enter Name Type Device: ").capitalize().strip()
            user_input_len = len(user_input)
            if user_input_len < 4 or user_input_len > 60: 
                click.echo(click.style("Error", fg="red")+": Min digits 4, Max digits 60")
                return False
            else:
                if DeviceType.query.filter(DeviceType.name == user_input).first():
                    click.echo(click.style("Error", fg="red")+": Name is already in use")
                    return False
                else:
                    device = DeviceType(name=user_input)
                    db.session.add(device)
                    db.session.commit()
                    click.echo(click.style("Success", fg="green")+": Insert Data DeviceType")
                    return False

    @app.cli.command()
    def populate_type():
        """Populate Table DeviceType"""
        deviceType = DeviceType.query.all()
        insertType = ['Switch', 'Sensor']
        insertType_len = len(insertType)
        if not deviceType:
            for x in range(insertType_len):
                name_type = insertType[x]
                device = DeviceType(name=name_type)
                db.session.add(device)
                db.session.commit()
        click.echo(click.style("Success", fg="green")+": Populate Table Type")

    @app.cli.command()
    def populate_icon():
        """Populate Table Icon"""
        icon = Icon.query.all()
        insert_icon = ['fas fa-power-off','fas fa-lightbulb','fas fa-plug','fas fa-thermometer-three-quarters','fas fa-cloud-showers-heavy','fas fa-coffee', 'fas fa-fan']
        insert_icon_len = len(insert_icon)
        if not icon:
            for x in range(insert_icon_len):
                icon_type = insert_icon[x]
                icon_class = Icon(html_class=icon_type)
                db.session.add(icon_class)
                db.session.commit()
        click.echo(click.style("Success", fg="green")+": Populate Table Icon")
